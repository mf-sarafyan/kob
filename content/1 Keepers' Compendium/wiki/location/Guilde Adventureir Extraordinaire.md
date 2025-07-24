---
type: location
location_type: Building
parent:
  - "[[Baldur's Gate]]"
---
Uma mansao em [[Baldur's Gate]] onde jovens prodígios sao treinados pra serem aventureiros. Podem vir de qqr lugar - de nepotismo e investimento a adoção ou ate resocializacao. Tem um sistema de mestre-aprendiz, e os pcs sao aprendizes da main party.

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