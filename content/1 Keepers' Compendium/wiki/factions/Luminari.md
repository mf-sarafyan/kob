---
title: Luminari
aliases:
  - Luminari
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: 
leader: ""
---


Do povo, para o povo. Cansados de servir de capacho pra criminosos, lideranças de algumas guildas se juntaram pra entrar no jogo sujo também. Nada acontece na cidade sem que eles fiquem sabendo: gondoleiros, acendedores de lâmpada, limpadores de chaminés. Olhos e ouvidos em todo lugar. Os **Luminari** mantém as outras Famiglias (e quem for necessário) em cheque na base da informação, e todos preferem que eles não precisem partir pra ação. 

Vibe: Você tentando olhar o piloto da gôndola pra ver se ele tem uma tatuagem de gangue. Criança assoviando código secreto no telhado. Uma Nonna que fala manso mas pode te destruir socialmente. 


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
