
```base
filters:
  and:
    - type == "character"
    - factions.contains("kbβ42")
properties:
  file.name:
    displayName: Name
  class:
    displayName: Class
  race:
    displayName: Race
  origin:
    displayName: Origin
views:
  - type: table
    name: Crew members
    order:
      - file.name
      - class
      - race
      - origin
    columnSize:
      note.class: 193
      note.race: 181

```

