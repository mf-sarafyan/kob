#!/usr/bin/env python3
# lights_out_nomod_flow.py
# A 6-node Lights-out-style puzzle with two presets (no modulus):
#   - "ring":   simple adjacent flow (+1 at i, -1 at i+1)
#   - "spice":  nonlocal 4-touch flow (+1 at i, -1 at i±1, +1 at i+3)
#
# Both preserve SUM==constant. Goals:
#   - zeros  -> feasible iff sum==0
#   - equal  -> feasible iff sum%6==0
#   - vector -> feasible iff target sum equals current sum (plus extra invariants in 'spice')
#
# Commands:
#   preset ring|spice   Switch button layout.
#   b1..b6 / bX*n       Press a button (optionally n times).
#   set / add           Set or add a 6-vector.
#   goal zeros|equal|vector
#   rand L..H [xN]      Generate a solvable random state for current goal.
#                       In 'ring', we build a state with compatible sum.
#                       In 'spice', we SCRAMBLE the goal by N random moves (default 12)
#                       so it's always solvable; we retry until bounds L..H hold.
#   scramble N          Scramble current target by N random moves (always solvable).
#   solve               Solver: exact integer plan for 'ring'; for 'spice', uses stored scramble
#                       (if present) to reverse; otherwise attempts integer solve and may fail.
#   hint                If a scramble plan exists, reveal the next reverse move.
#   show / history / undo / reset / help / quit
#
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import random
import sys
import math

ORDER = ["A","B","C","D","E","F"]

def make_moves(preset: str) -> Dict[str, Dict[str, int]]:
    preset = preset.lower()
    if preset == "ring":
        # +1 on i, -1 on i+1
        mv = {}
        for j in range(6):
            eff = {ORDER[j]: +1, ORDER[(j+1)%6]: -1}
            mv[f"B{j+1}"] = eff
        return mv
    elif preset == "spice":
        # +1 on i, -1 on i-1 and i+1, +1 on opposite i+3 (sum zero, 4 nodes per move)
        mv = {}
        for j in range(6):
            eff = {
                ORDER[j]: +1,
                ORDER[(j-1)%6]: -1,
                ORDER[(j+1)%6]: -1,
                ORDER[(j+3)%6]: +1,
            }
            mv[f"B{j+1}"] = eff
        return mv
    else:
        raise ValueError("Unknown preset. Use 'ring' or 'spice'.")

HELP_TEXT_BASE = """
Commands:
  preset ring|spice     Switch button layout.
  b1..b6                Press a button once (case-insensitive), e.g. 'b3'.
  bX*n                  Press a button n times, e.g. 'b1*3' or 'b4x5'.
  set a,b,c,d,e,f       Set exact state (spaces ok).
  add a,b,c,d,e,f       Add vector to state.
  goal zeros|equal      Choose a goal (or 'goal a,b,c,d,e,f').
  rand L..H [xN]        Build a random SOLVABLE state within [L,H].
                        In 'ring': sum-compatible sampler.
                        In 'spice': scramble-from-goal with N random presses (default 12).
  scramble N            Scramble current TARGET by N random presses (guaranteed solvable).
  solve                 'ring': exact integer solver. 'spice': reverse stored scramble if present,
                        else attempt integer solve (may report unsolvable due to invariants).
  hint                  Peek the next reverse move if a scramble exists.
  show / history / undo / reset / help / quit
"""

def parse_vector(arg: str) -> List[int]:
    s = arg.replace(",", " ").split()
    if len(s) != 6:
        raise ValueError("Expected 6 numbers.")
    return [int(x) for x in s]

def parse_range(arg: str) -> Tuple[int, int]:
    if ".." not in arg:
        raise ValueError("Range must be MIN..MAX (e.g., -3..3).")
    lo_s, hi_s = arg.split("..", 1)
    lo, hi = int(lo_s.strip()), int(hi_s.strip())
    if lo > hi:
        lo, hi = hi, lo
    return lo, hi

@dataclass
class Puzzle:
    state: List[int] = field(default_factory=lambda: [0]*6)
    goal_mode: str = "equal"
    goal_vector: Optional[List[int]] = None
    preset: str = "spice"  # default to spicy!
    history: List[str] = field(default_factory=list)
    initial_state: List[int] = field(default_factory=list)
    scramble_plan: List[str] = field(default_factory=list)  # moves applied to GOAL to create current state

    def __post_init__(self):
        if not self.initial_state:
            self.initial_state = self.state.copy()
        self.MOVES = make_moves(self.preset)

    # --- Mechanics ---
    def apply_move(self, move: str, times: int = 1, record_history: bool = True):
        move = move.upper()
        if move not in self.MOVES:
            raise ValueError(f"Unknown move '{move}'.")
        for _ in range(times):
            for k, delta in self.MOVES[move].items():
                idx = ORDER.index(k)
                self.state[idx] += delta
            if record_history:
                self.history.append(move)

    def add_vector(self, vec: List[int]):
        self.state = [a + b for a, b in zip(self.state, vec)]

    def set_state(self, vec: List[int], capture_initial: bool = False):
        self.state = vec.copy()
        if capture_initial:
            self.initial_state = self.state.copy()

    def set_goal(self, mode: str, vec: Optional[List[int]] = None):
        mode = mode.lower()
        if mode not in ("zeros", "equal", "vector"):
            raise ValueError("Goal mode must be 'zeros', 'equal', or 'vector'.")
        self.goal_mode = mode
        if mode == "vector":
            if vec is None or len(vec) != 6:
                raise ValueError("Goal vector must have 6 integers.")
            self.goal_vector = vec.copy()
        else:
            self.goal_vector = None
        # changing goal invalidates old scramble
        self.scramble_plan.clear()

    def set_preset(self, name: str):
        self.preset = name.lower()
        self.MOVES = make_moves(self.preset)
        self.history.clear()
        self.scramble_plan.clear()

    def sum(self) -> int:
        return sum(self.state)

    def target_vector(self) -> Optional[List[int]]:
        if self.goal_mode == "zeros":
            return [0]*6
        elif self.goal_mode == "equal":
            s = self.sum()
            if s % 6 != 0:
                return None
            t = s // 6
            return [t]*6
        elif self.goal_mode == "vector":
            return self.goal_vector
        else:
            return None

    def is_solved(self) -> bool:
        tv = self.target_vector()
        return tv is not None and self.state == tv

    # --- Random generation ---
    def randomize_ring(self, lo: int, hi: int) -> Tuple[bool, str]:
        # Make a random vector within bounds whose sum matches the goal constraints.
        Smin, Smax = 6*lo, 6*hi

        # derive target sum
        if self.goal_mode == "zeros":
            target_sum = 0
        elif self.goal_mode == "equal":
            start = math.ceil(Smin/6)*6
            if start > Smax:
                return False, f"No multiple of 6 exists in sum range [{Smin},{Smax}] for bounds [{lo},{hi}]."
            count = (Smax - start)//6 + 1
            target_sum = start + 6*random.randrange(count)
        elif self.goal_mode == "vector":
            if self.goal_vector is None:
                return False, "Goal vector not set."
            target_sum = sum(self.goal_vector)
            if not (Smin <= target_sum <= Smax):
                return False, f"Target sum {target_sum} not achievable within bounds [{lo},{hi}]."
        else:
            return False, "Unknown goal mode."

        # sample & adjust
        for _ in range(1000):
            v = [random.randint(lo, hi) for _ in range(6)]
            diff = target_sum - sum(v)
            if diff == 0:
                self.state = v
                self.scramble_plan.clear()
                return True, "OK"
            if diff > 0:
                for i in range(6):
                    room = hi - v[i]
                    add = min(room, diff)
                    v[i] += add
                    diff -= add
                    if diff == 0: break
            else:
                need = -diff
                for i in range(6):
                    room = v[i] - lo
                    sub = min(room, need)
                    v[i] -= sub
                    need -= sub
                    if need == 0: break
            if sum(v) == target_sum:
                self.state = v
                self.scramble_plan.clear()
                return True, "OK"
        return False, "Failed to find a solvable random state within bounds."

    def scramble_from_target(self, steps: int, lo: Optional[int]=None, hi: Optional[int]=None) -> Tuple[bool,str]:
        """Start at target and apply random moves; store reverse plan; enforce bounds if given."""
        tv = self.target_vector()
        if tv is None:
            return False, "Current goal has no concrete target (check sum / divisibility)."
        # Try multiple times to respect bounds
        for _ in range(200):
            state = tv.copy()
            plan = []
            for _ in range(steps):
                move = random.choice(list(self.MOVES.keys()))
                # apply to state (forward), record reverse (same move, but will be undone later)
                for k, delta in self.MOVES[move].items():
                    idx = ORDER.index(k)
                    state[idx] += delta
                plan.append(move)
            if lo is not None and hi is not None:
                if any((x < lo or x > hi) for x in state):
                    continue
            # accept
            self.state = state
            self.scramble_plan = plan  # reversing plan means applying moves in reverse order with minus times; but since moves commute not necessarily; we'll compute reverse by applying inverse (same move with -1) in LIFO
            self.history.clear()
            return True, "OK"
        return False, "Could not scramble into bounds; relax bounds or increase steps."

    def randomize(self, lo: int, hi: int, steps: Optional[int]) -> Tuple[bool,str]:
        if self.preset == "ring" and steps is None:
            return self.randomize_ring(lo, hi)
        # spice or ring with steps: scramble method
        if steps is None:
            steps = 12
        ok,msg = self.scramble_from_target(steps, lo, hi)
        return ok,msg

    # --- Solve ---
    def solve_ring(self) -> Tuple[bool,str,Optional[List[int]]]:
        # Constructive integer solution (nonnegative) for ring moves.
        tv = self.target_vector()
        if tv is None:
            if self.goal_mode == "zeros":
                return False, "Unsolvable: total sum must be 0 for 'zeros' goal.", None
            if self.goal_mode == "equal":
                return False, "Unsolvable: total sum must be divisible by 6 for 'equal' goal.", None
            return False, "Unsolvable: no valid target vector set.", None
        delta = [t - s for t,s in zip(tv, self.state)]
        if sum(delta)!=0:
            return False, "Unsolvable: target must preserve total sum.", None
        # Δ_A = x1 - x6
        # Δ_B = x2 - x1
        # Δ_C = x3 - x2
        # Δ_D = x4 - x3
        # Δ_E = x5 - x4
        # Δ_F = x6 - x5
        p = [0,
             0,
             delta[1],
             delta[1]+delta[2],
             delta[1]+delta[2]+delta[3],
             delta[1]+delta[2]+delta[3]+delta[4],
             delta[1]+delta[2]+delta[3]+delta[4]+delta[5]]
        k = -min(p[1:])
        x = [None] + [p[i]+k for i in range(1,7)]
        min_x = min(x[1:])
        x = [None] + [v - min_x for v in x[1:]]  # remove common offset
        # verify by applying
        test = self.state.copy()
        for btn, times in enumerate(x[1:], start=1):
            if times==0: continue
            move=f"B{btn}"
            for _ in range(times):
                for kname, dval in self.MOVES[move].items():
                    idx = ORDER.index(kname)
                    test[idx] += dval
        if test != tv:
            return False, "Solver verification failed (ring).", None
        return True, "OK", x[1:]

    def solve_spice(self) -> Tuple[bool,str,Optional[List[int]]]:
        # If we have a scramble plan, just reverse it.
        if self.scramble_plan:
            plan = list(reversed(self.scramble_plan))  # reverse order
            # Inverse of a single press is pressing the same move with -1 times.
            # To keep counts nonnegative, we accumulate counts and then shift by +k later.
            counts = {f"B{i}":0 for i in range(1,7)}
            for mv in plan:
                counts[mv] += 1
            # Apply plan
            return True, "OK (reversing scramble)", [counts[f"B{i}"] for i in range(1,7)]
        # Otherwise attempt an integer solve via simple integer least squares rounding + verify
        tv = self.target_vector()
        if tv is None:
            return False, "No concrete target (check sum / divisibility).", None
        delta = [t - s for t,s in zip(tv, self.state)]
        # Build matrix M for current preset
        import numpy as np
        M = np.zeros((6,6), dtype=int)
        for j in range(6):
            for k, d in self.MOVES[f"B{j+1}"].items():
                M[ORDER.index(k), j] = d
        # Try to find integer x by least squares then adjust by adding c*1 (nullspace) to make nonneg
        x_real, *_ = np.linalg.lstsq(M.astype(float), np.array(delta, float), rcond=None)
        x_rounded = np.rint(x_real).astype(int)
        # verify, else fail gracefully
        if np.all(M @ x_rounded == np.array(delta)):
            # shift to nonnegative by adding constant if needed
            mn = x_rounded.min()
            if mn < 0:
                x_rounded = x_rounded - mn
            return True, "OK (integer solve)", [int(v) for v in x_rounded.tolist()]
        return False, "Could not find an integer press plan for this state with 'spice' (invariants likely block it). Use 'scramble'/'rand xN' to generate solvable puzzles, or switch to 'ring'.", None

    def solve(self) -> Tuple[bool,str,Optional[List[int]]]:
        if self.preset == "ring":
            return self.solve_ring()
        else:
            return self.solve_spice()

    # --- Utilities ---
    def undo(self):
        if not self.history:
            print("Nothing to undo.")
            return
        last = self.history.pop()
        for k, delta in self.MOVES[last].items():
            idx = ORDER.index(k)
            self.state[idx] -= delta

    def reset(self):
        self.state = self.initial_state.copy()
        self.history.clear()
        self.scramble_plan.clear()

    def pretty(self) -> str:
        pairs = [f"{name}:{val:+d}" for name, val in zip(ORDER, self.state)]
        return "  ".join(pairs)

def banner(puz: Puzzle):
    print("="*64)
    print(f" No-Mod Puzzle — preset: {puz.preset.upper()}  (switch with 'preset ring' / 'preset spice') ")
    print("="*64)
    print(HELP_TEXT_BASE)
    print("Buttons:")
    for b in [f"B{i}" for i in range(1,7)]:
        eff = puz.MOVES[b]
        parts = [f"{k}{'+' if v>=0 else ''}{v}" for k,v in eff.items()]
        print(f"  {b}: " + ", ".join(parts))

def show(puz: Puzzle):
    print(f"\nState: {puz.pretty()}")
    total = puz.sum()
    if puz.goal_mode == "vector":
        goal = f"vector {puz.goal_vector}"
    else:
        goal = puz.goal_mode
    print(f"Sum: {total} | Goal: {goal} | Preset: {puz.preset} | Moves so far: {len(puz.history)}")
    if puz.scramble_plan:
        print(f"Scrambled by {len(puz.scramble_plan)} moves (hint/solve will reverse).")
    if puz.is_solved():
        print("✅ SOLVED!\n")

def repl(initial: Optional[List[int]] = None):
    puz = Puzzle(state=initial or [0]*6)
    banner(puz)
    show(puz)
    while True:
        try:
            raw = input("\n> ").strip()
        except EOFError:
            print()
            break
        if not raw:
            show(puz)
            continue
        cmd = raw.lower()

        if cmd in ("q","quit","exit"):
            break
        if cmd in ("h","help","?"):
            banner(puz)
            continue
        if cmd == "show":
            show(puz); continue
        if cmd == "history":
            print("History:", " ".join(puz.history) if puz.history else "(empty)"); continue
        if cmd == "undo":
            puz.undo(); show(puz); continue
        if cmd == "reset":
            puz.reset(); show(puz); continue

        if cmd.startswith("preset "):
            name = cmd.split(None,1)[1].strip()
            try:
                puz.set_preset(name)
            except Exception as e:
                print(e); continue
            banner(puz); show(puz); continue

        # Buttons with multipliers: b1*3 or b1x5
        if cmd[0] == "b" and (len(cmd) >= 2):
            base = cmd[:2].upper()
            if base in puz.MOVES:
                times = 1
                rest = cmd[2:]
                if rest:
                    if rest[0] in ("*","x"):
                        try: times = int(rest[1:])
                        except ValueError:
                            print("Invalid multiplier. Use e.g. b3*4"); continue
                    else:
                        print("Unknown suffix for button. Use e.g. b5*3"); continue
                puz.apply_move(base, times)
                show(puz); continue

        if cmd.startswith("goal "):
            arg = cmd[5:].strip()
            if arg == "zeros": puz.set_goal("zeros")
            elif arg == "equal": puz.set_goal("equal")
            else:
                try: vec = parse_vector(arg)
                except Exception as e: print("Bad goal vector:", e); continue
                puz.set_goal("vector", vec)
            show(puz); continue

        if cmd.startswith("set "):
            try: vec = parse_vector(cmd[4:].strip())
            except Exception as e: print("Bad set vector:", e); continue
            puz.set_state(vec, capture_initial=True); show(puz); continue

        if cmd.startswith("add "):
            try: vec = parse_vector(cmd[4:].strip())
            except Exception as e: print("Bad add vector:", e); continue
            puz.add_vector(vec); show(puz); continue

        if cmd.startswith("rand "):
            arg = cmd[5:].strip()
            parts = arg.split()
            LH = parts[0]
            steps = None
            if len(parts) > 1:
                if parts[1][0] in ("*","x"):
                    try: steps = int(parts[1][1:])
                    except: print("Bad steps after xN."); continue
            try: lo, hi = parse_range(LH)
            except Exception as e: print("Bad range:", e); continue
            ok,msg = puz.randomize(lo, hi, steps)
            if not ok: print("rand:", msg)
            show(puz); continue

        if cmd.startswith("scramble "):
            try: N = int(cmd.split()[1])
            except: print("Usage: scramble N"); continue
            ok,msg = puz.scramble_from_target(N)
            if not ok: print("scramble:", msg)
            show(puz); continue

        if cmd == "hint":
            if puz.scramble_plan:
                nxt = puz.scramble_plan[-1]
                print("Hint: press", nxt)
            else:
                print("No scramble history available.")
            continue

        if cmd == "solve":
            ok,msg,plan = puz.solve()
            if not ok:
                print("Solve:", msg); show(puz); continue
            pairs = [f"B{i+1}*{n}" for i,n in enumerate(plan) if n]
            print("Press plan:", " ".join(pairs) if pairs else "(no presses needed)")
            for i,n in enumerate(plan, start=1):
                if n: puz.apply_move(f"B{i}", n)
            show(puz); continue

        print("Unknown command. Type 'help' for commands.")

if __name__ == "__main__":
    seed: Optional[List[int]] = None
    if len(sys.argv) > 1:
        try: seed = parse_vector(sys.argv[1])
        except Exception: seed = None
    repl(seed)
