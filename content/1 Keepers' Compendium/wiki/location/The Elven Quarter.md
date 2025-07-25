---
type: location
location_type: Park
parent:
  - "[[La Citta]]"
aliases:
  - Il Bosco
---
Against the walls where [[La Citta]] meets [[Viscura]], right below [[The Man O War]] in [[Montevia]], a miracle grows amid the city: a mystical grove of enchanted birch, laurel, ash and oak trees, many of which appear to be several hundred years old; possibly the most beautiful place in the asteroid. Enchantments ensure those who have no business there quickly find themselves outside, in marvel and slight confusion. 

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