---
title: Cult of Iuz
type: faction
parent: ""
location: "[[Greyhawk]]"
faction_type: Evil Cult
alignment: Evil
---
O culto de Iuz venera o semideus tirano [[Iuz]], uma figura aterrorizante que é ao mesmo tempo humano, demônio e deus. Governante cruel do norte de Flanaess, Iuz busca expandir seu império de terror através de guerra, necromancia e corrupção. Seus seguidores — necromantes, demônios, fanáticos e mortos-vivos — atuam como infiltradores, sabotadores e agentes do medo. Mais do que conquista territorial, o culto deseja impor o domínio absoluto de Iuz sobre corpo e alma, transformando o mundo num reflexo de sua vontade caótica e cruel.


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
