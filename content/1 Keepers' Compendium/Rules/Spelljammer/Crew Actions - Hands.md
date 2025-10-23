# Crew & Hands (Core)

**Hands.** Each conscious crewmember on duty provides **1 Hand** per round. A PC can, on their turn, spend their **Action** to count as **1 Hand** for a single task that round.

**Crew Proficiency Bonus (Crew PB).** Crew quality sets PB for tasks that call for a roll:

- Green **+1**, Amateur **+2**, Professional **+3**, Specialist **+4** (if acting on their specialty).

**Crew Tags.** Individual crew can carry tags that modify their contribution. Examples:

- **Heavy Lifter:** counts as **2 Hands** on tasks with the **Heavy** tag (e.g., large guns).
- **Repair Savant (Wizpop):** counts as **2 Hands** on **Repair** tasks; gains **+1** to Tools checks there.
- **Arcane Bracer (Miken, Leron, Vaaz):** while **Bracing**, adds **+1** to the **temp BP** total (see Brace) in addition to their Crew PB.  
    Tags stack and apply only to the task that crewmember is assigned to this round.

**Casualties / Morale.** Effects that would cause casualties or shaken morale instead **knock out Hands**: reduce available Hands by the indicated number until **Stabilize Wounded** succeeds (Damage Control task).

---

# Task System (Tactical Round)

You assign **Hands** to tasks. Unless a task calls for a check, it succeeds. Where a check is listed and no PC is personally performing it, roll using **Crew PB** (Green +1 / Amateur +2 / Professional +3 / Specialist +4).

## Gunnery (weapon-dependent)

> Each ship weapon has a **Weapon Profile** that sets Hand costs and any checks. Example profiles below.

- **Reload [Weapon]** — **Hands:** per weapon profile; **Heavy**.  
    Load charge & shot, swab/ram, run out. Special ammo adds **+1 Hand**.
- **Fire [Weapon]** — **Hands:** per profile.  
    If no PC is Directing Fire (see talents), attack bonus = **+3 + Crew PB** (adjust to ship tier).
- **Clear Misfire (if applicable)** — **Hands:** per profile; **Check:** **DC** per profile (Tools). On fail, jam persists.
- **Traverse Mount (change facing 90°)** — **Hands:** per profile (often 1).

### Weapon Profile Template (put this on each weapon’s entry)

- **Light Ballista**: **Reload 1**, **Fire 1**, **Traverse 1**, **Misfire —**
- **Light Cannon (6–8 lb)**: **Reload 2**, **Fire 1**, **Traverse 1**, **Misfire 2 (DC 12)**
- **Heavy Cannon (12 lb)**: **Reload 3**, **Fire 1**, **Traverse 2**, **Misfire 2 (DC 13)**, **Heavy**
- **Bombard / Carronade**: **Reload 4**, **Fire 1**, **Traverse 2**, **Misfire 3 (DC 14)**, **Heavy**

> **Heavy**: crew with the **Heavy Lifter** tag count as **2 Hands** for this task.

---

## Rigging & Sails

- **Set Full Sails** — **3 Hands**, **duration:** until changed. **Heavy.**
    While set: **+20 ft Speed** and **–45° Maneuverability**.
- **Reef (Low) Sails** — **3 Hands**, **duration:** until changed. **Heavy.**
    While set: **–20 ft Speed** and **+45° Maneuverability**.
- **Brace a Side** — **variable Hands** (any number may join); choose a 90° arc; **duration:** until start of your next turn.  
    You gain **temporary BP** equal to the **sum of Crew PB** of all Bracing contributors (add tag bonuses like **Arcane Bracer**). This temp BP is depleted first by attacks from that arc.


## Damage Control

- **Restore Bulwark** — **1 Hands**, **Check:** **DC 13** (Carpenter’s or Tinker’s Tools).  
    Success: restore **1d4 BP**; Fail: restore **1 BP**.  
    Multiple crews may perform this in the same round; each is a separate roll.
- **Fix Disabled Module** — **3 Hands**, **Check:** **DC 15** (relevant Tools).  
    Success: clear **Disabled** from one weapon/sail/module and restores 10 HP to it; Fail: no effect.
- **Extinguish Fire** — **2 Hands** (minor) / **3 Hands** (major), **Check:** **DC 13/15** (Athletics or Tools).  
    Success: remove the fire; Fail: fire persists.
- **Stabilize Wounded** — **2 Hands**, **Check:** **DC 12 Medicine** (or Tools).  
    Success: restore **1 knocked-out Hand** to duty at the start of next round.

## Boarding

- **Throw Grapple Lines** — **2 Hands**, target within **30 ft**; **Opposed Check:** your **Athletics (Crew PB +3)** vs. target ship. On success, ships are **Grappled**.
- **Haul Together / Maintain Grapple** — **2 Hands** per active line each round.
- **Drop Planks / Boarding Nets** — **2 Hands**.
- **Engage**. Requires ship grapple and planks/nets to be deployed. Each *engaging* Hand has to be engaged by one Hand from the opposing ship, lowering their actions! 


# Fighters (Small Craft)

- **Launch / Recover Fighter** — Usually **2 Hands** each (from carrier). Depends on fighter model.
Regular crew won't pilot fighters - but maybe you can recruit specialized pilots eventually?

---

# Bridge Talents (Free-Form Picks)

**All talents cost 1 point.** Each character gains **4 points at 1st level**, then **+2 at 5, 9, 13, 17**. Unless noted, a talent does not change Hands costs; it changes _options_, _tempo_, or _who rolls_.

## Command (Captain / First Mate)

- **Bark Orders (Bonus).** Choose one task this round; reduce its **Hands** cost by **1** (min 1).
- **Rally to Stations (Action, 1/rest).** Immediately grant **2 temporary Hands** usable only for **Damage Control** tasks this round.
- **Grapple Master (Passive).** You have **advantage** on the opposed check to establish a Grapple.
- **Keep It Together! (Reaction, 2/rest).** When your ship would suffer a **Shaken**-style effect, ignore it.
- **Deck Whip (Bonus).** Choose one task; if it calls for a check, the crew performing it rolls with **advantage**.
- 
## Helm (Chair)

- **Hold the Line (Prepared Movement).** Instead of moving in your turn, you choose a target ship or mega creature. Until the start of your next turn, if it moves, you can use your reaction to follow it, maintaining the same distance, up to your movement speed. 
- **Crash Stop (Bonus, 1/rest).** Drop Speed to **0**; rams/collisions against you this round deal **half** damage.
- **Evasive Handling (Reaction, PB/rest).** Impose **disadvantage** on one ship-scale attack targeting your ship.

## Gunnery

- **Direct Fire (Action).** Choose one weapon that will **Fire** this round; you make the attack roll using your own **ranged attack** bonus instead of the crew’s. If you can make more than one attack on your turn, you can do this that many times.
- **Volley Timing (Bonus).** Direct your guns to overwhelm a ship's defenses. Choose two or more weapons on your ship. If at least two of them hit the same ship this turn, they deal double damage to **Bulwark Points (BP)**.
- **Spotter (Bonus).** Designate a target; the first allied ship attack against it this round gains **+1d4** to hit.

## Fighter Ops 

- **Fighter Qualified (Passive).** You can launch/pilot a fighter and make called shots.
- **Cut Their Lines (Passive).** Your fighter’s called shots vs. rigging/sails **don’t** suffer disadvantage. Requires **Fighter Qualified.**
- **Barrel Roll (Reaction).** When your fighter is targeted by an attack, impose **disadvantage** on that attack. Requires **Fighter Qualified.**



---
