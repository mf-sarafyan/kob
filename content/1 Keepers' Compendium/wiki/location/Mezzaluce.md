---
type: location
location_type: Sub-district
parent: "[[Bragora]]"
appears_in: []
image: "[[mezzalucce.png]]"
---

# Mezzaluce (A Meia-Luz)

**Mezzaluce** é o subdistrito do crepúsculo. Lanternas e velas derretem cera sobre os becos estreitos, criando sombras profundas e reflexos trêmulos. É um lugar de sussurros e passos contidos, onde tudo parece oficial demais para ser simples e perigoso demais para ser ignorado.  

### Locais de Destaque
- **[[Low Magistrate's Office]]**, um edifício de pedra escura coberto de velas, onde a lei da cidade baixa é interpretada — com ampla margem para favoritismo e corrupção.  
- **Escritório Cartocci de Bragora**, logo ao lado: um ponto de atendimento da Famiglia [[Cartocci]] para a população. Quem sofreu um roubo em duplicidade, foi extorquido por duas gangues diferentes ou precisa da “permissão certa” para operar, vem até aqui registrar reclamações e buscar arbitragem.  
- **Teatro Silencioso**, uma casa de espetáculos oculta, conhecida por apresentações que falam mais em gestos e sombras do que em palavras — frequentemente metáforas políticas.  

### Cultura e Vida
- Para o povo de Bragora, **Mezzaluce é onde se resolve tudo**: disputas criminais, reclamações formais, denúncias contra outros criminosos… tudo com recibo carimbado. O povo reclama de ter que pagar a máfia, mas os que lembram como era a vida com os [[Gravanzo]] amargamente concordam que as coisas melhoraram. 
- Os **[[Cartocci]]** dão as cartas aqui, funcionando como um ministério do crime organizado. 
- O bairro vive num constante **meio-tom**: negócios legais e ilegais se misturam, e todos sabem que falar alto demais pode ser perigoso. Fale muito alto e pode ser que patrulheiros joguem um *silence* em você e te encham de porrada no xiu. 
- Visitantes descrevem Mezzaluce como o lugar onde “a própria burocracia é uma arma”.

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
