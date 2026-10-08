---
type: location
location_type: Crystal Sphere
parent:
  - "[[Vodoni Empire]]"
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Gorthspace"
campaign_setting: "Spelljammer (Vodoni Empire)"
---

# Gorthspace

Source: [Gorthspace](https://spelljammer.fandom.com/wiki/Gorthspace)

## Details
- **Setting:** Spelljammer (Vodoni Empire)
- **Inhabitants / control:** Vodoni Empire — shore-leave bases; no known sentient natives.

## Astral bodies
- **Gorth** — Only habitable planet — lush ancient forests, no sentient life.

## Lore
Centrally located Vodoni sphere used as hunting ground and shore-leave destination for enforcers.

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

