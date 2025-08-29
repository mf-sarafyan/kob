---
type: location
location_type: Sub-district
parent:
  - "[[kob/content/1 Keepers' Compendium/wiki/location/Bragora]]"
appears_in: []
image: "[[bragora docks.png]]"
---
Distrito das docas de [[kob/content/1 Keepers' Compendium/wiki/location/Bragora|Bragora]], separado em dois pelo **Rio Maggiore**: **Riva Alta** e **Riva Bassa**.


# Dockside (Riva Alta & Riva Bassa)
Dockside é a linha de frente de Bragora: o primeiro cheiro que o viajante sente ao desembarcar é o da maresia artificial, de peixe fervido e cordas molhadas. O bairro se divide em dois blocos principais — **Riva Alta** e **Riva Bassa** — separados por canais e unidos pela famosa **Ponte Enferrujada**, onde gôndolas sempre param vendendo camarões cozidos e cabeças de peixe.

### Riva Alta
A parte mais alta é dominada por **armazéns e depósitos**, pertencentes às casas nobres e às grandes companhias mercantis. Navios descarregam cargas inteiras direto para estas construções, e é aqui também que se encontra o **Escritório do Mestre das Docas**, que regula (ou finge regular) a atividade portuária.  
Entre os prédios imponentes, destaca-se a **Casa Murawa**, residência do mercador mais rico da comunidade Shou, cercada de armazéns próprios.

### Riva Bassa
Mais próxima da água e da bagunça do cais, Riva Bassa é uma mistura de tavernas esfumaçadas e oficinas modestas. Aqui se encontram estabelecimentos como a lendária **The Laughing Beholder**, além de lojas que vendem tudo o que uma tripulação precisa: velas, cordas, armamentos básicos produzidos em [[Soffiera]]. É o ponto de encontro das tripulações menos glamourosas, mas indispensáveis para o funcionamento da cidade.

### Notas e Cultura
- O movimento constante faz de Dockside um dos lugares mais barulhentos de Bragora.  
- Guardas da cidade passam, mas raramente intervêm; a “lei” pertence tanto às guildas quanto às máfias.  
- Dizem que nenhum carregamento entra ou sai sem que ao menos uma Famiglia tenha sua parte.

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
