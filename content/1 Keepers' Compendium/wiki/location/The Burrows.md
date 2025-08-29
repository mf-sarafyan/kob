---
type: location
location_type: Sub-district
parent: "[[Bragora]]"
appears_in: []
image: "[[burrowsmj.png]]"
---

# The Burrows

**The Burrows** é o bairro dos pequenos povos — halflings, gnomos e alguns kobolds pacíficos que se misturaram à vizinhança. O bairro se espalha em ladeiras íngremes e passagens estreitas, onde casas parecem brotar direto da pedra. Muitas portas exigem que visitantes maiores se abaixem, e a vida aqui é feita em escala reduzida: mesas baixas, janelas miúdas, escadas que dão em tocas aconchegantes.  

O bairro é principalmente residencial: os restaurantes ou lojinhas costumam ser pequenos, pra atender o povo daqui. Os pequeninos normalmente trabalham o dia, até nos outros bairros, depois voltam pra suas toquinhas.

### Locais de Destaque
- **Osteria da Nonna Meu**; lendária pela comida caseira, mas conhecida só por quem manja mesmo da cultura gastronômica da cidade (ou por quem tem parentesco pequnino). 
- **Ponte di Piccolo**, que conecta os Burrows ao [[Dwarven District]]. O nome era óbvio. (Piccolo é pequeno em italiano, não só aquele alien verde).
- Pequenas oficinas de tinkers e relojoeiros, onde gnomos artesãos criam engenhocas inesperadas. A maioria trabalha mais por diversão que pelo lucro - se fosse, poderiam ter oficinas maiores em [[Soffiera]].

### Cultura e Vida
- Há um forte senso de **comunidade e hospitalidade**: festas de rua com música e comida abundante são comuns.  
- Apesar do clima leve, os Burrows não estão livres da influência das Famiglias; rumores dizem que os [[Luminari]] têm muitos olhos e ouvidos aqui.

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
