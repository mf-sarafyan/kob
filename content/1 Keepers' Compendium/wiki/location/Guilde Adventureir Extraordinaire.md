---
type: location
location_type: Building
parent:
  - "[[Baldur's Gate]]"
appears_in: []
image: ""
---
Uma mansao em [[Baldur's Gate]] onde jovens prodígios sao treinados pra serem aventureiros. Podem vir de qqr lugar - de nepotismo e investimento a adoção ou ate resocializacao. Tem um sistema de mestre-aprendiz, e os pcs sao aprendizes da main party.



# **Anadia**

The surface of Anadia is an expanse of badlands and dry washes except at its poles, where the land flattens out into gently rolling, fertile hills dotted with forests and patches of grassland. Communities of halflings occupy the polar areas, while the barren wastes are populated by monstrous predators and scavengers.

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
