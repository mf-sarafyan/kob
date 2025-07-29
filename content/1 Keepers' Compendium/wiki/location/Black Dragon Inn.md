---
type: location
location_type: Building
parent:
  - "[[Clerkburg]]"
appears_in:
---
Uma taverna de 3 andares e meio detonada, apresentada por uma placa com um dragão negro sorridente. Comida boa e quartos baratos. O dono do lugar é [[Miklos Dare]], um veterano de guerra que participou da [[Battle of the Emridy Meadows]]. Tem uma rivalidade amistosa com o [[Silver Dragon Inn]]. 

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