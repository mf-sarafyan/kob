---
type: faction
parent:
  - "[[Zenonni]]"
location: ""
faction_type: Band
alignment: Chaotic Jazzy
leader:
---
## Xenophonics
A banda usual do Laughing Beholder, esse trio de jazz especial progressivo psicodélico avant-garde é composta por: 


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