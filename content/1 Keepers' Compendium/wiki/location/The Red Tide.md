---
type: location
location_type: Phlogiston Region
parent:
  - "[[The Phlogiston]]"
appears_in: []
author: DM
---

# The Red Tide

A darker stretch of the Flow on the **frontier between the Phlogiston and [[Numyncrowyr]]** — where the rainbow rivers run thin and the near Flow bleeds influence inward.

## Details

- **Setting:** Campaign homebrew
- **Inhabitants / control:** No fixed sovereignty; transient spelljamming traffic, frontier outposts, and whatever rides the currents through the border
- **Character:** A **darker Phlogiston** zone, often flooded with **dark red energy waves** that roll out of the adjacent near Flow

## Notable features

- **Crimson surges** — Periodic waves of deep red light through the Flow; visibility drops, helms feel sluggish, and tempers shorten
- **The Numyncrowyr border** — Mariners treat crossing here as leaving "ordinary" phlogiston currents and entering something older and more volatile

## Lore

Sailors say the Red Tide **brings angry, warmongering feelings** to those caught in a surge — brawls on deck, rash course changes, feuds that outlast the voyage. **Elven captains** especially claim the effect is not confined to ships: the waves **touch spheres downstream**, stirring unrest among folk who never left their world.

Whether that is metaphysics, superstition, or something leaking from [[Numyncrowyr]] is unsettled. Most fleets **harden watches** when the sky turns red and avoid lingering on the border longer than they must.

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
