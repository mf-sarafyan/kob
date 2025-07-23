---
type: faction
parent: "[[kbβ42]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: 
alignment: ""
leader: ""
---

Dividem [[Pffred]] e [[Krik'Lit]] entre os dois tb  
[[kob/content/1 Keepers' Compendium/wiki/characters/Baang|Baang]] - Gambling Hall/Stock Exchange. **The Baank**: "feeling lucky?" / **Lucky Ones**: 2 d20s rolando 1. Aprendizes do Il Veluto como crupies. 4 hirelings. Gerente Dick Vigarista? 
[[Bad Juju]] - Tavern num barco estacionado no beco atrás do Baank. Cramped e seedy. Barco de 2 andares. Bem rude com Cartoccis e afins. Cinders no bar. Usados pra delivery também. Ajudam a entregar coisas do Gizmo. Bartender tubarao humanoide (wereshark?). Punks, drags e punks drags. ***The Asscrack?***

[[kob/content/1 Keepers' Compendium/wiki/characters/Gizmo|Gizmo]] - Workshop : Sem nome. Wizpop trabalha, plus um Giff. Soffiera. Mascara de solda e avental de couro. Vendem pra todos - especialmente Cinders. [[Kurrzot]] carrega coisas. 

[[Rhogar]] - 

[[kob/content/1 Keepers' Compendium/wiki/characters/Vax|Vax]] - Cat Maid Cafe? Gatos e Tabaxis. Os gatos tem roupas de maid. **Gatto QuiLatte.** Hot cocoa e cafézinhos. Middle City. Pub. 


----
Miken e Vaz? Leron?

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