---
type: location
location_type: Sub-district
parent: "[[Bragora]]"
appears_in: []
image: "[[gifftown.png]]"
---
# Gifftown

**Gifftown** é o maior e mais espaçoso bairro de Bragora. As ruas aqui são largas, os edifícios são robustos, e as praças parecem mais campos de parada militar do que locais de convivência. O ar está sempre carregado de fumaça de pólvora e do riso estrondoso dos giffs, que transformaram o distrito em uma caricatura viva de sua própria cultura marcial.  

A grande maioria dos moradores oferece serviços individuais como mercenários e expõe, na frente de casa, a **sua própria bandeira**. Todas as bandeiras óbvias já foram usadas; por isso, cada novo giff no mercado inventa um estandarte mais esquisito e exagerado que o último. O resultado é uma floresta de bandeiras coloridas e ridículas tremulando por toda parte.  

### Locais de Destaque
- **The Hippodrome**, uma arena colossal usada para corridas de pólvora, exibições de artilharia, duelos e qualquer outra coisa que envolva explosões.  
- **Blackpowder Cups**, famoso por suas bebidas fortificadas com pólvora em pó.  
- **Quartel-Cívico de Tomojak**, um prédio monumental que mistura prefeitura e quartel-general. É a sede do **General Tomojak**, líder reconhecido da comunidade giff em Bral. O edifício abriga tanto escritórios burocráticos quanto salões de treino e depósitos de armas.  
- **Campos de Tiro** públicos, onde qualquer um pode pagar para experimentar diferentes calibres ou simplesmente ver quem acerta o alvo primeiro.  

### Cultura e Vida
- Gifftown é **grande e barulhento**, mas também organizado em sua própria lógica militar. Cada esquina tem espaço para desfiles improvisados ou competições.  
- O bairro é autossuficiente: além das tavernas e arenas, há lojas especializadas em armas, armaduras e pólvora.  
- Apesar de seu exagero, Gifftown é relativamente seguro. Violência entre giffs é rara; os acidentes explosivos, por outro lado, são diários.  
- Escadarias monumentais conectam o bairro diretamente à [[Via Capitani]], em [[La Citta]], reforçando os laços entre as companhias mercenárias giff e o coração militar da cidade.

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
