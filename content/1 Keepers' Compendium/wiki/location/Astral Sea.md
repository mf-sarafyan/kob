---
type: location
location_type: Plane
parent:
  - "[[The Great Wheel]]"
aliases:
  - Astral
  - Plano Astral
relates_to:
  - "[[Space Lore]]"
appears_in: []
image: "[[astralplane.jpg]]"
---
# Astral Sea

## **O Mar Astral**  
Além e entre as esferas de cristal, **entre os ovos**, encontra-se o **Mar Astral**, um domínio infinito e surreal que conecta não apenas os mundos físicos, mas também os planos de existência. Aqui não há ar ou gravidade — as viagens ficam à mercê de eventos cósmicos e das **Correntes Astrais**. Imagine finas neblinas variando geralmente entre o roxo, lilás, lavanda; incontáveis estrelas no céu, cada uma contendo seus sistemas de mundos materiais. Imagine, também, como regiões diferentes tem seus próprio ambientes; como o caos multicolorido e arco-íris do **Phlogiston** entre os **Mundos Conhecidos**, o turbilhão sanguinolento das **Cataratas Escarlate**, ou as trevas calmas do **Véu Espectral**. 

As **Esferas** não são tudo que se encontra nesse universo. Restos de **deuses mortos**, esquecidos pelo tempo, flutuam eternamente. Deuses vivos têm seus **domínios astrais**, palácios de maravilhas entre as esferas de sua influência. **Faróis arcanos**, construções enigmáticas de passado desconhecido, guiam os viajantes e servem como portos seguros para restoque e comércio; corpos estelares - como asteróides perdidos de qualquer esfera - podem ter cidades **Githyanki**, e portais cintilantes chamados de **poças coloridas** conectam o Mar Astral aos Planos Exteriores. Há também perigos como criaturas impensáveis como **Astral Dreadnoughts**, dragões cósmicos e fantasmas do Fluxo, e tempestades psíquicas que podem arrastar os incautos para territórios inexplorados ou mesmo para os braços de caçadores de escravos.

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
