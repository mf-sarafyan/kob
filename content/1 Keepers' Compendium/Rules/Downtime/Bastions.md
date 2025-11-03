---
type: entry
entry_type: Rules
relates_to: []
author: DM
aliases:
  - Bastion
  - Bastion Rules
---
# Summary

A **Bastion** is a character’s seat of influence in Bral—part home base, part crew, part paperwork. Bastions convert table downtime into concrete gains: gold, gear, information, cover, and political leverage. During downtime, the campaign switches to **Bastion Turns** (about 7 days). Each Bastion Turn (about a week in-game) you select orders for each of your facilities, pursue faction relations, react to the city’s mood, and handle any trouble.

This file defines the loop and shared language. Facility catalogs, crafting, and faction procedures live in sibling files.

> Before reading this, read [[Faction Relations]] to get a sense of how political play works. Bastion play also allows [[Crafting]] items - that file has details on the mechanics.


---
## Setting up: First Choices

Pick three things when you found a Bastion:

1. **Flavor.** Name the place and flavour of your place; pick a district in [[The Rock of Bral|Bral]] for your location and choose what goes on in there.  
2. **First Business Facility.** Pick one from the business catalog that matches your play goals (e.g., Workshop/Smithy for crafting; Arcane Study for scrolls; Storehouse for steady coin).
3. **First Political Facility.** Pick one passive effect that best supports how you plan to operate (e.g., discount Meetings, stronger defense, or cheaper Cash‑ins). 

You gain additional facilities at levels **9/13/17** as per the table below.

## Facilities
Facilities are the rooms, staff, and agreements that give a Bastion life. Mechanically they’re either **Business** (Trade & Craft) or **Political** (Factions). You can skin a facility as a room, hireling, or contract; the ability is what matters.

_**Business Facilities.**_ Workshops, Smithies, Labs, Arcane Studies, Docks, Archives, etc. provide income and special DnD-play bonuses. Each business facility has its own set of possible orders, and sometimes additional passive effects. Each Special Facility also lists an **Alignment** and **Defense Die** for Bastion Attacks (see below). See [[Bastions - Business Facilities]]. 

***Political Facilities***. Allies, envoys, contracts. These provide ways to affect faction relations and interact with the city politics - for better or worse. Different from Business Facilities, there are a couple of default political orders, and you facilities improve their effectiveness. See [[Bastions - Political Facilities]]. 

**Your Bastion starts with one Business and one Political facility.** You gain more facilities (no cost) at some level breakpoints (then you can . Some facilities can be upgraded, too; by paying gold and spending one turn unavailable for orders as work is done there. 

> Take a look and understand these rules before checking the facilities!

| Level | Special Facilities |
| ----- | ------------------ |
| 5     | 2                  |
| 9     | 4                  |
| 13    | 5                  |
| 17    | 6                  |
### Income
Your Bastion's "business as usual" financial activities provide you with a bit of income per Bastion Turn: 

**Baseline = 20 gp × character level**

Some **Business Facilities** will alter that value via passive effects or actions. 

---


## Running a Bastion Turn

A Bastion Turn represents roughly a week of focused effort, meetings, and maintenance.

_**Sequence of Play**_

1. **_Declare Participation_.** Each character who is present in Bral may take Bastion actions this turn.
2. **_Set Active Factions_.** Pick which factions are exerting themselves in each city tier this turn (e.g., Bragora, La Città). For each active faction, we’ll roll a single **Base Posture** (see _Faction Approaches_ below).
3. **_Players Choose Orders_.** Each participating character gives orders **to each of their facilities**.
4. **_Resolve Faction Approaches_.** Per-turn faction approaches depend on player relations and will affect their actions and income. 
5. **_Resolve Actions_.** Apply facility modifiers, political abilities, and effects from faction approaches.
6. **_Update Records_.** Record Standing, Favours, gold gained/spent, project progress, and any facility changes.


---

## Orders
Bastion play uses two families of orders: **Business** (money and projects) and **Political** (relationships and cash-ins). 

### Business Orders
Business actions affect regular DnD play by giving resources such as money, items and other bonuses like inspiration. 
**Each business facility has its own set of available orders** - some may let you craft or harvest items, or spend time to gain temporary buffs. 
These are facility-specific and are detailed on their descriptions on [[Bastions - Business Facilities]]. 

Some examples:
- **Trade.** Your Bastion earns coin through rents, enterprises, and sales. Baseline income is **20 gp × character level**. Facilities often add flat gp or % modifiers for **this turn**.
- **Craft.** Start or advance a project (mundane or magical) on a facility with the appropriate Tools. See **[[Crafting]]** for time, assistants, tools, and Essence.
- **Recruit / Empower / Harvest, etc.** Facility‑specific business orders which can give other regular play bonuses.

### Political Orders


---

## Faction Events
This section references the standing/favours model. For details on Favours, Standing, Meetings, and Cash‑Ins, see **[[Faction Relations]]**.

### Active Factions (per tier)
For each city tier this turn ([[Soffiera]], [[Bragora]] & [[La Citta]]), pick or roll an active faction:

| d8  | Active Faction                                  | Style        | Vibe                                       |
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

Faction Approach represents both:
- How the current activity drives the economy of the region this turn
	- which alters general income and prices, as in:
		- if the faction is cracking down and people are staying home and not spending on player businesses, or raising their prices to cover for faction "taxes"
		- if the faction is encouraging business, people are going around spending more, prices get lower. 
- And how the faction treats the PCs' businesses specifically
	- Even if the faction may have a positive approach in a turn, if they absolutely loathe that PC, they'll still give them trouble. The same is true for the opposite - if they're on a crackdown, they'll still give benefits to their friends.
		- That doesn't change the general economy in the district, though!

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

Different characters may land on **different bands** from the **same** Base Posture.

### Band Effects (this turn)
**Sea Storm (≤0)** — _Attack!_ Resolve a **Bastion Attack** against this character (see below), in addition to Gale Warning's effects.

**Gale Warning (1–2)** — _disruptive posture_
- With this faction: **Patronage/Enforcement** or **Cool‑Off** you do **with them** also grants **+1 Favour** (on top of normal gains). 
- Meetings don't consume an action if below 0 Standing.
- If you court others: **Patronage/Enforcement** you do for **another** faction this turn causes **−2/-3 Favours** with this faction.

**Headwinds (3–4)** — _pressuring posture_
- With this faction:  **Patronage** or **Cool‑Off** you do **with them** grants **+1 Favour**.
- If you court others: **Patronage/Enforcement** for someone else this turn causes **−1/-2 Favours** here.

**Steady Waters (5–6)** — _business as usual_
- No extra effects. 
- **Courtesy:** if you did **Patronage** to them, you don't lose favours with other factions.

**Favorable Winds (7–8)** — _mild patronage_
- With this faction: **Patronage/Enforcement** with them yields **+1 extra Favour**.
- A **Cash-in** this turn costs **-1 favour** (min 0).
- If you court others: **Patronage/Enforcement** for someone else this turn causes **−1/-2 Favours** here.

**Full Sail (9–10)** — _strong patronage_
- With this faction: **Patronage/Enforcement** with them yields **+1 extra Favour**.
- Your next **Cash-in** with them costs **−1 Favour** (min 0).
- A **Meeting** may be held **without consuming your action** (still costs **3 Favours**). 
- If you court others: **Patronage/Enforcement** you do for **another** faction this turn causes **−2/-3 Favours** with this faction.

**Fair Tide (≥11)** — _windfall_
In addition to Full Sail's effects:
- **Free Minor Cash‑In** now (no cost, no action, no check), or your **next Cash‑In with this faction** today costs **−2 Favours** (min 0).



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