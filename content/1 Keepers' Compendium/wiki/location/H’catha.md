---
type: location
location_type: Planet
parent:
  - "[[Realmspace]]"
---
# **H’catha**

H’catha is a disk of water floating in space, with a single large mountain called the Spindle jutting from its center. The water disk tapers at the edge to form a rim. The Spindle is 200 miles across at its base, and tapers to a peak 1,000 miles above the surface of the water. The caverns inside the Spindle are home to five warring subspecies of beholders.

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