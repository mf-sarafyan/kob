---
type: faction
parent: "[[Keepers of the Balance]]"
location: ""
faction_type: Adventurer Party
alignment: Good
leader: "[[kob/content/1 Keepers' Compendium/wiki/characters/Captain Jordal Brambletopple|Jordal]]"
---
 ![[kb-alpha-1.bmp|350]] 

**kbα1**
*Dragonfly-class Spelljammer*
- Luxury Spelljammer
- Carefully made hypoallergenic for Captain Jordal
- Extremely hihg speed


## kbα1
*Keepers of the Balance, Alpha-one squad* se refere tanto à nave quanto ao lendário grupo de aventureiros interplanares e interdimensionais. Quando eles não estão lidando com ameaças de escala cósmica, eles lecionam na [[Guilde Adventureir Extraordinaire]], onde cada um - com exceção da constructa mágica - tem um ou dois pupilos, protegidos, aprendizes: vocês.

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