This is a centralized list of things that need to be done. It is
maintained by the SuperTux development team. It can include issues
that are outstanding, or resource requests. The document will also be
used to track decisions on these issues and requests.

Please have a look at our issue tracker on GitHub where you can also
find issues by `category:` tags (e.g.: `category:design` for
graphics/UX tasks, `category:code` for code tasks, and
`category:levels` for level design tasks).

> **Note:** This TODO is not to be used blindly. Use your brain and
  figure out which feature is most important and most practical to
  implement. Don't chase pie-in-the-sky ideas that you'll never get
  done. Also be aware that some of the items listed here might be out
  of date or not good ideas to begin with.

### Graphics

##### Main Menu

- [x] Add more detail to the ice frame (it is also too blurry)

##### Tiles

- Levels
  - [ ] Animation for deeper areas of modern lava
  - [ ] Potentially parallax background castle tiles of all castle styles for levels near a castle
  - [x] More background assets for Icy Island, Rooted Forest and the Ghost Forest.
  - [ ] Decorative tiles for the underground forest
  - [x] Crystalcave tileset should be fixed to be usable
  - [ ] Waterfall graphics fitting to the new water type
  - [ ] Add modern fluid style acid/poison (purple liquid) and swamp
  - [x] Add castle tiles adapted to their location in story mode (e.g. mossy bricks for the forest castle)
  - [ ] Decorative tiles for underwater areas in all themes
  - [ ] Redraw poles
  - [x] Fix tilling for crystal cave tileset (potentially redo it from ground up)
  - [ ] Cloud tiles are screwed up with vertical lines going through it
  - [ ] Improve ice bridge tiles (right now they are just a recolor)

- Worldmap
  - [x] Transition tiles from normal to ghost forest
  - [ ] Decorative mountain worldmap tiles, similar to those of Icy Island
  - [x] More decoration tiles for the ghost forest
  - [x] Underground forest worldmap tiles

##### Backgrounds

- [ ] More diverse backgrounds for all themes
- [ ] Sky backgrounds for every time of day (i.e. sunrise, midday, sunset, night)
- [ ] Divide backgrounds into multiple layers

##### Objects

- Badguys
  - [ ] Improve/Redesign all forest badguys
  - [ ] Update yeti sprites to fit the games art style
  - [ ] Proper Ghost Tree graphics

- Interactives
  - [x] Alternative light sources (glowing crystals, hanging/standing brazier, glowing plants)
  - [ ] Visual effects for willowisp warp and level flip
 
- Powerups
  - [ ] Get rid of hats and replace them with proper powerup costumes (only keep christmas hat)
  - [ ] Carryable light sources limited to dark levels (e.g. small torch, hardhat)

##### Meta

- Source files for all stuff?
- Clarify license? GPLv2+ only? CC-BY-SA what version only? Dual: GPLv2+ / CC-BY-SA Y.Z?

---

### Levels

- [ ] Improved level design for all worlds
- [ ] Update all levels that have water sections to work with the swim mechanic

---

### Cutscenes

##### Icy Island
  - [x] Intro: Picnic with Penny
  - [x] Interlude: A Yeti in the distance
  - [x] Interlude: Where is Penny?
  - [ ] Outro: Towards the Glacier Isle
##### Rooted Forest
  - [x] Intro: A New Location
  - [x] Interlude: An Eerie Plague
  - [ ] Interlude: Gigantic tree
  - [ ] Outro: Bye bye forest

---

### Code

- [ ] Comments: explain arbitary(?) constants in physics code
- [ ] Improve Zeekling behavior
- [ ] Sliding
- [x] Swimming
- [ ] Discuss: fluid simulation as game object rather than tiles?
- [x] Coin: expose to scripting interface for path/movement settings
- [x] HeavyCoin: expose to scripting interface to enable/disable effect of gravity

---

### Translations

Translations are always a very important part of the game. You can contribute
to them [on Transifex](https://www.transifex.com/arctic-games/supertux/).

<Category:Development>
