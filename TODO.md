This is a centralized list of things that need to be done. It is maintained by
the SuperTux development team. It can include issues that are outstanding, or
resource requests. The document will also be used to track decisions on these
issues and requests.

Please have a look at our issue tracker on GitHub where you can also find
issues by `category:` tags (e.g.: `category:design` for graphics/UX tasks,
`category:code` for code tasks, and `category:levels` for level design tasks).

### Artwork

#### Cutscenes

- [ ] Intro: Picnic with Penny
  - [x] Make it look less like a level
  - [ ] Fix some minor issues with new version
- [ ] Antarctica part II
  - [ ] Interlude: Yeti
  - [ ] Interlude: Where is Penny?
  - [ ] Outro: Leaving Antarctica…

#### Graphics

- [ ] Sliding (Tux)
- [ ] Swimming (Tux)

##### Tiles

- Levels
  - Add tiles for deeper areas of modern lava (needed for castles)
  - Parallax background tiles (Milestone 1 castle, Snow Castle, Brown Castle, DFK Castle) that can be used in levels close to the castles
  - More background tiles (parallax background) such as those in Antarctica, but for (Ghost Forest)
  - Dead bushes
  - More variants of dead trees
  - Underground tiles (<https://github.com/SuperTux/data/issues/48>; Parallax background tiles, slopes, decoration, tiles that can be used to make a platform some tiles higher without having to end the platform and having to make a new one)
  - Fixed tiling for Snow and Brown Castle
  - Crystalcave tileset should be fixed to be usable
  - Waterfall graphics fitting to the new water type
  - Electrified version of new water
  - Add modern fluid style acid/poison (purple liquid)
  - Castle: Add tiles adapted to the location of the castle (example: upper right-hand corner of <http://supertux.lethargik.org/wiki/images/9/97/Forestworldoverview.jpg>)

- Worldmap
  - Dark forest worldmap tiles without river required for transition
  - Ghost Forest worldmap tiles matching the new, blue-grass style from the levels (Ghost Forest style from <http://supertux.lethargik.org/wiki/File:Forestworldoverview.jpg> will be used later for Wasteland, no need for that now)
  - Transition tiles from normal as well as dark forest to ghost forest
  - Mountain worldmap tiles, similar to those of Icy Island
  - "Slope" tiles for the worldmap too, to create an illusion of height on the Forest Island.
  - Small forest castle tiles (Snow/Brown castle variant as well as Dark Forest Keep castle variant) (already discussed before)
  - All castle tile variants in a smaller version, as a tower
  - "Also some decoration for the ghost forest worldmap: dead bushes and dead trees (or are we using those decals from the halloween worldmap?). The same for the forest in general. The tiles should have a transparant background, so you can use them everywhere, like the trees, slopes and edges of icy island, because some decoration tiles from forest and darker forest have a background of the land that they are placed on." ~ RustyBox
  - Forest cave/underground worldmap tiles

##### Backgrounds

- More diverse Ghost Forest backgrounds

##### Objects

- Badguys
  - MrIceBlock: waking graphics (see <https://github.com/SuperTux/supertux/pull/581>)
  - Ghost enemy (<http://supertux.lethargik.org/wiki/images/8/8b/Ghost-sprite.png>)

##### Meta

- Source files for all stuff?
- Clarify license? GPLv2+ only? CC-BY-SA what version only? Dual: GPLv2+ / CC-BY-SA Y.Z?

#### Levels

- [ ] Improved Forest World

### Code

- [ ] Comments: explain arbitary(?) constants in physics code
- [ ] Ghost enemy
- [ ] Sliding
- [ ] Swimming
  - [x] Basic code for moving in water tiles
  - [ ] How to move underwater?
  - [ ] Discuss: fluid simulation as game object rather than tiles?

### Translations

Translations are always a very important part of the game. You can contribute
to them [on Transifex](https://www.transifex.com/arctic-games/supertux/).

### Meta

- [ ] Improve wiki content
- [ ] Maintain this To-Do list
