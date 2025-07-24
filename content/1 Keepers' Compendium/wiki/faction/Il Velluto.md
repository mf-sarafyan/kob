---
title: Il Velluto
aliases:
  - Il Velluto
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: Chaotic
leader: "[[The Juggler]]"
---
Led by [[The Juggler|The Juggler]].

Também "the Jugglers", são quase que o completo oposto dos [[Malvessi]]: refinados, elegantes, até artísticos. Uma máfia de bardos, artistas e golpistas que domina as operações em [[The Rock of Bral#Montevia|Montevia]]. Seu estilo é roubos de alto perfil, performáticos; que atraem mais aplausos do que horror. A fachada de glamour e escândalo deve esconder algo a mais, mas parece que a maioria está contente com isso. A alta sociedade tolera suas atividades pela fofoca que elas geram. 

Vibe: pendurar em chandeliers, roubar as jóias de um cofre impenetrável e deixar exposto em praça pública, just because.

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