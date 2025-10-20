---
type: location
location_type: Quarter
parent:
  - "[[The Rock of Bral|Bral]]"
appears_in: []
image: ""
---
# Soffiera

## Soffiera
E a região mais pra baixo está de ponta-cabeça. Debaixo das docas, uma correntinha de água caindo da região de cima se mistura com fumaça vinda de baixo. O porto bloqueia a maior parte da vista, mas vocês conseguem reconhecer construções grandes de pedra e de metal. Canais que parecem o rio Pinheiros com gôndolas grandonas e cheias de caixas coloridas (tipo uns contâineres). Chaminés cuspindo fumaça preta. 

A cidade pra cima é limpinha e arrumada porque varreram o trabalho pesado aqui pra baixo. Apesar de tudo, os canais e as passarelas são maiores, tudo parece mais controlado e organizado.

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
