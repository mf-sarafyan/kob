---
type: faction
parent: ""
location: "[[The Rock of Bral|Bral]]"
faction_type: Nobility
alignment: ""
leader: "[[Andru Cozar]]"
aliases:
  - House Cozar
appears_in: []
---
# Monarquia Braliana

A liderança oficial de Bral, o monarca [[Andru Cozar]] segura o poder principalmente por controlar as terras férteis do asteróide. 

Andru orquestrou com cuidado a sucessão, organizando o assassinato de seu irmão mais velho em 6 dias de reinado, e assegurando o apoio das Famiglias. Ele conta especialmente com os [[Cartocci]] pra manter as atividades "sob controle" - pelo adequadas na visão da coroa. Permitindo dissidência suficiente pra não atrair uma total revolta, mas não o suficiente pra ser ruim pros negócios. Sempre o suficiente pra manter tudo funcionando. 

É sempre isso: a monarquia equilibra trocentos pratos pra manter o status quo, o poder, e a prosperidade deles e da cidade. Isso envolve apoiar não só a Mano Legata, mas um pouco seus oponentes, também. Permitir suas atividades, mas cortar quando a linha for cruzada.

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
