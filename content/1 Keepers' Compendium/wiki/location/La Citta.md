---
type: location
location_type: Quarter
parent:
  - "[[The Rock of Bral|Bral]]"
---
O bairro de cima era dominado por construções coloridas e pontilhado por jardins verdes; agora, o próximo é um mar de tons suaves, terracotas, brancos, azuis fracos. É como se você tivesse jogado Tetris com uma cidadezinha italiana. É parecido com em cima, mas diferente: telhados e varandas que viram passarelas, entuxadas de gente; gôndolas, mas cheias de caixas. Cordas entre uma casa e outra, segurando roupas secando ao invés de bandeiras. Praças lotadas ao invés de jardins. Ainda é um labirinto de escadas, pontes, arcos, abóbadas. Tem florestas de tendinhas de mercado - uma em especial, onde deve ser o mercado principal da cidade. Do outro lado do mercado, uma torre fortificada cinza-escuro quebra o esquema de cores. Entre os dois passa a hidro-avenida principal da cidade, que vocês vêem que leva até o palácio lá em cima. 

Outros lugares constrastam com a arquitetura mais homogênia daqui: um prédio alto e hexagonal; um coliseu que parece feito do mesmo mármore dourado que o palácio; um parque ou bosque logo embaixo do restaurante lá de cima. Aqui e ali alguns brilhos tomam o olho: reflexos de constructos metálicos ou lanternas mágicas. 

La Città e seus canais ainda se extendem pra dentro da montanha; dá pra ver pelo fluxo de gente passando pelos arcos enormes entalhados no asteróide. 
![[Pasted image 20250731183801.png]]
# The Barrios

- Lakeside
	- entre Montevia e o lago. Casas chiques. 
	- Wall Street: centro financeiro encostado no penhasco, embaixo das Docas Reais. [[The Royal Exchequer]].
- La Sindiatta: [[The Elven Quarter]], mt arborizado
- Festival Grounds: peninsula com parque e [[The Arena of Frun]]
- Magisterium: Debaixo do [[Palazzo Celestia]]; centro burocrático, livrarias, guildhalls e [[Middle Magister's Office]]
- Steelrows: quase uma continuação do [[Dwarven District]], lojas de armas e armaduras. Onde fica a [[Torri di Corsario]]. 
- Entertainment district: tavernas, pubs, teatros, cinemas (cinemas!?), casas de show. [[The Red Spiral]]. 
- Market Heights: muitas lojinhas, HQs das trade companies. [[Grand Bazaar]]. 
- The Balconies: Casas e terraços de madeira e cordas construídas por cima de Bragora.
- Merc quarter: HQs das companhias mercenárias mais fancy. 
- Aetherium & Campanarium: universidades, lojas e escolas de magia arcana no norte, Temple Quarter no sul. 
- Lake Dock/Restaurant Row: onde chega a produção agrícola de Bral, vinda do outro lado do lago. Melhores restaurantes. 

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