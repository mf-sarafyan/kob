---
title: Luminari
aliases:
  - Luminari
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: ""
leader: ""
appears_in: []
---
# Luminari

Do povo, para o povo. Cansados de servir de capacho pra criminosos, lideranças de algumas guildas se juntaram pra entrar no jogo sujo também. Nada acontece na cidade sem que eles fiquem sabendo: gondoleiros, acendedores de lâmpada, limpadores de chaminés. Olhos e ouvidos em todo lugar. Os **Luminari** mantém as outras Famiglias (e quem for necessário) em cheque na base da informação, e todos preferem que eles não precisem partir pra ação. 

Vibe: Você tentando olhar o piloto da gôndola pra ver se ele tem uma tatuagem de gangue. Criança assoviando código secreto no telhado. Uma Nonna que fala manso mas pode te destruir socialmente.

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
