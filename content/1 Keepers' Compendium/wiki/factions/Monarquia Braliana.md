---
type: faction
parent: ""
location: "[[The Rock of Bral|Bral]]"
faction_type: Nobility
alignment: ""
leader: ""
---
A liderança oficial de Bral, o monarca [[Andru Cozar]] segura o poder principalmente por controlar as terras férteis do asteróide. 

Andru orquestrou com cuidado a sucessão, organizando o assassinato de seu irmão mais velho em 6 dias de reinado, e assegurando o apoio das Famiglias. Ele conta especialmente com os [[Cartocci]] pra manter as atividades "sob controle" - pelo adequadas na visão da coroa. Permitindo dissidência suficiente pra não atrair uma total revolta, mas não o suficiente pra ser ruim pros negócios. Sempre o suficiente pra manter tudo funcionando. 

É sempre isso: a monarquia equilibra trocentos pratos pra manter o status quo, o poder, e a prosperidade deles e da cidade. Isso envolve apoiar não só a Mano Legata, mas um pouco seus oponentes, também. Permitir suas atividades, mas cortar quando a linha for cruzada. 




---

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
LIST map("!" + "[[" + file.name + "]]")
WHERE type = "entry" AND contains(about, this.file.link)
SORT file.ctime DESC
```


