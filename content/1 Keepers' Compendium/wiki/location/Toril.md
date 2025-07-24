---
type: location
location_type: Planet
parent:
  - "[[Realmspace]]"
---
# **Toril**

Toril, the locale of the Forgotten Realms setting, is the most populous world in Realmspace and home to some of the most powerful individuals in this system. It has regular and prosperous ties with the various nations and factions of Wildspace.

Toril’s single large moon, Selune, has a breathable atmosphere and is occupied by isolated groups of inhabitants. Toril’s space-dwelling communities generally congregate in a cluster of asteroids that trails behind Selune in the same orbit.

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