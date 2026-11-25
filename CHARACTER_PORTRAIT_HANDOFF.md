# Starhaven character cards and portraits handoff

The Dummy Legends roster has 128 cards with local portrait files and 9 awaiting portraits as of November 25, 2026. All 21 Zharak Emirates Dummy Legends have portraits, including the three officers of the Gilded Standard Company. The next faction in the portrait queue is Irondeep Confederacy.

## Where to work

- [starhaven_wiki.html](starhaven_wiki.html) holds the cards in the `DUMMY_LEGENDS` JavaScript array. The second tag supplies the kingdom used by the Dummy Legends filter. House and clan labels use additional tags.
- [starhaven_chars_image](starhaven_chars_image/) holds the portrait assets. New portraits use 1024 × 1536 PNGs under `dummy-legend-<slug>.png`. The wiki supports an alternate JPG extension for older assets.
- [character_portrait_prompts.txt](character_portrait_prompts.txt) is a reference and working queue. Its headline counts do not track the live roster reliably. Confirm a card’s image path and the local file before treating a portrait as pending. The Image Prompt section was removed from the shared card layout.
- [starhaven-unit-wiki.html](starhaven-unit-wiki.html), [unit_roster.md](unit_roster.md), and [unitImages](unitImages/) give existing unit names and visual references. The card’s `commands` field displays the assigned unit on the character card.

## Portrait status

| Faction | Saved portraits |
|---|---:|
| Karvossa | 4 |
| Stonemark Holds | 4 |
| Frostspire Dominion | 3 |
| Elderwood Sovereignty | 4 |
| Velmora | 6 |
| Ironmere | 4 |
| Golden Coast Federation | 3 |
| Kessirn Horselords | 20 |
| Varathos | 3 |
| Ardenhal | 5 |
| Skyward Isles | 3 |
| Corthane | 7 |
| Verdant Crown | 17 |
| Karath Sultanate | 3 |
| Isle-States of Mirren | 1 |
| Eldridge Kingdom | 6 |
| Thalassian League | 3 |
| Coral Archipelago | 5 |
| Zharak Emirates | 21 |
| Kethravai Isles | 6 |

Three factions have three pending portraits each. In queue order they are Irondeep Confederacy, Sable Isles, and Highland Coalition. Irondeep’s entries are Drelvian Qorandel, Nothessa Vessalon, and Othmarin Thamvyr.

## Decisions worth preserving

- **Kessirn Horselords** has five clans and four characters per clan. Portraits were approved clan by clan. Each clan has a distinct palette, mostly human characters, and a mix of mounted and foot roles. Commanders have named equipment and an assigned unit. The current cards contain later corrections including Börte the Swift’s lance cavalry, Khadan the Howler’s earth shamans, and Qara’s elf-orc heritage. Kessir the Unifier’s card makes him an S-rank archmage wielding Iron Oath as a staff. His approved portrait predates that card edit.
- **Corthane** uses the seven human replacements headed by King Veylan Corth and Queen Seris Corth. The user asked for direct image creation without adding prompt entries for this batch.
- **Verdant Crown** uses five Veldrath, seven Langford, and five Greymantle cards. Athrelis Thyravelland has the longer surname. Velqara is a High Elf, Thornak is a Dwarf, and Kane and Thane Langford are brothers.
- **Karvossa** has four vampire cards with ages listed as Unknown. Other factions use the ages on their own cards.

## Continuing the work

1. Confirm the next faction or batch from the user’s direction. Read its current cards and inspect existing faction portraits or unit art before choosing the armor and palette.
2. Match race, role, weapons, and mounts to the card and the user’s latest instructions. Use reference art for visual inspiration. Give each character a recognizably different face and silhouette. Show foot troops on foot and mounts where the role calls for them.
3. For commanders, fill in `commands` when the assignment is part of the requested card work. Search the wiki and unit roster before using any new unit name. Use the user’s stated ages and biography details.
4. Check the generated portraits visually, verify dimensions, and confirm each card resolves to its saved asset. When editing the wiki, syntax-check the embedded JavaScript with Node and run `git diff --check`.

The working tree has uncommitted changes. The Verdant Crown portraits were untracked at handoff, alongside modifications to the wiki and portrait queue. Include the intended assets and card edits if preparing a commit.
