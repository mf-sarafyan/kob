---
type: location
location_type: Crystal Sphere
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Krynnspace"
campaign_setting: "Dragonlance"
---

# Krynnspace

Source: [Krynnspace](https://spelljammer.fandom.com/wiki/Krynnspace)

## Details
- **Setting:** Dragonlance
- **Inhabitants / control:** Krynn natives; considered primitive/pristine by other spelljamming cultures.

## Astral bodies
- **The Sun** — Fire body primary.
- **Sirrion** — Inert inner fire body.
- **Reorx** — Earth body with one moon.
- **Krynn** — Main earth body — Dragonlance setting; three moons.
- **Chislev** — Liveworld earth body.
- **Zivilyn** — Air body with twelve moons.
- **Nehzmyth** — Ovoid earth body in the Black Clouds; suspected liveworld.
- **Stellar Islands** — Asteroid cluster.

## Lore
Large, cold sphere plagued by clouds of freezing vapour. Part of the Radiant Triangle with one-way Flow routes to Realmspace and from Greyspace.

<!-- DYNAMIC:related-entries -->

# Links

## Sub-Locations
```base
filters:
  and:
    - 'type == "location"'
    - or:
        - 'list(parent).contains(this)'
        - 'list(parent).contains(this.file.asLink())'
        - 'parent == this'
        - 'parent == this.file.asLink()'
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

