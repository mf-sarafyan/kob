---
type: location
location_type: Phlogiston Region
parent:
  - "[[The Phlogiston]]"
appears_in: []
author: DM
---

# Corellon's Gardens

A celebrated region of the Flow where **rainbow rivers run clear**, **floating vegetation** drifts in vast hanging gardens, and elven influence is absolute — both mundane and divine.

## Details

- **Setting:** Campaign homebrew
- **Inhabitants / control:** [[Elven Imperial Navy]] patrols; elven colonies on nearby **small spheres**; the **astral domain of Corellon** overlaps this stretch of Flow

## Notable features

- **Floating gardens** — Luminous vines, drifting groves, and pollen-sweet air; one of the most visibly "alive" tracts in the Phlogiston
- **Colonized spheres** — Minor crystal spheres claimed and settled under Imperial Fleet auspices (including [[Seldarspace|Seldar]], [[Korvspace|Korv]], [[Celenaresspace|Celenares]] on the campaign map)
- **Corellon's domain** — Sailors with the right gifts swear they can sense the god's realm **adjacent to wildspace here**, not quite in Arvandor and not quite in the Flow

## Lore

Corellon's Gardens is **beautiful and guarded**. EIN ships are everywhere — flitters on garden detail, armadas on patrol routes, men-o-war that appear when a non-elven fleet loiters too long. **Visitors without legitimate business** are escorted out; the politeness varies by captain, but the message does not.

Elves treat the Gardens as **sacred imperial space**: a living monument to Corellon and proof that the Fleet's mandate extends beyond any single sphere. Others treat it as a **no-go zone** unless invited — or unless they enjoy being "firmly redirected elsewhere."

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
