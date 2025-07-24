---
type: location
location_type: Planet
parent:
  - "[[Realmspace]]"
---
# **Chandos**

Chandos is a large water world with thousands of floating islands that often collide with one another, making these locations less than ideal for permanent settlements. Beneath the islands, in the depths of Chandos, live all sorts of bioluminescent aquatic creatures.

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