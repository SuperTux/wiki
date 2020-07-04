# About this Document

This document is a work in progress, nothing here is considered even remotely final. Also, SuperTux uses version numbers instead of milestones now. There is a list of stuff that needs to be done, and at the bottom is a list of ideas that could be implemented too.

# Overview

SuperTux 0.7.0 will bring about a completion to the first two worlds so work can begin on World 3. This means improving/revamping the graphics, sound effects, code, story and levels in many areas and adding some new features/mechanics as well. (swimming, etc.)

# Audio

**Tux, Penny, Nolok**

Add new sounds/cutscene speech. Perhaps use a new VA?

# Revamped Graphics

**Backgrounds**

- Light Forest – add a few varying parallax BGs for normal light levels.
- General - More cloud BGs would be cool.
- Parallax-ify many BGs.

**Tiles/Decals**

- Actually implement the already made new forest tiles, bush tiles, forest background tiles and slime tiles.
- A multitude of new forest trees and tree branches to make the forest pretty.
- The tree moviestar exit.
- Revamp/large extension of the icy island background decals to live up to the new forest stuff. Could include things like snowmen, flags, crates, bridge improvements, improvement/expansion of the current tiles, etc. as well as animated things like animals and flags. Look to Pingus for inspiration, maybe?
- Miscellaneous other new tilesets for the forest/ghost forest to give it variety and a finished/varied feel
- New underwater decoration
- Simple bridge/scaffolding unisolid tiles
- Treetop Tileset
- Deeper Lava/Acid
- Waterfall tiles
- New decoration (Forest) - Could include things like animals, shrubs, as well as things for the ghost forest.
- Snowtops for use in levels
- Ghost tree root tiles
- Library tiles, as well as library decoration
- New decoration for castles
- New decoration for everyplace!

**Objects**

- Wide/Wider Stationary Trampolines
- New/Better Billboards
- Moving platform, bone version

**Enemies**

- **Ghost Forest**
- Rotten Leaf/Ivy
- Rotten Tree/Leafless Tree
- Rotten Stumpy
- Ghost Tree Roots
- **Light Forest**
- Spring Leaf
- Autumn Leaf
- Tree
- Leafless Tree
- Stumpy
- Leafshot
- Zeekling
- Igel
- Snail
- Big Snail
- **Icy Island**
- Spiky Walking
- Crystallo
- Snowman
- Bouncing Snowball
- Snowshot

**Characters**

- Tux
  - Skidding
  - Swimming
  - Ducking
  - Backflip
  - Kicking
  - Dead
  - Worldmap Boat
  - Other/cutscene sprites…
- Penny
  - Other/cutscene sprites…
- Nolok
  - Other/cutscene sprites…
- Yeti
- Ghost Tree

# Features/Mechanics

**Locked Doors and Keys**

Suggested by RustyBox, key would be like a powerup and would hovering over Tux and auto-unlock any locked door. Locked doors can&#39;t be opened, etc. Would be useful for puzzle stages. Sometimes, multiple keys are needed to open a door and this should be signalled.

**Ghost Tree and Yeti**

Update boss fight/level/behavior to accommodate new ideas and graphics.

# Other, Unconfirmed Ideas

Only some, few or none of this stuff may be added, or might get added at a later time.

**-Tux movement**

**Thumbs up**

Tux should twirl and do a happy little thumbs up while the level ending is playing.

**Controllable Fall Speed**

Tux should fall faster if he is holding down.

**Coyote Time**

Hardcoded coyote time should be implemented in the game for easier jumps.

**Walljumping**

Could be quite useful and nice to have. Would extend move set of Tux. Possible on certain tiles. To decide: Does Tux cling to the wall or slide down slower?

**Slope Sliding**

Due to current slope detection this might not get added, but it would be awesome to have Tux slide on his belly to hurt enemies and then fly off slopes after gaining momentum.

**Ice Cutlass**

A sword where Tux does a little dash. Might be available as a rock or as a powerup. If it is a powerup, it will replace the ice flower and its freezing ability.

**-Performance Improvements**

**Editor Improvements**

A better text editor, Also improve infoblock UI (more like scripting UI)

**Check for updates**

Upon booting up game, check for updates, and if update is available, place a "Update Game" dialogue item when the game is first opened. If the current version equals the installed version, it's plays normally. Normally only works for major releases, but in dev mode works for every nightly build.

**More particle events/effects/use of screen shaking**

We need more particle effects for different things, like for wind, to make it look better than just some small cubes, and give it actual images rather than just rects. Also, it would be nice for particles to be used more, such as when Tux/badguy lands, on wind, when slipping on ice or slime, walljumping, etc. in those events, but also in normal behavior, such as with fire/lava having particles come off/particles around it, and also there should be more particle objects, like falling leaves/blowing wind in the normal forest or sky "fairies"/glowing floaty particles in the air in the ghost forest. Also, it would be nice to shake the screen more, such as in cutscenes, when Tux is jolted, to convey certain emotions, when bombs explode, when Tux is hurt, etc. Also bubbles when Tux enters or leaves water, or makes a sudden motion/boosts/starts moving again. Many more particle events and shaking could be added to add liveliness to the game.

**More sound effects**

Add sound effects for when Tux walks on different tiles, and overall better sounds for when he dies or speaks or enters water.

**-Object Improvements/New Object ideas**

**Better background system**

Sprite files as BGs would be cool.

**Better cutscene methods**

Cutscenes should be skippable, trigger only once per level session, and text should be passed through via a button.

**Better cloud system**

Changing what/the variety of images in cloud particles, as well as speed.

**Ghoul improvements**

Ghouls should not collide with each other, and should not collide with solid land. Their flying speed should be configurable and there should be a blue light object which attracts them when it is turned on, shifting their focus away from Tux. Also, there should be an object that can only be broken by collision with ghouls.

**Pigeons**

These are special background objects who, when Tux is near, flee in the direction away from his body.

**Better Wind**

It should be easier to move in wind, and movement shouldn't be entirely obscured. Also wind should affect Tux while he stands, too.

**Swinging on flag strings**

Adding certain strings that can be swung on like Alto Adventure would be nice and would suit an ice game.

**Tintable lightbulb/lantern**

A colorable, easily placeable light source for pretty effects in levels. Also, a creepy pulsing light object for the ghost forest.

**Light source objects**

Objects with sprites (cones, etc.) that specifically lit up an area or light didn't apply there, lit it up, etc. might doable using the newer graphic engine surfaces. Z-pos editable, too, and it can be rotated, and it is not solid.

**Blinking Tiles**

Tiles whose solidity blinks back and forth.

**Sideways Bouncers**

Either an option for trampolines or an entirely new object for bouncing sideways. The bounce should be stronger than Tux's jump length so it is important and should be a little longer than 32 px so it can be embedded in the side of terrain.

**Colored Text per speaker**

In future cutscenes, Tux, Penny and Nolok might have speaking parts and there should be the ability to change color of Text in the text object per character (green for Nolok, purple for Penny, etc.) It would also be nice to have high def/large face renders of the characters to appear from the bottom of the screen when they speak.

**Change the tint + speed of decals**

For custom BGs, add ability to change a decal's scroll speed and tint. Also there should be the option to change the tint of background images.

**Pushbutton Improvements**

Add an option for an "unpress" script, or an option for the script to only play when an activator's on it. Maybe have a different sprite.

**Rocks activating pushbuttons**

This should definitely be added for puzzle stages.

**Rock throwing improvements**

Make rocks bounce off of Tux rather than killing him. Rocks should not be able to kill Tux.

**Dispensers obeying gravity**

Dispensers should have an option to obey gravity.

**Respawning falling tiles/stalactites**

Skulltiles should respawn when they have fallen.

**-Moving platform Improvements**

**More velocity/acceleration driven platforms**

Allow platforms to be more velocity/acceleration driven, along with other objects that move (like Camera) and also allow the player to retain velocity that they did while on moving platforms (for events such as Tux being flung off a platform)

**Better movement on moving tilemaps**

Tux should move better on moving tilemaps. Currently he can hardly jump, or move left to right, etc.

**-New moving platforms**

**Falling Platform**

An object that shakes and falls when Tux is on it or is under it. A UNISOLID option should be added as well.

**Semi-controllable platforms**

One type that only moves as long as Tux is on it, and when he leaves, it returns to its home.

**Circular Platforms**

Platforms with circular paths, just like a flame, whose path speed can be configurable and whatnot.

**Ice floes**

Ice floes that respond to the gravity placed on top of them would add some goodness.

**-Enemy ideas**

**Enemy Idea - Cod**

Simply a little fish enemy that swims back and forth should be added. It swims left to right, switching directions upon hitting a wall. Two variants should be added: a small and big one.

**Enemy Idea - Shadow Tux**

An enemy who copies exactly Tux's behavior and when catches up to him or collides with him Tux dies. Unkillable, but can be trapped as it only obeys Tux's moves and therefore how he collides as well. Basically a "shadow-tux" (or dark rayman-like), but would have a delay that the player can set.

**Enemy Idea - Mother**

A huge sleeping snail mother that Tux cannot pass/jump over, but he can wake it up, so he has to find a way to block or move its awake form in order to progress. Possibly also produces a set amount of snail offspring, similar to a dispenser with a set value of enemies. RustyBox's snail concept but much bigger can possibly be used for this enemy.

**Enemy Idea - Bluejay**

A sneaky bluejay who sits on top of stuff and periodically throws acorns down at Tux. Acorns don't collide with tiles, but do collide with enemies and Tux. When Tux gets near it, it flies away, never to be seen again. Does a cheeky laugh/giggle after throwing the acorn, and its eyes probably follow Tux.

**Enemy Idea - Woodpecker**

The smart variant to the bluejay, the woodpecker pecks down pinecones at Tux, and sits there for a while. Tux can then use the pinecone and throw it up to defeat the woodpecker. Either the pinecone respawns after a while, or the woodpecker is smart enough to go seek out another tree with pinecones.

**Enemy Idea - Pinecone**

The pinecone for the woodpecker. Upon falling, which it only falls when pecked by woodpecker, it doesn't despawn, as it can be picked up and used as a projectile (like the rock, just with better range), but when it is falling, it can hurt Tux.

**Enemy Idea - Acorn**

The acorn that the bluejay throws. If used by itself, it falls normally, like a stalactite would, but if the bluejay throws it, it immediately begins falling no matter what. Doesn't collide with tiles, but does collide with enemies/players.

**Enemy Idea - Tentacle Monster**

A underwater enemy, which grabs Tux with his arm/tentacle and pulls him deeper into the water (or the bottom edge of the level, to be specific) to his demise. Could be used for older levels, where the swimming feature was not present.

**Enemy Idea - Blinking Ghost Roots**

These are ghost tree roots that attack based on a timer. Most similar to the tree's usage of them.

**Enemy Idea - Growing Ghost Roots**

If Tux steps on them, after he leaves them they grow up so Tux cannot walk on that terrain anymore.

**-Easter eggs**

**3AM easter egg**

If the player plays Icy Island/other worlds between 3AM and 3:30AM, certain scripting events can happen. Levels get darker, scary, etc. easter eggs like &#39;bridge stuck&#39;

**After-a-while easter eggs/Idle-Graphics**

Snowballs and other enemies do a little break after a while. After all, they were walking for so much time… Tux, after a while of not moving, also gets angry and curses the screen. Jumpy just stops jumping after a while

# Story

  - Improve it, make it better. There used to be more here but I deleted it because nothing is final yet.

# Levels

**Levels in general**

The levels of the Add-On menu (Bonus Islands I-IV, Halloween 2014, etc.) should be divided from other contrib levels, which can be downloaded manually or in-game from "Add-Ons". Manually downloaded levelpacks would be subfoldered under "Community Levels", while those already in game would be in a own folder named "Add-Ons". This would make the list of Add-Ons shorter and would clear up which levels are official and which not.

**Normal Levels**

Update with the new graphics for their assets. Also: make them more interesting! Most levels are your run-of-the-mill left to right levels and don&#39;t make use of everything available, like most enemies, vertical space, varying directions, multiple paths, autoscrolling, signs, moving tilemaps, unisolids, bricks, multiple paths, those scripting bonus blocks that can be activated by rocks, etc. Make the most of the level gimmicks!

One of the most stupid and awful level design philosophies I have seen (especially since it was used to block level proposals in the past) is to water down the quality of certain levels to make others stand out, and to this I say: No! That is stupid! You&#39;re only going to improve with time, so you can always go back and add on more and more and make ultimately all levels better. And anyway, would you rather have two amazing levels of the same quality or one crappy level + one amazing level?

Another problem with current levels is sometimes having to hit bonus blocks to advance in a level. Some official levels do this and it should be removed, because every level should be beatable without hitting a bonus block.

**Secret paths on worldmap**

Whenever a secret exit to a bonus level is unlocked, a path appears leading to that level. Currently able and might be easy to implement.

**Cutscene Levels**

Update these levels with the new story decisions and the new graphics/stuff decided for the characters.

**Boss Levels**

Update to accommodate the new fights and to make them a lot more interesting.
