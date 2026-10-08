---
type: location
location_type: Crystal Sphere
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Korvspace"
campaign_setting: "Spelljammer generic"
---

# Korvspace

Source: [Korvspace](https://spelljammer.fandom.com/wiki/Korvspace)

## Details
- **Setting:** Spelljammer generic
- **Inhabitants / control:** Korvadan Empire (elven); Elven Imperial Navy in Kleggra's Bones; pirates and neogi in outer system.

## Astral bodies
- **Tezcat** — Fire-body primary.
- **Korvada** — Imperial homeworld with moons Xbal and Anque.
- **Trerze** — Elliptical water body.
- **Sidar** — Cube-shaped plant body.
- **Kleggra's Bones** — Asteroid belt separating inner and outer systems.
- **Glayse** — Outer water world with neogi presence.

## Lore
Elven-dominated sphere ruled from Korvada. EIN patrols the Bones against piracy and illithid incursions.

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

