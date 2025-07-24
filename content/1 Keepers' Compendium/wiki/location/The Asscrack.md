---
type: location
location_type: Building
parent:
  - "[[The Rock of Bral|Bral]]"
  - "[[Bragora]]"
---
[[Bad Juju]] - Tavern num barco estacionado no beco atrás do [[The Baank - Lucky Ones]]. Cramped e seedy. Barco de 2 andares. Bem rude com [[Cartocci]]s e afins. [[Cinders]] no bar. Usados pra delivery também. Ajudam a entregar coisas do Gizmo. Bartender tubarao humanoide (wereshark?). Punks, drags e punks drags. ***The Asscrack?***

Tem ajuda de [[Krik'Lit]] e [[Pffred]] também.

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