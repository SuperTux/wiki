> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

Abstract base class for `MovingObject`s, that are represented by a sprite

Instances
--------

None.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* CollisionListener

The following classes inherit functions and variables from this class:
* AngryStone
* [BadGuy](https://github.com/SuperTux/supertux/wiki/ScriptingBadGuy)
* BicyclePlatformChild
* Block
* Bomb
* BonusBlock
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
* CrusherRoot
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
* OneUp
* Owl
* Plant
* Platform
* PneumaticPlatformChild
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
`void set_sprite(string file)` | Sets the sprite of the object
`string get_sprite()` | Returns the file of the object's sprite
`string get_action()` | Returns the name of the current action of the sprite
`void set_action(string name)` | Sets the current action of the sprite and resizes the bounding box
`void set_action_loops(string name, int loops)` | Sets the current action of the sprite, as well as the number of times it should loop, and resizes the bounding box


Variables
---------

None.

Constants
---------

None.
