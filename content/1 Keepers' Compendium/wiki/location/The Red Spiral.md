---
type: location
location_type: Street
parent:
  - "[[Viscura]]"
aliases:
  - Bral Red Light
  - Amante Vermiglio
---
O **red light district** de Bral é a **rua em espiral subindo à volta do fungo bioluminescente afrodisíaco vermelho.** 
Sim, é isso. 

As lendas diferem, mas a mais difundida é que ele nasceu do encontro de um fungo dos [[Far Realms]] com o sangue de uma **succubus**. O cogumelo em si é chamado de **Amante Vermiglio**, e além de ter "orelhas" que brilham avermelhadas, seus esporos tem efeitos interessantíssimos nos humanóides: euforia, suscetibilidade, e HORNY. Em poucas quantidades, claro. Dizem que doses altas podem causar tosse, dependência, queda de pinto,  transfigurações aberrantes e reencarnação abissal.

Dito isso, os bordéis da cidade são construídos à sua volta; a espiral é uma rua inclinada por dentro dos túneis da montanha que sobe em volta do fungo, construída dos níveis de Bragora até Montevia - e a qualidade e preço dos serviços cresce junto com o Amante. 

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