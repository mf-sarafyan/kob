---
type: location
location_type: Planet
parent:
  - "[[Realmspace]]"
---
# **Glyth**

Spelljamming ships known as nautiloids (described in the Astral Adventurer’s Guide) patrol the space within 100 million miles of Glyth and hide behind the planet’s three moons. This is not surprising because mind flayers are the undisputed masters of Glyth. The planet’s air smells like it came from a charnel house, but it is not poisonous. The surface of the planet is a desolate wasteland, but beneath the crust is a labyrinth of subterranean caves inhabited by mind flayer colonies.

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