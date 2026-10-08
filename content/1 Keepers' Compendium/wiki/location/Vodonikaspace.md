---
type: location
location_type: Crystal Sphere
parent:
  - "[[Vodoni Empire]]"
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Vodonikaspace"
campaign_setting: "Spelljammer (Vodoni Empire)"
---

# Vodonikaspace

Source: [Vodonikaspace](https://spelljammer.fandom.com/wiki/Vodonikaspace)

## Details
- **Setting:** Spelljammer (Vodoni Empire)
- **Inhabitants / control:** Vodoni Empire — largest enforcer garrison and military shipyards.

## Astral bodies
- **Vodonika** — Capital ('New Vodoni') — main forge of Vodoni military.
- **Four other planets** — All five habitable worlds densely populated.

## Lore
Military-industrial backbone of the empire; previous inhabitants eradicated after the Vodoni exodus.

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

