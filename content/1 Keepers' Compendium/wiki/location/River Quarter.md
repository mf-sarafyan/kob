---
type: location
location_type: Quarter
parent:
  - "[[Greyhawk]]"
appears_in:
---
Tavernas e locais de entretenimento (eu acho que sei o que o livro quis dizer com isso), além das docas de Greyhawk no rio Selintan. 

É a parte mais mercantil, diversa e multicultural da cidade.

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