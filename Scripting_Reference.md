> This file is auto-generated from the [SuperTux source code](https://github.com/SuperTux/supertux/tree/master/src), using the template [ScriptingHome.md](https://github.com/SuperTux/wiki/tree/master/templates/ScriptingHome.md).

Since May 2005, SuperTux sports a Squirrel scripting interface useful
for level designers who want to add some interactive pep to their
levels. This document poses as a reference article for those who want
to explore the various objects of the SuperTux scripting model.

What is Squirrel?
-----------------

One of your first questions might be, “What does a rodent have to do
with a penguin?” [Squirrel](http://www.squirrel-lang.org/) is a
language with a syntax not much unlike other C-like languages (C, C++,
Java, ...). In the current implementation, it is integrated as
elements in the SuperTux level and worldmap files. The
[Console](Console "wikilink") is a full-fledged Squirrel interpreter
as well.

Squirrel, S-expr and SuperTux
-----------------------------

I have no clue if the developers simply chose Squirrel just because
the name so nicely integrates into the series of words “SuperTux” and
“[S-Expression](S-expr "wikilink")”. Currently, the Squirrel code is
integrated in string arguments of Scheme elements in SuperTux level
files. (Whew.) This is an example code block inside a level:

    (supertux-level
      (version 2)
      (name (_ "Go Blind"))
      (author "Team")
      (sector
        (name "main")
        (music "Annoying_penguin_gawking_sounds.ogg")

        ;; tilemaps, objects, whatever. (optional)
        ;...

        (init-script "
    Effect.fade_out(2.5);
    ")

        ;; more tilemaps, objects, and whatever. (optional)
        ;...

      )
    )

When this level loads, the screen fades out completely during two and
a half seconds right after the level is loaded. (Mind you, this would
be a frustrating experience for the player if you add a horde of
badguys near the spawn point...)

Object reference
----------------

If you are interested in an object and what cans of worms you can open
with it, this section is for you.

“(NYI)” after the function name symbolises functions that haven't been
implemented yet. Calling them will result in a line being printed to
standard output informing anybody who reads it that the script is
using a function that actually doesn't exist.

### Classes

* [AmbientSound](https://github.com/SuperTux/supertux/wiki/ScriptingAmbientSound)
* [AnchorPoints](https://github.com/SuperTux/supertux/wiki/ScriptingAnchorPoints)
* [Background](https://github.com/SuperTux/supertux/wiki/ScriptingBackground)
* [BadGuy](https://github.com/SuperTux/supertux/wiki/ScriptingBadGuy)
* [Camera](https://github.com/SuperTux/supertux/wiki/ScriptingCamera)
* [Candle](https://github.com/SuperTux/supertux/wiki/ScriptingCandle)
* [CloudParticleSystem](https://github.com/SuperTux/supertux/wiki/ScriptingCloudParticleSystem)
* [ConveyorBelt](https://github.com/SuperTux/supertux/wiki/ScriptingConveyorBelt)
* [CustomParticleSystem](https://github.com/SuperTux/supertux/wiki/ScriptingCustomParticleSystem)
* [Decal](https://github.com/SuperTux/supertux/wiki/ScriptingDecal)
* [DisplayEffect](https://github.com/SuperTux/supertux/wiki/ScriptingDisplayEffect)
* [FloatingImage](https://github.com/SuperTux/supertux/wiki/ScriptingFloatingImage)
* [GameObject](https://github.com/SuperTux/supertux/wiki/ScriptingGameObject)
* [GameObjectManager](https://github.com/SuperTux/supertux/wiki/ScriptingGameObjectManager)
* [Globals](https://github.com/SuperTux/supertux/wiki/ScriptingGlobals)
* [Gradient](https://github.com/SuperTux/supertux/wiki/ScriptingGradient)
* [Granito](https://github.com/SuperTux/supertux/wiki/ScriptingGranito)
* [GranitoBig](https://github.com/SuperTux/supertux/wiki/ScriptingGranitoBig)
* [Level](https://github.com/SuperTux/supertux/wiki/ScriptingLevel)
* [LevelTime](https://github.com/SuperTux/supertux/wiki/ScriptingLevelTime)
* [LitObject](https://github.com/SuperTux/supertux/wiki/ScriptingLitObject)
* [MovingObject](https://github.com/SuperTux/supertux/wiki/ScriptingMovingObject)
* [MovingSprite](https://github.com/SuperTux/supertux/wiki/ScriptingMovingSprite)
* [PathObject](https://github.com/SuperTux/supertux/wiki/ScriptingPathObject)
* [Player](https://github.com/SuperTux/supertux/wiki/ScriptingPlayer)
* [RainParticleSystem](https://github.com/SuperTux/supertux/wiki/ScriptingRainParticleSystem)
* [ScriptedObject](https://github.com/SuperTux/supertux/wiki/ScriptingScriptedObject)
* [Sector](https://github.com/SuperTux/supertux/wiki/ScriptingSector)
* [Spotlight](https://github.com/SuperTux/supertux/wiki/ScriptingSpotlight)
* [TextArrayObject](https://github.com/SuperTux/supertux/wiki/ScriptingTextArrayObject)
* [TextObject](https://github.com/SuperTux/supertux/wiki/ScriptingTextObject)
* [Thunderstorm](https://github.com/SuperTux/supertux/wiki/ScriptingThunderstorm)
* [TileMap](https://github.com/SuperTux/supertux/wiki/ScriptingTileMap)
* [Torch](https://github.com/SuperTux/supertux/wiki/ScriptingTorch)
* [WillOWisp](https://github.com/SuperTux/supertux/wiki/ScriptingWillOWisp)

