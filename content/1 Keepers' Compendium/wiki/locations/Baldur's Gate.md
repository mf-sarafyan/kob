---
type: location
location_type: City
parent: "[[Realmspace]]"
---
O Rio de Janeiro da Costa da Espada. 

---
## Factions Based Here
```dataview
TABLE faction_type, alignment
WHERE type = "faction" AND location = this.file.link
SORT file.name ASC
```

## Sub-Locations
```dataview
TABLE location_type
WHERE type = "location" AND contains(parent, this.file.link)
SORT file.name ASC
```

## Related Entries
```dataview
LIST map("!" + "[[" + file.name + "]]")
WHERE type = "entry" AND contains(about, this.file.link)
SORT file.ctime DESC
```
