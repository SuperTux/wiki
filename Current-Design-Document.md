# About this Document

This document is a work in progress, nothing here is considered even remotely final. Also, SuperTux uses version numbers instead of milestones now. There is a list of stuff that needs to be done, and at the bottom is a list of ideas that could be implemented too. Check our [TODO List](https://github.com/SuperTux/supertux/wiki/TODO) to see what things are being currently worked on or have been finished.

# Overview

SuperTux 0.7.0 will bring about a completion to the first two worlds so work can begin on World 3. This means improving/revamping the graphics, sound effects, code, story and levels in many areas and adding some new features/mechanics as well. (swimming, etc.)

# Contents
  1. [Story](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Story)
  2. [Levels](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Levels)
  3. [Audio](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Audio)
  4. [Graphics](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Graphics)
  5. [Mechanics](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Mechanics)
  6. [Badguys](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Badguys)
  7. [Post-0.7 Tasks](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Post-0.7)
  8. [Unconfirmed Ideas](https://github.com/SuperTux/supertux/wiki/Current-Design-Document#Ideas)

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

**Boss Levels**

Add new fights and make the existing ones more interesting.

Maybe use [Boss Attack '07](https://discarded-ideas.org/sites/discarded-ideas.org/files/music/bossattack07.ogg) as a boss pinch theme?

---

# Audio

**Tux, Penny, Nolok**

Add new sounds/cutscene speech. Perhaps use a new VA?

---

# Graphics

**Backgrounds**

- Rooted Forest – add a few varying parallax BGs for the normal and ghost forest theme.
(Alzter: IMO the forest backgrounds are in need of a redo, the current ones seem very flat)
- General - More cloud BGs would be cool.

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



**Tiles/Decals**

- Improved forest tiles, bush tiles, forest background tiles, as well as new additional tilesets (such as slime).
- A multitude of new forest trees and tree branches to make the forest prettier.

(Gwater and BlasterMaster's tree designs are both great examples of this)

- The tree movie star (outhouse) exit.
- Revamp/large extension of the icy island background decals to live up to the new forest stuff. Could include things like snowmen, flags, crates, bridge improvements, improvement/expansion of the current tiles, etc. as well as animated things like animals and flags. Look to Pingus for inspiration, maybe?
- Miscellaneous other new tilesets for the forest/ghost forest to give it variety and a finished/varied feel
- Underwater decoration (icy + forest)
- Simple bridge/scaffolding unisolid tiles
- Treetop Tileset
<details>
<summary>(Reference)</summary>

![](https://user-images.githubusercontent.com/22513909/91283578-1b912e00-e7ce-11ea-8458-1c201bb04d95.png)
</details>

- Updates to Deeper Lava/Acid
- Waterfall tiles
- New decoration (Forest) - Could include things like animals, shrubs, as well as things for the ghost forest.
- Ghost tree root tiles
- Library tiles, as well as library decoration
- New decoration for castles
- New bridge/pier decoration
- New ice cave decoration
- Sideways unisolid tiles
- Signs declaring something is walljumpable and one that isn't walljumpable
- Squishy moss and soft snow for walljumping
- Convert crystal cave, ghost forest and snowfort tiles to walljumping

**Objects**

- New/Better Billboards
- Moving Platform, made of bones

**Badguys**

- **Icy Island**
  - Snowman
  - Bouncing Snowball
  - Snowshot
  - Spiky
  - Sleeping Spiky
  - Crystallo
- **Icy - Underwater**
  - Small docile fish (1 x 1)
  - Small enemy fish (1.5 x 1)
  - Large enemy fish (3 x 2)
- **Rooted Forest**
  - Poison Ivy
  - Walking Leaf
  - Mr. Tree
  - Stumpy
  - Leafshot
  - Zeekling
  - Igel
  - Snail
  - Big Snail
- **Ghost Forest**
  - Ghost Forest
  - Rotten Ivy/Leaf
  - Rotten Tree
  - Rotten Stumpy
  - Ghost Tree Roots

**Characters**

- **Tux**
  - Skidding
  - Swimming
  - Ducking
  - Backflip
  - Kicking
  - Dead
  - Worldmap Boat
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
- **Toucan**
  - Flying
  - Other/cutscene sprites
- **Totem Boss**
  - Inactive
  - Activate
  - Head attacks
  - Other/cutscene sprites

---

# Mechanics

### Mechanic Improvements

**Rock**

Make rocks bounce off of Tux rather than killing him. Rocks should not be able to kill Tux!

**Coyote Time**

This would add some more fair gameplay. This is the fact that Tux can still jump a bit after he leaves the ground, since players can't respond that quickly to whether Tux is on-ground.

### Mechanic Ideas

**Locked Doors and Keys**

Suggested by RustyBox, key would be like a powerup and would hovering over Tux and auto-unlock any locked door. Locked doors can&#39;t be opened, etc. Would be useful for puzzle stages. Sometimes, multiple keys are needed to open a door and this should be signalled.

**Docile Fish**

A small swimming fish shall be added. It doesn't harm Tux and flees from him when near.

---

# Badguys

### Badguy Improvements

**Ghoul**

Ghouls should not collide with each other, and should not collide with solid land. Their flying speed should be configurable. They should also have better pathfinding, although if they don't move through solid terrain then this would be unneccesary.

**Haywire**

Haywire should be able to jump over a short distance (like captain snowball) while chasing Tux and not collide with/defeat all enemies in its path.

**Poison Ivy & Walking Leaf**

Poison Ivy and Walking Leaf should fall slower, to differentiate it from the snowball and make it more realistic. Requires new sprite first.

**Crystallo**

It should turn better (easing?) and also instead of squishing, it should burst out into shards that fly around.

### Badguy Ideas

**Shadow Tux**

This is something that will tie in to the game's general story. It is a "shadow tux" that mimmicks Tux's movement on a delay (similar to keys) and appears in a sort of "Nightmare Library"

**Cod**

Simply a little fish enemy that swims back and forth should be added. It swims left to right, switching directions upon hitting a wall. Two variants should be added: a small and big one.

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

# Post-0.7 Tasks

This contains confirmed features/tasks for post 0.7/World 3+.

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

The toucan will primarly fly high up while performing several attacks from above. Occasionally, (if totem boss is present in the same sector) they will  land on the highest totem head to protect it from Tux - otherwise they will occasionally land on the ground, allowing for an attack by Tux.

The totem boss consists out of 5 head pieces which must all be destroyed in order to defeat the boss. Depending on how many head pieces are remaining the totem boss will perform a different attack.

- 5 heads: chases Tux and tries to squish him against a wall (requires Up Splasher or trampoline to avoid)
- 4 heads: totem shoots spikeball projectile while chasing Tux and trying to squish him
- 3 heads: spins its sharp wings while constantly jumping (instead of running)
- 2 heads: reveal spikes on top (other head spits out 1 fire rock & 1 normal rock in sequence normal rock must thrown against upper head)
- 1 head: totem flies over Tux and stombs down once it is right above Tux (like ice crusher) giving Tux time for a final attack

If a totem head is destroyed it pushes Tux away to prevent landing on the next head right away (like the 'push-explosion' radius). The throwable rock will be a mechanic in the 3rd castle or prior in world 3, allowing to break through certain walls and crush enemies (informing the player that they are throwable and effective against enemies).

---

# Non-Priority Features

These are features that will come to the game, preferably before 0.7, but aren't really a priority for the time being.

**Walljumping**

Could be quite useful and nice to have. Would extend move set of Tux. Possible on certain tiles. To decide: Does Tux cling to the wall or slide down slower?

**Slope Sliding**

Tux sliding down slopes like a real live penguin would be nice.

**Editor Improvements**

A better text editor, Also improve infoblock UI (more like scripting UI) and BGs shouldn't shift weirdly when placed. Also, editor options should save to the config file.

**Better cutscene methods**

Cutscenes should be skippable, trigger only once per level session, and text should be passed through via a button.

**Colored Text per speaker**

In future cutscenes, Tux, Penny and Nolok might have speaking parts and there should be the ability to change color of Text in the text object per character (green for Nolok, purple for Penny, etc.) It would also be nice to have high def/large face renders of the characters to appear from the bottom of the screen when they speak.

**More editing options for decals**

Add ability to change a decal's scroll speed and tint. Also decals should be scriptable, and should fade.

**Tux storing velocity while on moving platforms**

Tux should have momentum from when on moving objects stored, so he can "fling" off high-speed platforms.

**Better movement on moving tilemaps**

Tux should move better on moving tilemaps. Currently he can hardly jump, or move left to right, etc.

**Pigeons/Tiny Fish**

These are special background objects who, when Tux is near, flee in the direction away from his body.

# Unconfirmed Ideas

Only some, few or none of this stuff may be added, or might get added at a later time.

### Performance Improvements

**Check for updates**

Upon booting up game, check for updates, and if update is available, place a "Update Game" dialogue item when the game is first opened. If the current version equals the installed version, it's plays normally. Normally only works for major releases, but in dev mode works for every nightly build.

**More particle events/effects/use of screen shaking**

We need more particle effects for different things, like for wind, to make it look better than just some small cubes, and give it actual images rather than just rects. Also, it would be nice for particles to be used more, such as when Tux/badguy lands, on wind, when slipping on ice or slime, walljumping, etc. in those events, but also in normal behavior, such as with fire/lava having particles come off/particles around it, and also there should be more particle objects, like falling leaves/blowing wind in the normal forest or sky "fairies"/glowing floaty particles in the air in the ghost forest. Also, it would be nice to shake the screen more, such as in cutscenes, when Tux is jolted, to convey certain emotions, when bombs explode, when Tux is hurt, etc. Also bubbles when Tux enters or leaves water, or makes a sudden motion/boosts/starts moving again. Many more particle events and shaking could be added to add liveliness to the game.

**More sound effects**

Add sound effects for when Tux walks on different tiles, and overall better sounds for when he dies or speaks or enters water.


### Object Improvements/Ideas

**Weighted Pushbutton**

A pushbutton who is only activated when something is pressing it and otherwise turns off. Would have a different color and sprite to differentiate it.

**Skull Tile & Falling Tiles**

Skull tiles as well as falling tiles should respawn when they have fallen. Either off-screen or on-screen.

**Better background system**

Sprite files as BGs would be cool.

**Better cloud system**

Changing what/the variety of images in cloud particles, as well as speed.

**Tintable lightbulb/lantern**

A colorable, easily placeable light source for pretty effects in levels. Also, a creepy pulsing light object for the ghost forest.

**Light source objects**

Objects with sprites (cones, etc.) that specifically lit up an area or light didn't apply there, lit it up, etc. might doable using the newer graphic engine surfaces. Z-pos editable, too, and it can be rotated, and it is not solid.

### Moving Platform Improvements

**New moving platforms**

Add more designs for moving platforms to fit in multiple scenarios better.


### Badguy Ideas

**Mother Snail**

A huge sleeping snail mother that Tux cannot pass/jump over, but he can wake it up, so he has to find a way to block or move its awake form in order to progress. Possibly also produces a set amount of snail offspring, similar to a dispenser with a set value of enemies. RustyBox's snail concept but much bigger can possibly be used for this enemy.

**Bluejay**

A sneaky bluejay who sits on top of stuff and periodically throws acorns down at Tux. Acorns don't collide with tiles, but do collide with enemies and Tux. When Tux gets near it, it flies away, never to be seen again. Does a cheeky laugh/giggle after throwing the acorn, and its eyes probably follow Tux.

**Woodpecker**

The smart variant to the bluejay, the woodpecker pecks down pinecones at Tux, and sits there for a while. Tux can then use the pinecone and throw it up to defeat the woodpecker. Either the pinecone respawns after a while, or the woodpecker is smart enough to go seek out another tree with pinecones.

**Pinecone**

The pinecone for the woodpecker. Upon falling, which it only falls when pecked by woodpecker, it doesn't despawn, as it can be picked up and used as a projectile (like the rock, just with better range), but when it is falling, it can hurt Tux.

**Acorn**

The acorn that the bluejay throws. If used by itself, it falls normally, like a stalactite would, but if the bluejay throws it, it immediately begins falling no matter what. Doesn't collide with tiles, but does collide with enemies/players.

**Tentacle Monster**

A underwater enemy, which grabs Tux with his arm/tentacle and pulls him deeper into the water (or the bottom edge of the level, to be specific) to his demise. Could be used for older levels, where the swimming feature was not present.


### Other

**Ice floes**

Ice floes that respond to the gravity placed on top of them would add some goodness.

**Thumbs up**

Tux should twirl and do a happy little thumbs up while the level ending is playing.

**"3AM easter egg"**

If the player plays a worlds between a certain time frame, certain scripting events can happen. E.g. Levels get darker, scary, etc. easter eggs like &#39;bridge stuck&#39;

**After-a-while easter eggs/Idle-Graphics**

Snowballs and other enemies do a little break after a while. After all, they were walking for so much time… Tux, after a while of not moving, also gets angry and curses the screen. Jumpy just stops jumping after a while

