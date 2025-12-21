> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

A `BadGuy` that was given a name can be controlled by scripts. 

Instances
--------

A `BadGuy` is instantiated by placing a definition inside a level. It can then be accessed by its name from a script or via `sector.name` from the console. 

Inheritance
--------

This class inherits functions and variables from the following base classes:
* [MovingSprite](https://github.com/SuperTux/supertux/wiki/ScriptingMovingSprite)
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* Portable
* GameObjectComponent

The following classes inherit functions and variables from this class:
* AngryStone
* Boss
* BouncingSnowball
* CaptainSnowball
* CorruptedGranito
* CorruptedGranitoBig
* Crystallo
* Dart
* DartTrap
* Dispenser
* DiveMine
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
* Haywire
* Igel
* Jumpy
* KamikazeSnowball
* Kugelblitz
* LeafShot
* LiveFire
* LiveFireAsleep
* LiveFireDormant
* Mole
* MoleRock
* MrBomb
* MrIceBlock
* MrTree
* Owl
* Plant
* RCrystallo
* Root
* RootSapling
* SCrystallo
* SSpiky
* ShortFuse
* SkyDive
* SmartBall
* SmartBlock
* Snail
* SnowBall
* SnowExplosionParticle
* Snowman
* Spiky
* Stalactite
* StickyBadguy
* Stumpy
* Tarantula
* Toad
* Totem
* TreeWillOWisp
* ViciousIvy
* WalkingBadguy
* WalkingCandle
* WalkingLeaf
* [WillOWisp](https://github.com/SuperTux/supertux/wiki/ScriptingWillOWisp)
* Yeti
* YetiStalactite
* Zeekling


Methods
-------

Method | Explanation
-------|-------
`void kill()` | Sets the badguy to kill/falling state, which makes it fall of the screen (its sprite is turned upside-down). 
`void ignite()` | Kills the badguy by igniting it. 


Variables
---------

None.

Constants
---------

None.
