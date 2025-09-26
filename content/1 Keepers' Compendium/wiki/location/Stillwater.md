---
type: location
location_type: Sub-district
parent: "[[Bragora]]"
appears_in: []
image: "[[stillwater1.png]]"
---

# Stillwater (L’Acqua)

**Stillwater** é o subdistrito sempre alagado de Bragora. Canais transbordam, a umidade escorre pelas paredes, e o ar está impregnado de mofo e peixe. É o lugar onde o teto pinga constantemente, por causa ao elevador que leva de [[La Citta]] até [[Montevia]] logo acima. As passagens aqui raramente estão secas, e moradores caminham sobre tábuas improvisadas ou simplesmente de pés descalços na água.  

### Locais de Destaque
- **Mercado de Peixe**, uma confusão de barracas fedidas oferecendo desde peixes frescos até espécies exóticas de wildspace, sempre com moscas rondando.  
- **Bathhouses** — algumas luxuosas, outras suspeitas — onde marinheiros e mercadores procuram tanto relaxamento quanto prazeres menos confessáveis.  
- **Arenas Submersas**, fossos secretos de luta clandestina, onde competidores são forçados a duelar em ambientes alagados e até submersos.  

#### Praça Do Afogado
No coração de Stillwater fica a praça do **Afogado**, uma antiga estátua de bronze erguida na época do Capitão Bral, mais de dois séculos atrás. O monumento homenageava um pirata cujo nome se perdeu na história — talvez um aliado, talvez um rival.  

Hoje, a figura está coberta de pátina verde, musgo e crostas de sal, com a base constantemente submersa pela água que pinga dos níveis superiores. O rosto já mal se distingue; apenas o gesto vago de um sabre levantado resiste ao tempo.  

O Afogado se tornou o ponto de encontro de Stillwater: mercados improvisados se espalham ao redor da praça, marinheiros marcam reuniões “na sombra do Afogado”, e crianças brincam de escalar a estátua escorregadia. Rumores locais dizem que moedas jogadas em sua água sombria trazem boa sorte para contrabandistas.  
![[o afogado.png|350]]

### Cultura e Vida
- Morar em Stillwater significa se acostumar a estar **sempre molhado**: roupas nunca secam totalmente, e botas são um artigo essencial.  
- O bairro é famoso por seus **negócios de fachada**: casas de banho que escondem bordéis ou arenas ilegais; vendedores de peixe que oferecem contrabando no fundo dos baldes.  
- Guerras de facções raramente explodem aqui, mas disputas pessoais se resolvem nas arenas — muitas vezes com corpos boiando depois.  
- Sempre há alguém gritando “guarda-chuvas, guarda-chuvas!” nas esquinas.

## Vibe Visual
Garoa constante. Botas fazendo schlorp, schlorp. 

Duas casas de banho, uma do lado da outra, ambas te chamando pra entrar; uma tem uma gostosa com pouca roupa, e outra um maluco tatuado e cheio de cicatrizes. 

Gente aglomerada debaixo de um telhadinho apertando, esperando passar uma gotejada mais violenta. 


![[stillwater2.png]]

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
