---
type: faction
parent: "[[La Mano Legata]]"
location: "[[The Rock of Bral|Bral]]"
faction_type: Crime Family
alignment: Lawful Evil
leader: "[[Don Vico Cartocci]]"
---
A **famiglia Cartocci** é apenas a extensão de seu líder, [[Don Vico Cartocci]]. 

Os idealizadores de La Mano, a Cartocci é uma máfia administrada como um ministério. Toda atividade tem sua devida nota e formulário. Todo cidadão - que paga o que é devido - tem direito de recurso, e o criminoso que não cumpre as regras - rouba em duplicidade, ataca sem a licença correta - é punido com eficiência assustadora. Essa famiglia opera na base de que seguir o protocolo faz tudo funcionar melhor pra todo mundo, e tem o músculo por trás pra implementar isso. 

Vibe: Dave Bautista com mini oculos. Mafiosos de terno apertado pq são musculosos. Espancamentos com suitcase. 

# Obliviattos
A Ordem dos Obliviattos são um serviço conveniente que se tornou indispensável na cidade: uma equipe de juízes e magistrados Cartocci que operam com total garantia de sigilo, através do uso de magias e poções de esquecimento. 

Sejam contratos secretos ou criminosos, as partes podem sempre contar com a mediação e validação de um Obliviatto (pagando o preço certo, claro), sem se preocupar com vazamentos de informação. 


---

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