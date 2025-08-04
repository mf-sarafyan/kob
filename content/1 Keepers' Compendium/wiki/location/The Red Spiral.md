---
type: location
location_type: Street
parent:
  - "[[Viscura]]"
aliases:
  - Bral Red Light
  - Amante Vermiglio
---
O **red light district** de Bral é a **rua em espiral subindo à volta do fungo bioluminescente afrodisíaco vermelho.** 
Sim, é isso. 

As lendas diferem, mas a mais difundida é que ele nasceu do encontro de um fungo aberrante com o sangue de uma **succubus**. O cogumelo em si é chamado de **Amante Vermiglio**, e além de ter "orelhas" que brilham avermelhadas, seus esporos tem efeitos interessantíssimos nos humanóides: euforia, suscetibilidade, e HORNY. Em poucas quantidades, claro. Dizem que doses altas podem causar tosse, dependência, queda de pinto,  transfigurações aberrantes e reencarnação abissal.

Dito isso, os bordéis da cidade são construídos à sua volta; a espiral é uma rua inclinada por dentro dos túneis da montanha que sobe em volta do fungo, construída dos níveis de Bragora até Montevia - e a qualidade e preço dos serviços cresce junto com o Amante. 


# Lista de nomes engraçados de puteiro/motel

**Low City**
- Fogo na Popa
- La Mamma Joanna
- O Morto Muito Louco
- Convés Molhado
- L'Occhio di Kraken (o único que oferece mind flayers)
- O Casco Furado
- De Popa é R\*la
- **Boccaporto Bagnato** (The Wet Hatch)
- Booty Calls
- Segue Sua Nau
- Dungeons and Dragons (for scalies)
**Middle City**
- O Levantar do Mastro
- A Remada Dupla
- Land Ho
- High Tide
- Vento Abundante
- Broadside
- **Pescato del Giorno** (ofertas diferentes cada dia)
- **La Gondola Segreta** (te levam numa gôndola fechada pelos canais)
- A Gôndola do Amor (te levam numa gôndola **aberta** pelos canais)
- Disco Verde (for aliens)
**High City**
- Silky Sails
- Vendo Estrelas
- G Marks the Spot
- Rigger John's (especialistas em shibari)
- Concha da Vênus
- La Perla di Selûne
- Anzóis Dourados
- **Cabina del Capitano** - The Captain's Quarters


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