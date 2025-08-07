---
type: location
location_type: Quarter
parent:
  - "[[The Rock of Bral|Bral]]"
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
- Noble Council
	- 
- Upper Magistrate
- The Crystal Lamp - taverna fancy 
- [[The Red Spiral]] (The Cap) - bordéis highest-end
- [[Ferrucio's Spire]]

<!-- DYNAMIC:related-entries -->

## Factions Based Here

 ```dataview
    TABLE faction_type, alignment
    WHERE type = "faction" AND location = this.file.link
    SORT file.name ASC
 ```

## Sub-Locations

```dataview
    TABLE location_type
    WHERE type = "location" AND contains(parent, this.file.link)
    SORT file.name ASC
```

## Related Entries

```dataview
    TABLE entry_type, author
    WHERE type = "entry" AND contains(relates_to, this.file.link)
    SORT file.ctime DESC
```

<!-- /DYNAMIC -->