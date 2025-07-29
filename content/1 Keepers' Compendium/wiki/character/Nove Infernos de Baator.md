---
type: location
location_type: Plane
parent:
  - "[[The Great Wheel]]"
appears_in:
---
O plano que encarna o **Lawful Evil**; lar dos diabos. 

Dividido em nove níveis, cada um liderado por seu arquidiabo: 
- [[Avernus]], e [[Zariel]]
- [[Dis]], e [[Dispater]]
- [[Minauros]], e [[Mammon]]
- [[Phlegethos]], e [[Belial]] e [[Fierna]]
- [[Stygia]], e [[Levistus]]
- [[Malbolge]], e [[Glasya]]
- [[Maladomini]], e [[Baalzebul]]
- [[Cania]], e [[Mephistopheles]]
- Finalmente, [[Nessus]], a morada do próprio [[Asmodeus]].

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