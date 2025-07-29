---
type: location
location_type: ""
parent: []
appears_in:
---
Os Reinos Distantes, fora da [[The Great Wheel]], onde entidades ininteligíveis residem. Lar e origem das Aberrações. Fora do Multiverso, e do entendimento de mentes mortais. 

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