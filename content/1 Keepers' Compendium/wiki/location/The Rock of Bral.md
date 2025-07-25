---
title: The Rock of Bral
aliases:
  - Bral
  - Rock of Bral
  - Pedra de Bral
  - A Pedra
type: location
location_type: City
parent:
  - "[[Greyspace]]"
---
# A Cidade

É, essencialmente, Minas Tirith se fosse Veneza. 

As construções vão diminuindo de cima pra baixo, e elas são ligadas por canais de água, calçadas de pedra e pontes em vários níveis. A cidade é construída em níveis - quanto mais pra baixo, mais largos - conectados por escadas, elevadores com engrenages à mostra, e pelo menos um negócio que parece um tobogã. Um burburinho de pessoas de cores e tamanhos variados corre de um lado pro outro enquanto gôndolas flutuam, algumas na água, algumas em nada. Mesmo de "manhã", pontinhos azuis de lâmpadas alquímicas entram e saem de passages que levam pra dentro da montanha.  

De cima pra baixo: [[Montevia]], com suas mansões empilhadas; [[La Citta]], um labirinto terracota de telhados, piazzas e passarelas; [[Bragora]], uma floresta de construções de madeira envergada e úmida; e, invertida e cuspindo fumaça, [[Soffiera]]. 

# O Asteróide

Bral é uma cidade tão apertada como é porque o restante do asteróide é fértil, e 100% do espaço é usado pra alimentá-la: tanto de comida quanto de indústria. 

O lado de "cima" - onde ficam [[Bragora]], [[La Citta]] e [[Montevia]] - é onde ficam as produções agrícolas; fazendas de trigo, tomates, alho, uvas, e outros verdes, e do gado da variedade local de **Giant Space Hamsters**. As terras são oficialmente da [[Monarquia Braliana|Coroa]], mas concedidas a várias casas e entidades mercantis que lucram com a produção. 

O lado de "baixo", além de um Castelo de defesa e as Docas da marinha real, é lotado de plantações ultra-eficientes de **madeira** que é usada em [[Soffiera]] para a indústria de Spelljamming da cidade. 


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