---
type: faction
parent: ""
location: ""
faction_type: race
alignment: usually Lawful Good
leader: ""
appears_in: []
---
## Overview
Os **dracons** são uma raça de centauros-dragões que começou a aparecer aos poucos nas [[The Phlogiston#Esferas Conhecidas|Esferas Conhecidas]] no último século. Seus Spelljammers (em geral navios com pé-direito mais alto) já foram vistos nas bordas do [[The Phlogiston|Phlogiston]], e eles já fizeram algum contato com as comunidades espaciais: em especial, tendo um enclave em [[Wyrmways]], em [[The Rock of Bral|Bral]].

## Description
A dracon is centaur-like in appearance, with a heavy four-legged body with broad, flat, elephantine feet and a long, snakelike tail. Its torso and arms are human-like, although its six-fingered hands end in claws. A dracon's head is reptilian, with the horns and flanges of a dragon.

Dracons speak their own language and that of dragons. A few speak the common trade tongue, though haltingly and with a thick accent. Their speech is often formal and ornately ceremonial.

## Personality
Dracons are herd creatures, and their lives are circumscribed by a series of formal rituals designed to allow them to interact with the rest of the herd with no dissension. To humans, dracon formality is seen as condescending and a weakness; a view that is superficially supported by their willingness to flee or discuss a situation rather than fight. More than one human has been surprised. however. at how effective they are once the herd has made up its mind.

A lone dracon is a freak. Most dracons cannot survive outside the family unit, and become sick and confused if denied access to the leadership of the eldest of their herd for extended periods of time. A dracon left by itself will try to find another dracon family to adopt it. If this is impossible, it will attempt to form a new herd, even adopting non-dracons into its "family".[5]

Most observers speculate that only the most adventurous of the dracon species have traveled into wildspace, but even so most dracons seem stuffy and passive, more content to retreat than fight. There are exceptions, in particular those dracons who have adopted humanoids into their family units.[4] 

<!-- DYNAMIC:related-entries -->

## Member Characters

 ```dataview
    TABLE race, class, alignment
    WHERE type = "character" AND contains(factions, this.file.link)
    SORT file.name ASC
 ```

## Child Factions

 ```dataview
    TABLE faction_type, alignment
    WHERE type = "faction" AND parent = this.file.link
    SORT file.name ASC
 ```

## Related Entries

 ```dataview
    TABLE entry_type, author
    WHERE type = "entry" AND contains(relates_to, this.file.link)
    SORT file.ctime DESC
```

<!-- /DYNAMIC -->