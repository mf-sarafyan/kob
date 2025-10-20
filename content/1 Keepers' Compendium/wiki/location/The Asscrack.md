---
type: location
location_type: Building
parent:
  - "[[kob/content/1 Keepers' Compendium/wiki/location/Bragora]]"
appears_in: []
image: ""
---
# The Asscrack

[[Bad Juju]] - Tavern num barco estacionado no beco atrás do [[The Baank - Lucky Ones]]. Cramped e seedy. Barco de 2 andares. Bem rude com [[Cartocci]]s e afins. [[Cinders]] no bar. Usados pra delivery também. Ajudam a entregar coisas do Gizmo. Bartender tubarao humanoide (wereshark?). Punks, drags e punks drags. ***The Asscrack?***

Tem ajuda de [[Krik'Lit]] e [[Pffred]] também.

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
