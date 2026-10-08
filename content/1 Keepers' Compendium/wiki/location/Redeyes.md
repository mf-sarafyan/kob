---
type: location
location_type: Crystal Sphere
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Redeyes"
campaign_setting: "Spelljammer generic"
---

# Redeyes

Source: [Redeyes](https://spelljammer.fandom.com/wiki/Redeyes)

## Details
- **Setting:** Spelljammer generic
- **Inhabitants / control:** Scavvers, space stirges, reavers, rogue death tyrant; contested human/illithid border zone.

## Astral bodies
- **Two dark red fire bodies** — Pair of very large suns dominating the sphere.
- **Battlefield debris** — Vast salvage fields from human/illithid conflicts.

## Lore
Huge sphere between human- and illithid-dominated Flow regions, littered with war debris. Many guilds require a space stirge corpse from Redeyes as an initiation rite.

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

