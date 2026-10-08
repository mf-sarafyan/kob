---
type: location
location_type: Crystal Sphere
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: https://spelljammer.fandom.com/wiki/Doomspace
campaign_setting: Spelljammer (5e Astral Sea)
---

# Doomspace

Source: [Doomspace](https://spelljammer.fandom.com/wiki/Doomspace)

## Details
- **Setting:** Spelljammer (5e Astral Sea)
- **Inhabitants / control:** Survivors of Fyreen and Malas; no central authority.

## Astral bodies
- **Eye of Doom** — Lightless vortex at the centre — devouring former sun and remaining bodies.
- **Fyreen** — Volcanic world, partially plundered.
- **Malas** — Former water world, now ice-covered.
- **En (remnants)** — Former gas giant; substance used to build the crystal shell.
- **Crystal shards** — Asteroid-sized shell fragments.

## Lore
Recently destroyed system: returning gods collapsed the sun into the Eye of Doom after inhabitants refused worship. (5e Astral Sea canon.)

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

