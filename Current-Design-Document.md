# About this Document

This document is a work in progress, nothing here is considered even remotely final. Also, SuperTux uses version numbers instead of milestones now. There is a list of stuff that needs to be done, and at the bottom is a list of ideas that could be implemented too. Check our [TODO List](https://github.com/SuperTux/supertux/wiki/TODO) to see what things are being currently worked on or have been finished.

# Overview

SuperTux 0.7.0 will bring about a completion to the first two worlds so work can begin on World 3. This means improving/revamping the graphics, sound effects, code, story and levels in many areas and adding some new features/mechanics as well. (swimming, etc.)

This will be organized based off of the order it will likely be done in.

# Contents
  1. [Graphics](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Graphics)
  2. [Audio](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Audio)
  3. [Mechanics](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Mechanics)
  4. [Badguys](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Badguys)
  5. [Story](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Story)
  6. [Levels](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Levels)
  7. [Post-0.7 Tasks](https://github.com/SuperTux/supertux/wiki/Current-Design-Document##Post-07-Tasks)
  8. [Unconfirmed Ideas](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Unconfirmed-Ideas)

# Graphics

**Tiles/Decals**

- **Icy Island**
  - *Decorative Tiles*
    - Snow-topped rocks + stones
    - More unique decoration for:
      - Icy plains (snowmen, snow formations, etc.)
      - Cave levels (Rock formations, natural pillars, etc.)
      - Crystal Mines (Crystal plants, mineshafts, etc.)
      - Bridge/Pier sections (Crates, fences)
      - Icy Castle (Castle elements?)
      - High Altitudes (animated flags)

- **Normal Forest**
  - *Solid Tilesets*
    - Base forest tiles
      - Separated dirt from the base tiles
      - Separated grass from the base tiles
      - Base forest slopes
      - Separated dirt from the base forest slopes
      - Separated grass from the base forest slopes
      - Moss textures for the base forest tiles
      - Underground bone decoration for the base forest tiles
    - Remake the spike vine tiles to appear more dangerous
    - Slick slime to slide on
    - A Tileset in the Treetops
    - Tree Branches to stand on
  - *Non-Solid Tilesets*
    - Redo the background tileset for the normal forest textures
    - Redesign the Forest Bushes
    - The generic tileable tree
  - *Decorative Tiles*
    - Forest Rocks, some with growth on them
    - Forest Foliage, like vines, growths, mushrooms, flowers and clovers
    - New decoration for underground zones
    - New decoration for castle/ruins sections
  - *Decals*
    - Outhouse Exit
    - Tree Movie Star Exit (possibly transparent?)
    - A multitude of new forest trees and tree branches to make the forest prettier.
      (Gwater and BlasterMaster's tree designs are both great examples of this)
  - Other Background Decoration
  - Other tilesets, possibly
  
- **Ghost Forest**
  - *Solid Tilesets*
    - Root spike tiles
    - Haunted Library base tiles
  - *Non-Solid Tilesets*
    - Bookshelves for the Haunted Library
    - Background walls for the Haunted Library
  - *Decorative Tiles*
    - Decoration for the Haunted Library
    - Warped versions of the tiled forest decorative elements
  - *Decals*
    - Remake the Ghost Forest mushrooms
    - Warped versions of the larger decal forest decorative elements
  - New Tilesets (both for solid and decoration), Probably

- **General**
  - *Tiles and Tilesets*
    - Level end goalposts
    - Underwater decoration
    - Simple bridge/scaffolding unisolid tiles
    - Waterfall Tiles
    - Green Acid
    - Transparent version of the old green castle vine tile
    - Sideways unisolids
  - *Objects and Decals*
    - Better/New Billboards
    - Wide Trampolines
    - New Variants to moving platform, such as one made of bones
  
<details>
<summary>(Reference)</summary>

![](https://user-images.githubusercontent.com/22513909/91283578-1b912e00-e7ce-11ea-8458-1c201bb04d95.png)
</details>

**Badguys**

- **Icy Island**
  - Crystallo
  - Small docile fish (1 x 1)
  - Small enemy fish (1.5 x 1)
  - Large enemy fish (3 x 2)
- **Rooted Forest**
  - Poison Ivy
  - Walking Leaf
  - Leafshot
  - Mr. Tree
  - Stumpy
  - Mole
  - Igel
  - Zeekling
  - Snail (1x1)
  - Big Snail (2x2)
- **Ghost Forest**
  - Ghoul
  - Ispy
  - Spidermite
  - Rotten Ivy/Leaf
  - Rotten Tree
  - Rotten Stumpy
  - Shadow Tux
  - Ghost Tree Roots (stationary)
  - Ghost Tree Roots (blinking)
  - Ghost Tree Roots (growing)

**Characters**

- **Tux**
  - Skidding
  - Swimming
  - Ducking
  - Backflip
  - Kicking
  - Dead
  - Worldmap Boat
  - Slope Sliding
  - Other/cutscene sprites
- **Penny**
  - Other/cutscene sprites
- **Nolok**
  - Other/cutscene sprites
- **Yeti**
  - Throw attack
  - Idle
  - Run
  - Jump
  - Yell
  - Other/cutscene sprites
- **Ghost Tree**
  - Idle
  - Dying
  - Scream
  - Inhale
  - Other/cutscene sprites

**Backgrounds**

- Rooted Forest – Completely redesign backgrounds throughout all of World 2
(Alzter: IMO the forest backgrounds are in need of a redo, the current ones seem very flat)
- General - More Cloud BGs

<details>
  <summary>(Alzter: you mean like these?)</summary>
  
  ![](https://user-images.githubusercontent.com/22513909/91281292-3ada8c00-e7cb-11ea-9dac-474cd849eee2.png)

  [Source XCF](https://github.com/SuperTux/media/blob/master/images/tiles/snow/cave7.xcf)
  
  ![](https://user-images.githubusercontent.com/22513909/91281362-52197980-e7cb-11ea-9ead-ee72a6f78f84.png)

  [Source XCF](https://github.com/SuperTux/media/blob/master/images/tiles/snow/mountain.xcf)
  
  ![](https://user-images.githubusercontent.com/22513909/91281639-ade40280-e7cb-11ea-8545-fcd405b48d31.png)

  [Source XCF](https://github.com/SuperTux/media/blob/master/images/background/snow_background.xcf)
</details>

- Parallax-ify many BGs.

---

# Audio

**Tux, Penny, Nolok**

Add new sounds/cutscene speech. Perhaps use a new VA?

---

# Mechanics

### Mechanic Improvements

**Rock**

Make rocks bounce off of Tux rather than killing him. Rocks should not be able to kill Tux!

### Mechanic Ideas

**Walljumping**

Could be quite useful and nice to have. Would extend move set of Tux. Possible on certain tiles. To decide: Does Tux cling to the wall or slide down slower?

**Slope Sliding**

Tux sliding down slopes like a real live penguin would be nice.

**Locked Doors and Keys**

Suggested by RustyBox, key would be like a powerup and would hovering over Tux and auto-unlock any locked door. Locked doors can&#39;t be opened, etc. Would be useful for puzzle stages. Sometimes, multiple keys are needed to open a door and this should be signalled.

### Level Editor

- Backgrounds shouldn't shift upon placement (default the x and y variables to 0, 0 upon placement)
- Level Editor settings should be saved to the config file (they are saved even when the player exits the game)
- Adapt the textboxes to the new text editing capabilities.
- Layer Toolbar Subfolders
- Inner-tilegroup Subfolders

### Swimming

- Adapt to a rotating hitbox, or make the current one more forgiving.
- It should be easier to stop in the water (more friction)
- Improve indentation/code quality of swimming sprite and code files.
- Reduce/optimize the sprite, and make it less messy and buggy.
- Boosting should be handled better. (One suggestion was to make the boost a "hold" action instead of a "pressed" action but there are also some against this.)

---

# Badguys

### Badguy Improvements

**Ghoul**

- They should not go through each other.
- Their flying speed should be configurable.
- They should either have better pathfinding OR be able to go through solid land.

**Poison Ivy & Walking Leaf**

- Poison Ivy and Walking Leaf should fall slower, to differentiate it from the snowball and make it more realistic. (requires new sprite)

**Crystallo**

- It should turn around better, with easing.
- Instead of squishing, it should burst out into shards that fly around.
- It should have an option to spawn by bursting out of walls that emerge when Tux is near, perhaps bursting out shards at the same time?
- Crystallos should be immune to their own spikes, of course.

**Haywire**

- They should be able to jump over a short distance, like the captain snowball.
- They should not collide with or defeat all enemies in its path.

### Badguy Ideas

**Shadow Tux**

This is something that will tie in to the game's general story. It is a "shadow tux" that mimmicks Tux's movement on a delay (similar to keys) and appears in a sort of "Nightmare Library"

**Swimming Fish**

A fish enemy that swims back and forth should be added. It swims left to right, switching directions upon hitting a wall or when its range is up (the player can set the range, similar to crystallo). Three variants should be added: a small and big one, as well as a non-harmful tiny variant. They are planned to appear in the Icy Island and resemble the frozen fish.

**Crystal Shards**

Similar to the mole rock, it goes up and then down and kills anything in its path. If it collides with something, it sticks to it (its drawing layer is behind normal tiles) and 4 burst out of crystallos when they die.  They disappear after a short time but remain dangerous when stuck.  They also rotate depending on their direction.

**Stationary Ghost Roots**

Not really an enemy, but just ghost forest "spikes" that are squirming roots.

**Blinking Ghost Roots**

These are ghost tree roots that attack based on a timer. Most similar to the tree's usage of them.

**Growing Ghost Roots**

If Tux steps on them, after he leaves them they grow up so Tux cannot walk on that terrain anymore.

### Bosses

These are mainly ideas that are somewhat cemented but can change at any time. These do not serve as mandatory tasks for bosses but are highly encouraged to be implemented.

**Yeti**

Before stomping and letting stalactites fall from above, the yeti will throw 2-3 bouncy snowballs. In Pinch Mode, after his throwing attack the yeti will throw a gigantic snowball that rolls to the other side of the arena and can crush Tux against the wall if not avoided quickly. This snowball breaks when hitting a wall.

**Ghost Tree**

The ghost tree will remain idle for a short time period, its eys following Tux and only attacking from below with its roots. These can be spotted by a crack in the ground. After this, the ghost tree will scream, followed by it inhaling one set of colored ghost wisps (red > green > blue > repeat). Depending on which color has been swallowed, the tree's eys will glow in that color and it will unleash a powerful attack.

- red wisp: ghost tree rages and create a wave of roots which must be jumped over
- green wisp: summons multiple ghost forest enemies
- blue wisp: spawns an object that allows hurting the tree (maybe something like a bomb? or the lanterns, like are currently used)

While the green and blue wisps are inhaled, the roots attack will continue to accour! In Pinch Mode the ghost tree will inhale all ghost wisps and combine all their attacks continuesly. Once it looses another life all returns to normal when hit until all ghost wisps are inhaled again.

---

# Story

Improve it, make it better. There used to be more here but I deleted it because nothing is final yet.

---

# Levels

**Levels in general**

The levels of the Add-On menu (Bonus Islands I-IV, Halloween 2014, etc.) should be divided from other contrib levels, which can be downloaded manually or in-game from "Add-Ons". Manually downloaded levelpacks would be subfoldered under "Community Levels", while those already in game would be in a own folder named "Add-Ons". This would make the list of Add-Ons shorter and would clear up which levels are official and which not.

**Normal Levels**

Update with the new graphics for their assets. Also: make them more interesting! Most levels are your run-of-the-mill left to right levels and don&#39;t make use of everything available, like most enemies, vertical space, varying directions, multiple paths, autoscrolling, signs, moving tilemaps, unisolids, bricks, multiple paths, those scripting bonus blocks that can be activated by rocks, etc. Make the most of the level gimmicks!

One of the most stupid and awful level design philosophies I have seen (especially since it was used to block level proposals in the past) is to water down the quality of certain levels to make others stand out, and to this I say: No! That is stupid! You&#39;re only going to improve with time, so you can always go back and add on more and more and make ultimately all levels better. And anyway, would you rather have two amazing levels of the same quality or one crappy level + one amazing level?

Another problem with current levels is sometimes having to hit bonus blocks to advance in a level. Some official levels do this and it should be removed, because every level should be beatable without hitting a bonus block.

**Secret paths on worldmap**

Whenever a secret exit to a bonus level is unlocked, a path appears leading to that level. Currently able and might be easy to implement.

**Cutscenes**

Update cutscenes with the new story decisions and the new graphics/stuff decided for the characters.

Maybe add designated text boxes for characters when they speak instead of using the default info box?

**The Castle of Nolok**

The cutscene at the very beginning should be skippable. (Although skippable cutscenes exist, they don't place Tux where he needs to be. Fix this!!)

The cutscene at the very beginning should also only play once per level session. (If the player dies in the level, DON'T show it.  If the player leaves the level and reenters it, then DO show it.)

If you play through the cutscene after the level and don't skip it, then the level stats will be erased or overridden. This should be fixed!!

**Boss Levels**

Add new fights and make the existing ones more interesting.

Maybe use [Boss Attack '07](https://discarded-ideas.org/sites/discarded-ideas.org/files/music/bossattack07.ogg) as a boss pinch theme?

---

# Post-0.7 Tasks

This contains confirmed features/tasks for post 0.7/World 3+.

### Graphics

**Characters**

- **Toucan**
  - Flying
  - Other/cutscene sprites
- **Totem Boss**
  - Inactive
  - Activate
  - Head attacks
  - Other/cutscene sprites

### Mechanic Ideas

**Up Splasher**

A 2x2 tile wide rock-like object that acts as a less powerful trampoline. It will burst a small water fountain out of its head once Tux stands on it which shoots Tux upwards a bit.

### Badguy Ideas

![](https://user-images.githubusercontent.com/22513909/91284400-30ba8c80-e7cf-11ea-85d8-86e3db499659.png)

**Rusty Bomb**

Rusty Bombs are a large variant of Mr. Bomb which are 3x3 tiles in size. They move much slower compared to other bombs but have a wider explosion radius. Furthermore, when they explode they shoot out 2-3 smaller normal sized bombs (= Hellbent).

**Hellbent**

Hellbents are black bombs that run straight towards Tux and explode on contact with either Tux, another enemy or a wall. If they face away from Tux they will turn around to run towards Tux again.

### Bosses

**Toucan and Totem Boss**

The toucan will primarly fly high up while performing several attacks from above. Occasionally, (if totem boss is present in the same sector) they will land on the highest totem head to protect it from Tux - otherwise they will stay midair constantly!

Attacks the toucan could perform:
 
- Spits 3 seeds in an arc (triple shot) - repeats this attack at a set interval depending on its current health
  (i.e. 5 lives -> attack once, 4 health -> attack twice, ... etc.)
- A dive attack Tux must jump over to avoid, also giving him a chance of attacking the toucan
- Toucan summons a few of his normal sized totem minions (if totem boss is not present/defeated beforehand)

The totem boss consists out of 5 head pieces which must all be destroyed in order to defeat the boss. Depending on how many head pieces are remaining the totem boss will perform a different attack.

- 5 heads: chases Tux and tries to squish him against a wall (requires Up Splasher or trampoline to avoid)
- 4 heads: totem shoots spikeball projectile while chasing Tux and trying to squish him
- 3 heads: spins its sharp wings while constantly jumping (instead of running)
- 2 heads: reveal spikes on top (other head spits out 1 fire rock & 1 normal rock in sequence normal rock must thrown against upper head)
- 1 head: totem flies over Tux and stombs down once it is right above Tux (like ice crusher) giving Tux time for a final attack

If a totem head is destroyed it pushes Tux away to prevent landing on the next head right away (like the 'push-explosion' radius). The throwable rock will be a mechanic in the 3rd castle or prior in world 3, allowing to break through certain walls and crush enemies (informing the player that they are throwable and effective against enemies).

---

# Unconfirmed Ideas

Only some, few or none of this stuff may be added, or might get added at a later time.

### Features that would affect current gameplay

**Mother Snail**

A huge sleeping snail mother that Tux cannot pass/jump over, but he can wake it up, so he has to find a way to block or move its awake form in order to progress. Possibly also produces a set amount of snail offspring, similar to a dispenser with a set value of enemies. RustyBox's snail concept but much bigger can possibly be used for this enemy.

**Bluejay + Acorn**

A sneaky bluejay who sits on top of stuff and periodically throws acorns down at Tux. Acorns don't collide with tiles, but do collide with enemies and Tux. When Tux gets near it, it flies away, never to be seen again. Does a cheeky laugh/giggle after throwing the acorn, and its eyes probably follow Tux.

The acorn that the bluejay throws. If used by itself, it falls normally, like a stalactite would, but if the bluejay throws it, it immediately begins falling no matter what. Doesn't collide with tiles, but does collide with enemies/players.

**Woodpecker + Pinecone**

The smart variant to the bluejay, the woodpecker pecks down pinecones at Tux, and sits there for a while. Tux can then use the pinecone and throw it up to defeat the woodpecker. Either the pinecone respawns after a while, or the woodpecker is smart enough to go seek out another tree with pinecones.

Upon falling, which it only falls when pecked by woodpecker, the pinecone doesn't despawn, as it can be picked up and used as a projectile (like the rock, just with better range), but when it is falling, it can hurt Tux.

**Tentacle Monster**

A underwater enemy, which grabs Tux with his arm/tentacle and pulls him deeper into the water (or the bottom edge of the level, to be specific) to his demise. Could be used for older levels, where the swimming feature was not present.

**Tux storing velocity while on moving platforms**

Tux should have momentum from when on moving objects stored, so he can "fling" off high-speed platforms.

**Better movement on moving tilemaps**

Tux should move better on moving tilemaps. Currently he can hardly jump, or move left to right, etc.

**Weighted Pushbutton**

A pushbutton who is only activated when something is pressing it and otherwise turns off. Would have a different color and sprite to differentiate it.

**Skull Tile & Falling Tiles**

Skull tiles as well as falling tiles should respawn when they have fallen. Either off-screen or on-screen.

### Features that wouldn't affect current gameplay

**More editing options for decals**

Add ability to change a decal's scroll speed and tint. Also decals should be scriptable, and should fade.

**Better background system**

Sprite files as BGs would be cool.

**Better cutscene methods**

Skipping cutscenes should move Tux to the proper place, and there should be an option to trigger a script only once per level session.  The color of cutscene text should also be editable.

**Pigeons**

These are special background objects who, when Tux is near, flee in the direction away from his body.

**Liquid Refactor**

Liquids could be changed into objects that autotile themselves, so effects when entering the water and exiting could be added.

**Check for updates**

Upon booting up game, check for updates, and if update is available, place a "Update Game" dialogue item when the game is first opened. If the current version equals the installed version, it's plays normally. Normally only works for major releases, but in dev mode works for every nightly build.

**More particle events/effects/use of screen shaking**

We need more particle effects for different things, like for wind, to make it look better than just some small cubes, and give it actual images rather than just rects. Also, it would be nice for particles to be used more, such as when Tux/badguy lands, on wind, when slipping on ice or slime, walljumping, etc. in those events, but also in normal behavior, such as with fire/lava having particles come off/particles around it, and also there should be more particle objects, like falling leaves/blowing wind in the normal forest or sky "fairies"/glowing floaty particles in the air in the ghost forest. Also, it would be nice to shake the screen more, such as in cutscenes, when Tux is jolted, to convey certain emotions, when bombs explode, when Tux is hurt, etc. Also bubbles when Tux enters or leaves water, or makes a sudden motion/boosts/starts moving again. Many more particle events and shaking could be added to add liveliness to the game.

**More sound effects**

Add sound effects for when Tux walks on different tiles, and overall better sounds for when he dies or speaks or enters water.

**Tintable lightbulb/lantern**

A colorable, easily placeable light source for pretty effects in levels, and the editor can decide if it obeys gravity, what color it is, its shape + rotation, etc...

**Ice floes**

Ice floes that respond to the gravity placed on top of them would add some goodness.

**Thumbs up**

Tux should twirl and do a happy little thumbs up while the level ending is playing.

**Scripting events based off of a time of day**

There should be support for adding scripts that only happen if the player is playing at a certain time of day.

**After-a-while easter eggs/Idle-Graphics**

Snowballs and other enemies do a little break after a while. After all, they were walking for so much time… Tux, after a while of not moving, also gets angry and curses the screen. Jumpy just stops jumping after a while

