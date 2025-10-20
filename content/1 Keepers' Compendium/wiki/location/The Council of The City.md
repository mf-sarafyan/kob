---
type: location
location_type: Building
parent:
  - "[[Lo Strozzo]]"
appears_in: []
image: ""
---
# The Council of The City

The **Council of the City** is a relatively powerless body of 30 individuals, known as "**Councilmen**", each of which represents a particular interest group in the city. These include each of the major guilds, prominent racial groups, as well as the various neighbourhoods or barrios of Bral. On occasion membership will change to reflect the fluid makeup of the population of the Rock, though appointment to the council is usually for life. At any one time, the council may include representatives from the dwarves, elves, and giff, as well as the shipwrights, merchants and nobles of the city. Unsurprisingly, each [[La Mano Legata|La Mano]] family also sends a representative to the council.

In theory, the Council of the City advises the Prince on civic affairs and can, through a unanimous vote, overturn any royal decree. Unfortunately, the members of the council are all royal appointees and, obviously enough, have never overruled the current ruling prince. Instead, the council tends to rubber stamp the prince’s edicts with little debate.

<!-- DYNAMIC:related-entries -->

# Links

## Sub-Locations
```base
# Only show locations whose 'parent' includes *this* location
filters:
  and:
    - 'type == "location"'
    - or:
        - 'list(parent).contains(this)'
        - 'list(parent).contains(this.file.asLink())'
        - 'parent == this'
        - 'parent == this.file.asLink()'

# Column labels
properties:
  file.name:
    displayName: "Name"
  location_type:
    displayName: "Type"
  parent:
    displayName: "Parent"

views:
  - type: table
    name: "Sub-Locations"
    order:
      - file.name
      - location_type
      - parent
  - type: cards
    name: "Sub-Locations (Cards)"
```

## Factions Based Here
```base
filters:
  and:
    - 'type == "faction"'
    - or:
        - 'location == this'
        - 'location == this.file.asLink()'
        - 'list(location).contains(this)'
        - 'list(location).contains(this.file.asLink())'
properties:
  file.name:
    displayName: "Name"
views:
  - type: table
    name: "Factions Based Here"
    order:
      - file.name
  - type: cards
    name: "Factions (Cards)"
```

## Related Entries
```base
filters:
  and:
    - 'type == "entry"'
    - or:
        - 'list(relates_to).contains(this)'
        - 'list(relates_to).contains(this.file.asLink())'
properties:
  file.name:
    displayName: "Name"
views:
  - type: table
    name: "Related Entries"
    order:
      - file.ctime
  - type: cards
    name: "Related Entries (Cards)"
```

<!-- /DYNAMIC -->
