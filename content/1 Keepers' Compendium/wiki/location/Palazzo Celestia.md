---
type: location
location_type: Building
parent:
  - "[[Montevia]]"
---
O palácio base da [[Monarquia Braliana]]; o trono do príncipe [[Andru Cozar]].

Fileiras de colunas engravadas seguram a torre principal, um bloco de mármore branco com veias douradas refletindo o sol distante. Metal esverdeado segura janelas de cristal; terraços derramam plantas e vinhas; escadas externas serpenteiam subindo torres que acabam em observatórios. Daqui, dá pra ver um pouco dos jardins, canais e fontes que rodeiam a *Villa*.

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