---
type: location
location_type: Crystal Sphere
parent:
  - "[[Vodoni Empire]]"
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Vergonspace"
campaign_setting: "Spelljammer (Vodoni Empire)"
---

# Vergonspace

Source: [Vergonspace](https://spelljammer.fandom.com/wiki/Vergonspace)

## Details
- **Setting:** Spelljammer (Vodoni Empire)
- **Inhabitants / control:** Warlike Vergon on six planets; Vodoni divide-and-rule occupation.

## Astral bodies
- **Six planets** — Worlds at war with each other for centuries under Vodoni manipulation.

## Lore
Vodoni deliberately keep the Vergon divided. After Vulkaran's fall they could retake the system if they united.

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

