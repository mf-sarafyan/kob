---
type: location
location_type: Quarter
parent:
  - "[[The Rock of Bral|Bral]]"
appears_in: []
image: ""
---
O bairro nobre e ilustre coroa a cidade, e o **[[Palazzo Celestia]]** é a sua jóia central. Fileiras de colunas engravadas seguram a torre principal, um bloco de mármore branco com veias douradas refletindo o sol distante. Metal esverdeado segura janelas de cristal; terraços derramam plantas e vinhas; escadas externas serpenteiam subindo torres que acabam em observatórios. Daqui, dá pra ver um pouco dos jardins, canais e fontes que rodeiam a *Villa*. 
*Inspiração: Pallazo Ducale, VIlla d'Este*

O nível em volta do palácio foi uma tentativa de consolidar o maior número de mansões no menor espaço possível, o que acabou com elas um pouco *emaranhadas* - os telhados são calçadas, restaurantes no andar de cima de casas com pontes abobadadas levando pro vizinho, cachoeiras enfeitando a passagem de um andar pro outro. Torres e domos quebram o horizonte em alturas diferentes. Gárgulas mecânicos olham de um lado pro outro. Árvores retorcidas e varandas se extendem ao espaço na horizontal. É como se tivessem tentado colocar arte em cada centímetro. 

Guardas de capa azul celeste patrulham o céu em grifos, levando bandeiras azuis com o símbolo de um grifo.

Algumas construções chamam a atenção ainda mais que as outras - um Domo vermelho maior que os outros; uma cúpula dourada tem um telescópio gigantesco; uma das paredes tem várias extensões especialmente floradas e cheias de mesinhas. Uma das mansões tem uma torre fina de metal cheia de canos cuspindo fumaça. 

![[upper city.png]]

# Noble Houses
[[Noble Houses of Bral]] (Pelo menos 14 casas nobres já estabelecidas; acho que não tem espaço pra tanto mais que isso. Devem ter o que, umas 20 max)

# Other Places
- [[The Library of the Spheres]]: biblioteca de conhecimento 
- [[The Man O' War]] - restaurante fancy 
- Royal Theatrical Company
- The Noble Council
- Upper Magistrate
- The Crystal Lamp - taverna fancy 
- [[Ferrucio's Spire]]

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
