---
type: location
location_type: Building
parent:
  - "[[La Citta]]"
  - "[[The Rock of Bral|Bral]]"
---
Gambling Hall/Stock Exchange. **The Baank**: "feeling lucky?" / **Lucky Ones**: 2 d20s rolando 1. Aprendizes do Il Veluto como crupies. 4 hirelings. Gerente Dick Vigarista? 

Dono: [[Baang]]
Funcionários frequentes: [[Pffred]], [[Krik'Lit]]

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