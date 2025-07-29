---
type: location
location_type: Dungeon
parent:
  - "[[Viscondado de Verbobonc]]"
appears_in:
---
Teoricamente abandonado, era a fonte de hordas malignas de monstros sanguinários que perambulavam pelas terras de [[Central Flanaess]]. Base do antigo [[Cult of Elemental Evil]].

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