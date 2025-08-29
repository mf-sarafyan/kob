---
type: location
location_type: Sub-district
parent:
  - "[[Bragora]]"
appears_in: []
image: "[[lostrozzo.png]]"
---

# Lo Strozzo (As Cordas)

Conhecido como **Lo Strozzo** — “O Estrangulamento” — este bairro é um labirinto de cordas, andaimes e plataformas de madeira que se estendem em múltiplos níveis sobre os canais. O lugar range e balança a cada passo, como se toda a vizinhança estivesse sempre prestes a despencar. O cheiro forte de madeira molhada, couro curtido e fibras úmidas domina o ar, junto do eco de martelos e rodas de fiar.  

Nos telhados altos o suficiente para alcançar [[La Citta]], Lo Strozzo dá lugar a [[The Balconies]]. 

### Locais de Destaque
- **Oficinas de cordame e tanoarias**: as maiores produtoras de cordas, velas e barris de toda Bral. O bairro fede a couro molhado e fibras sendo fervidas.  
- **[[The Council of The City]]**: ironicamente instalado aqui, em meio à confusão de plataformas. Muitos dizem que foi escolha política, para lembrar os conselheiros de onde vem o povo.  
- **Tavernas brutas**, como a infame **The Rockrat**, frequentadas por marujos, mercenários e piratas. Brigas aqui não são apenas comuns — são esperadas.  

### Cultura e Vida
- É um bairro de **perigo constante**: quedas são frequentes, e ninguém recomenda andar distraído nas passarelas.  
- A criminalidade aqui é mais aberta, com gangues locais disputando território sem tanta interferência da [[La Mano Legata]].  
- Lo Strozzo é visto como “teste de coragem” para forasteiros: sobreviver a uma noite no bairro sem perder os dentes já é motivo de respeito.

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
