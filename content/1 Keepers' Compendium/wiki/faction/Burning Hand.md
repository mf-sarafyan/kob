---
type: faction
parent: 
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Conglomerate
alignment: 
leader: "[[Serena Blackwood]]"
---
**The Burning Hand**. Uma aliança entre os **[[Cinders]]** de **Serena Blackwood** e outras gangues que querem destruir o domínio da Mano Legata. 


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