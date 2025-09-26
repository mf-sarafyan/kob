---
type: location
location_type: Sub-district
parent: "[[Bragora]]"
appears_in: []
image: "[[dwarvendistrictmj.png]]"
---

# Dwarven District

**Dwarven District** é o subdistrito mais sólido de Bragora, literalmente. As ruas são calçadas em pedra perfeitamente encaixada, as casas parecem fortificações e até as tavernas têm colunas grossas como muralhas. É um bairro de guildas, oficinas e cervejarias, onde cada pedra carrega o orgulho dos anões que o ergueram. Alguns anões vivem uma vida tão restrita à vertical DD - Soffiera - Steelrows que é como se eles vivessem numa cidadezinha isolada do resto de Bral. 

### Locais de Destaque
- **Guild Halls** de pedreiros, ferreiros e cervejeiros, onde se decide desde contratos de construção até festivais de chope.  
- **The Rusty Axe**, a taverna mais famosa do distrito, ponto de encontro de artesãos e mercenários em busca de trabalho.  
- **Dwarven Boarding Company**, uma das maiores companhias mercenárias de Bral, com escritórios aqui e em [[Merctown]].  
- **Passagens Conectadas**, túneis que ligam o bairro diretamente a [[Soffiera]] abaixo e a [[Steelrows]] acima, reforçando a natureza “ponte” do distrito.  

### Cultura e Vida
- O bairro é conhecido por sua **neutralidade feroz**: os anões não permitem que nenhuma gangue ou Famiglia domine suas ruas.  
- A vida gira em torno das **guildas**: cada artesão pertence a uma, e todas têm voz ativa na política interna.  
- Cerveja é tão importante quanto pedra e aço; muitos dizem que o Dwarven District tem as melhores tavernas da cidade.  
- A disciplina e o rigor anão tornam o bairro um dos mais seguros de Bragora — embora visitantes reclamem que é também um dos mais fechados e carrancudos.

## Vibe Visual
Torres estoicas de tijolos de pedra com detalhes em aço, indo do chão ao teto da caverna: passagens que vão tanto pra [[Soffiera]] quanto pras [[Steelrows]]. 

BIERGARTENS! Anões também podem ter plantinhas no rolê. 

Anões de boinas vermelhas palestrando sobre sindicatos (muitos vão só pela cerveja grátis). Corais graves sobre cavernas e ouro vindo da janela de uma taverna. 

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
