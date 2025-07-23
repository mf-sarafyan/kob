---
title: Cult of Elemental Evil
type: faction
parent: ""
location: "[[Greyhawk]]"
faction_type: Evil Cult
alignment: Evil
---
O **Culto do Mal Elemental** é uma seita sombria dedicada à adoração das forças primordiais da destruição: ar, fogo, terra e água em seus aspectos mais caóticos e cruéis. Embora se apresentem como druídas, profetas ou reformadores, seus verdadeiros objetivos são libertar entidades elementais malignas — os Príncipes do Mal Elemental — e mergulhar o mundo em catástrofes naturais. Em Greyhawk, eles já ergueram templos, manipularam vilas inteiras e quase romperam as barreiras entre os planos elementais e o mundo material. O culto opera nas sombras, usando fanatismo, corrupção e magia devastadora para espalhar o caos.


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
