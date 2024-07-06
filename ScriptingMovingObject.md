> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

Base class for all dynamic/moving game objects

Instances
--------

None.

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* CollisionListener

The following classes inherit functions and variables from this class:
* [AmbientSound](https://github.com/SuperTux/supertux/wiki/ScriptingAmbientSound)
* AngryStone
* [BadGuy](https://github.com/SuperTux/supertux/wiki/ScriptingBadGuy)
* BezierMarker
* BicyclePlatformChild
* Block
* Bomb
* BonusBlock
* BouncingSnowball
* Brick
* Bullet
* Bumper
* [Candle](https://github.com/SuperTux/supertux/wiki/ScriptingCandle)
* CaptainSnowball
* CirclePlatform
* Climbable
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
* Flower
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
* InvisibleWall
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
* MarkerObject
* Mole
* MoleRock
* [MovingSprite](https://github.com/SuperTux/supertux/wiki/ScriptingMovingSprite)
* MrBomb
* MrIceBlock
* MrTree
* NodeMarker
* OneUp
* Owl
* ParticleZone
* Plant
* Platform
* [Player](https://github.com/SuperTux/supertux/wiki/ScriptingPlayer)
* PneumaticPlatformChild
* PowerUp
* PushButton
* RCrystallo
* ResizeMarker
* Rock
* Root
* RootSapling
* RubLight
* RustyTrampoline
* SCrystallo
* SSpiky
* ScriptTrigger
* [ScriptedObject](https://github.com/SuperTux/supertux/wiki/ScriptingScriptedObject)
* SecretAreaTrigger
* SequenceTrigger
* Shard
* ShortFuse
* SkyDive
* SmartBall
* SmartBlock
* Snail
* SnowBall
* SnowExplosionParticle
* Snowman
* SpawnPointMarker
* SpawnPointObject
* SpecialRiser
* SpecialTile
* Spiky
* [Spotlight](https://github.com/SuperTux/supertux/wiki/ScriptingSpotlight)
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
* TextArea
* Toad
* [Torch](https://github.com/SuperTux/supertux/wiki/ScriptingTorch)
* Totem
* Trampoline
* TreeWillOWisp
* Trigger
* UnstableTile
* ViciousIvy
* WalkingBadguy
* WalkingCandle
* WalkingLeaf
* WaterDrop
* WeakBlock
* [WillOWisp](https://github.com/SuperTux/supertux/wiki/ScriptingWillOWisp)
* Wind
* WorldMapObject
* Yeti
* YetiStalactite
* Zeekling


Methods
-------

Method | Explanation
-------|-------
`float get_x()` | Returns the object's X coordinate
`float get_y()` | Returns the object's Y coordinate
`void set_pos(float x, float y)` | Sets the position of the object
`void move(float x, float y)` | Moves the object by `x` units to the right and `y` down, relative to its current position
`float get_width()` | Returns the object's hitbox width
`float get_height()` | Returns the object's hitbox height


Variables
---------

None.

Constants
---------

None.
