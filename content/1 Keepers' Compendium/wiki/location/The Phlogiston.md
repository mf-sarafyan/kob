---
type: location
location_type: Planar Region
parent:
  - "[[kob/content/1 Keepers' Compendium/wiki/location/Astral Sea|Astral Sea]]"
aliases:
  - Phlogiston
relates_to:
  - "[[Space Lore]]"
appears_in: []
image: "[[phlogiston.png]]"
---
# Phlogiston: The Rainbow Flow
O Phlogiston é uma das mais belas e perigosas [[Wildspace, o Mar Astral e as Correntes Astrais|correntes]] do Mar [[kob/content/1 Keepers' Compendium/wiki/location/Astral Sea|Astral]]. De longe, parece um rio cósmico, derramando-se entre as Esferas de Cristal como uma ponte líquida de arco-íris. Ondas de cores iridescentes se movem em padrões hipnóticos, ora suaves como seda, ora revoltas como tempestades. A luz aqui não vem de nenhum sol — é a própria substância que brilha, pintando as velas e cascos das naves com reflexos dourados, verdes, lilases e rubros.

Mas sob toda essa beleza lateja um perigo mortal: o Phlogiston é **altamente inflamável**. Inflamável talvez nem seja a palavra certa; a substância que compõe o Phlogiston (confusamente, também chamada de Phlogiston) é nomeada pela substância conceitual teórica alquímica que todo objeto inflamável possui; ou seja, o Phlogiston **É** a "inflamabilidade". O Próprio Fogo. 
Qualquer chama aberta — seja uma tocha, um disparo de pólvora ou uma magia de fogo — pode transformar a corrente num inferno instantâneo, engolindo navio e tripulação numa explosão que ecoa pelo vazio. É por isso que marinheiros atravessam essa rota às escuras, usando luz fria ou magia não-incendiária, enquanto mantêm cada barril de pólvora lacrado como se fosse um tesouro proibido. Veteranos de Phlogiston mantém sua aversão a chamas mesmo em outras regiões. É um costume que não se perde fácil. 

Tentativas de extrair essa substância do Astral não tiveram sucesso: assim como outras Correntes, o Phlogiston não é manipulável; é como se ele existisse no tecido do universo, numa existência diferente da material. 

Mesmo com o risco, o Phlogiston é um presente para os navegantes: rápido, direto, e capaz de levar uma embarcação a reinos distantes sem tocar o resto do Mar Astral. Dizem, porém, que sua corrente muda de rumo como se fosse viva, e que aqueles que subestimam seu temperamento acabam desaparecendo entre as ondas de luz.

## Esferas Conhecidas
**As Esferas Conhecidas** (os cenários clássicos de campanhas de D&D) ficam no Phlogiston, próximas uma do outra: [[Realmspace]], [[Greyspace]] e [[Krynnspace]]. As correntes entre elas (também chamadas de *Radiant Triangle*) são relativamente estáveis e muito trafegadas, e fluem mais rápido na direção Realm -> Grey -> Krynn -> Realm. Cada corrente tem, inclusive, um [[Farol Astral]] no caminho. Sair do Radiant Triangle é mais raro e precisa de uma navegação mais precisa; os fluxos levando pra fora são mais erráticos. 

# Related

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
