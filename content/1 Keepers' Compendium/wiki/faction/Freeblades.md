---
type: faction
parent: []
location: "[[Greyhawk]]"
faction_type: Gang
alignment: Chaotic Chaotic
leader: 
appears_in:
  - "[[The Feather of Zariel]]"
---
Um misto de gangue de mercenários, culto e filosofia que tem causado problemas em [[Greyhawk]]. Acreditam que "might makes right": o que é seu só é seu se você conseguir defendê-lo. Se não, é de quem tomar. 

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