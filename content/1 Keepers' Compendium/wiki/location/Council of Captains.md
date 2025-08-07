---
type: location
location_type: Building
parent:
  - "[[La Citta]]"
appears_in:
---
Contains a large hexagonal council chamber and two grand wings. The wings contain the offices of the Bureau of Customs and the Bureau of Trade. The Council of Captains meets once a month, but most members prefer to send a representative in their place. The offices of the **Secretary to the Council of Captains**, [[Bianca Micharle]], is also located here. The Secretary is also the head of both Bureaus, and has recently attracted a lot of attention by arming her customs agents and instituting a crackdown on smuggling.

# Council Members (Canon)

- Bianca Micharle, the Secretary to the Council of Captains, and Prince Andru's representative in Council meetings. 
- Talosa Baniasar, the Senior Agent for the local chapter of the Trading Company.
- Daargaz, the leading representative of the Arcane on the Rock of Bral who has been invited to sit on the Council of Captains as a courtesy to his people.
- Nolan DeVries, the Senior Agent for the local office of Gaspar's Reclamations.
- Vasgar Eirenfezt, the head of House Eirenfezt and an independent merchant trafficking in silks and spices.
- Niesse Hurnoc, the senior representative of the Smith's Coster on the Rock.
- Tarilia Moune, a retired adventurer and founder of House Moune, a relatively wealthy and powerful merchant house on the rise.
- Valkan Riogan, owner and operator of Valkan's Legion, the largest and most successful mercenary company on the Rock.
- Kurishi Otobe, also known as the Dragon Lady, is primarily a speculator and moneylender who purchases unusual cargoes and sells them later for a hefty profit.
- Ozamata Ku Murawa, the head of the Murawa family and one of the most powerful and wealthy Shou on Bral.

# Other Council Members
- **Roberto [[Malvessi]]**
- **Don Vico [[Cartocci]]**


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