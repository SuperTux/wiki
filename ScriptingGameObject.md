> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingPage.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingPage.md).

Summary
-------

Base class for all the things that make up Levels' Sectors

Instances
--------

None.

Inheritance
--------

The following classes inherit functions and variables from this class:
* AmbientLight
* [AmbientSound](https://github.com/SuperTux/supertux/wiki/ScriptingAmbientSound)
* AngryStone
* [Background](https://github.com/SuperTux/supertux/wiki/ScriptingBackground)
* [BadGuy](https://github.com/SuperTux/supertux/wiki/ScriptingBadGuy)
* BezierMarker
* BicyclePlatform
* BicyclePlatformChild
* Block
* Bomb
* BonusBlock
* BouncingSnowball
* BouncyCoin
* Brick
* Bullet
* Bumper
* [Camera](https://github.com/SuperTux/supertux/wiki/ScriptingCamera)
* [Candle](https://github.com/SuperTux/supertux/wiki/ScriptingCandle)
* CaptainSnowball
* CirclePlatform
* Climbable
* [CloudParticleSystem](https://github.com/SuperTux/supertux/wiki/ScriptingCloudParticleSystem)
* Coin
* CoinExplode
* CoinRain
* [ConveyorBelt](https://github.com/SuperTux/supertux/wiki/ScriptingConveyorBelt)
* CorruptedGranito
* CorruptedGranitoBig
* Crusher
* CrusherRoot
* Crystallo
* [CustomParticleSystem](https://github.com/SuperTux/supertux/wiki/ScriptingCustomParticleSystem)
* CustomParticleSystemFile
* Dart
* DartTrap
* [Decal](https://github.com/SuperTux/supertux/wiki/ScriptingDecal)
* Dispenser
* [DisplayEffect](https://github.com/SuperTux/supertux/wiki/ScriptingDisplayEffect)
* DiveMine
* Door
* Electrifier
* EndSequence
* EndSequenceFireworks
* EndSequenceWalk
* Explosion
* FallBlock
* FallingCoin
* Firefly
* Fireworks
* FishChasing
* FishHarmless
* FishJumping
* FishSwimming
* Flame
* [FloatingImage](https://github.com/SuperTux/supertux/wiki/ScriptingFloatingImage)
* FloatingText
* Flower
* FlyingSnowBall
* GhostParticleSystem
* GhostTree
* Ghoul
* GoldBomb
* [Gradient](https://github.com/SuperTux/supertux/wiki/ScriptingGradient)
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
* [LevelTime](https://github.com/SuperTux/supertux/wiki/ScriptingLevelTime)
* Light
* [LitObject](https://github.com/SuperTux/supertux/wiki/ScriptingLitObject)
* LiveFire
* LiveFireAsleep
* LiveFireDormant
* MagicBlock
* MarkerObject
* Mole
* MoleRock
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [MovingSprite](https://github.com/SuperTux/supertux/wiki/ScriptingMovingSprite)
* MrBomb
* MrIceBlock
* MrTree
* MusicObject
* NodeMarker
* OneUp
* Owl
* ParticleSystem
* ParticleSystem_Interactive
* ParticleZone
* Particles
* PathGameObject
* Plant
* Platform
* [Player](https://github.com/SuperTux/supertux/wiki/ScriptingPlayer)
* PlayerStatusHUD
* PneumaticPlatform
* PneumaticPlatformChild
* PowerUp
* PulsingLight
* PushButton
* RCrystallo
* [RainParticleSystem](https://github.com/SuperTux/supertux/wiki/ScriptingRainParticleSystem)
* RainSplash
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
* SmokeCloud
* Snail
* SnowBall
* SnowExplosionParticle
* SnowParticleSystem
* Snowman
* SoundObject
* SpawnPointMarker
* SpawnPointObject
* SpecialRiser
* SpecialTile
* Spiky
* [Spotlight](https://github.com/SuperTux/supertux/wiki/ScriptingSpotlight)
* SpriteChange
* SpriteParticle
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
* [TextArrayObject](https://github.com/SuperTux/supertux/wiki/ScriptingTextArrayObject)
* [TextObject](https://github.com/SuperTux/supertux/wiki/ScriptingTextObject)
* TextScroller
* [Thunderstorm](https://github.com/SuperTux/supertux/wiki/ScriptingThunderstorm)
* [TileMap](https://github.com/SuperTux/supertux/wiki/ScriptingTileMap)
* Toad
* [Torch](https://github.com/SuperTux/supertux/wiki/ScriptingTorch)
* Totem
* Trampoline
* TreeWillOWisp
* Trigger
* Tux
* UnstableTile
* VerticalStripes
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
`string get_display_name()` | Returns the display name of the object, translated to the user's locale
`int get_version()` | Returns the current version of the object
`int get_latest_version()` | Returns the latest version of the object
`bool is_up_to_date()` | Checks whether the object's current version is equal to its latest one
`int get_type()` | Returns the type index of the object
`string get_name()` | Returns the name of the object


Variables
---------

None.

Constants
---------

None.
