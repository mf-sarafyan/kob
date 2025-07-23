---
title: Bral Underworld
type: faction
location: ""
faction_type: ""
alignment: ""
---
A história da Pedra de Bral foi construída fora da legalidade, começando com o infame pirata que lhe deu o nome. 


# Facções Menores

**The Burning Hand**. Uma aliança entre os **[[Cinders]]** de **Serena Blackwood** e outras gangues que querem destruir o domínio da Mano Legata. 
Eles tem auxílio de outros grupos e indivíduos interessados em minar a Mano - normalmente para expandir seus próprios negócios. Um desses é [[Vocath]]! 

**[[The Unknowable One]]**. 

**Dottori**. Uma das famílias mais ricas de Bral, donos de bancos e galerias de arte, com membros na corte, nas guildas, nas Famiglias. 

**Red Anvil**. Guilda e sindicato dos anões.


---

## Member Characters
```dataview
TABLE race, class, alignment
WHERE type = "character" AND contains(factions, this.file.link)
SORT file.name ASC
```

## Related Entries
```dataview
LIST map("!" + "[[" + file.name + "]]")
WHERE type = "entry" AND contains(about, this.file.link)
SORT file.ctime DESC
```
