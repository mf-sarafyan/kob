---
type: location
location_type: Astral Empire
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: https://spelljammer.fandom.com/wiki/Vodoni_Empire
campaign_setting: Spelljammer generic
---

# Vodoni Empire

Source: [Vodoni Empire](https://spelljammer.fandom.com/wiki/Vodoni_Empire)

## Details
- **Setting:** Spelljammer generic
- **Inhabitants / control:** Emperor Vulkaran the Dark; Vodoni enforcers, breeders, and subject peoples across 12 spheres.

## Astral bodies
- **[[Vodonispace]]** — Imperial capital sphere.
- **[[Vodonikaspace]]** — Military-industrial hub.
- **[[Zelanispace]]** — Zalani shipyards.
- **[[Golotspace]]** — Dragon-ruled human sphere.
- **[[Gorthspace]]** — Forest shore-leave sphere.
- **[[Kofuspace]]** — Solid-sphere anomaly.
- **[[Passarspace]]** — Mining/asteroid sphere.
- **[[Salzarspace]]** — Magic-dead water-sphere.
- **[[Vergonspace]]** — Six warring planets.
- **Kra'akenspace** — Ruins searched for lost magic.
- **Lostspace** — Deserted ruins.
- **Thasiaspace** — Jungle world Thasia.

## Lore
Stable configuration of twelve mutually connected spheres conquered by Vulkaran. Invaded the Known Spheres across [[The Weird]].

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

