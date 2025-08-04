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

De cima pra baixo: [[Montevia]], com suas mansões empilhadas; [[La Citta]], um labirinto terracota de telhados, piazzas e passarelas; [[kob/content/1 Keepers' Compendium/wiki/location/Bragora]], uma floresta de construções de madeira envergada e úmida; e, invertida e cuspindo fumaça, [[Soffiera]]. 

# O Asteróide

Bral é uma cidade tão apertada como é porque o restante do asteróide é fértil, e 100% do espaço é usado pra alimentá-la: tanto de comida quanto de indústria. 

O lado de "cima" - onde ficam [[kob/content/1 Keepers' Compendium/wiki/location/Bragora]], [[La Citta]] e [[Montevia]] - é onde ficam as produções agrícolas; fazendas de trigo, tomates, alho, uvas, e outros verdes, e do gado da variedade local de **Giant Space Hamsters**. As terras são oficialmente da [[Monarquia Braliana|Coroa]], mas concedidas a várias casas e entidades mercantis que lucram com a produção. 

O lado de "baixo", além de um Castelo de defesa e as Docas da marinha real, é lotado de plantações ultra-eficientes de **madeira** que é usada em [[Soffiera]] para a indústria de Spelljamming da cidade. 

# Business
As atividades econômicas mais relevantes em Bral: 
- Compra e venda (e appraisal) de artigos de todas as esferas; 
- Spelljammer ship stuff (compras, reparos, equipamentos);
	- Sempre tem pelo menos um [[Arcane]] vendendo Spelljamming Helms.
	- Star charts e crew tb;
- Trade company stuff (contratos de carga/etc pras companhias que fazem negócios aqui);
- Companhias de Mercenários; 
- Adventuring Gear
	- itens mundanos e mágicos
- Exploração/prospecção de asteróides no Grinder;
	- Tipo contratar aventureiros pra procurar um lugar pra instalar uma mina de enxofre pra fazer póvora
- Comida e bebida de luxo (turismo inclusive); 
	- Algumas vindas de fora, algumas de produção local
- Muitas tavernas de qualidade variável
- [[The Red Spiral]]: red light district


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