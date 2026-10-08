---
type: location
location_type: Dark Region
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/The_Weird"
campaign_setting: "Spelljammer generic"
---

# The Weird

Source: [The Weird](https://spelljammer.fandom.com/wiki/The_Weird)

## Details
- **Other names:** Vodoni name for a Dark Region
- **Setting:** Spelljammer generic
- **Inhabitants / control:** Undead (legendary); haunted ghost ships.

## Astral bodies
- **Dark Region cloud** — Inky black negative-energy region in the Flow — not a crystal sphere.

## Lore
Sinister barrier between the [[Vodoni Empire]] and the Known Spheres. Legends say anyone killed within rises as undead.

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

