---
type: location
location_type: Building
parent:
  - "[[La Citta]]"
aliases:
  - Bral's Tower
  - Tower of Bral
  - Bral Donjon
appears_in: []
image: "[[Il Torre Di Corsario.png]]"
---
# Torri di Corsario

A massive bastion of ash-gray stone with bronze filigree and rotating gun-towers. A stocky gray mound amid [[La Citta]]'s orange and terracotta terraces. Part keep, part garrison, part prison. The Old Castle of Captain Bral, the city's founder.

- **Public Face**: Bral’s show of strength—its ballistae track ships in the sky from mechanized turrets.
- **The Lord Donjon**: A brutal realist loyal only to stability. Known to host midnight strategy salons.
- **The Deep Cells**: The four subterranean levels use inverse gravity and null-magic runes. Prisoners are “turned inward,” with whispers of something monstrous guarding the lowest vault.

![[Il Torre Di Corsario.png|400]]

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
