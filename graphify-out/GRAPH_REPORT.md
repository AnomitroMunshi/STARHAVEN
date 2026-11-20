# Graph Report - STARHAVEN  (2026-11-18)

## Corpus Check
- Large corpus: 870 files · ~1,269,864 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 872 nodes · 1570 edges · 62 communities (47 shown, 15 thin omitted)
- Extraction: 92% EXTRACTED · 7% INFERRED · 1% AMBIGUOUS · INFERRED: 114 edges (avg confidence: 0.76)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Rayden & the Mercenary Years
- Thorin, Greenveil & Drevak War
- Seraphine & the Ashen Guard
- Drev & the Arcanum Scholars
- Sable Conclave & Nullis
- The Eleven & Allied Commanders
- Kael & the Havenfire Founders
- Cain Drakhar & the Iron Legion
- Saltmere & the Thalassian Navy
- Zareth Kull & the Void Watch
- Orc Highland Clans
- Dren Solm's Band
- Lyria & the Silent Wardens
- Velkan Drake & the Mages
- Karath Sultanate
- Ashfield Settlement
- Oaksmane Orphanage & Caelum
- Marcus Ironmane's Farm
- Starhaven Command Staff
- Nyx & the Umbral Web
- Bram Ashford's Circle
- House Silverhorn
- Sorin & Vaelmark
- Dresh & the Ironmane Lancers
- Helna & the Beast Corps
- Bob Vale & the Resonance Corps
- Kira Null & the Null Blades
- Clea Vorn's Field Officers
- Kingdom of Ironmere
- Kestrel Ashby's Company
- Henhallow Villagers
- First Field Army
- Skywarden Corps
- Silver Swan Cavalry
- Highland Beast Cavalry
- Fourth Field Army
- Blackstone Gaol
- Starhold Military Academy
- Veilborn Arcanum
- Amberfield Village
- Troutford
- Tunnel Crew
- The Starhold Crier
- Veilhold Keep
- Redbone Cavalry
- The Skyward Family
- Silverchain Mages
- Brix Holt
- Drel Voss
- Orvin Slate
- Ironjaw Clan
- Ironveil Spear Corps
- The Undying Colors
- Vel'Nathar
- Veyrhold Marches
- The Web
- Zharak Emirate
- Lumenfield SS+ Dungeon
- Blackwall
- Dunmere
- Greypeak Foothills
- Greypeak Highlands

## God Nodes (most connected - your core abstractions)
1. `Rayden Cale` - 129 edges
2. `Velkan Drake` - 65 edges
3. `Kael Varric` - 59 edges
4. `Seraphine Mire` - 43 edges
5. `Nyx Ravel` - 42 edges
6. `Thorin Blackroot` - 42 edges
7. `Rhegar Thorne` - 36 edges
8. `Cain Drakhar` - 35 edges
9. `Lyria Valen` - 32 edges
10. `Marcus Ironmane` - 32 edges

## Surprising Connections (you probably didn't know these)
- `Lyria Valen` --located_at--> `Hollow Frontier`  [AMBIGUOUS]
  starhaven_wiki.html → Lores/chapters/Starhaven_Chapter4.html
- `Rayden Cale` --founds--> `Starhaven`  [INFERRED]
  starhaven_wiki.html → Lores/chapters/Starhaven_Chapter2.html
- `Darian Wolfe` --member_of--> `Ashkar Dominion`  [AMBIGUOUS]
  starhaven_wiki.html → Lores/chapters/Starhaven_Chapter2.html
- `The King beyond the Void` --enemy_of--> `Rayden Cale`  [EXTRACTED]
  Lores/chapters/Starhaven_Chapter6.html → starhaven_wiki.html
- `Rayden Cale` --leads--> `Stone Table`  [INFERRED]
  starhaven_wiki.html → Lores/chapters/Starhaven_Chapter9.html

## Hyperedges (group relationships)
- **Night of Fire (Oaksmane Orphanage Massacre)** — char_caelum_vey, char_garrick_cale, char_halbrecht_veyne, char_marianne_vale, char_rayden_cale, place_oaksmane_orphanage [EXTRACTED 1.00]
- **Hollowwatch Expedition (The Six)** — char_dorun_graymaw, char_hollowwatch_guardian, char_korr_vash, char_nyssa_veil, char_rayden_cale, char_selene_voss, char_tharel_ethen, place_hollowwatch [EXTRACTED 1.00]
- **Temporal Rift Expedition** — char_lysara_quill, char_nyssa_veil, char_rayden_cale, char_selene_voss, char_tharel_ethen, char_varik_stonevein, place_temporal_rift [EXTRACTED 1.00]
- **Battle of Lowmere Field** — char_darian_wolfe, char_rayden_cale, char_selene_voss, fac_allied_army, fac_ashkar_dominion, place_lowmere_field [EXTRACTED 1.00]
- **Siege of Blackwall Ridge** — char_darian_wolfe, char_pyrewing, char_rayden_cale, char_selene_voss, char_velkan_drake, place_blackwall_ridge [EXTRACTED 1.00]
- **Fall of Veynehold** — char_halbrecht_veyne, char_rayden_cale, fac_black_wolf, place_veynehold [EXTRACTED 1.00]
- **Battle of the Black Hollow Checkpoint** — char_kael_varric, char_rayden_cale, char_void_listener, place_black_hollow_pass [EXTRACTED 1.00]
- **Deepforge Expedition** — char_corin, char_daven_holt, char_kael_varric, char_rayden_cale, place_deepforge [EXTRACTED 1.00]
- **Battle of the Ironmane Farm** — char_daven_holt, char_dresh_ironmane, char_helna_ironmane, char_kael_varric, char_lyria_valen, char_marcus_ironmane, char_rayden_cale, place_ironmane_farm [EXTRACTED 1.00]
- **Siege of Havenfire (Ash and Silver Fire)** — char_brek_stonefall, char_daven_holt, char_dresh_ironmane, char_helna_ironmane, char_kael_varric, char_lyria_valen, char_marcus_ironmane, char_pyrewing, char_rayden_cale, char_sorin_vael, char_velkan_drake, char_vera, fac_siegeborn_titans, place_havenfire [EXTRACTED 1.00]
- **Purging of Kael's Corruption** — char_helna_ironmane, char_kael_varric, char_seraphine_mire, char_velkan_drake [EXTRACTED 1.00]
- **The Cleansing March against the Waking Tree** — char_brek_stonefall, char_daven_holt, char_kael_varric, char_lyria_valen, char_pyrewing, char_rayden_cale, char_seraphine_mire, char_sorin_vael, char_velkan_drake, fac_siegeborn_titans [EXTRACTED 1.00]
- **Battle of Moonfall Lake** — char_grond, char_kael_varric, char_lyria_valen, char_nyx_ravel, char_rayden_cale, char_seraphine_mire, char_thorin_blackroot, char_velkan_drake, place_moonfall_lake [EXTRACTED 1.00]
- **Havenfire War Council** — char_dren_solm, char_kael_varric, char_lyria_valen, char_nyx_ravel, char_rayden_cale, char_seraphine_mire, char_thorin_blackroot, char_velkan_drake [EXTRACTED 1.00]
- **Sable Conclave Crisis** — char_pyrewing, char_seraphine_mire, char_sorvane_nullis, char_velkan_drake, fac_sable_conclave, place_sable_isles [EXTRACTED 1.00]
- **Battle of Starhold (War of Starhold)** — char_caelum_vey, char_drevak, char_garruk_blackroot, char_kael_varric, char_lyria_valen, char_nyx_ravel, char_rayden_cale, char_seraphine_mire, char_sorin_vael, char_sorvane_nullis, char_thorin_blackroot, char_velkan_drake, fac_coalition_army, fac_drevak_army, fac_sable_conclave, place_starhold [EXTRACTED 1.00]
- **Meteor Chamber Confrontation** — char_drevak, char_fourth_commander, char_lyria_valen, char_nyx_ravel, char_rayden_cale, char_seraphine_mire, char_velkan_drake [EXTRACTED 1.00]
- **Founding Council and Choosing of Starhaven's King** — char_dren_solm, char_kael_varric, char_rayden_cale, char_seraphine_mire, char_sorin_vael, char_sorvane_nullis, char_thorin_blackroot, char_velkan_drake, fac_starhaven [EXTRACTED 1.00]
- **Battle of the Third Chain (Vrak Isles)** — char_admiral_king_crest_vane, char_aurelia_vex, char_cain_drakhar, char_daven_holt, char_elysia_nocturne, char_nyx_ravel, char_rayden_cale, char_seraphine_mire, char_velkan_drake, char_zephyros, place_vrak_isles [EXTRACTED 1.00]
- **The Old House tavern gathering of Havenfire veterans** — char_brek_stonefall, char_daven_holt, char_helna_ironmane, char_kael_varric, char_lyria_valen, char_marcus_ironmane, char_nyx_ravel, char_rayden_cale, char_renzo_fal, char_thorin_blackroot, char_velkan_drake, char_vera_holt [EXTRACTED 1.00]
- **Ashfield observer-dungeon clearing** — char_caelum_vey, char_lena_crest, char_nyx_ravel, char_rayden_cale, place_ashfield [EXTRACTED 1.00]
- **Battle of Saltmere** — char_admiral_king_crest_vane, char_bob_vale, char_doran_ashe, char_dresh_ironmane, char_lyria_valen, char_rhegar_thorne, char_seraphine_mire, char_solen_aure, fac_first_field_army, fac_golden_coast_federation, fac_thalassian_league, place_saltmere [EXTRACTED 1.00]
- **Clearing of the Lumenfield SS+ Dungeon** — char_aurelia_vex, char_bob_vale, char_brynhild_voss, char_cain_drakhar, char_elysia_nocturne, char_kael_varric, char_lena_crest, char_lyria_valen, char_malgrath, char_nyx_ravel, char_rayden_cale, char_seraphine_mire, char_thorin_blackroot, char_velkan_drake, place_lumenfield_ss_dungeon [EXTRACTED 1.00]
- **Trial of the Eleven** — char_aurelia_vex, char_bob_vale, char_cain_drakhar, char_dren_solm, char_elysia_nocturne, char_kael_varric, char_lyria_valen, char_nyx_ravel, char_rayden_cale, char_seraphine_mire, char_thorin_blackroot, char_velkan_drake [EXTRACTED 1.00]
- **Battle of the Greenveil Plain** — char_brokk_graniteborn, char_dena_veil, char_dresh_ironmane, char_drogar_stonefang, char_drokha_bloodtusk, char_gorvak_doomhide, char_irae_duskwind, char_kethra_blackfang, char_kragh_skullsplitter, char_sira, char_thorin_blackroot, place_greenveil_plain [EXTRACTED 1.00]
- **Stone Table Council on the Highland Threat** — char_cain_drakhar, char_isolde_cren, char_kael_varric, char_nyx_ravel, char_rayden_cale, char_rhegar_thorne, char_thorin_blackroot, char_velkan_drake, fac_stone_table [EXTRACTED 1.00]
- **Gorvak's Death and the Coalition Kneeling to Drogar** — char_drogar_stonefang, char_drokha_bloodtusk, char_gorvak_doomhide, char_karsh_redspire, char_kaszrek, char_kethra_blackfang, char_korga [EXTRACTED 1.00]
- **The Eleven Pillars of Starhaven** — char_aurelia_vex, char_bob_vale, char_cain_drakhar, char_elysia_nocturne, char_kael_varric, char_lyria_valen, char_nyx_ravel, char_rayden_cale, char_seraphine_mire, char_thorin_blackroot, char_velkan_drake [EXTRACTED 1.00]
- **The Unicorn in the Dark (Silverhorn secret pact)** — char_cassian_silverhorn, char_corwin_leonhart, char_elowen_sunspire, char_nyx_ravel, char_rayden_cale, char_rhegar_thorne, char_senna_ash [EXTRACTED 1.00]
- **Dren Solm Ensemble** — char_dren_solm, char_lyra_ashfen, char_orik_drum, char_ryn_vael, char_sera_dusk, char_vel_carn [INFERRED 0.85]

## Communities (62 total, 15 thin omitted)

### Community 0 - "Rayden & the Mercenary Years"
Cohesion: 0.07
Nodes (55): Aruksha, Ashen Scholar, Brak Graymaw, Bramm Calder, Brannoc Tinhammer, Brim, Caedran Morveil, Corrupted King of Veyr Kharos (+47 more)

### Community 1 - "Thorin, Greenveil & Drevak War"
Cohesion: 0.05
Nodes (54): Bjorn Axeholt, Bren Oakshield, Cult Battalion Commander, Dagny Blackroot, Dena Veil, Drevak, Duskfang, Fenrik (+46 more)

### Community 2 - "Seraphine & the Ashen Guard"
Cohesion: 0.05
Nodes (51): Aldren Greyne, Aldric Solenne, Aureate, Auriel, Beatrix Lune, Blackwall Voss, Brynhild Voss, Constant (+43 more)

### Community 3 - "Drev & the Arcanum Scholars"
Cohesion: 0.05
Nodes (48): Aldren Hander, Althea Sorn, Barnaby Thistlewick, Benedek Sorrel, Bertil Greyhelm, Bryony Applewhite, Carrick, Cato Brightmantle (+40 more)

### Community 4 - "Sable Conclave & Nullis"
Cohesion: 0.05
Nodes (47): Amara Sunvale, Calvan Eres, Celestine Valcourt, Durgan Blackwall, Elara Sunmere, Federation flagship — "The Golden Current", Fizzwick Cogsworth, Gilbert Lakesby (+39 more)

### Community 5 - "The Eleven & Allied Commanders"
Cohesion: 0.05
Nodes (47): Augustin Gus Fellwind, Aurelia Vex, Aurumvex — ancient gold dragon, personal bond, Barek Kade, Bjarni Redcrest, Bora Ironshield, Borg Brassvein, Brokk Graniteborn (+39 more)

### Community 6 - "Kael & the Havenfire Founders"
Cohesion: 0.06
Nodes (47): Black Silence, Branna Holloway, Brek, Brek Stonefall, Brek Tane, Brenna Tane, Corin, Daven Holt (+39 more)

### Community 7 - "Cain Drakhar & the Iron Legion"
Cohesion: 0.06
Nodes (44): Aldric Morne, Arren Drenn, Asha Rennick, Astrya Lenn, Bane Crux, Bastian Orrel, Brimstone — Armored Dreadmaw War Boar. Full plate barding, custom fitted. The only mount in Starhaven's registry that has charged a fortified gate and come through it., Cain Drakhar (+36 more)

### Community 8 - "Saltmere & the Thalassian Navy"
Cohesion: 0.06
Nodes (43): Admiral-King Crest Vane, Bram, Bram Seawall, Caspian Wavecrest, Covenant flagship — "The Deep Memory", Cressia Stormdrift, Ela Seawall, Greta Flaxley (+35 more)

### Community 9 - "Zareth Kull & the Void Watch"
Cohesion: 0.10
Nodes (35): Calder Fael, Cova Drell, Cray, Darvin, Elysia Nocturne, Gavel, Illen, Luna (+27 more)

### Community 10 - "Orc Highland Clans"
Cohesion: 0.08
Nodes (34): Drogar Stonefang, Gorvak Doomhide, Karsh Redspire, Kaszrek, Kethra Blackfang, Korga, Kraag Half-Ear, Kragh Skullsplitter (+26 more)

### Community 11 - "Dren Solm's Band"
Cohesion: 0.08
Nodes (30): Amadeo Lark, Ambrose Tilly, Brom Hopwood, Dren Solm, Eluned Brightfacet, Idris Calloway, Lyra Ashfen, Lyrin Songwood (+22 more)

### Community 12 - "Lyria & the Silent Wardens"
Cohesion: 0.10
Nodes (26): Aelindra, Ancient grove-elk — bonded 200 years, Ashpaw — bonded dire wolf of the ancient Grimspine bloodline, Brex Ashpaw, Caelveth, Cass Thorn, Coldmarch draft horse — patrol, Coren Veld (+18 more)

### Community 13 - "Velkan Drake & the Mages"
Cohesion: 0.13
Nodes (23): Brannock Dusthollow, Cassia Vayne, Cirrus Galewick, Corisande Hale, Drelin Sash, Eirathra Veyl Frostborne, Emrys Shorewell, Ione Gale (+15 more)

### Community 14 - "Karath Sultanate"
Cohesion: 0.14
Nodes (20): Aria al-Kavar, Bramble Honeydew, Faris Sahir, Hettie Candlewright, Leyla al-Amar, Navid Saffrani, Rosamund Thistledown, Samir al-Dusk (+12 more)

### Community 15 - "Ashfield Settlement"
Cohesion: 0.11
Nodes (18): Coran Hale, Femi Hartfield, Garek Tyrant, Grena Vashk, Iven Dusken, Lucien Varga, Saska Quickrein, Senn Aldric (+10 more)

### Community 16 - "Oaksmane Orphanage & Caelum"
Cohesion: 0.25
Nodes (16): Ardyn Vorrath, Caelum Vey (Kai), Cinderwing, Elowen Brightwater, Ezrion Vorrath, Garrick Cale, Halbrecht Veyne, Marianne Vale (+8 more)

### Community 17 - "Marcus Ironmane's Farm"
Cohesion: 0.17
Nodes (16): Deven Ashkari, Gideon Fairweather, Ironmane Stallion, Marcus Ironmane, Marit Featherstone, Raul Ketterick, Tallis Greymeadow, Wren Dusk (+8 more)

### Community 18 - "Starhaven Command Staff"
Cohesion: 0.15
Nodes (14): Corran Ashvane, Elina, Fosho Tanachi, Ironmere Warhorse, Iva Renn, Pell Ashcord, Rhegar Thorne, Riva Trid (+6 more)

### Community 19 - "Nyx & the Umbral Web"
Cohesion: 0.15
Nodes (14): Cren Voss, Grex Redclaw, Lisette Rosier, Nyx Ravel, Ollo Brask, Serell Vane, Handler Vex, Zix (+6 more)

### Community 20 - "Bram Ashford's Circle"
Cohesion: 0.17
Nodes (12): Bram Ashford, Corrin Woolsey, Gunnar Tuskwell, Hesta Ashford, Odette Saltwhite, Osric Hackett, Acornholt, Greypeak Summit (+4 more)

### Community 21 - "House Silverhorn"
Cohesion: 0.18
Nodes (11): Cassian Silverhorn, Corwin Leonhart, Elowen Sunspire, Gurn Bramblefist, Rosalind Thornfield, Wrenna Willowmere, House Silverhorn, Thornridge Warband (+3 more)

### Community 22 - "Sorin & Vaelmark"
Cohesion: 0.24
Nodes (11): Dael Ashe, Elodie Brightpane, Lumi Fernglow, Sorin Vael, Arcane Artillery Corps, Elderwood, Ninth Sky Corps, Vaelmark (+3 more)

### Community 23 - "Dresh & the Ironmane Lancers"
Cohesion: 0.20
Nodes (10): Dresh Ironmane, Goldstorm, Irae Duskwind, RedMane, Stonehoof, Swiftmere, Vespera Drakewynn, Black Charge (+2 more)

### Community 24 - "Helna & the Beast Corps"
Cohesion: 0.31
Nodes (9): Alder Thornbury, Corvin Ashby, Helna Ironmane, Ironmane Mare, Sira, Beast Regiment, Starhaven Beast Corps, Greenveil College of Husbandry & Agriculture (+1 more)

### Community 25 - "Bob Vale & the Resonance Corps"
Cohesion: 0.31
Nodes (9): Bob Vale, Orin Dael, Sara Venn, Snow, Vessa Glimmerforge, Ysolde Wenn, Resonance Corps, Glimmerdeep (+1 more)

### Community 26 - "Kira Null & the Null Blades"
Cohesion: 0.32
Nodes (8): Dravan, Handler Vex, Kira Null, Marevon, The Crown Shadows, Null Blades, Duskwall Hidden Bastion, Karath Dun

### Community 27 - "Clea Vorn's Field Officers"
Cohesion: 0.29
Nodes (7): Aera Coldwind, Clea Vorn, Maren Coldhand, Petra Keen, Solace, Windmere — grey plains-bred warhorse, exceptional speed, The Dawnlancers

### Community 28 - "Kingdom of Ironmere"
Cohesion: 0.33
Nodes (7): Aldric Vorn, King Aldric Vorn, Mira Vorn, Roland Ashguard, Ironmere, Ironmere Shock Heavy Infantry, Kingdom of Ironmere

### Community 29 - "Kestrel Ashby's Company"
Cohesion: 0.29
Nodes (7): Ashi Thorncall, Benji Tallowmere, Dorian Fenwick, Halvard Embrecht, Kestrel Ashby, Lucan Weir, Saskia Updale

### Community 30 - "Henhallow Villagers"
Cohesion: 0.29
Nodes (7): Berrit Ovenhall, Clementine Sweetwater, Dorcas Featherby, Ned Clayborne, Henhallow, Kilnbury, Sugarbrook

### Community 31 - "First Field Army"
Cohesion: 0.29
Nodes (7): Cyren, Doran Ashe, Ironside, Sora Ashe, First Field Army, Starhaven, Varenmoor

### Community 32 - "Skywarden Corps"
Cohesion: 0.33
Nodes (6): Brightfeather, Kestra, Ren Dael, Sola Dren, Tobin Cress, Skywarden Corps

### Community 33 - "Silver Swan Cavalry"
Cohesion: 0.33
Nodes (6): Caelen Voss, Silver Swan Cavalry Corps, Silver Swan East Depot, Silver Swan North Depot, Silver Swan South Depot, Silver Swan West Depot

### Community 34 - "Highland Beast Cavalry"
Cohesion: 0.33
Nodes (6): Drokha Bloodtusk, Sabertooth, Highland Beast Cavalry, Bull War Riders, Cyclopean Crushers, Hyena Riders

### Community 35 - "Fourth Field Army"
Cohesion: 0.33
Nodes (6): Ereth Tal, Sylara Evenmere, Veyra Tal, Wenna Voss, Fourth Field Army, Silverleaf Corps

### Community 36 - "Blackstone Gaol"
Cohesion: 0.50
Nodes (5): Cassian Sond, Mace Torn, Ottar Deepbar, Varek Sond, Blackstone Gaol

### Community 37 - "Starhold Military Academy"
Cohesion: 0.40
Nodes (5): Ilsa Garrow, Joss Brannoch, Odile Marchbank, Starhold Military Academy, Starhold Training Grounds

### Community 38 - "Veilborn Arcanum"
Cohesion: 0.40
Nodes (5): Mireille Dunmore, Odalys Fernquill, Soltherion Vael, The Grey Scholar, Veilborn Arcanum

### Community 39 - "Amberfield Village"
Cohesion: 0.50
Nodes (4): Agatha Thresh, Hob Wheatley, Amberfield, Rookthorn

### Community 40 - "Troutford"
Cohesion: 0.50
Nodes (4): Astrid Coldwater, Finnian Brookes, The Frostrun Bends, Troutford

### Community 41 - "Tunnel Crew"
Cohesion: 0.50
Nodes (4): Calla Brennick, Crex, Tunnel-Voice Rusk, Veld Ashe

### Community 42 - "The Starhold Crier"
Cohesion: 0.50
Nodes (4): Fennimore Inkley, Quentin Reamer, Millwater, The Starhold Crier

### Community 43 - "Veilhold Keep"
Cohesion: 0.50
Nodes (4): Umbra, Virel Ashmark, Veilhold Keep, Veilmarsh Observation Post

### Community 44 - "Redbone Cavalry"
Cohesion: 0.67
Nodes (3): Ashfall — bonded duskstrider, Year 1044. Black coat, red-ember eyes. Has thrown exactly one rider. It was not Dusk., Dusk Ferren, Redbone Cavalry

### Community 45 - "The Skyward Family"
Cohesion: 1.00
Nodes (3): Ingrid Skyward, Lola Skyward, Marika Goldspear

### Community 46 - "Silverchain Mages"
Cohesion: 1.00
Nodes (3): Mael Sorn, Thessaly Vorn, Silverchain Mages

## Ambiguous Edges - Review These
- `Rayden Cale` → `Elira Voss`  [AMBIGUOUS]
  starhaven_wiki.html · relation: mentor_of
- `Gorvak Doomhide` → `Drokha Bloodtusk`  [AMBIGUOUS]
  starhaven_wiki.html · relation: chain_of_command_with
- `Darian Wolfe` → `Ashkar Dominion`  [AMBIGUOUS]
  Lores/chapters/Starhaven_Chapter2.html · relation: member_of
- `Kael Varric` → `Iron Legion`  [AMBIGUOUS]
  Lores/chapters/Starhaven_Chapter5.html · relation: fought_in
- `Lyria Valen` → `Hollow Frontier`  [AMBIGUOUS]
  Lores/chapters/Starhaven_Chapter4.html · relation: located_at
- `Ashen Scholar` → `Blue-Flame Void Listener`  [AMBIGUOUS]
  Lores/chapters/Starhaven_Chapter3.html · relation: possibly_same_as
- `Black Silence` → `Havenfire Protectors`  [AMBIGUOUS]
  Lores/chapters/Starhaven_Chapter4.html · relation: watched
- `Brynhild Voss` → `Rufus`  [AMBIGUOUS]
  Lores/chapters/Starhaven_Chapter9.html · relation: related_to

## Knowledge Gaps
- **345 isolated node(s):** `Temporal Rift`, `Mournhollow Sink`, `Blackroot Crypt`, `Brim`, `Veyrhold Marches` (+340 more)
  These have ≤1 connection - possible missing edges. (Counts symbols only; 345 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Rayden Cale` connect `Rayden & the Mercenary Years` to `Thorin, Greenveil & Drevak War`, `Seraphine & the Ashen Guard`, `Drev & the Arcanum Scholars`, `Sable Conclave & Nullis`, `The Eleven & Allied Commanders`, `Kael & the Havenfire Founders`, `Cain Drakhar & the Iron Legion`, `Saltmere & the Thalassian Navy`, `Zareth Kull & the Void Watch`, `Orc Highland Clans`, `Dren Solm's Band`, `Lyria & the Silent Wardens`, `Velkan Drake & the Mages`, `Karath Sultanate`, `Ashfield Settlement`, `Oaksmane Orphanage & Caelum`, `Marcus Ironmane's Farm`, `Starhaven Command Staff`, `Nyx & the Umbral Web`, `House Silverhorn`, `Sorin & Vaelmark`, `Dresh & the Ironmane Lancers`, `Bob Vale & the Resonance Corps`, `Kira Null & the Null Blades`, `Kingdom of Ironmere`, `Henhallow Villagers`, `First Field Army`, `Fourth Field Army`, `Blackstone Gaol`, `Amberfield Village`?**
  _High betweenness centrality (0.451) - this node is a cross-community bridge._
- **Are the 10 inferred relationships involving `Rayden Cale` (e.g. with `Aurelia Vex` and `Garrick Cale`) actually correct?**
  _`Rayden Cale` has 10 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Temporal Rift`, `Mournhollow Sink`, `Blackroot Crypt` to the rest of the system?**
  _345 weakly-connected nodes found - possible missing edges._
- **Should `Rayden & the Mercenary Years` be split into smaller, more focused modules?**
  _Cohesion score 0.0707070707070707 - nodes in this community are weakly interconnected._
- **Why does `Velkan Drake` connect `Velkan Drake & the Mages` to `Rayden & the Mercenary Years`, `Thorin, Greenveil & Drevak War`, `Seraphine & the Ashen Guard`, `Drev & the Arcanum Scholars`, `Sable Conclave & Nullis`, `The Eleven & Allied Commanders`, `Kael & the Havenfire Founders`, `Cain Drakhar & the Iron Legion`, `Saltmere & the Thalassian Navy`, `Zareth Kull & the Void Watch`, `Dren Solm's Band`, `Lyria & the Silent Wardens`, `Oaksmane Orphanage & Caelum`, `Nyx & the Umbral Web`, `House Silverhorn`, `Sorin & Vaelmark`, `Bob Vale & the Resonance Corps`, `Kestrel Ashby's Company`, `First Field Army`, `Veilborn Arcanum`, `Silverchain Mages`?**
  _High betweenness centrality (0.144) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Rayden Cale` and `Elira Voss`?**
  _Edge tagged AMBIGUOUS (relation: mentor_of) - confidence is low._
- **What is the exact relationship between `Gorvak Doomhide` and `Drokha Bloodtusk`?**
  _Edge tagged AMBIGUOUS (relation: chain_of_command_with) - confidence is low._