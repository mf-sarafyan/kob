---
type: faction
parent: 
location: "[[Greyhawk]]"
faction_type: Church
alignment: Chaotic
leader: 
appears_in:
  - "[[The Feather of Zariel]]"
---
Uma **filosofia espiritual** que nasceu em [[Greyhawk]] nos últimos anos. Não são uma igreja monoteísta; ao invés disso, pregam que felicidade, equilíbrio e liberdade vem através da reconexão com as energias primitivas do fogo, água, ar, e terra. 

Imagine rituais de limpeza, realinhamento de energias, meditação, horóscopos com os quatro quadrantes elementais. Vêm ganhando espaço na cidade por conta de sua estrutura descentralizada e facilidade de interação. 



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