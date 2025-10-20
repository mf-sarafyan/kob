---
type: location
location_type: Plane
parent:
  - "[[The Great Wheel]]"
appears_in: []
image: ""
---
# Nove Infernos de Baator

O plano que encarna o **Lawful Evil**; lar dos diabos. 

Dividido em nove níveis, cada um liderado por seu arquidiabo: 
- [[Avernus]], e [[Zariel]]
- [[Dis]], e [[Dispater]]
- [[Minauros]], e [[Mammon]]
- [[Phlegethos]], e [[Belial]] e [[Fierna]]
- [[Stygia]], e [[Levistus]]
- [[Malbolge]], e [[Glasya]]
- [[Maladomini]], e [[Baalzebul]]
- [[Cania]], e [[Mephistopheles]]
- Finalmente, [[Nessus]], a morada do próprio [[Asmodeus]].

<!-- DYNAMIC:related-entries -->

# Links

## Sub-Locations
```base
# Only show locations whose 'parent' includes *this* location
filters:
  and:
    - 'type == "location"'
    - or:
        - 'list(parent).contains(this)'
        - 'list(parent).contains(this.file.asLink())'
        - 'parent == this'
        - 'parent == this.file.asLink()'

# Column labels
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
