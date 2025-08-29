---
type: location
location_type: Building
parent:
  - "[[Lo Strozzo]]"
appears_in:
---
The **Council of the City** is a relatively powerless body of 30 individuals, known as "**Councilmen**", each of which represents a particular interest group in the city. These include each of the major guilds, prominent racial groups, as well as the various neighbourhoods or barrios of Bral. On occasion membership will change to reflect the fluid makeup of the population of the Rock, though appointment to the council is usually for life. At any one time, the council may include representatives from the dwarves, elves, and giff, as well as the shipwrights, merchants and nobles of the city. Unsurprisingly, each [[La Mano Legata|La Mano]] family also sends a representative to the council.

In theory, the Council of the City advises the Prince on civic affairs and can, through a unanimous vote, overturn any royal decree. Unfortunately, the members of the council are all royal appointees and, obviously enough, have never overruled the current ruling prince. Instead, the council tends to rubber stamp the prince’s edicts with little debate.

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