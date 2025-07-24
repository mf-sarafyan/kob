---
type: location
location_type: Quarter
parent:
  - "[[The Rock of Bral|Bral]]"
---
O bairro de cima era dominado por construções coloridas e pontilhado por jardins verdes; agora, o próximo é um mar de tons suaves, terracotas, brancos, azuis fracos. É como se você tivesse jogado Tetris com uma cidadezinha italiana. É parecido com em cima, mas diferente: telhados e varandas que viram passarelas, entuxadas de gente; gôndolas, mas cheias de caixas. Cordas entre uma casa e outra, segurando roupas secando ao invés de bandeiras. Praças lotadas ao invés de jardins. Ainda é um labirinto de escadas, pontes, arcos, abóbadas. Tem florestas de tendinhas de mercado - uma em especial, onde deve ser o mercado principal da cidade. Do outro lado do mercado, uma torre fortificada cinza-escuro quebra o esquema de cores. Entre os dois passa a hidro-avenida principal da cidade, que vocês vêem que leva até o palácio lá em cima. 

Outros lugares constrastam com a arquitetura mais homogênia daqui: um prédio alto e hexagonal; um coliseu que parece feito do mesmo mármore dourado que o palácio; um parque ou bosque logo embaixo do restaurante lá de cima. Aqui e ali alguns brilhos tomam o olho: reflexos de constructos metálicos ou lanternas mágicas. 

La Città e seus canais ainda se extendem pra dentro da montanha; dá pra ver pelo fluxo de gente passando pelos arcos enormes entalhados no asteróide. 

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