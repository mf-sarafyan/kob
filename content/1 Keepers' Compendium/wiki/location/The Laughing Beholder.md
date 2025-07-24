---
type: location
location_type: Building
parent:
  - "[[Bragora]]"
---
**The Laughing Beholder** is a staple of the Low City, owned by its namesake, the smiling **[[Luigi Zenonni|Large Luigi]]** - who often mixes and delivers drinks using his *telekinesis eye rays*. His second-in-command is Commodore Krux, who also takes care of Luigi's green parrot. It is a spacious inn with a very high ceiling - so the owner can float around - held up by arched pillars in red and gold, and serves not only local Brailian ales and wines but from all over the Known Spheres.

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