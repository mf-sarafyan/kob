---
type: character
race: ""
class: ""
origin: "[[Baldur's Gate]]"
known_locations: []
factions: []
alignment: ""
---

<!-- DYNAMIC:related-entries -->

## Related Entries

```dataview
    TABLE entry_type, author
    WHERE type = "entry" AND contains(relates_to, this.file.link)
    SORT file.ctime DESC
```

<!-- /DYNAMIC -->