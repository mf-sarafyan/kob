---
type: location
location_type: City
parent:
  - "[[Central Flanaess]]"
appears_in: []
image: ""
---
# Greyhawk

(Descrição provisória do GPT)
A cidade-estado de **Greyhawk** (Free City of Greyhawk), em **Oerth**, era o cenário do jogo de D&D do criador Gary Gygax, e o local de origem e aventuras de vários personagens famosos, como [[Mordenkainen]], [[Iggwilv]], [[Bigby]], e etc. 

## 🌆 A Cidade de Greyhawk

Conhecida como a “Jóia das Terras Flan”, Greyhawk é uma cidade-estado vibrante, cosmopolita e cheia de perigos — o coração do mundo de Oerth e um dos principais centros de poder político, arcano e mercantil do continente de Flanaess. Originalmente uma fortaleza fundada por aventureiros, Greyhawk cresceu para se tornar uma metrópole de influência continental, famosa tanto por suas oportunidades quanto por suas intrigas.

### 🧭 Localização

Greyhawk fica à margem do rio Selintan, com acesso fácil ao Lago Nyr Dyv (conhecido como o “Mar Interior”), o que garante à cidade grande prosperidade comercial e influência regional.

### ⚖️ Governo

A cidade é governada por um **Conselho Diretor** liderado por um dos mais famosos personagens de D&D: **Zagyg Yragerne**, o Arquimago Louco (embora ele tenha desaparecido, sua influência permanece). Na prática, o Conselho é formado por nobres, líderes de guildas, clérigos poderosos e magos arcanos — todos disputando poder em uma dança política constante. A corrupção é comum, mas faz parte do jogo.

### 💰 Economia e Guildas

Greyhawk é um **caldeirão de guildas poderosas**: ladrões, comerciantes, magos, alquimistas, ferramenteiros — todas têm suas próprias sedes, leis e até tribunais internos. A cidade sobrevive vendendo licenças e permissões, incluindo para... atividades questionáveis. Quer ser um ladrão profissional? Basta pagar a guilda certa.

### 🏛️ Magia e Religião

O poder arcano em Greyhawk é liderado pela **Guilda dos Magos**, que rivaliza com os próprios templos. Diversos deuses são adorados na cidade, com destaque para **Boccob (deus da magia)**, **St. Cuthbert (deus da justiça severa)**, **Nerull (deus da morte)**, e **Wee Jas (deusa da magia e da morte)**. Cultos sombrios, no entanto, também têm sua influência nos becos escondidos.

### 🏴‍☠️ Intriga e Aventura

Greyhawk é um **íman para aventureiros**. Masmorras antigas como a **Dungeon de Castle Greyhawk**, mercados de itens mágicos, ruínas próximas e rivalidades entre facções garantem que sempre haja trabalho... e perigo. É também um ninho de espiões e assassinos, onde alianças mudam com a mesma rapidez que moedas trocam de mão.

### 🧭 Importância Multiversal

Na sua campanha Spelljammer, Greyhawk (ou Oerth) é uma esfera clássica do multiverso. Muitos consideram Greyhawk o "mundo base" das aventuras, e é comum que ela funcione como ponto de encontro, partida ou disputa entre forças extraplanares e viajantes intersferiais. É o lar de vários personagens icônicos (Mordenkainen, Iuz, Tenser, Rary) e conflitos lendários como a **Grande Guerra de Greyhawk**.

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
