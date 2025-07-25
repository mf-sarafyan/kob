---
type: location
location_type: Building
parent:
  - "[[La Citta]]"
---
Two-tiered open market hall at the heart of La Città, filled with tents, spice caravans, appraisers, entertainers and luxury shops. The busiest place in the city. Merchants peddle good ranging from local fine craftsmanship to imports from know (and sometimes unknown) Spheres. 

> The Great Market is perhaps the most vital and exciting place in the city. No other place embodies the same love-of-life and gold nor conveys the Rock's mercantile spirit in quite the same way. The Great Market attracts the curious and the greedy from dozens of spheres and it is said that anything can be bought, or sold, in the Great Market of Bral.
> In the stalls and alleyways of the Great Market, you can find armorers, astrologers, bakers, barbers, barristers, beggars, blacksmiths, bookbinders, brewers, butchers, carpenters, carters, cartographers, chandlers, clerks, clockmakers, cobblers, cutlers, dyers, embroiderers, fullers, furriers, gilders, girdlers, glassblowers, glaziers, grocers, haberdashers, horners, hosiers, joiners, limners, mercers, painters, pipers, porters, scribes, tailors, tanners, tinkers, and weavers of every description. Several hundred people constantly throng the square during business hours, so much so that pickpockets and beggars are an enduring problem.

Surrounded by angelic statues, one in each of the second tier's corner, and dominated by its central bell tower, in classic italianesque architecture.

The deeper you need to go in (and the more people you need to push around), the more niche the shops get. Easy-to-find stuff (fine food and drink, silks and tailors, alchemists, smiths) is by the larger kisoks near the canal, but the real oddities are hidden on the second tier: representatives from Merchant Houses, astrologers with star charts, one or two Arcane selling Spelljamming Helms, collectors of cursed items, and shady vendors of stuff that's forbidden where it comes from - but not in Bral. 

The Bazaar sits right by the main canal, across the river from the [[Torri di Corsario]]. 

# Visual Inspiration 

![[Grand Market But The Tower Is Short.png|400]]

![[Grand Market Too.png|400]]

![[grand market 1.png|400]]



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