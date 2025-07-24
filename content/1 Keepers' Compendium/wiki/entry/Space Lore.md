---
type: entry
entry_type: 
relates_to: 
author: DM
---

```dataview
    TABLE entry_type, author
    WHERE contains(entry_type, this.file.link)
    SORT file.ctime DESC
```
