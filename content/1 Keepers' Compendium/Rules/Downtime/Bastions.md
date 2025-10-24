---
type: entry
entry_type: Rules
relates_to: []
author: DM
---
# Summary

A **Bastion** is a character’s seat of influence in Bral—part home, part workshop, part political machine. During downtime, the campaign switches to **Bastion Turns** (about 7 days). In each turn, characters improve holdings, craft items, recruit crew, cultivate faction ties, and prepare for the next venture.

This section presents the shared framework your table uses whenever Bastions come into play. Specific political/business facilities, crafting, and faction procedures live in their own chapters.

---

## Facilities
Facilities are the rooms, staff, and agreements that give a Bastion teeth. Mechanically they’re either **Business** (Trade & Craft) or **Political** (Patronage, Enforcement, Cool‑Off, Meeting, Cash‑In). You can skin a political ability as a room, hireling, or contract; the ability is what matters.

_**Business Facilities.**_ Workshops, Smithies, Labs, Arcane Studies, Docks, Archives, etc. provide income and special dnd bonuses. Each Special Facility lists an **Alignment** and **Defense Die** for Bastion Attacks (see below). See [[Bastions - Business Facilities]]. 

***Political Facilities***. See at [[Bastions - Political Facilities]]. Affects political actions and faction relations. 

**Your Bastion starts with one Business and one Political facility.** You gain more facilities (no cost) at some level breakpoints. Some facilities can be upgraded, too. 

| Level | Special Facilities |
| ----- | ------------------ |
| 5     | 2                  |
| 9     | 4                  |
| 13    | 5                  |
| 17    | 6                  |

---


## Running a Bastion Turn

A Bastion Turn represents roughly a week of focused effort, meetings, and maintenance.

_**Sequence of Play**_

1. **_Declare Participation_.** Each character who is present in Bral may take Bastion actions this turn.
2. **_Set Active Factions_.** Pick which factions are exerting themselves in each city tier this turn (e.g., Bragora, La Città). For each active faction, we’ll roll a single **Base Posture** (see _Faction Approaches_ below).
3. **_Players Choose Actions_.** Each participating character takes **one Business Action** (per Bastion; some facilities let you affect this) and **one Political Action**.
4. **_Resolve Faction Approaches_.** Per-turn faction approaches depend on player relations and will affect their actions and income. 
5. **_Resolve Actions_.** Apply facility modifiers, political abilities, and effects from faction approaches.
6. **_Update Records_.** Record Standing, Favours, gold gained/spent, project progress, and any facility changes.

> **DM Guidance.** Keep the tempo brisk. Ask each player for their plan up front, roll Base Postures once per active faction, then walk the table resolving outcomes in one pass.

---

## Actions
Bastion play uses two families of actions: **Business** (money and projects) and **Political** (relationships and pull). 

### Business Actions
Business actions affect regular DnD play by giving resources such as money, items and other bonuses like inspiration. These are facility-specific and are detailed on their descriptions on [[Bastions - Business Facilities]]. 

- **Trade.** Your Bastion earns coin through rents, enterprises, and sales. Baseline income is **20 gp × character level** (or a facility’s alternate). Facilities often add flat gp or % modifiers for **this turn**.
- **Craft.** Start or advance a project (mundane or magical). See **Crafting** for time, assistants, tools, and Essence. Business facilities apply here (workshops, labs, yards, archives).
- **Recruit / Empower / Harvest, etc.** Facility‑specific business orders which can give other regular play bonuses.

### Political Actions
![[Factions - Political Actions]]


---

## Faction Events
This section references the standing/favours model. For details on Favours, Standing, Meetings, and Cash‑Ins, see **[[Faction Relations]]**.

### Active Factions (per tier)
For each city tier this turn, pick or roll an active faction:

| d8  | Active Faction                                  | Style        | Notes                                      |
| :-: | ----------------------------------------------- | ------------ | ------------------------------------------ |
|  1  | Cartocci                                        | Bureaucratic | Permits, audits, legal shields.            |
|  2  | Monarquia Braliana                              | Bureaucratic | Royal writs, dispensation, guard presence. |
|  3  | Malvessi                                        | Physical     | Hits, stoppages, escorts.                  |
|  4  | Cinders                                         | Physical     | Strikes, sabotage, cell support.           |
|  5  | Luminari                                        | Social       | Boycotts, lantern walks, street whispers.  |
|  6  | Il Velluto                                      | Social       | Galas, snubs, society columns.             |
|  7  | Zenonni                                         | Weird        | Anomalies, specialists, windfalls.         |
|  8  | Two active—roll twice again; ignore further 8s. | —            | —                                          |

---

### Faction Approaches 
At the start of the turn—**before** resolving actions—set a **Base Posture** for each **active** faction. Then, as characters interact, derive **Personal Treatment** from that one roll.

#### Step 1 — Base Posture
The DM rolls **1d10** for each active faction **once**. Apply the **district economy** to everyone **this turn**:

| Base Roll | Vibe                | District Economy (this turn)     |
| :-------: | ------------------- | -------------------------------- |
|  **≤ 0**  | **Sea Storm**       | **Income −20%**, **Prices +20%** |
|  **1–2**  | **Gale Warning**    | **Income −20%**, **Prices +20%** |
|  **3–4**  | **Headwinds**       | **Income −10%**, **Prices +10%** |
|  **5–6**  | **Steady Waters**   | **±0%**                          |
|  **7–8**  | **Favorable Winds** | **Income +10%**, **Prices −10%** |
| **9–10**  | **Full Sail**       | **Income +20%**, **Prices −20%** |
| **≥ 11**  | **Fair Tide**       | **Income +20%**, **Prices −20%** |

**Stacking:** Sum all active factions’ income/price modifiers, cap at **−30% / +30%**.

#### Step 2 — Personal Treatment (per character × faction)
Each faction's approach to a character depends on their approach but is modified by their standing:

**Personal Total = Base Roll + Standing + Favours\***
*Negative favours always apply and are consumed. Positive favours can add to the total if the player chooses to when approaches are rolled.*

Map the Personal Total to the **same bands**. That band is the character’s **Personal Treatment** for action effects with that faction this turn.

- Different characters will often land on **different bands** from the **same** Base Posture.
- Per faction, per character, you may claim **one** boon/surcharge from your band this turn; further touches default to **Steady Waters**.

### Band Effects (this turn)
**Sea Storm (≤0)** — _Attack!_ Resolve a **Bastion Attack** against this character (see below), in addition to Gale Warning's effects.

**Gale Warning (1–2)** — _disruptive posture_
- With this faction: the first **Patronage/Enforcement** or **Cool‑Off** you do **with them** also grants **+1 Favour** (on top of normal gains). 
- Meetings don't consume an action if below 0 Standing.
- If you court others: the **first** **Patronage/Enforcement** you do for **another** faction this turn causes **−2 Favours** with this faction.

**Headwinds (3–4)** — _pressuring posture_
- With this faction: the first **Patronage** or **Cool‑Off** you do **with them** grants **+1 Favour**.
- If you court others: your **first** **Patronage** for someone else this turn causes **−1 Favour** here.

**Steady Waters (5–6)** — _business as usual_
- No extra effects. 
- **Courtesy:** if you did **Patronage** to them, you don't lose favours with other factions.

**Favorable Winds (7–8)** — _mild patronage_
- With this faction: your first **Patronage/Enforcement** with them yields **+1 extra Favour**.
- A **Pull** this turn costs **-1 favour** (min 0).
- If you court others: your **first** **Patronage/Enforcement** for another faction inflicts **−1 Favour** with this active faction.

**Full Sail (9–10)** — _strong patronage_
- With this faction: your first **Patronage/Enforcement** with them yields **+1 extra Favour**.
- Your next **Pull** with them costs **−1 Favour** (min 0).
- A **Meeting** may be held **without consuming your action** (still costs **3 Favours**). 
- If you court others: your **first** **Patronage/Enforcement** for another faction inflicts **−2 Favours** with this active faction.

**Fair Tide (≥11)** — _windfall_
In addition to Full Sail's effects:
- **Free Minor Cash‑In** now (no cost, no check), or your **next Cash‑In with this faction** today costs **−2 Favours** (min 0).



---

# Bastion Styles
**Styles** become relevant when resolving attacks. Factions and bastions can be aligned to **Physical**, **Social** or **Bureaucratic**. Each has advantage against another: 
- **Physical** intimidation outweighs **Social** commentary, but yields to the correct **Bureaucratic** permits. 
- **Social** can ridicule or talk itself out of **Bureaucratic** sanctions, but can't stop a **Physical** slap to the face. 
- **Bureaucratic** forms can stop a **Physical** goon on its tracks, but won't stop **Social** whispers at the next gathering.
It's Rock-Paper-Scissors: Physical > Social > Buroca > Physical. 

Factions have their own aligment (Zenonni are random!). Bastions take the alignment of the majority of its facilities (player chooses on ties). 

## Attack and Defense
When a character’s **Personal Treatment** is **Sea Storm** (≤0), resolve a quick clash.

**Facility Defense.** Each Special Facility lists an **Alignment** and a **Defense Die** (default **1d6**; fortifying sites like **Barracks/War Room** may list **1d8**; optional size steps Cramped d4 / Roomy d6 / Vast d8). See more on [[Facilities List]].

**Resolve:**
1. **Style.** Check who has advantage due to style.
2. **Roll attack.** Attacker **1d6 + current negative Favours**. 
3. **Roll Defense.** Roll the largest die among facilities. 
4. **Outcome.** Whatever the outcome, negative favours are spent. If the attack roll beats the defense roll, one facility at random is disabled for this round, as its focused on repairs: its actions can't be taken, its bonuses are deactivated, and its income is zero. 

---

## Quick GM Flow (with d10)

1. **Active factions.** Pick per tier.
2. **Base Posture.** Roll **1d10** once per active faction; apply economy modifiers (respect caps).
3. **Plans.** Players declare actions: business and political.
4. **District Economy.** Calculate incomes and prices from current faction approaches.
5. **Attacks.** If any Personal Treatment is **Sea Storm**, run a Bastion Attack.
6. **Resolve.** Get results from plans considering the faction events and attacks. 
7. **Record.** Update Standing, Favours, income, projects.

---

## Design Notes

- **Two dials only.** Standing and Favours do all the work—no extra clocks.
- **This‑turn effects.** No delayed penalties; the Bastion phase stays snappy.
- **District breathes.** Money dials (income/prices) reflect street weather, while bands shape political friction.
- **Player choice.** You decide when to climb (Meetings at **3 Favours**); debts drag you down automatically.