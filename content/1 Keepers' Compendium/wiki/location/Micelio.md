---
type: location
location_type: Sub-district
parent: "[[Bragora]]"
appears_in: []
image: ""
---

# Micélio (Fungal Warrens)

**Micélio** é o subdistrito mais estranho de Bragora. Uma rede de cavernas úmidas onde colônias de fungos crescem até o teto, soltando esporos brilhantes que iluminam o bairro com tons de vermelho, azul e verde. Os becos são tomados por cheiros fortes — ora de mofo, ora de poções fervendo. É aqui que a cidade experimenta com tudo o que não caberia em outro lugar: alquimia, drogas, prazeres bizarros e diplomacia alienígena.  

### Locais de Destaque
- **[[The Red Spiral]]**, um distrito de bordéis e prazeres exóticos construído em torno de um gigantesco fungo bioluminescente que atravessa vários níveis da cidade.  
	- **O Morto Muito Louco**, o mais infame dos bordéis, especializado em acompanhantes mortos-vivos “carregados” por magia.  
- **[[Illithid Embassy]]**, um edifício orgânico e alienígena, onde os mind flayers costumavam visitantes em silêncio desconfortável. Hoje, a comunidade ilítide está passando por uma renascença cultural; uma facção de Ilitides Veganos vem crescendo em tentativa a se inserir melhor na sociedade educada da cidade (onde consumir os cérebros dos amiguinhos ainda é considerado rude). 
- **Oficinas de Alquimistas e Apotecários**, que usam os fungos locais para produzir drogas, perfumes, venenos e remédios — todos difíceis de distinguir uns dos outros.  
- **Mario's**: a casa de [[Mario Zenonni]], um refúgio seguro pra todos que não se encaixam. 

#### Philosophi Spori
A **Philosophi Spori** é a guilda-escola de alquimistas e apotecários de Bragora, estabelecida em **Micelio**. Sob suas abóbadas cobertas de fungos bioluminescentes, aprendizes trituram ervas, fervem extratos e inalando vapores suspeitos em busca de novas fórmulas.  

A guilda atua tanto como **escola de magia alquímica** quanto como **corporações de ofício**: regula preços, garante a qualidade mínima das poções vendidas e arbitra disputas entre apotecários rivais. Seus membros ostentam manchas de tinta e queimaduras nas mãos como medalhas de honra.  

- Respeitados e temidos, os Spori são vistos como **gênios loucos**: curam um dia, envenenam no outro.  
- Sua influência se estende até [[The Red Spiral]], onde fornecem substâncias tanto para o prazer quanto para o vício.  
- Diz-se que até os [[Illithid Embassy|illithids]] respeitam a guilda, por seu conhecimento singular sobre fungos e fluidos cerebrais.  

### Cultura e Vida
- Morar em Micélio significa viver cercado por **luzes psicodélicas e cheiros intensos**; visitantes muitas vezes saem “alterados” apenas pela exposição prolongada aos esporos. 
- O distrito é território fértil para facções menores, guildas alquímicas e experimentos ilícitos. Mesmo assim, os [[Zenonni]] têm um carinho às vezes pouco agressivo pelos habitantes. 
- Apesar do caos, há um certo **sentido de comunidade excêntrica**: artistas, bruxos e apotecários veem no bairro um refúgio para criações que seriam proibidas em qualquer outro lugar.  
- O lugar inspira tanto fascínio quanto repulsa — dizem que, se Bragora tem um coração estranho e pulsante, ele está escondido em Micélio.  

## Vibe visual
Mariposas gigantes e coloridas rodeando postes-vivos feitos de fungo bioluminescente.

Uma placa "Não Comer!" com uma caveirinha na frente de um cogumelo particularmente apetitoso. 

Feirinhas vendendo poções, bálsamos, e picles. Os vendedores tem cogumelinhos crescendo nas costas - não sabemos se plantados ou na própria pele.

Pessoas vão pro outro lado da rua pra deixar um mind flayer passar flutuando.

<!-- DYNAMIC:related-entries -->

# Links

## Sub-Locations
```base
# Only show locations whose 'parent' includes *this* location
filters:
  and:
    - 'type == "location"'
    - or:
        - 'list(parent).contains(this)'
        - 'list(parent).contains(this.file.asLink())'
        - 'parent == this'
        - 'parent == this.file.asLink()'

# Column labels
properties:
  file.name:
    displayName: "Name"
  location_type:
    displayName: "Type"
  parent:
    displayName: "Parent"

views:
  - type: table
    name: "Sub-Locations"
    order:
      - file.name
      - location_type
      - parent
  - type: cards
    name: "Sub-Locations (Cards)"
```

## Factions Based Here
```base
filters:
  and:
    - 'type == "faction"'
    - or:
        - 'location == this'
        - 'location == this.file.asLink()'
        - 'list(location).contains(this)'
        - 'list(location).contains(this.file.asLink())'
properties:
  file.name:
    displayName: "Name"
views:
  - type: table
    name: "Factions Based Here"
    order:
      - file.name
  - type: cards
    name: "Factions (Cards)"
```

## Related Entries
```base
filters:
  and:
    - 'type == "entry"'
    - or:
        - 'list(relates_to).contains(this)'
        - 'list(relates_to).contains(this.file.asLink())'
properties:
  file.name:
    displayName: "Name"
views:
  - type: table
    name: "Related Entries"
    order:
      - file.ctime
  - type: cards
    name: "Related Entries (Cards)"
```

<!-- /DYNAMIC -->
