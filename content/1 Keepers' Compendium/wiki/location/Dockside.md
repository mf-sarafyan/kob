---
type: location
location_type: Quarter
parent:
  - "[[kob/content/1 Keepers' Compendium/wiki/location/Bragora]]"
appears_in: 
---
Distrito das docas de [[kob/content/1 Keepers' Compendium/wiki/location/Bragora|Bragora]], separado em dois pelo **Rio Maggiore**: **Riva Alta** e **Riva Bassa**.

# Riva Alta

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