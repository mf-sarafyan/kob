---
type: location
location_type: Building
parent:
  - "[[La Citta]]"
---
An impressive stadium of the same white granite used in the palace. Although the Arena can seat 500 people comfortably, the facility is rarely opened to the public. Once a year, on Charter Day (the anniversary of Cozar's coronation), a series of games and races, including jumping contests and mock gladiatorial fights, are held for the public to celebrate.

While these contests may attract some attention, most of the more bloodthirsty citizens of the city prefer to patronize the illegal pit fights of the Low City. The Arena is occasionally used by duelists as a neutral ground to resolve their differences.

The Arena sits by the cliff, with additional, extra-fancy balconies climbing the steps up; and some of its facilities extend into [[Viscura]].

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