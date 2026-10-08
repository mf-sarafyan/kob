---
type: location
location_type: Crystal Sphere
parent:
  - "[[The Phlogiston]]"
appears_in: []
author: DM
---
# Sendospace

An unlucky crystal sphere caught between the borders of the [[Vodoni Empire]] and the [[Illithid Dominion]]. Sendo is unnaturally rich in **Mythral** and **adamantine**, which has made it disputed territory and the site of unceasing warfare for as long as anyone in the Flow can remember.

## Details

- **Other names:** Sendo (map label)
- **Setting:** Campaign homebrew
- **Inhabitants / control:** No stable imperial authority — battleground of Vodoni and Illithid interests; the Sendotalians endure on Sendotale
- **Resources:** Mythral and adamantine deposits across the sphere (heavily fought over)

## Astral bodies

- **Sendotale** — Jungle world; the only slightly hospitable body in the sphere. Home to the Sendotalian civilization and their hidden volcanic forges.

## The Sendotalians

The one slightly hospitable body in the sphere is the jungle planet **Sendotale**. During lulls between the great powers’ wars, pirates, mercenaries, and adventurers were drawn to the world and its riches. Over time they consolidated into a scrappy civilization: the **Sendotalians**.

In underground forges hidden from Vodoni and Illithid alike, they developed a fighting, survival-focused culture. They built **volcanic forges** to alloy the planet’s metals into **Deskar** — a light, extremely resistant material. Deskar gear is deeply personal and sacred to them; Sendo mercenaries are highly valued across the Flow for their equipment and their ability to operate in the sphere’s perpetual conflict.

![[sendotalian.png]]

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
