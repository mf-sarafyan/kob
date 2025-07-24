---
type: location
location_type: Building
parent:
  - "[[Soffiera]]"
---
[[kob/content/1 Keepers' Compendium/wiki/character/Gizmo|Gizmo]] - Workshop : Sem nome. [[Wizpop]] trabalha, plus um Giff. Soffiera. Mascara de solda e avental de couro. Vendem pra todos - especialmente Cinders. [[Kurrzot]] carrega coisas.

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