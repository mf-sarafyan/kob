---
type: location
location_type: Sub-district
parent:
  - "[[La Citta]]"
appears_in: []
image: ""
---
# A Floresta Élfica
Dizem que o ar muda quando se entra no **Bosco d’Argento**. O som da cidade se apaga, e o mundo se torna mais lento, mais suave. O bairro é todo arborizado — não com as árvores jovens dos parques de Frun, mas com carvalhos e salgueiros antigos, de troncos retorcidos e copas que tocam umas nas outras como velhos conhecidos. Muitos juram que aquelas árvores são mais velhas do que a cidade, ou mesmo do que os próprios elfos que vivem sob elas.

O solo é coberto de folhas douradas, mesmo fora do outono. Trilhas de pedra branca serpenteiam entre os troncos, iluminadas por lanternas em forma de folhas e vaga-lumes — que nunca se apagam, mesmo quando não deveriam estar acesas. Sempre há uma brisa leve, mesmo nos dias mais abafados, e sempre, em algum ponto, a sugestão de uma **lua pálida** aparece entre os galhos. Uma lua que não tem fonte, nem motivo, mas insiste em brilhar.

Elfos vivem aqui. Alguns, em casas modestas feitas de madeira viva, integradas ao ambiente com uma delicadeza que faz parecer que nasceram ali. Outros, em palácios que parecem nascer da própria pedra, varandas arqueadas e cúpulas verdes, escondidos por camadas de árvores e magia. Há quem diga que ninguém "mora" de verdade no Bosco — apenas permanece. Que os elfos caminham entre as árvores por anos, e eventualmente encontram um lugar onde repousar.

Poucos não-élfos ousam se instalar aqui. E poucos visitantes permanecem por muito tempo. Há algo no Bosco que, sutilmente, desencoraja a permanência. Não por hostilidade — muito pelo contrário. É tudo tão calmo, tão tranquilo, que o visitante logo se vê caminhando de volta por onde veio, satisfeito, como se tivesse acabado de acordar de um sonho bom.

Na **Piazza Sindarina**, o coração do bairro, fontes murmuram músicas arcanas e esculturas representam cenas de histórias antigas demais para lembrar. Grupos de elfos sentam-se sob as árvores, tocando alaúdes, recitando poesia, jogando xadrez planar com peças que se movem sozinhas. À noite, o bairro inteiro parece brilhar por conta própria — não com luz, mas com presença.

E mesmo os bralianos mais céticos admitem: há algo no ar do Bosco que **não se discute**.

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
