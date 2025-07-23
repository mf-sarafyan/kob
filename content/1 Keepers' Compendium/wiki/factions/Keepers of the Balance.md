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


---

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
LIST map("!" + "[[" + file.name + "]]")
WHERE type = "entry" AND contains(about, this.file.link)
SORT file.ctime DESC
```
