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
É, essencialmente, Minas Tirith se fosse Veneza. 

As construções vão diminuindo de cima pra baixo, e elas são ligadas por canais de água, calçadas de pedra e pontes em vários níveis. A cidade é construída em níveis - quanto mais pra baixo, mais largos - conectados por escadas, elevadores com engrenages à mostra, e pelo menos um negócio que parece um tobogã. Um burburinho de pessoas de cores e tamanhos variados corre de um lado pro outro enquanto gôndolas flutuam, algumas na água, algumas em nada. Mesmo de "manhã", pontinhos azuis de lâmpadas alquímicas entram e saem de passages que levam pra dentro da montanha.  


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