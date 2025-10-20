---
title: Il Velluto
aliases:
  - Il Velluto
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: Chaotic
leader: "[[The Juggler]]"
appears_in: []
---
# Il Velluto

Led by [[The Juggler|The Juggler]].

Também "the Jugglers", são quase que o completo oposto dos [[Malvessi]]: refinados, elegantes, até artísticos. Uma máfia de bardos, artistas e golpistas que domina as operações em [[The Rock of Bral#Montevia|Montevia]]. Seu estilo é roubos de alto perfil, performáticos; que atraem mais aplausos do que horror. A fachada de glamour e escândalo deve esconder algo a mais, mas parece que a maioria está contente com isso. A alta sociedade tolera suas atividades pela fofoca que elas geram. 

Vibe: pendurar em chandeliers, roubar as jóias de um cofre impenetrável e deixar exposto em praça pública, just because.

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
