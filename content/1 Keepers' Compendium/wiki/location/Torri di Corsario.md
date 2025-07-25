---
type: location
location_type: Building
parent:
  - "[[La Citta]]"
aliases:
  - Bral's Tower
  - Tower of Bral
  - Bral Donjon
---
A massive bastion of ash-gray stone with bronze filigree and rotating gun-towers. A stocky gray mound amid [[La Citta]]'s orange and terracotta terraces. Part keep, part garrison, part prison. The Old Castle of Captain Bral, the city's founder.

- **Public Face**: Bral’s show of strength—its ballistae track ships in the sky from mechanized turrets.
- **The Lord Donjon**: A brutal realist loyal only to stability. Known to host midnight strategy salons.
- **The Deep Cells**: The four subterranean levels use inverse gravity and null-magic runes. Prisoners are “turned inward,” with whispers of something monstrous guarding the lowest vault.

![[Il Torre Di Corsario.png|400]]

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