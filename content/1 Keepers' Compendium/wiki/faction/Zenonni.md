---
title: Zenonni
aliases:
  - Zenonni
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: ""
leader: ""
appears_in: []
---
# Zenonni

Sempre existiram em Bral as tripulações que aceitavam os rejeitados, os esquecidos, os alienígenas. Os Xenos. Zenonni - o nome nasceu daí - é sua união que aceita o diferente com apêndices sortidos abertos. Seu símbolo é um aperto de mãos com um tentáculo. Uma congregação ferozmente leal de entidades esquisitas. Você mexe com um primo, você mexeu com todos. 

Muitos negócios únicos em Bral tem donos únicos - imagine bibliotecários mind flayers, ou o próprio Luigi - e eles se ajudam através dessa família. 

Vibe: um ogro e um gith andando juntos. Um fornecedor de poções de Alter Self. 

Os Zenonni não são exatamente um grupo sumarizável: eles são um grupo de poucos indivíduos muito influentes, cada um de sua maneira.

<!-- DYNAMIC:related-entries -->

# Links

## Member Characters
```base
filters:
  and:
    - 'type == "character"'
    - or:
        - 'list(factions).contains(this)'
        - 'list(factions).contains(this.file.asLink())'
        - 'factions == this'
        - 'factions == this.file.asLink()'
properties:
  file.name:
    displayName: "Name"
  race:
    displayName: "Race"
  class:
    displayName: "Class"
  alignment:
    displayName: "Alignment"
views:
  - type: table
    name: "Member Characters"
    order:
      - file.name
      - race
      - class
      - alignment
  - type: cards
    name: "Member Characters (Cards)"
```

## Child Factions
```base
filters:
  and:
    - 'type == "faction"'
    - or:
        - 'parent == this'
        - 'parent == this.file.asLink()'
        - 'list(parent).contains(this)'
        - 'list(parent).contains(this.file.asLink())'
properties:
  file.name:
    displayName: "Name"
  faction_type:
    displayName: "Type"
  alignment:
    displayName: "Alignment"
views:
  - type: table
    name: "Child Factions"
    order:
      - file.name
      - faction_type
      - alignment
  - type: cards
    name: "Child Factions (Cards)"
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
  entry_type:
    displayName: "Type"
  author:
    displayName: "Author"
views:
  - type: table
    name: "Related Entries"
    order:
      - file.ctime
  - type: cards
    name: "Related Entries (Cards)"
```

<!-- /DYNAMIC -->
