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
- [[Steelrows]]: quase uma continuação do [[Dwarven District]], lojas de armas e armaduras. Onde fica a [[Torri di Corsario]]. 
	- The Watchers HQ, de frente pro Magisterium
- Entertainment district: tavernas, pubs, teatros, cinemas (cinemas!?), casas de show. [[The Red Spiral]]. 
	- O Mastro Levantado
- Market Heights: muitas lojinhas, HQs das trade companies. 
	- [[Grand Bazaar]]. 
	- Manor of the Arcane 
	- Vocath's Mansion
	- [[Gaspar's Reclamation]]
	- [[The Smith's Coster]]: recentemente moveram o HQ pra Bral
	- [[Sindiath Line Office]] (apesar de ter um maior na Sindiatta)
	- [[House Eirefezt]] 
- The Balconies: Casas e terraços de madeira e cordas construídas por cima de Bragora.
	- vibe bem hipster artista poeta pobre, cafés e bares, jardins. 
- [[merctown]]: HQs das companhias mercenárias mais fancy. 
	- Agamour's Platoon: Giffs, direto nas escadas pra Gifftown
	- Dwarven Boarding Company Office (o HQ eh no distrito)
	- Golden Brotherhood (descendente do Bral, bem Malvessi)
	- The Long Fangs (Chaotic Evil)
	- The Trading Company (tb vendem armas)
	- Valkan's Legion (nobre)
	- The War-Drakes (ex-Imperial Armada)
	- Xenotermination, Ltd. 
- Aetherium & Campanarium: universidades, lojas e escolas de magia arcana no norte, Temple Quarter no sul. 
	- Aetherium
		- The Seekers' School
		- The Pragmatic Order of Thought (anti-slavers)
		- The Fireball Alliance (caster militia da cidade)
		- The Honored Mage's Guild of Bral
	- Campanarium
		- Planar Church of Olympus/Arborea 
		- Planar Church of the Seven Heavens/Celestia
		- Temple of Týr (sim o nordico da banda)
		- College of Celestian (spacefarer deity; Salt)
		- The House of the Path and the Way (Celestial Bureaucracy)
		- Temple of Ptah, o mais influente (deus de artistas e criação, panteão egípcio, realmspace)
		- Holy Keep of Bane (sim, o nosso queridinho de Baldur's Gate)
		- Temple of Odin (sim, o nordico, tem uns vikings na cidade)
		- House of Tempus (realmspace)
		- Keep of Gond (artifice god, realmspace, gnomos) (sim tem um templo dele no bg3)
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