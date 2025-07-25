---
type: location
location_type: Building
parent:
  - "[[Montevia]]"
---
Flowered terraces climbing the cliff from [[La Citta]] up toward [[Montevia]] offer a spectacular view of the city and Wildspace as the most distinguished citizens of the city dine in one of the finest inns and restaurants of any sphere. Dress code and good conduct are enforced by not only highly payed mercenaries, but the eyes of the highest of society. The plush suites are often reserved by diplomats or other high-ranking visitors. 

![[Man O War.png|400]]

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