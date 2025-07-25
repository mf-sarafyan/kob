---
title: Malvessi
aliases:
  - Malvessi
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: Neutral Evil
leader: ""
---

Os herdeiros da cultura pirática de Bral, a família Malvessi é a junção das tradições mais antigas da Pedra. 
Sob o comando do lendário Commodoro [[Roberto Malvessi]], capitães manejam cada um sua micro-gangue e seus territórios; a hierarquia e a cadeia de comando são fortes, mas na ponta, cada capitão cria suas regras. 

> They're the pirate crew gang, the Commodore's armada, and surely the crime syndicate with the most reach outside of Bral. Things can get messy, though: mutiny, theft, each pirate for themselves. True pirate crews are tight because they must; at sea (or Wildspace), you don't have anyone else to turn to. In Bral, you can become anyone else, at any time. Loyalties are hard to keep. That's where the Malvessi struggle. A great leader would keep them in line. If that was so, they'd rule the city by now. So we need a leader that is just looking out for himself.

Vibe: Set My Jib, linguajar nautico, multiplos empreendimentos. Motins. Tricornes. Cada um por si.

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