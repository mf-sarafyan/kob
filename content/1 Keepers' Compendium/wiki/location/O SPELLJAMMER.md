---
type: location
location_type: Ship
parent:
  - "[[kob/content/1 Keepers' Compendium/wiki/location/Astral Sea|Astral Sea]]"
appears_in: []
image: ""
aliases:
  - The Spelljammer
---
# O SPELLJAMMER
Como a WOTC odeia clareza em suas nomeclaturas, além do **Spelljammer** (nome da campanha) e dos **Speljammers** (embarcações mágicas que cruzam o espaço e o astral), existe **O** **SPELLJAMMER** (Spelljammer-class Spelljammer), uma lendária cidade-nave viva, a maior do seu tipo; teorizado ser tão velho quanto as Esferas, tripulado por constructos que ele próprio produzia, habitado por criaturas que eram magicamente *encantadas* por ele, e cercado de lendas, mistérios, e tesouros. 

Ele parece uma mistura entre arraia e escorpião, com as asas longas, rabo retorcido pra cima, e castelos construídos no topo. 

## Smalljammers
Como uma criatura viva, ele se reproduz (sério). Ele tem filhotinhos que são versões pequenininhas dele, chamados **Smalljammers**. Se um dia **O SPELLJAMMER** é destruído - como já foi presenciado, num ataque de uma frota de dezenas de navios neogi - ele emite um sinal metafísico através do plano etério que causa o crescimento do Smalljammer mais próximo, que em menos de um ano cresce a ponto de assumir o manto de **O SPELLJAMMER**.

<!-- DYNAMIC:related-entries -->

# Links

## Sub-Locations
```base
# Only show locations whose 'parent' includes *this* location
filters:
  and:
    - 'type == "location"'
    - or:
        - 'list(parent).contains(this)'
        - 'list(parent).contains(this.file.asLink())'
        - 'parent == this'
        - 'parent == this.file.asLink()'

# Column labels
properties:
  file.name:
    displayName: "Name"
  location_type:
    displayName: "Type"
  parent:
    displayName: "Parent"

views:
  - type: table
    name: "Sub-Locations"
    order:
      - file.name
      - location_type
      - parent
  - type: cards
    name: "Sub-Locations (Cards)"
```

## Factions Based Here
```base
filters:
  and:
    - 'type == "faction"'
    - or:
        - 'location == this'
        - 'location == this.file.asLink()'
        - 'list(location).contains(this)'
        - 'list(location).contains(this.file.asLink())'
properties:
  file.name:
    displayName: "Name"
views:
  - type: table
    name: "Factions Based Here"
    order:
      - file.name
  - type: cards
    name: "Factions (Cards)"
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
views:
  - type: table
    name: "Related Entries"
    order:
      - file.ctime
  - type: cards
    name: "Related Entries (Cards)"
```

<!-- /DYNAMIC -->
