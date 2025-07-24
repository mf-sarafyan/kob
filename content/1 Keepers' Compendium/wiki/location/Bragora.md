---
type: location
location_type: Quarter
parent:
  - "[[The Rock of Bral|Bral]]"
---
Bral é quase um degradê. O acobreado da Città escurece conforme chega perto da linha de gravidade. A parte baixa da cidade é de cinzas e marrons - paredes de tijolo e passarelas de madeira molhada, envergadas perigosamente com o peso da civilização. Bragora é sobre eficiência: cada centímetro é usado pra alguma coisa, e o objetivo final quase sempre é te vender algum produto. Se pra cima os telhados viravam passarelas, aqui até as suas paredes viram escadas.  Sempre que possível as casas tem um puxadinho protuberando pra frente, transformando as ruas e canais em becos escuros. 

Mesmo esse caos é meio arrumadinho. Dá pra ver que as casas são bem feitas, as placas são bem pintadas. Tem canos de cobre refletindo onde a luz consegue alcançar. Algumas construções se sobressaem, principalmente uma que parece a cabeça de uma lula gigante. 
Dá pra imaginar, também, que essa parte da cidade se extendo pra caralho pra dentro da montanha. 

A bagunça diminui vindo pra frente, onde as construções maiores devem ser armazéns e casas de guilda; finalmente levando até as docas, que se expandem em direção ao espaço vazio. Spelljammers lotam o porto, alguns navios, como vocês conhecem, outros mais exóticos; em formas de insetos e crustáceos enormes. Alguns de ponta-cabeça - dá pra ver que tem uma "sub-doca" que leva pra dentro de uma caverna entre essa região e a de baixo. Sim, tem uma mais pra baixo.  
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