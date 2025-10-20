---
type: faction
parent: ""
location: "[[Central Flanaess]]"
faction_type: Evil Cult
alignment: Chaotic Evil
leader: ""
appears_in: []
---
# Cult of Elemental Evil

O **Culto do Mal Elemental** é uma seita sombria dedicada à adoração das forças primordiais da destruição: ar, fogo, terra e água em seus aspectos mais caóticos e cruéis. Embora se apresentem como druídas, profetas ou reformadores, seus verdadeiros objetivos são libertar entidades elementais malignas — os Príncipes do Mal Elemental — e mergulhar o mundo em catástrofes naturais. Em Greyhawk, eles já ergueram templos, manipularam vilas inteiras e quase romperam as barreiras entre os planos elementais e o mundo material. O culto opera nas sombras, usando fanatismo, corrupção e magia devastadora para espalhar o caos.

Foram um grande inimigo das forças do bem [[Central Flanaess]], até sua derrota na [[Battle of the Emridy Meadows]].

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
