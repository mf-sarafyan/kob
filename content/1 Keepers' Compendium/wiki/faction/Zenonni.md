---
title: Zenonni
aliases:
  - Zenonni
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: ""
leader: ""
---
Sempre existiram em Bral as tripulações que aceitavam os rejeitados, os esquecidos, os alienígenas. Os Xenos. Zenonni - o nome nasceu daí - é sua união que aceita o diferente com apêndices sortidos abertos. Seu símbolo é um aperto de mãos com um tentáculo. Uma congregação ferozmente leal de entidades esquisitas. Você mexe com um primo, você mexeu com todos. 

Muitos negócios únicos em Bral tem donos únicos - imagine bibliotecários mind flayers, ou o próprio Luigi - e eles se ajudam através dessa família. 

Vibe: um ogro e um gith andando juntos. Um fornecedor de poções de Alter Self. 

Os Zenonni não são exatamente um grupo sumarizável: eles são um grupo de poucos indivíduos muito influentes, cada um de sua maneira. 


<!-- DYNAMIC:related-entries -->

## Member Characters

 ```dataview
    TABLE race, class, alignment
    WHERE type = "character" AND contains(factions, this.file.link)
    SORT file.name ASC
 ```

## Child Factions

 ```dataview
    TABLE faction_type, alignment
    WHERE type = "faction" AND parent = this.file.link
    SORT file.name ASC
 ```

## Related Entries

 ```dataview
    TABLE entry_type, author
    WHERE type = "entry" AND contains(relates_to, this.file.link)
    SORT file.ctime DESC
```

<!-- /DYNAMIC -->