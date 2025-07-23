---
type: faction
parent: ""
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: 
leader: "[[Serena Blackwood]]"
---
Gangue piromaníaca de [[Serena Blackwood]], que lidera uma facção anti-establishment que quer destruir o domínio da [[Bral Minor Factions#La Mano Legata|Mano Legata]]. 

Vibe punk-rock, molotovs, Jinx. 



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
