---
type: location
location_type: Sub-district
parent: "[[Bragora]]"
appears_in: []
image: "[[cutewyrmways.png]]"
---

# The Wyrmways
**Wyrmways** é o reduto dos dracônicos de Bral — dragonborns, dracons, kobolds, lizardfolk e, dizem, até dragões disfarçados. A arquitetura dracônica é intimidadora; cada casa parece uma entrada de masmorra amaldiçoada, com pedras negras, braseiros em correntes negras e estátuas e bustos dracônicos em cima das portas. Mas por cima disso, é tudo colorido: toldos, bandeiras, barracas, comidas, roupas. 

O bairro pulsa com cheiros de especiarias ardidas, metais aquecidos e incenso forte. As casas têm telhados em escamas de cobre e ferro, e as ruas são estreitas mas cheias de luz: tochas, lanternas e brasas iluminam cada canto, como se o fogo fosse parte da própria identidade do lugar.  

Wyrmtown é cheio de colecionadores muito específicos e especializados querendo adicionar aos seus pequenos e individuais covis de tesouros. 

### Locais de Destaque
- **[[Dracon Consulate]]**. Os [[Dracons]], apesar de raros, são vistos como os líderes políticos dos escamosos em Bral. A embaixada garante a sua voz política, e também protege seus segredos. 
- **Bancos e Casas de Câmbio**, menos glamourosos que os de La Città, mas famosos por transações rápidas e discretas — muitas vezes em troca de tesouros antigos. Dia sim, dia não, uma é fechada pela [[La Mano Legata]], e depois reaberta com um nome diferente.
- **Mercados de Antiguidades**, onde se encontram joias quebradas, moedas de esferas distantes e relíquias de dragões. Os mais célebres tem suas próprias tendinhas no [[Grand Bazaar]].
- **Restaurantes de Comida Dracônica**, célebres pelas receitas absurdamente apimentadas, capazes de derrubar até um giff. Uma bebida comum de acompanhamento funciona como uma *potion of dragon's breath* (mas que também faz um dragon's breath pra dentro)! 
- **Tooth & Tail, Claw & Scale**: Centro de bem-estar para aqueles da disposição reptiliana. Dentistas, manicures de garras, limpadores e tatuadores de escamas. "Barbeiros" de chifres. Apotecários para os órgãos de cuspir fogo. 

### Cultura e Vida
- Wyrmtown é um lugar de **negócios estranhos**: cada esquina pode esconder um cambista, um antiquário ou um sacerdote kobold pregando a glória de dragões esquecidos.  
- A vida aqui é barulhenta, cheia de cores e odores fortes; moradores dizem que o bairro nunca dorme.  
- Muitos acreditam que o bairro abriga um ou mais **dragões disfarçados**, controlando o território nos bastidores.  
- Visitantes saem com a língua queimada, o bolso mais leve e, muitas vezes, um artefato de origem duvidosa.

# Img
![[wyrmways1.png]]
![[cutewyrmways.png]]
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
