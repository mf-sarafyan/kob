---
type: location
location_type: Plane
parent: ""
---
https://forgottenrealms.fandom.com/wiki/Mechanus 

O plano na cosmologia da Grande Roda que representa o alinhamento LEAL E NEUTRO. 

> "Mechanus is a place of _rules_. Law and process. _Organization above all_. The denizens of this place disagree on how order is to be _maintained_, but in the end we _all_ serve its _structure_. Without structure, we are _nothing_."

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

**Millicent Milleau's Mille Eaus** is a renowned perfumes & potions shop, owned by a mysterious lilac-wearing lady with a special interest in the occult. 