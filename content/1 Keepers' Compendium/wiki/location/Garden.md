---
type: location
location_type: Astral Body
parent:
  - "[[Realmspace]]"
---
# **Garden**

Garden is a cluster of seven planetoids inside a common air envelope, each of them linked to the others by the roots of an unimaginably large plant sometimes referred to as Yggdrasil’s Child. Wildspace travelers sometimes come to Garden to restock their food, water, and air.

Garden is a refuge for spacefaring pirates, who hide their spelljamming ships in the maze of passageways that run between Yggdrasil’s Child and the planetoids, and might do the same in the craters and canyons on any of Garden’s eleven moons.

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