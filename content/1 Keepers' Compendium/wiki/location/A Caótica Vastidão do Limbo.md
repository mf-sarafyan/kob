---
type: location
location_type: Plane
parent: []
---
https://forgottenrealms.fandom.com/wiki/Limbo

O plano na cosmologia da Grande Roda que representa o alinhamento CAÓTICO E NEUTRO. 

>Breathe the fire;  
  Walk the air;  
  Drink the earth;  
  Warm your hands at the water.

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