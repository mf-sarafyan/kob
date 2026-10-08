---
type: location
location_type: Crystal Sphere
parent:
  - "[[The Phlogiston]]"
appears_in: []
source: "https://spelljammer.fandom.com/wiki/Winterspace"
campaign_setting: "Spelljammer generic"
---

# Winterspace

Source: [Winterspace](https://spelljammer.fandom.com/wiki/Winterspace)

## Details
- **Setting:** Spelljammer generic
- **Inhabitants / control:** Radole traders; Elven Imperial Navy blockading Armistice.

## Astral bodies
- **Radole** — Tidally locked trade hub with habitable equatorial ribbon.
- **Armistice** — Prison world — EIN blockade; exiled goblinoid fleet.
- **Whyst** — Ice world with spelljammer port Remagin.
- **Ryme** — Cold gas giant with mineral-rich moons.

## Lore
Cold sphere famous as trade centre (Radole) and prison world Armistice after the First Unhuman War.

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

