---
type: location
location_type: Quarter
parent:
  - "[[The Rock of Bral|Bral]]"
---
## Viscura
A montanha onde Bral é construída é um formigueiro. Debaixo dos níveis superiores, a cidade continua, mais escura, mais úmida, e mais perigosa. Esculpida por vários tipos de apêndices e magias, os túneis de Viscura são o tapete pra onde o que não é glamoroso em Bral acaba sendo varrido.

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