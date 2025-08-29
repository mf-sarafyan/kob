---
type: location
location_type: Quarter
parent:
  - "[[Bragora]]"
appears_in: []
image: "[[arsenale.png]]"
---
# Arsenale

O **Arsenale** é o coração industrial e naval de Bragora, um complexo de estaleiros, guindastes e cavernas portuárias onde se constroem e reparam spelljammers de todos os tipos. O som constante de martelos e serras mágicas ecoa pelos canais, misturado ao cheiro acre de óleo, madeira e fumaça. É um lugar de movimento pesado, onde operários, engenheiros e mercenários se cruzam a cada instante.  

### Locais de Destaque
- **[[Cuttle Tower]]**, a sede da Guilda dos Construtores de Navios, se ergue como uma fortaleza no centro do complexo. Uma carcaça de um antigo Spelljammer **Cuttle Command**; ou seja, uma cabeça gigante de lula, tornada prédio imponente (e esquisito). 
- **Museu do Arsenale**, uma mistura de sala de troféus e propaganda, onde se exibem peças de navios famosos, relíquias de batalhas contra neogi e mapas cósmicos raros. Suas peças incluem também um [[O SPELLJAMMER#Smalljammers|Smalljammer]], um cadáver de bio-navio neogi, e canhões do navio do fundador da cidade - [[Bral of the Black Brotherhood]]. 
- **Elevadores inversores**, enormes plataformas que conectam o Arsenale às docas subterrâneas de [[Soffiera]], levando cargas pesadas e navios inteiros de um lado ao outro da Pedra.  

### Cultura e Vida
- Operários passam turnos exaustivos sob a vigilância de capatazes e guildas. Muitos são estrangeiros que acabam morando nos outros bairros de Bragora.  
- Apesar do clima de trabalho duro, o bairro pulsa com **orgulho naval**: tavernas próximas estão sempre cheias de canções de marinheiros e histórias de estaleiro.  
- Diferente dos outros bairros de Bragora, a Coroa tem presença reforçada no Arsenal - guardas com impecáveis tabardos azuis com a imagem do Grifo e halberds afiados nas costas patrulham a área, e funcionários públicos com pranchetas registram cada embarcação em reparos. 


---
# Links

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
