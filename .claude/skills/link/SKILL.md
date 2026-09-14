---
name: link
description: Make a new file, folder, document or outside source findable from the manual with the smallest correct route. Use when the owner says "link this", "add this to the system", "make sure you can find this", "route this", "remember where this lives", or adds something the system cannot currently find.
argument-hint: "<file, folder, link or source> [what it is for]"
---

# Link

A thing the assistant cannot find does not exist. This adds one clean route to it, in the right place, and proves the route works.

1. Confirm what the target is and that it exists. Open it and read enough to know what it is. For an outside link you cannot open, write that access is not checked.
2. If what it is for, or where it belongs, is unclear, ask one short question. Use what they already said.
3. Find the right home using `System/Map.md`. Usually the route goes in an existing index, not the root manual:
   - Project material goes in that project's `_index.md`.
   - A business source goes in the matching `Context/` file.
   - A tool goes in `System/Connections.md`.
   - Something outside the folder that the owner uses often can be a `reference_` memory.
   - Only a whole new area of the system earns a row in the manual's knowledge base table.
4. Write one line: when to use it, then the exact path or link. Never copy its contents or its changing numbers into the route.
5. If a route already works, change nothing and say so.
6. Follow the route back from the manual to the index to the target, and confirm it lands.
7. If `CLAUDE.md` changed, copy it over `AGENTS.md`. Run `python3 Tools/check.py`. Commit.

Reply in two lines: what was linked and where the route lives.
