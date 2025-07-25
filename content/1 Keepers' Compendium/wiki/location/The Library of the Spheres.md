---
type: location
location_type: ""
parent:
  - "[[Montevia]]"
---
Serves as the regional headquarters of [[The Seekers]], and contains an impressive collection of books, tomes, scrolls, and manuscripts of all descriptions. The city of Bral is too young to warrant a library of this size, but the Seekers were forced to move two of their smaller collections to Bral about 30 years ago. These two collections account for the majority of books found in the library.

Its head librarian and keeper is [[Marvo Threnn]], an eccentric vegan mind flayer. 

![[Seekers Library.png|400]]
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