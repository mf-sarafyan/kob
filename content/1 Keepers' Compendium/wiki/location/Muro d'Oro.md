---
type: location
location_type: Sub-district
parent:
  - "[[La Citta]]"
appears_in: []
image: ""
---

# Muro d’Oro
Do alto do lago, com a luz artificial se derramando sobre a água, o Muro d’Oro brilha. Não por mágica, mas por metal: frisos dourados, cúpulas de cobre polido, placas metálicas gravadas com brasões e letras ornamentadas. É a fachada mais reluzente de Bral — e, como toda fachada, esconde muito mais do que mostra.

O bairro é construído rente ao penhasco, abaixo das Docas Reais e acima do Grande Lago. A parede da rocha foi esculpida com arcadas, colunatas e nichos; como se a montanha tivesse sido convencida a virar palácio. São poucos os prédios aqui, mas cada um ocupa espaço como se valesse um distrito inteiro.

Por fora, é elegância. Por dentro, é papelada.  
O Royal Exchequer — sede da tesouraria da Coroa — domina o centro, com bandeiras azuis e brancas esvoaçando ao vento. O prédio é um monstro em mármore branco, com corredores de colunas que se perdem nos níveis inferiores, onde contratos são arquivados em cilindros de vidro e aço. Ali são computados os impostos sobre tudo: da carga das galés aos hectares do campo. 

Ao leste, os bancos **Dottori** dominam os quarteirões. Ninguém chama de “banco”, claro. São _casas de crédito_, _galerias_, _conservatórios financeiros_. Cada fachada é uma aula de opulência: mármore polido, esculturas de deuses mercantis — Ptah, Waukeen, às vezes mesmo Tiamat, se o cliente for generoso — e janelas em vitral espelhado. O público é bem selecionado: nobres, capitães de grandes cargueiros, intermediários de consórcios anônimos.

E entre esses colossos, um sem-número de escritórios de câmbio e seguradoras menores: placas de madeira bem pintadas, varandas onde corretores bebem vinho branco enquanto gritam ofertas de carga. O som aqui é outro: sinos de metal, guizos de gôndolas oficiais, pena riscando papel de linho, e o tilintar sutil de moedas sendo pesadas. O cheiro não é de peixe ou suor — como em Bragora —, mas de cera de vela, incenso leve, e documentos antigos.

Do lado de cá da **Via Riserva**, o tom muda. A Oeste, e cercada pelo pequeno canal, tem uma pontinha de residências de luxo, amontoadas na parede. A pompa cívica dá lugar ao silêncio doméstico. Um pequeno arco de pedra atravessa o canal estreito, permitindo a passagem de gôndolas privadas, menores e mais silenciosas.

Essa seção do bairro, separada pela água e protegida por portões ornamentados, abriga **casas luxuosas em estilo baixo**, com jardins internos, pérgulas de pedra e fontes murmurantes. As janelas aqui têm cortinas grossas. Os portões têm brasões esculpidos em ouro e cobre. Servos com librés discretas carregam frutas exóticas, quadros, caixas lacradas — e ocasionalmente, mensagens mais pesadas.

É um lugar de vizinhos que não se cumprimentam.  
Um lugar onde se paga caro pelo silêncio, pela distância, pela vista do lago — e pela proximidade com o verdadeiro poder.

É um bairro quase silencioso, com movimentos precisos, e sorrisos que não chegam nos olhos. Mas todo mundo sabe: é aqui que se mede o pulso de Bral. Se o ouro para de fluir no Muro d’Oro, o resto da cidade afunda.


## Locais Notáveis

- **Royal Exchequer** – Câmbio central da Coroa; quase o "banco central" da cidade. Bem no centro do distrito, em frente à ponte para os [[Festival Grounds]]. Lembrando que Bral não tem uma moeda central, e o controle do câmbio de moedas estrangeiras via **Royal Exchequer** é uma das maiores fontes de renda da Coroa. Até existem outras casas (ou profissionais) de câmbio, mas não pagar as taxas é um atalho rápido para as celas da [[Torri di Corsario]].
- **Bancos Dottori** – Palazzi luxuosos que funcionam como casas bancárias e galerias de arte.  
- **Praça da Moeda** – Em frente ao Exchequer. A única parte "plana" do bairro. Praça coberta com colunas douradas onde cambistas e agiotas oferecem serviços em todas as moedas conhecidas (e algumas inventadas).  


## Dinâmica

O Muro d’Oro é palco de disputas silenciosas entre coroa, famiglias e companhias mercantis. Quem domina a moeda, domina Bral — e todos sabem disso.  

---

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
