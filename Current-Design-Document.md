# About this Document

This document is a work in progress, nothing here is considered even remotely final. Also, SuperTux uses version numbers instead of milestones now. There is a list of stuff that needs to be done, and at the bottom is a list of ideas that could be implemented too.

# Overview

SuperTux 0.7.0 will bring about a completion to the first two worlds so work can begin on World 3. This means improving/revamping the graphics, sound effects, code, story and levels in many areas and adding some new features/mechanics as well. (swimming, etc.)

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

# Audio

**Tux, Penny, Nolok**

Add new sounds/cutscene speech. Perhaps use a new VA?

# Revamped Graphics

**Backgrounds**

- Light Forest – add a few varying parallax BGs for normal light levels.

**Tiles/Decals**

- Actually implement the already made new forest tiles and slime tiles.
- A multitude of new forest trees and tree branches to make the forest pretty.
- The tree moviestar exit.
- Revamp of the icy island tileset and icy background tilesets to live up to the new forest stuff.
- Miscellaneous other new tilesets for the forest/ghost forest to give it variety and a finished/varied feel

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
- **Icy Island**
- Spiky Walking
- Crystallo
- Jumpy
- Snowman
- Bouncing Snowball
- Flying Snowball
- Snowshot
- **General**
- Bomb
- Haywire
- Goldbomb
- Shortfuse

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

# New Graphics

**Deeper Lava (tintable?) –** Suggested by mt and Daniel

**Door billboard -** A billboard conveying to the player how to enter a door.

**Big Snails -** Sprites for bigger sized snails can be added.

**Acid –** Perhaps could be retinted lava.

**New Unstable Platforms -** Varieties of these tiles/bigger versions would make things look a lot more varied.

**Wide Trampolines -** Wider versions of unportable trampolines for puzzle areas.

**Waterfall -** Waterfall graphics matching the modern water style.

**New Icy Island Deco** – Perhaps look to Pingus for inspiration? The tileset should be as detailed as the forest, imo

**Treetop tileset** - A tileset for when Tux is in the trees.

**Snowfort Tileset** - A small tileset for snowy structures.

**Alternate Icy Tileset** - Forest has one alternate tileset, and it would be cool to have a deep blue ice tileset, or a dirt/rock terrain alternate option for the icy island.

**New decoration (Icy)** - Could include things like snowmen, flags, crates, bridge improvements, improvement/expansion of the current tiles, etc. as well as animated things like animals and flags.

**New decoration (Forest)** - Could include things like animals, shrubs, as well as things for the ghost forest.

**Other...** - Whatever new features get added need proper images, obviously.

# Features/Mechanics

**Tree Roots**

Ghost Tree&#39;s root attack roots should be used in earlier levels to foreshadow his coming. Suggested by RustyBox.

**Fish enemy**

So Tux doesn&#39;t get lonely while swimming, a normal left-right fish enemy shall be added (equivalent of snowball in the water)

**Locked Doors and Keys**

Suggested by RustyBox, key would be like a powerup and would hovering over Tux and auto-unlock any locked door. Locked doors can&#39;t be opened, etc. Would be useful for puzzle stages. Sometimes, multiple keys are needed to open a door and this should be signalled.

**Ghost Tree and Yeti**

Update boss fight/level/behavior to accommodate new ideas and graphics.

# Other, Unconfirmed Ideas

Only some, few or none of this stuff may be added, or might get added at a later time.

**More particle events/effects/use of screen shaking**

We need more particle effects for different things, like for wind, to make it look better than just some small cubes, and give it actual images rather than just rects. Also, it would be nice for particles to be used more, such as when Tux/badguy lands, on wind, when slipping on ice or slime, walljumping, etc. in those events, but also in normal behavior, such as with fire/lava having particles come off/particles around it, and also there should be more particle objects, like falling leaves/blowing wind in the normal forest or sky "fairies"/glowing floaty particles in the air in the ghost forest. Also, it would be nice to shake the screen more, such as in cutscenes, when Tux is jolted, to convey certain emotions, when bombs explode, when Tux is hurt, etc. Also bubbles when Tux enters or leaves water, or makes a sudden motion/boosts/starts moving again. Many more particle events and shaking could be added to add liveliness to the game.

**Better background system**

It would be nice to have better/more variety parallax BGs for the foreground and background. And since the very back uses just a gradient, it would also be cool to have more variation in the cloud particle system for more unique clouds. And for BGs with still clouds, it would be nice to have more images for that too. Also, adding sprite files as backgrounds would enhance gameplay as well. Another good idea is to add ability to edit the scroll speed of decals for the sake of very custom forest FGs, or maybe just add forest FG tiles? Extending the image set of parallax and parallax tiles would be nice as well.

**Thumbs up**

Tux should twirl and do a happy little thumbs up while the level ending is playing.

**Squash and Stretch**

We use this for backgrounds, so why not for players/objects? I'd recommend adding a squash and stretch effect for Tux jumping, falling and landing, as well as for the bouncing snowball landing. Alternatively, these could just be drawn and programmed to work right, except the landing animation most likely wouldn't work.

**Pigeons**

These are special background objects who, when Tux is near, flee in the direction away from his body.

**Better Wind**

It should be easier to move in wind, and movement shouldn't be entirely obscured. Also wind should affect Tux while he stands, too.

**Sideways Icecrushers**

Yes.

**Shift activated platforms**

Platforms that only go to their node when the player presses shift.

**Bone rider things**

See World 8 of new mario games, they have a nice bone rider thing we could use.

**Swinging on flag strings**

Adding certain strings that can be swung on like Alto Adventure would be nice and would suit a penguin game.

**More sound effects**

Add sound effects for when Tux walks on different tiles, and overall better sounds for when he dies or speaks or enters water.

**Better background tiles/decals**

Ones who are animated (some not) and varied to bring life to the game. THis could be snowy rocks, snowmen, flowing snow grass, more snowpiles, crystals, flags in the wind, sleeping polar bears, arctic foxes/foxes playing, little birds, squirrels, other animals, flowing grass, etc.

**Tintable lightbulb/lantern**

A colorable, easily placeable light source for pretty effects in levels. Also, a creepy pulsing light object for the ghost forest.

**Light source objects**

Objects with sprites (cones, etc.) that specifically lit up an area or light didn't apply there, lit it up, etc. might doable using the newer graphic engine surfaces. Z-pos editable, too, and it can be rotated.

**Blinking Tiles**

Tiles whose solidity blinks back and forth.

**Sideways Bouncers**

Either an option for trampolines or an entirely new object for bouncing sideways. The bounce should be stronger than Tux's jump length so it is important and should be a little longer than 32 px so it can be embedded in the side of terrain.

**Bouncing Bubbles**

Some object that toss Tux in the opposite direction y-wise and in the opposite direction of impact x-wise (like being thrown back by something) would be nice to have.

**Coyote Time**

Hardcoded coyote time should be implemented in the game for easier jumps.

**Colored Text per speaker**

In future cutscenes, Tux, Penny and Nolok might have speaking parts and there should be the ability to change color of Text in the text object per character (green for Nolok, purple for Penny, etc.) It would also be nice to have high def/large face renders of the characters to appear from the bottom of the screen when they speak.

**Check for updates**

Upon booting up game, check for updates, and if update is available, place a "Update Game" dialogue item when the game is first opened. If the current version equals the installed version, it's plays normally. Normally only works for major releases, but in dev mode works for every nightly build.

**Change the tint + speed of decals**

For custom BGs, add ability to change a decal's scroll speed and tint. Also there should be the option to change the tint of background images.

**Pushbutton Improvements**

Add an option for an "unpress" script, or an option for the script to only play when an activator's on it.

**Rocks activating pushbuttons**

This should definitely be added for puzzle stages.

**Rock throwing improvements**

Make rocks bounce off of Tux rather than killing him.

**Dispensers obeying gravity**

Dispensers should have an option to obey gravity.

**Airflower improvements**

When wearing the air hat, it should be changed to a flying snowball's propeller hat, and pressing up propels Tux up once, like propeller hat from Super Mario. Also, he should be lighter and not activate falling tiles unless buttjump.

**Respawning falling tiles/stalactites**

Skulltiles should respawn when they have fallen.

**Music names**

The music should use a proper name instead of a filename when selecting it in the level editor.

**MULTIPLAYER**

First step, offline coop multiplayer, step 2 online multiplayer via Servers or a user code.

**Walljumping**

Could be quite useful and nice to have. Would extend move set of Tux. Possible on certain tiles. To decide: Does Tux cling to the wall or slide down slower?

**Wallclimbing**

Different from walljump, as Tux clings on to/climbs/declimbs these tiles, and a different tiletype is used. Still, both can be jumped off.

**Sliding**

Due to current slope detection this might not get added, but it would be awesome to have Tux slide on his belly to hurt enemies and then fly off slopes after gaining momentum.

**Ice Cutlass**

A sword where Tux does a little dash. Might be available as a rock or as a powerup. If it is a powerup, it will replace the ice flower and its freezing ability.

**Picking up frozen enemies**

A very niche feature, especially if the ice cutlass powerup is added, but would be nice.

**Better frozen enemy graphics**

Every frozen enemy should have an overlay of an iceblock instead of unique frozen graphics for each, who look just plain ugly.

**3AM easter egg**

If the player plays Icy Island/other worlds between 3AM and 3:30AM, certain scripting events can happen. Levels get darker, scary, etc. easter eggs like &#39;bridge stuck&#39;

**After-a-while easter eggs/Idle-Graphics**

Snowballs and other enemies do a little break after a while. After all, they were walking for so much time… Tux, after a while of not moving, also gets angry and curses the screen. Jumpy just stops jumping after a while

**Editor Improvements**

Autosave and a better text editor, open settings on creation of new level. Also improve infoblock UI (more like scripting UI)

**More velocity/acceleration driven platforms**

Allow platforms to be more velocity/acceleration driven, along with other objects that move (like Camera) and also allow the player to retain velocity that they did while on moving platforms (for events such as Tux being flung off a platform)

**Better movement on moving tilemaps**

Tux should move better on moving tilemaps. Currently he can hardly jump, or move left to right, etc.

**Falling Platforms/Tilesets**

Set an option for platforms or tilemaps to function like icicles/icecrushers

**Add support for rotatable/growing hitboxes**

Support for growing hitboxes should be added. Rotatable hitboxes might be a bit harder, though

**Controllable Platforms**

Two types: One where Tux holds UP to move it and one where Tux can move it freely. They should have sprites to separate them from others, though

**Semi-controllable platforms**

One type that only moves as long as Tux is on it, and when he leaves, it returns to its home.

**Sinking Platforms**

Platforms that sink when Tux is on them, and when he leaves, they go back up

**Circular Platforms**

Platforms with circular paths, just like a flame, whose path speed can be configurable and whatnot.

**Movable climbables**

Climbables who move.

**Snow Dune**

A rising snow dune like the sand one from nsmbwii.

**Enemy Idea**

A walkable tree branch that functions like stalactite, but can be walked on, although still falls.

**Enemy Idea 2**

An enemy who copies exactly Tux's behavior and when catches up to him or collides with him Tux dies. Unkillable, but can be trapped as it only obeys Tux's moves and therefore how he collides as well. Basically a "shadow-tux" (or dark rayman-like), but would have a delay that the player can set.

**Enemy Idea 3**

A huge sleeping snail mother that Tux cannot pass/jump over, but he can wake it up, so he has to find a way to block or move its awake form in order to progress. Possibly also produces a set amount of snail offspring, similar to a dispenser with a set value of enemies. RustyBox's snail concept but much bigger can possibly be used for this enemy.

**Enemy Idea 4**

A sneaky bluejay who sits on top of stuff and periodically throws acorns down at Tux. Acorns don't collide with tiles, but do collide with enemies and Tux. When Tux gets near it, it flies away, never to be seen again. Does a cheeky laugh/giggle after throwing the acorn, and its eyes probably follow Tux.

**Enemy Idea 5**

The smart variant to the bluejay, the woodpecker pecks down pinecones at Tux, and sits there for a while. Tux can then use the pinecone and throw it up to defeat the woodpecker. Either the pinecone respawns after a while, or the woodpecker is smart enough to go seek out another tree with pinecones.

**Enemy Idea 6**

The pinecone for the woodpecker. Upon falling, which it only falls when pecked by woodpecker, it doesn't despawn, as it can be picked up and used as a projectile (like the rock, just with better range), but when it is falling, it can hurt Tux.

**Enemy Idea 7**

The acorn that the bluejay throws. If used by itself, it falls normally, like a stalactite would, but if the bluejay throws it, it immediately begins falling no matter what. Doesn't collide with tiles, but does collide with enemies/players.

**Enemy Idea 8**

Throwable snowball! Used to activate far off blocks/switches.
