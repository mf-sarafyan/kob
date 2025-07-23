---
type: location
location_type: Plane
parent: ""
---
https://forgottenrealms.fandom.com/wiki/Mechanus 

O plano na cosmologia da Grande Roda que representa o alinhamento LEAL E NEUTRO. 

> "Mechanus is a place of _rules_. Law and process. _Organization above all_. The denizens of this place disagree on how order is to be _maintained_, but in the end we _all_ serve its _structure_. Without structure, we are _nothing_."

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