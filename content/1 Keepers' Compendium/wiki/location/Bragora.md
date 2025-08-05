---
type: location
location_type: Quarter
parent:
  - "[[The Rock of Bral|Bral]]"
---
# The Lower City
Bral é quase um degradê. O acobreado da Città escurece conforme chega perto da linha de gravidade. A parte baixa da cidade é de cinzas e marrons - paredes de tijolo e passarelas de madeira molhada, envergadas perigosamente com o peso da civilização. Bragora é sobre eficiência: cada centímetro é usado pra alguma coisa, e o objetivo final quase sempre é te vender algum produto. Se pra cima os telhados viravam passarelas, aqui até as suas paredes viram escadas.  Sempre que possível as casas tem um puxadinho protuberando pra frente, transformando as ruas e canais em becos escuros. 

Mesmo esse caos é meio arrumadinho. Dá pra ver que as casas são bem feitas, as placas são bem pintadas. Tem canos de cobre refletindo onde a luz consegue alcançar. Algumas construções se sobressaem, principalmente uma que parece a cabeça de uma lula gigante. 
Dá pra imaginar, também, que essa parte da cidade se extendo pra caralho pra dentro da montanha. 

A bagunça diminui vindo pra frente, onde as construções maiores devem ser armazéns e casas de guilda; finalmente levando até as docas, que se expandem em direção ao espaço vazio. Spelljammers lotam o porto, alguns navios, como vocês conhecem, outros mais exóticos; em formas de insetos e crustáceos enormes. Alguns de ponta-cabeça - dá pra ver que tem uma "sub-doca" que leva pra dentro de uma caverna entre essa região e a de baixo. Sim, tem uma mais pra baixo.  

[[Map of Bragora|Mapa Interativo]]

# The Barrios
Bragora é subdividida em ilhas pelos seus canais; algumas inclusive se tornaram enclaves raciais. 

**Bragora externa:**
- [[Dockside]] (Riva Alta e Riva Bassa) é adjacente às Docas 
	- Riva Alta:
		- Muitas warehouses
			- Donos são casas nobres ou Trade Companies
		- [[House Murawa]]: home of the wealthiest Shou in town, next to his warehouses
		- [[Master of the Docks' Office]] - Alta
	- Riva Bassa
		- algumas tavernas ([[The Laughing Beholder]] - Bassa)
		- Frente de loja pra Spelljammer stuff menos glamouroso produzido em Soffiera. sailmakers, armas basicas, etc
	- Ponte enferrujada entre riva alta e bassa sempre com umas 3 gondolas estacionadas vendendo boiled praws e fish heads
- [[Arsenale]] - shipyards da cidade
	- [[Cuttle Tower]] (Shipwright's Guildhall)
	- mts acessos (elevadores inversores) pras docas de soffiera
	- Museu
- [[Lo Strozzo]] (The Strangle/The Ropeways) é um labirinto de cordas e plataformas de madeira
	- [[The Council of The City]] 
	- tanneries, ropemakers (stinky)
	- Tavernas mais hardcore da cidade. (The Rockrat)
- [[Shou Town]] é o bairro asiático (a Liberdade). O mais comfy de Bragora
	- Onde fica o [[Lesser Market]]
	- [[Shou Embassy]]
	- Tem a actual [[Yakuza]]. O nome canon é [[Yakuza]] mesmo. A [[La Mano Legata|La Mano]] não tem muita força aqui
	- Tea houses, jardinzinhos e italian-asian fusion food
	- Lanternas tradicionais e neon futurista
- [[The Burrows]] é o bairro dos halflings, gnomos e outros pequeninos
	- Bem inclinado, bom pra casinhas cavernosas
	- Muitos lugares bons pra comer! Osteria da Nonna meu. Turismo gastronômico
	- mostly residencial. uns poucos tinkers. a maioria mora aqui e trabalha em outro lugar
	- Tem que se abaixar pra passar pelas portas
	- Se dão bem com os amigos kobolds do outro lado do canal (atravessando a *ponte di piccolo*)
- [[Gifftown]] (autoexplicativo e autoexplosivo)
	- [[The Hippodrome]] (não sei o que é, mas gifftown precisa de um lugar com esse nome)
	- lojas de fumo (stinky)
	- Café com pólvora
	- shooting ranges
	- pode conter estadounidenses
- Andru's Gift:
	- Elevador no cruzamento entre shou town, mezzalucce, lo strozzo. Sobe pra [[La Citta]].
**Lower Viscura (Bragora Interna):**
- [[Mezzaluce]] (The Half-light): 
	- velas, lanternas
	- o [[Low Magistrate's Office]]. 
	- [[Cartocci]] te fazendo calar a boca
	- Teatro silencioso
- [[Stillwater]] (L'Acqua), quase sempre alagado, sempre pingando. Fica embaixo do elevador de La Citta pra Montevia.
	- Várias bathhouses (algumas com final feliz, mas de um jeito triste)
	- Fish market (stinky)
	- secret fighting pits with lots of drowning
	- Vendedores de guardachuva. 
- [[Micelio]] (Fungal Warrens), onde crescem fungos estranhos.
	- [[The Red Spiral]]
		- O Morto Muito Louco: bordel undead
	- [[Illithid Embassy]]
	- Alquimistas e apotecários (e suas guidas)
- [[Dwarven District]] (autoexplicativo e muito bem lapidado). Segundo melhor bairro daqui
	- Muitas casas que conectam com Soffiera embaixo e [[Steelrows]] em cima
	- Vários guild halls - stonecutters, smiths, brewers
	- cervejarias
	- The Rusty Axe
	- Dwarven Boarding Company (mercs) (outro escritorio em [[merctown]])
	- Fervorosamente evitam ser território de gangue
- [[Wyrmtown]] (dracons, dragonborns, kobolds, e com certeza não tem nenhum dragão disfarçado)
	- [[Dracon Consulate]]
	- Comida absurdamente apimentada
	- Bancos menos glamourosos, exchange houses clandestinas, lojas de antiguidades (pq eles querem ter tesouros)
	- Serviços mt específicos tipo limpeza de escamas e dentistas especializados 


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