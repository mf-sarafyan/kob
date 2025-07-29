---
type: location
location_type: Building
parent:
  - "[[Foreign Quarter]]"
appears_in:
---
Mais glamurosa que o [[Black Dragon Inn]], o Silver Dragon conta com seguranças pra garantir que ninguém entra com armas ou armaduras, e pratos mais caros (mas com comida pra caralho). Os donos (um casal, [[Olaf Al-Azul]] e [[Sivan Al-Azul]]) falam várias línguas e trocam idéia com todo mundo. Dignitários exóticos costumam ficar por aqui. 

<!-- DYNAMIC:related-entries -->

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
    TABLE entry_type, author
    WHERE type = "entry" AND contains(relates_to, this.file.link)
    SORT file.ctime DESC
```

<!-- /DYNAMIC -->