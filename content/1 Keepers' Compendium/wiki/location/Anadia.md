---
type: location
location_type: Planet
parent:
  - "[[Realmspace]]"
---
# **Anadia**

The surface of Anadia is an expanse of badlands and dry washes except at its poles, where the land flattens out into gently rolling, fertile hills dotted with forests and patches of grassland. Communities of halflings occupy the polar areas, while the barren wastes are populated by monstrous predators and scavengers.

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