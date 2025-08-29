---
type: location
location_type: Ship
parent:
  - "[[kob/content/1 Keepers' Compendium/wiki/location/Astral Sea|Astral Sea]]"
appears_in:
---
# O SPELLJAMMER
Como a WOTC odeia clareza em suas nomeclaturas, além do **Spelljammer** (nome da campanha) e dos **Speljammers** (embarcações mágicas que cruzam o espaço e o astral), existe **O** **SPELLJAMMER** (Spelljammer-class Spelljammer), uma lendária cidade-nave viva, a maior do seu tipo; teorizado ser tão velho quanto as Esferas, tripulado por constructos que ele próprio produzia, habitado por criaturas que eram magicamente *encantadas* por ele, e cercado de lendas, mistérios, e tesouros. 

Ele parece uma mistura entre arraia e escorpião, com as asas longas, rabo retorcido pra cima, e castelos construídos no topo. 

## Smalljammers
Como uma criatura viva, ele se reproduz (sério). Ele tem filhotinhos que são versões pequenininhas dele, chamados **Smalljammers**. Se um dia **O SPELLJAMMER** é destruído - como já foi presenciado, num ataque de uma frota de dezenas de navios neogi - ele emite um sinal metafísico através do plano etério que causa o crescimento do Smalljammer mais próximo, que em menos de um ano cresce a ponto de assumir o manto de **O SPELLJAMMER**. 



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