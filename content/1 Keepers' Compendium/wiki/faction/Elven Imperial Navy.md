---
type: faction
parent: ""
location: "[[The Phlogiston|Phlogiston]]"
faction_type: Galactic Organization
alignment: ""
leader: ""
appears_in:
  - "[[unhuman-wars]]"
---
# Elven Imperial Navy

The Elven Imperial Navy is the most powerful and far-reaching naval force in Wildspace, a vast interstellar empire commanded by the elves of the Imperial Fleet. Operating from living starships grown from enchanted wood, the Armada serves both as a military power and a colonial authority, projecting elven influence across crystal spheres. Its officers are disciplined, aloof, and often convinced of their cultural superiority, enforcing order (and elven interests) with quiet efficiency. While they claim to defend the flow of trade and suppress threats such as orcish hordes and neogi slavers, many view the Armada as an imperial force first and a protector second—its presence as likely to impose as to assist.



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
