---
type: location
location_type: Sub-district
parent: "[[Bragora]]"
appears_in: []
image: "[[bral shou town.png]]"
---

# Shou Town

**Shou Town** é o enclave cultural da diáspora Shou Lung em Bral. Entre lanternas de papel, jardins minuciosos e aromas de chá e especiarias, o bairro se destaca como um dos recantos mais tranquilos de Bragora. É o destino preferido para quem busca uma refeição refinada ou uma noite em uma casa de chá silenciosa — embora por trás da fachada pacífica se esconda a influência sutil da **[[Yakuza]]**. Aqui e ali, um jardim zen quase te faz esquecer que você ainda está em Bral. 

### Locais de Destaque
- **[[Lesser Market]]**: um mercado vibrante de especiarias, tecidos e bugigangas importadas, famoso por sua variedade exótica.  
- **[[Shou Embassy]]**: centro diplomático que garante aos Shou certa autonomia dentro da cidade. O embaixador atual, **Lord Chan Fu Wi**, trabalha arduamente para manter o equilíbrio entre os Shous honestos e a Yakuza em frente ao Príncipe e as máfias. Seu trabalho tem dado certo, mas como tudo aqui é pólvora, basta uma faísca pra mandar tudo pro ar.
- **Casas de chá e restaurantes de fusão italo-asiática**, que atraem tanto marinheiros nostálgicos quanto nobres curiosos. Imagina que gostoso os macarrãozinho. 
- **Monastério da Lótus Celestial**: onde treinam monges fiéis da **Burocracia Celestial**, a fé-intergalática originária de [[Shou Long]].

### Cultura e Vida
- Lanternas tradicionais se misturam a **letreiros de néon mágico**, criando um contraste único de passado e futuro.  
- O bairro é conhecido por seu **espírito comunitário**: jardins coletivos e festivais coloridos unem moradores e visitantes.  
- A [[La Mano Legata]] tem pouca força aqui; o território é dominado pela própria [[Yakuza]], que prefere negócios discretos a conflitos abertos.

# Imgs
![[bral shou town.png]]
![[bral shou town viscura.png]]
# Links

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
