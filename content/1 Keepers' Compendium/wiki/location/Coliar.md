---
type: location
location_type: Planet
parent:
  - "[[Realmspace]]"
---
# **Coliar**

This gas giant has a multitude of earth and water islands swirling around in its turbulent winds. These islands are occupied mostly by aarakocra, lizardfolk, and dragons. The lizardfolk, in particular, are accustomed to trading with spacefaring folk.

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