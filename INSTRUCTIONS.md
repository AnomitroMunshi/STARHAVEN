# STARHAVEN — Project Instructions

## What This Project Is

**The Starhaven Chronicles: Sundered Age** is an original high-fantasy universe — a full novel-length story (9 chapters), an interactive HTML wiki, a character encyclopedia, a military unit registry, a world atlas, and 26 original in-universe ballads. It is a personal creative project, not a game or published work.

**Core premise:** The story follows Rayden Cale from orphan survivor of a massacre (Year ~1025) through becoming King of Starhaven and building a kingdom. The tone is military/political fantasy — grounded, character-driven, with earned authority rather than chosen-one tropes.

**Timeline:**
- Year ~1025 — Oaksmane Orphanage massacre. Rayden survives.
- Year 1032 — Starhaven founded. Starhold proclaimed.
- Year 1047 — Story present (Chapter 8).
- Year 1052–1053 — Wiki/Codex reference date (in-universe "current").

**The primary supernatural threat** is the Void / Corruption. Malgrath is the Void's presiding force — perceivable only by Elysia Nocturne. Void entities are catalogued by Zareth Kull's Void Breakers. The Ashenveil region is its primary domain.

---

## Project Files

| File | Purpose |
|---|---|
| `starhaven_wiki.html` | Main interactive wiki — Story, Chronicles, Characters, Army Registry, Atlas, Map, Museum, Ballads |
| `starhaven-unit-wiki.html` | Interactive unit registry with filter system (branch, source, armor class) |
| `starhaven_codex_final.html` | Character encyclopedia — visual cards, abilities, relationships, portraits |
| `starhaven_armies_master.html` | Military force registry — all armies, garrisons, naval, siege engines, mercenaries |
| `more_charchter_bio.txt` | Detailed character descriptions for AI art generation |
| `unit_commanders.md` | Commander reference document |
| `Lores/chapters/` | 9 HTML story chapters (Starhaven_Chapter1–9.html) |
| `Lores/Ballads/` | 26 MP3 audio ballads by in-universe bard Dren Solm |
| `Lores/Mueseum/` | Historical images — army unit art, locations, battle scenes |
| `Lores/maps/map.png` | World map with pan/zoom |
| `Lores/weapons/` | Weapon images for all named weapons |
| `starhaven_chars_image/` | 70+ character portrait PNGs |
| `unitImages/` | Unit art for the unit wiki |

**Design system (all HTML pages):**
- Dark background: `--bg: #05060A` to `#181A26`
- Gold accents: `--gold: #D4A832`, `--gold2: #EEC854`, `--gold3: #FAE090`
- Fonts: Cinzel Decorative (titles), Cinzel (headings), Crimson Pro (body), JetBrains Mono (labels)
- Grain texture overlay via SVG filter
- Sidebar navigation + main content layout

---

## Story — Chapter Summary

**Chapter 1 — The Boy Who Ran Through Fire**
Rayden's origin. The Oaksmane massacre by Lord Halbrecht Veyne — the Night of Fire. Meets mentor Elira Voss (former A-rank adventurer), receives Dawnpiercer. Temporal Frenzy first manifests.

**Chapter 2 — Ashes Before Kingdoms**
Mercenary period. Battles: Lowmere Field, Siege of Blackwall Ridge, Red Orchard Engagement. Death of Selene Voss (Elira's daughter). Rayden acquires Kingsbane. Meets "the Woman Who Slapped the Monster." Ends at Veynehold.

**Chapter 3 — The Wandering Legends**
Aftermath of Veynehold. Meets Kael Varric — key introduction. Black Rain Ambush. Star-Eyed Huntress (Lyria). Arrives at Ironmane Farm. Havenfire — the settlement that becomes the kingdom's seed.

**Chapter 4 — The Gathering Storm**
Havenfire grows. Velkan joins (the Scholar of Vaelmark). Silverfire Trial — proving legitimacy. Kael's army joins. Meeting Seraphine. The Cleansing March.

**Chapter 5 — The Birth of Starhold**
Building the Starhold fortress. The Sable Conclave Crisis. The Greenveil Catastrophe (Thorin's introduction). March before Starhold.

**Chapter 6 — The War of Starhold**
The siege war. Mustering at Greenveil. First Assault. Battle for Outer Walls. The Heart of Corruption. The Birth of Starhaven — kingdom proclaimed. The First Dawn of Starhaven.

**Chapter 7 — A New Beginning** *(~19,000 lines — longest chapter)*
Building the kingdom. Year the Sky Changed (Aurelia/Zephyros). What the Sea Carries (naval alliances). The Third Chain. Years ~1033–1046 of nation-building.

**Chapter 8 — A New Beginning (cont.)**
Iron and Archive · The Western Horizon · Saltmere · The Bond That Was Already There. Set ~Year 1047. Western expansion and naval alliance.

**Chapter 9 — What the Mountains Sent**
Latest chapter. Mountains of Varathos region involved.

**Short Stories / Chronicles:**
- *The Ashfield Interception* (Year 1049) — Kael stops an army with a wall
- *The Trial of the Eleven* (Year 1048) — the Pillars fought each other
- *The War of the Ashen Passage* (Year 1046) — southern border war

---

## The Eleven — Core Leadership

The Eleven are Starhaven's supreme council. Each holds a **Pillar** title representing their domain, commands a personal army, and governs a city or domain.

| # | Name | Title / Pillar | Army | Key Trait |
|---|---|---|---|---|
| 1 | **Rayden Cale** | King · Pillar of the Dawn | Dawnguard (elite 500) | Fights from the ground. No crown, no ceremony. |
| 2 | **Kael Varric** | Minister of Defense · Pillar of the Wall | Ironwall (15,000) | Never lost a fortress. Immovable. |
| 3 | **Lyria Valen** | Pillar of the Eye | Silent Wardens | 127yo Moon Elf. Intelligence commander. Reads environments as text. |
| 4 | **Velkan Drake** | Grand Arcanist · Pillar of the Mind | Ninth Sky Corps | Drakari scholar-battlemage. Always thinking 3 steps ahead. Notebook always in hand. |
| 5 | **Seraphine Mire** | Pillar of the Heart · Saintess | Ashen Guard | Half-Celestial healer-fighter. Warm without performing warmth. |
| 6 | **Nyx Ravel** | Pillar of Secrets | Null Blades (classified) | Shadekin, shadow-bonded. The absence of presence. Already knows. |
| 7 | **Thorin Blackroot** | Pillar of the Land · Lord of Greenveil | Primal Vanguard | Wildblood Dwarf. Root-deep stillness. One sentence, usually correct. |
| 8 | **Aurelia Vex** | Pillar of the Sky | Stormriders | 21yo Storm Elf, youngest of the Eleven. Already moving before the problem is described. |
| 9 | **Elysia Nocturne** | Pillar of the Veil | Veil Watch | Astralborn, does not age. Only person who can perceive Malgrath directly. |
| 10 | **Bob Vale** | Pillar of the Bond | Resonance Corps | Soul Link Anchor. |
| 11 | **Cain Drakhar** | Pillar of Iron | Iron Legion | Based in Forgehaven. Commands 280 Iron Tide arcane tanks. |

**Character weapons (key):**
- Rayden: Dawnpiercer (curved saber), Kingsbane (6ft greatsword), Vossfang Bracer (grappling hook), Onslaught (transforming sidearm). Mount: Warblade.
- Kael: Gravetide (tower shield), Ironwall Judgement (war hammer). Mount: DreadMaw (armored rhino).
- Lyria: Eclipsing Whisper (moonwood longbow), Silverthorn Daggers. Pet: Nymeris (eagle).
- Velkan: Cinderwake (dragon staff). Mount: Pyrewing (volcanic elite drake, 40ft wingspan).
- Seraphine: Mercy (sacred censer), ceremonial blade.
- Nyx: Shadowfang Daggers, Whisper Crossbow. Mount: Umbra (shadowfang panther).
- Thorin: Stone-Fist Gauntlets, Rootcleaver (living axe). Mount: Grond (alpha dire bear).
- Aurelia: Storm Spear, Electro-Blades. Mount: Zephyros (Asiatic Elder Storm Dragon, several hundred years old).

---

## Character Generation

Character portraits are AI-generated. Reference descriptions live in `more_charchter_bio.txt`. Key consistency rules:

- Each character's **race** determines physical baseline: Moon Elves are ageless (Lyria appears 27 at 127), Drakari have draconic features (Velkan: amber-gold slit pupils), Stoneborn Humans have mineral-grey skin (Kael), Shadekin are dark-adapted grey-charcoal (Nyx), Astralborn do not age (Elysia), Storm Elves are Tempestian (Aurelia: perpetually windswept), Wildblood Dwarves have bark-textured skin (Thorin).
- **Armor and weapon designs** must match established descriptions — these are consistent across wiki, codex, and art.
- **Kai** (Arch-Battlemage) has a half-burnt face and rarely removes his hood. He is Rayden's childhood best friend from the orphanage, revealed during the War of Starhold. Born name: Caleum.
- **Elira Voss** is Rayden's mentor — the Iron Widow. Her daughter Selene died in Chapter 2.
- New characters receive detailed visual descriptions in `more_charchter_bio.txt` before portrait generation.

---

## Lore & World-Building

**Cities:**
- **Starhold** — capital, 280,000+, Year 1032. Rift Gate Terminus. Throne seat.
- **Goldgate** — commercial hub, ~280,000. Adventurers Guild seat. The Hearthrow (14 taverns). Guild Master: Drev Holt.
- **Sancthaven** — holy city, 95,000+. Grand Cathedral (capacity 40,000). Seraphine's domain.
- **Forgehaven** — industrial capital, 120,000+. Cain Drakhar's domain. Iron Tide built here.
- **Saltmere** — western coastal port, ~180,000. Dawnfleet HQ. Thalassian League embassy.
- **Vaelmark** — arcane capital, 60,000+. Royal Athenaeum. Ninth Sky Corps base. Velkan's domain.
- **Greenveil** — living city (grown, not built), 45,000+. Thorin's domain.

**Fortresses:**
- Ironpass Citadel — eastern border, 3 concentric rings, 60,000+ garrison. Never breached. Commanded by Brek Stonefall.
- Frosthold Bastion — northern mountains. Brynhild Voss commands.
- Dawncliff Sea Fortress — 300ft coastal cliff, 8 battery emplacements. Ela Seawall commands.
- Ashenveil HQ — Void research region. Zareth Kull's domain.

**Infrastructure:** Rift Gate network (4 in Starhold, 3 in Vaelmark, 2 each in Goldgate and others). Railway system built by Cyrus Vexley.

**Allied Nations:**
- **Thalassian League** — naval ally. Admiral-King Crest Vane (59yo). Seren Vane (Admiral-Consort). Embassy in Saltmere.
- **Varathos** — Giant Nation. Elder Kira (200+, 12ft), Elder Dravan. First giant-human alliance in 4,000 years. The lantern moment at Karath Dun — Kira held light 40ft above stone for trapped prisoners.

**The Void:** Supernatural corruption threat. Ashenveil region. Malgrath is the Void's presiding force. Void entities are taxonomized by Zareth Kull. Anti-corruption treatment exists for armor.

---

## Military Structure

**Total: ~400,000+ active military**

### Pillar Armies (personal to The Eleven)
Dawnguard · Ironwall · Silent Wardens · Ninth Sky Corps · Ashen Guard · Null Blades · Primal Vanguard · Stormriders · Veil Watch · Resonance Corps · Iron Legion

### Grand Standing Army (Grand Marshal Rhegar Thorne, 80,000)
- 1st Field Army — Doran Ashe — heavy infantry vanguard
- 2nd Field Army — Clea Vorn — cavalry/scout
- 3rd Field Army — Brek Tane — central defense rotation
- 4th Field Army — Veyra Tal — reserve/rapid redeployment
- Starfall Legion — elite standing reserve

### Heavy Cavalry
- Ironmane Lancers (Dresh Ironmane) — fastest heavy charge on the continent
- Black Charge — shock cavalry, first-contact breaching
- Windlance Cavalry — light cavalry, long-range flanking

### Specialized Units
- Arcane Artillery Corps (Arch-Battlemage Kai) — synchronized elemental bombardment, opens every major engagement
- Void Breakers (Zareth Kull) — Void entity hunters, Ashenveil operations
- Ironbolt Division — heavy ranged/ballista
- Holy Knights of Starhaven (Brynhild Voss) — consecrated heavy knights
- Crownwardens — palace/capital guard
- Dawnscope Corps — reconnaissance specialists
- Iron Tide — 280 arcane tanks built in Forgehaven

### Naval (240 warships total)
- Dawnfleet (Valtor Crane, 140 warships) — HQ at Saltmere
- Tideguard — support fleet
- Crowsnest Fleet — coastal/classified intelligence

### Fort Garrisons
- Ironpass Citadel — 60,000+ (Brek Stonefall)
- Dawncliff Sea Fortress — 28,000 (Ela Seawall)
- Frosthold Bastion (Brynhild Voss)
- Greenveil Defense Forces — 18,000–35,000

### Mercenaries (on retainer)
The Broken Crown Company · The Iron Reavers · Stormwing Brotherhood · Void Hounds

### Siege Engines
Ironveil Trebuchet Battery (18 units) · Rampart Siege Tower Division · Skyhammer (aerial bombardment) · Ironjaw Battering Ram Division · Ironbolt Static (fortress ballista network) · Void Siege Battery (classified) · Groundbreaker Tunnel Assault Corps · Stonethrow Corps

---

## Unit Wiki

The unit wiki (`starhaven-unit-wiki.html`) is a filterable registry of every named military unit in Starhaven. Each unit entry contains:

- **ID, name, branch, source** (own / allied / mercenary / enemy)
- **Class labels** (e.g., Heavy Infantry · Vanguard)
- **Commander, army affiliation, total strength**
- **Location**
- **Notes** — detailed doctrine, history, behavioral quirks, notable engagements
- **Equipment slots** — Body, Helm, Weapon, Secondary, Mount, etc. with full descriptions

**Filter dimensions:**
- Branch: Infantry · Cavalry · Flying · Magic · Naval · Siege · Recon · Support
- Source: Own (🏰) · Allied (🤝) · Mercenary (⚔) · New (🆕) · Enemy (👁)
- Armor class: Heavy · Medium · Light · None

**Unit entry rules:**
- Notes should capture **doctrine, not just description** — what the unit does and *how* it thinks
- Equipment descriptions explain *why* each item works the way it does, not just what it is
- Commanders are named and their personal doctrine is present in the notes
- Numbers are specific (not "hundreds" — give exact counts where established)
- Units from allied nations (Velhold Recurve Company, etc.) are marked as attached/allied, not Starhaven-raised

**Current unit wiki branch structure:**
- The Ninth Sky Corps fields units across two branches: Drake Riders under **Flying**, Battlemages/Artillery Corps under **Magic**
- They share the same parent army (Ninth Sky Corps — Velkan Drake) but are categorized by unit type in the wiki filter

---

## Ballads

26 original MP3 ballads by **Dren Solm** (in-universe royal chronicler and "Ironvoice" bard) live in `Lores/Ballads/`. They include battle anthems, nation anthems, and personal ballads (Kira's Door, Nobody, No Dragon Chose Her, etc.). Dren Solm is everywhere and invisible — ink-stained right hand, notebook always in hand, lute always on back.

---

## Tone, Style & AI Writing Persona

### The Core Tone

**Grounded military fantasy.** The world has dragons, magic, and giants — but none of it is treated as spectacle. The writing assumes the reader is already standing inside the world, not being shown it from the outside. Wonder is earned by what characters *do with* extraordinary things, not by describing those things as extraordinary.

**Weight over wonder.** A drake is not described as majestic. It is described as an 18–24ft wingspan predator whose bond with its rider grounds it permanently if that rider dies. The magic is real, specific, and has rules. The cost is always present.

**Competence as character.** The people in this world are very good at what they do. Their competence is not explained — it is demonstrated. Kael Varric doesn't say he never loses a fortress. The text describes what happens when someone tests his fortress.

**Earned emotion.** Nothing is announced. The lantern at Karath Dun — Kira holding light 40ft above stone so trapped prisoners could see — is not called moving. It is described, and left. The reader arrives at the feeling themselves.

---

### Writing Style

**Be specific, not vivid.** "3,500 mages" is better than "a vast mage corps." A named engagement (the Five Thrones War, the Ashfield Interception) is better than "countless battles." A named weapon is better than "her blade."

**Declarative sentences.** Short, confident, present-tense for wiki and codex entries. The world knows what it is. It does not hedge.

**Doctrine over description.** For units and military writing: capture *how the unit thinks*, not just what it carries. The Ninth Sky Battlemages' first cast is always defensive — that one line tells you more than a paragraph about their robes.

**Show the gap.** If something is unresolved — Dael Ashe flagged the void-origin casting vulnerability to Velkan Drake; the gap has not been resolved — say it plainly. Unresolved problems are more interesting than tidy ones.

**Names anchor everything.** Use them. Commander names, weapon names, battle names, city names. Proper nouns make the world feel like it existed before this sentence.

---

### Voice by Content Type

**Story chapters** — third-person limited, past tense, character-close. The narration knows what Rayden knows. No omniscient commentary. Dialogue is purposeful — characters say what they need to say, not what the reader needs to hear explained. Subtext carries more than text.

**Unit wiki notes** — third-person, present tense, confident. Written as if from a military analyst who has read every after-action report. Doctrine first, personality second. Commander philosophy embedded in how the unit operates. No passive voice.

**Codex / character entries** — third-person, present tense, compressed. Each detail earns its place. Physical description only if it reveals character (Kael's mineral-grey skin is Stoneborn heritage — it tells you what he is). Relationships named, not summarized.

**Ballads (Dren Solm's voice)** — lyrical, in-universe, first or second person. Solm writes *about* the people of Starhaven from the inside. His ballads are not propaganda — they capture truth as a bard sees it. Grief, pride, irony, weight. Rhyme and rhythm are deliberate, not forced.

---

### What to Avoid

- **Chosen-one framing.** Rayden is not destined. He survived, then decided. The distinction matters.
- **Hollow heroism.** Courage in this world is specific: Doran Ashe's black armor and the gold lion-crest people follow into a breach. Not "brave."
- **Purple prose.** No "the sky wept" or "darkness consumed all." If the sky matters, describe it factually. If darkness is a threat, name what it does.
- **Vague military writing.** "A large force" is not a Starhaven sentence. Name the army, give the number, name the commander.
- **Announced emotions.** Do not write "Rayden felt grief." Write what Rayden does when grief is in the room.
- **Inflation.** Not everything is the greatest, most powerful, or most feared. Reserve superlatives for things that have genuinely earned them (Kira's Karath Dun moment, Kael's unbroken fortress record, Kai's counter-magic archive).
- **Allied nations as props.** The Thalassian League and Varathos have their own perspective. Crest Vane's "the ocean is not the obstacle" is a worldview, not a catchphrase.

---

### The Narrator's Persona

The implied narrator of Starhaven is **a historian who was present**. They have access to field reports, personal accounts, and doctrine documents. They do not editorialize. They do not need to. The facts — specific, named, numbered — do the work. When something is remarkable, it is described at the same register as everything else. That restraint is the style.

For wiki and codex content specifically: write as if the Royal Athenaeum of Vaelmark produced the document. Precise, exhaustive on detail, quietly proud of the institution it describes.

---

## Writing & Lore Consistency Rules

- **Preserve established facts** — character ages, races, weapon names, city populations, battle outcomes, and relationships are fixed unless the user changes them.
- **Voice** — the narrative is grounded and earned. Characters are competent. Authority is demonstrated, not declared.
- **Rayden does not use a crown or ceremony.** He leads from the ground.
- **Kael Varric has never lost a fortress.** This is a hard fact, not flavor.
- **Kai's identity** (Rayden's childhood friend, the boy from the orphanage, revealed at the War of Starhold) is a major story beat. Handle with care.
- **The Void is not decorative** — it is an active existential threat with lore implications. Malgrath is not to be described as perceivable by anyone except Elysia Nocturne.
- **Allied nations are not absorbed** — the Thalassian League and Varathos Giant Nation are partners, not subjects.
- When adding new units or characters, check for consistency with existing army structures and pillar domains before placing them.
