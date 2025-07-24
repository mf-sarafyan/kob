---
type: location
location_type: Planet
parent:
  - "[[Realmspace]]"
---
# **Karpri**

This water world has icecaps at its poles and vegetation-choked waters in its equatorial region. In between, on either side of the equatorial zone, are bands of featureless ocean—nothing but water as far as the eye can see. Most of the planet’s indigenous creatures are aquatic and dwell in the tropical sargasso, since the planet has no land masses that can support life.

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