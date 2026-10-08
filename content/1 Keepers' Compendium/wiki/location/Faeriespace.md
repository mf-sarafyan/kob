---
type: location
location_type: Crystal Sphere
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Faeriespace"
campaign_setting: "Spelljammer generic"
---

# Faeriespace

Source: [Faeriespace](https://spelljammer.fandom.com/wiki/Faeriespace)

## Details
- **Setting:** Spelljammer generic
- **Inhabitants / control:** Aelivere the One-King (absolute ruler from capital Armon).

## Astral bodies
- **The Great Tree** — Enormous starbeast tree filling the sphere.
- **Sixteen suns** — Burning suns hanging from branches.
- **Upgood worlds** — Genia, Freemor, Agron, Tiqua — good-aligned branch planets.
- **Vastdarken worlds** — Morath, Krag, Beastra, Mish — evil-aligned branch planets.
- **Armon** — Capital at the trunk split.

## Lore
Magical sphere built around a colossal tree instead of a conventional sun-and-planets system. Connects to Herospace and Darkspace via Flow rivers.

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

