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

> Take a look and understand the rules in this document before checking the facilities!

_**Business Facilities.**_ Workshops, Smithies, Labs, Arcane Studies, Docks, Archives, etc. provide income and special DnD-play bonuses. Each business facility has its own set of possible orders, and sometimes additional passive effects. Each Special Facility also lists an **Alignment** and **Defense Die** for Bastion Attacks (see below). See [[Bastions - Business Facilities]]. 

***Political Facilities***. Allies, envoys, contracts. These provide ways to affect faction relations and interact with the city politics - for better or worse. Different from Business Facilities, there are a couple of default political orders, and you facilities improve their effectiveness. See [[Bastions - Political Facilities]]. 

**Your Bastion starts with one Business and one Political facility.** You gain more facilities (no cost) at some level breakpoints (then you can . Some facilities can be upgraded, too (details are on their descriptions); you pay gold and the Facility spends one turn unavailable for orders, as work is done there. 

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
2. **_Set Active Factions and Events_.** Roll which factions are exerting themselves in each city tier this turn (e.g., Bragora, La Città). For each active faction, we’ll roll random events.
3. **_Players Choose Orders_.** Each participating character gives one order **to each of their facilities**.
4. **_Resolve Actions_.** Apply facility modifiers, political abilities, and effects from factions.
5. **_Update Records_.** Record Standing, Favours, gold gained/spent, project progress, and any facility changes.


---

## Orders
Bastion play uses two families of orders: **Business** (money and projects) and **Political** (relationships and cash-ins). 

### Business Orders
Business actions affect regular DnD play by giving resources such as money, items and other bonuses like inspiration. 
**Each business facility has its own set of available orders** - some may let you craft or harvest items, or spend time to gain temporary buffs. 
These are facility-specific and are detailed on their descriptions on [[Bastions - Business Facilities]]. 

***Busy***. Some orders will specify they make you Busy. You can't be Busy with two things at once in a turn. If you issue an **Order: Craft**, and you're doing the crafting yourself, you'll be Busy. If your hirelings are crafting for you, you won't be busy; but they usually (before level 9) can only craft mundane items.

Some examples:
- **Trade.** Your Bastion earns coin through rents, enterprises, and sales. Baseline income per Bastion is **20 gp × character level**. Facilities often add flat gp or % modifiers for **this turn**.
- **Craft.** Start or advance a project (mundane or magical) on a facility with the appropriate Tools. See **[[Crafting]]** for time, assistants, tools, and Essence.
- **Recruit / Empower / Harvest, etc.** Facility‑specific business orders which can give other regular play bonuses.

### Political Orders
![[Factions - Political Orders]]

---

## Faction Events
Each turn, we model life in the city by rolling for random events. 
First, we draft the **active factions** for each city tier where players have Bastions. 

Then, we roll for events for each: opportunities, hostility, friendship, business. The outcome can be better or worse depending on each PC's relation to each faction. Most events present players with a choice that will affect their Bastion's effectiveness for the turn. 

### Active Factions 

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

### Events 
Before players choose orders, the DM rolls on a *(secret)* table to get how the current active factions approach each Bastion. Here are some examples: 

***Lockdown.*** You can't issue **orders** to your facilities this turn, as the faction is putting it on lockdown: either harassing staff and visitors, burying it in paperwork, or good old sabotage. You can clear this up by winning a **Contest** in the district - if you do, the Bastion works normally, but you take **-2 favours** with the faction.
***Smuggling Window.*** You get a golden opportunity - you can choose to A) take have 50% lower **prices** for the turn, but you need to win a **Contest**. If you lose, the money (50%) is spent and you get nothing. Or you can choose to play it safe and B) get 10% increased income this turn. 
***Visitor.*** A friendly NPC asks for recurring access to your Bastion this week. They won't disrupt your other orders. You choose: A) +1 Favour with the faction or B) +25% income in this turn. 

([[Bastion Events|Link fácil pro DM]])


---

# Contests and Styles
**Styles** become relevant when resolving **contests**. Factions and bastions can be aligned to **Physical**, **Social** or **Bureaucratic**. Each has advantage against another: 
- **Physical** intimidation outweighs **Social** commentary, but yields to the correct **Bureaucratic** permits. 
- **Social** can ridicule or talk itself out of **Bureaucratic** sanctions, but can't stop a **Physical** slap to the face. 
- **Bureaucratic** forms can stop a **Physical** goon on its tracks, but won't stop **Social** whispers at the next gathering.
It's Rock-Paper-Scissors: Physical > Social > Buroca > Physical. 

Factions have their own aligment (Zenonni are random!). Bastions take the alignment of the majority of its facilities (player chooses on ties). 

## Resolving Contests
When a character’s Bastion is **contested**, or the player decides to initiate a contest against an **Event**, both sides roll to resolve the issue. 

**Facility Defense.** Each Special Facility lists an **Alignment** and a **Defense Die** (default **1d6**; fortifying sites like **Barracks/War Room** may list **1d8** or give bonuses to rolls). See more on the facility lists linked above. 

**Resolve:**
1. **Style.** Check who has advantage due to style.
2. **Roll Faction.** DM rolls; usually **1d6 + current negative Favours**, but can change by Event.
3. **Roll Defense.** Player rolls the largest die among facilities, adds relevant bonuses. 
4. **Outcome.** Whatever the outcome, negative favours are spent.
	1. **Player-triggered contest**
		1. **Player wins** - negative effects from events are negated *for all contestable events in the entire district*. That means your friend can help you out. 
		2. **Player loses** - Contest again, now as a Faction attack.  
	2. **Faction Attack**
		1. **Player wins** - nothing happens; the Bastion is secure. 
		2. **Player loses** - one Facility at random is deactivated for the round. It can't take orders and its passive effects don't apply. 

> ***Difficulty***. Balance is TODO, but lower Standing thresholds (-1, -3 and -6) will probably trigger harsher contests, as the Faction will dedicate more towards fucking with you.