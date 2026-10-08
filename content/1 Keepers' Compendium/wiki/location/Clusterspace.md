---
type: location
location_type: Crystal Sphere
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Astromundi_Cluster"
campaign_setting: "Spelljammer (Astromundi Cluster)"
---

# Clusterspace

Source: [The Astromundi Cluster](https://spelljammer.fandom.com/wiki/Astromundi_Cluster)

## Details
- **Other names:** The Astromundi Cluster, The Shattered Sphere
- **Setting:** Spelljammer (Astromundi Cluster)
- **Inhabitants / control:** Antilan Empire (Sun Mages), Calidians, Varan, illithids, neogi, dwarves, Thoric traders, and many competing factions.

## Astral bodies
- **Firefall** — Primary — cluster of coloured fire bodies.
- **Denaeb** — Secondary sapphire sun.
- **Golden Girdle** — Richest asteroid belt; Antilan capital Mu-Thalak.
- **Inner Ring** — Heavily populated trade belt at the heart.
- **Dark Group** — Illithid-controlled asteroid clusters.
- **Great Belt / Fringe** — Outer populated belts and frontier zones.

## Lore
No full-sized planets — only asteroids and habitats. Shell is permeable to living spelljamming ships from inside but nearly impossible to exit by magic.

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

