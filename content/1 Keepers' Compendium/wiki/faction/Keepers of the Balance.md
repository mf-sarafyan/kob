---
type: faction
parent: ""
location: ""
faction_type: ""
alignment: ""
leader: "[[Mordenkainen]]"
aliases:
  - KOTB
---
A organização central da campanha; que concentra os esforços de [[Mordenkainen]] para manter a [[Blood War]] em equilíbrio.

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