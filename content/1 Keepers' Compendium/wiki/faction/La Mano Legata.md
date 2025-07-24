---
title: La Mano Legata
aliases:
  - La Mano
  - La Mano Legata
type: faction
parent: ""
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Conglomerate
alignment: ""
leader: ""
---
Tripulações e gangues sempre disputaram poder e influência, frequentemente até em plena luz do dia. Nos últimos anos, cinco dessas Famiglias chegaram num acordo tênue de que o conflito faz mal pros negócios, e desde então, a cidade entrou num estado de desgoverno organizado, e as cinco famílias cresceream sua influência significativamente. 

O símbolo do acordo é uma mão fechada, com um anel em cada dedo.

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