---
title: Malvessi
aliases:
  - Malvessi
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: Neutral Evil
leader: ""
appears_in: []
---
# Malvessi

Os herdeiros da cultura pirática de Bral, a família Malvessi é a junção das tradições mais antigas da Pedra. 
Sob o comando do lendário Commodoro [[Roberto Malvessi]], capitães manejam cada um sua micro-gangue e seus territórios; a hierarquia e a cadeia de comando são fortes, mas na ponta, cada capitão cria suas regras. 

> They're the pirate crew gang, the Commodore's armada, and surely the crime syndicate with the most reach outside of Bral. Things can get messy, though: mutiny, theft, each pirate for themselves. True pirate crews are tight because they must; at sea (or Wildspace), you don't have anyone else to turn to. In Bral, you can become anyone else, at any time. Loyalties are hard to keep. That's where the Malvessi struggle. A great leader would keep them in line. If that was so, they'd rule the city by now. So we need a leader that is just looking out for himself.

Vibe: Set My Jib, linguajar nautico, multiplos empreendimentos. Motins. Tricornes. Cada um por si.

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
