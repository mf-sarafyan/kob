---
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: Lawful Evil
leader: "[[Don Vico Cartocci]]"
appears_in: []
---
A **famiglia Cartocci** é apenas a extensão de seu líder, [[Don Vico Cartocci]]. 

Os idealizadores de La Mano, a Cartocci é uma máfia administrada como um ministério. Toda atividade tem sua devida nota e formulário. Todo cidadão - que paga o que é devido - tem direito de recurso, e o criminoso que não cumpre as regras - rouba em duplicidade, ataca sem a licença correta - é punido com eficiência assustadora. Essa famiglia opera na base de que seguir o protocolo faz tudo funcionar melhor pra todo mundo, e tem o músculo por trás pra implementar isso. 

Vibe: Dave Bautista com mini oculos. Mafiosos de terno apertado pq são musculosos. Espancamentos com suitcase. 

# Obliviattos
A Ordem dos Obliviattos são um serviço conveniente que se tornou indispensável na cidade: uma equipe de juízes e magistrados Cartocci que operam com total garantia de sigilo, através do uso de magias e poções de esquecimento. 

Sejam contratos secretos ou criminosos, as partes podem sempre contar com a mediação e validação de um Obliviatto (pagando o preço certo, claro), sem se preocupar com vazamentos de informação. 


---

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
