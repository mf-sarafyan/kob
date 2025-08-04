---
type: location
location_type: Quarter
parent:
  - "[[Greyhawk]]"
appears_in:
---
Construído ao redor de um grande mercado, o **Artisan's Quarter** de Greyhawk é onde vivem e trabalham os mais finos artesãos, e onde ficam as guildas da cidade.

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