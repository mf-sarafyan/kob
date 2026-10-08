---
type: location
location_type: Crystal Sphere
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Herospace"
campaign_setting: "Spelljammer generic"
---

# Herospace

Source: [Herospace](https://spelljammer.fandom.com/wiki/Herospace)

## Details
- **Setting:** Spelljammer generic
- **Inhabitants / control:** Rational Order of Magistrates (headquarters on moon Borden).

## Astral bodies
- **Nine suns + nine worlds** — Each small sun orbits one alignment-themed planet.
- **Gondorin** — Lawful Good world.
- **Ge'Neva** — Neutral Good world; seat of the Magistrates.
- **Chaostromme** — Chaotic Evil world.
- **Asylum** — True Neutral world.

## Lore
Alignment-segregated sphere: residents must prove worthiness to the Magistrates to settle on their matching world.

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

