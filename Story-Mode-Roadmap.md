This page aims to lay done the goals for story mode for the upcoming version SuperTux (v0.7)

## Cutscenes

**Part I: Improve current cutscene quality**

- Make sure all cutscenes script are stored in their own seperate .nut file.
- Add comments for things to be changed or subject to being update once certain conents are added or are missing for the being.
- Replace Tux (player object) with a ScriptedObect to allow for using animation not related to gameplay.

**Part II: Add missing cutscenes**

- A cutscene after the Yeti fight leading to the crystal mine level
- A cutscene after the Ghost Tree fight leading to Bye Bye Forest

## Level Difficutly

- Drasticly improve the overall difficulty curve to prevent drastic changes in difficulty across level. The first levels start off easy, increasing slowly in difficulty with the last few levels and castle level being one of the hardest of that world. When arriving at a subsequent world, the difficulty scales down again, roughly around the mid-way point of the previous world's difficulty.
- Insure levels are kept at a consistent length based on their position in the worldmap progression and story significance (see [Level-Deisgn](https://github.com/SuperTux/supertux/wiki/Level-Design#Size) for more details).

## Level Progression

- Teach mechanics in bite-sized chunks
  - First level introduces base mechanics only, nothing too complex
  - Second level is a first test of said mechanics
  - Third level solely introduces swimming alone since it will be a more common and important mechanic further on in story mode
  - Forth level introduces more "advanced" mechanics (i.e. switches, ladders, sliding)
  - ...

- Introduce powerups one at a time - in levels that make sense
  - Introduce Fire Flower in the first level along the other basic elements
  - Introduce Air Flower in the first airborne level of the 1st world
  - Introduce Earth Flower early in world 2 followed by the Ice Flower a couple level in (mid-way point at the latest)
