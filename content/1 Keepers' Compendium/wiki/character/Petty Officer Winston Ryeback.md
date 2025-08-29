---
origin: "?"
class: Galley Cook
race: Giff
type: character
known_locations: []
factions: []
alignment: ""
appears_in: []
relates_to: []
image: "[[winstonryeback.png]]"
---
# Petty Officer Winston Ryeback

**PETTY OFFICER WINSTON RYEBACK**

*Giff Galley Cook*

Petty Officer Ryeback (RIE-bak) is a muscular giff in charge of the food served at the Academy (and on the rare occasion, he crews a ship). Like anyone else who runs a respectable galley, he’s a staunch believer in the four basic food groups: beans, bacon, whiskey, and lard. He’s raucous and brash and gives bear hugs so good you think he might break a rib (but in a good way). His gray skin is usually coated with light sheen of sweat; kitchens are hot!

Quote: “The best way to someone’s heart is through their stomach.”

---

<!-- DYNAMIC:related-entries -->

# Links

```base
filters:
  and:
    - 'type == "entry"'
    - 'relates_to.contains(this)'
views:
  - type: table
    name: "Related Entries"
    order:
	  - file.name
      - file.ctime
  - type: cards
    name: "Related Entries (Cards)"
```

<!-- /DYNAMIC -->
