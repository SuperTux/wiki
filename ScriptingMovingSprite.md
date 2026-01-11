> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

Abstract base class for `MovingObject`s, that are represented by a sprite. 

Instances
--------

None.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)

The following classes inherit functions and variables from this class:
* AngryStone
* [BadGuy](https://github.com/SuperTux/supertux/wiki/ScriptingBadGuy)
* BicyclePlatformChild
* BigSnowball
* Block
* BonusBlock
* Boss
* BouncingSnowball
* Brick
* Bumper
* [Candle](https://github.com/SuperTux/supertux/wiki/ScriptingCandle)
* CaptainSnowball
* CirclePlatform
* Coin
* [ConveyorBelt](https://github.com/SuperTux/supertux/wiki/ScriptingConveyorBelt)
* CorruptedGranito
* CorruptedGranitoBig
* Crusher
* Crystallo
* Dart
* DartTrap
* [Decal](https://github.com/SuperTux/supertux/wiki/ScriptingDecal)
* Dispenser
* DiveMine
* Door
* Explosion
* FallBlock
* Firefly
* FishChasing
* FishHarmless
* FishJumping
* FishSwimming
* Flame
* FlyingSnowBall
* GhostTree
* GhostTreeRoot
* GhostTreeRootBlue
* GhostTreeRootGreen
* GhostTreeRootMain
* GhostTreeRootPinch
* GhostTreeRootRed
* Ghoul
* GoldBomb
* [Granito](https://github.com/SuperTux/supertux/wiki/ScriptingGranito)
* [GranitoBig](https://github.com/SuperTux/supertux/wiki/ScriptingGranitoBig)
* GranitoGiant
* GrowUp
* Haywire
* HeavyBrick
* HeavyCoin
* HurtingPlatform
* Igel
* InfoBlock
* InvisibleBlock
* Ispy
* Jumpy
* KamikazeSnowball
* Key
* Kugelblitz
* Lantern
* LeafShot
* LevelTile
* [LitObject](https://github.com/SuperTux/supertux/wiki/ScriptingLitObject)
* LiveFire
* LiveFireAsleep
* LiveFireDormant
* MagicBlock
* Mole
* MoleRock
* MrBomb
* MrIceBlock
* MrTree
* Owl
* Plant
* Platform
* [Player](https://github.com/SuperTux/supertux/wiki/ScriptingPlayer)
* PneumaticPlatformChild
* PocketPowerUp
* PowerUp
* PushButton
* RCrystallo
* Rock
* Root
* RootSapling
* RubLight
* RustyTrampoline
* SCrystallo
* SSpiky
* [ScriptedObject](https://github.com/SuperTux/supertux/wiki/ScriptingScriptedObject)
* Shard
* ShortFuse
* SkyDive
* SmartBall
* SmartBlock
* Snail
* SnowBall
* SnowExplosionParticle
* Snowman
* SpawnPointObject
* SpecialTile
* Spiky
* SpriteChange
* SpritedTrigger
* Stalactite
* Star
* StickyBadguy
* StickyObject
* StickyTrigger
* Stumpy
* Switch
* Tarantula
* Teleporter
* Toad
* [Torch](https://github.com/SuperTux/supertux/wiki/ScriptingTorch)
* Totem
* Trampoline
* TreeWillOWisp
* TuxDoll
* UnstableTile
* ViciousIvy
* WalkingBadguy
* WalkingCandle
* WalkingLeaf
* WaterDrop
* WeakBlock
* [WillOWisp](https://github.com/SuperTux/supertux/wiki/ScriptingWillOWisp)
* WorldMapObject
* Yeti
* YetiStalactite
* Zeekling


Methods
-------

Method | Explanation
-------|-------
`bool set_sprite(string file)` | Sets the sprite of the object. Returns `true` on success. 
`string get_sprite()` | Returns the file of the object's sprite. 
`string get_action()` | Returns the name of the current action of the sprite. 
`void set_action(string name, int loops = -1)` | Sets the current action of the sprite, as well as the number of times it should loop, and resizes the bounding box. <br /><br />**NOTE:** Use with care as you can easily get stuck when resizing the bounding box. <br /><br /> `loops` - Optional, -1 by default (negative value means infinite). Set to -100 to continue looping from the previous action. 
`void set_action_loops(string name, int loops)` | **Deprecated!** Use `set_action()` instead! <br /><br />Sets the current action of the sprite, as well as the number of times it should loop, and resizes the bounding box. <br /><br />**NOTE:** Use with care as you can easily get stuck when resizing the bounding box. <br /><br /> `loops` - Negative value means infinite. Set to -100 to continue looping from the previous action. 


Variables
---------

None.

Constants
---------

None.
