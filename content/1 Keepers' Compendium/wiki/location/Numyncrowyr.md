---
type: location
location_type: Planar Region
parent:
  - "[[Astral Sea]]"
appears_in: []
image: ""
---
# Numyncrowyr

Planar region of the [[Astral Sea]] bordering the Phlogiston at [[The Red Tide]].

Mariners and scholars agree that Numyncrowyr—like the Red Tide beside it—is a place steeped in **anger, hatred, and conflict**. Fleets that skirt the border report frayed tempers, old grudges reignited, and violence that feels out of proportion to the provocation. Beyond that, reliable knowledge is scarce: unlike the well-traveled reaches of the [[The Phlogiston|Phlogiston]], Numyncrowyr has **few charted routes**, little settled trade, and almost no authority willing to claim responsibility for what lies inside.

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
