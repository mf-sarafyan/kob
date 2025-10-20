---
type: faction
parent: "[[Keepers of the Balance]]"
location: ""
faction_type: Adventurer Party
alignment: Good
leader: "[[Captain Jordal Brambletopple|Jordal]]"
appears_in: []
---
# kbα1

![[kb-alpha-1 1.bmp|350]] 

**kbα1**
*Dragonfly-class Spelljammer*
- Luxury Spelljammer
- Carefully made hypoallergenic for Captain Jordal
- Extremely hihg speed


## kbα1
*Keepers of the Balance, Alpha-one squad* se refere tanto à nave quanto ao lendário grupo de aventureiros interplanares e interdimensionais. Quando eles não estão lidando com ameaças de escala cósmica, eles lecionam na [[Guilde Adventureir Extraordinaire]], onde cada um - com exceção da constructa mágica - tem um ou dois pupilos, protegidos, aprendizes: vocês.

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
