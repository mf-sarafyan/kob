---
type: location
location_type: Building
parent:
  - "[[La Citta]]"
---
[[kob/content/1 Keepers' Compendium/wiki/character/Vax|Vax]] - Cat Maid Cafe? Gatos e Tabaxis. Os gatos tem roupas de maid. **Gatto QuiLatte.** Hot cocoa e cafézinhos. Middle City. Pub.

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