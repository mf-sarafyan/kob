---
type: location
location_type: Quarter
parent:
  - "[[The Rock of Bral|Bral]]"
---
## Soffiera
E a região mais pra baixo está de ponta-cabeça. Debaixo das docas, uma correntinha de água caindo da região de cima se mistura com fumaça vinda de baixo. O porto bloqueia a maior parte da vista, mas vocês conseguem reconhecer construções grandes de pedra e de metal. Canais que parecem o rio Pinheiros com gôndolas grandonas e cheias de caixas coloridas (tipo uns contâineres). Chaminés cuspindo fumaça preta. 

A cidade pra cima é limpinha e arrumada porque varreram o trabalho pesado aqui pra baixo. Apesar de tudo, os canais e as passarelas são maiores, tudo parece mais controlado e organizado.

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