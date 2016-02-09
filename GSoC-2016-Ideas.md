Even though it's still unclear whether SuperTux will be accepted into
[GSoC 2016](https://summerofcode.withgoogle.com/), this page should serve as a
list of potential ideas for students. This is not an exact plan, and changes can
be proposed. The page can also be used to coordinate mentor assignments.

### Multi-Player / Split-Screen

A long-requested feature from the user community is having two people (or even more)
playing the game. An [old patch](https://github.com/SuperTux/supertux/blob/master/contrib/supertux-coop.diff)
implements the basics such as multiple instances of the player and multiple input devices,
but it does not affect the camera. The plan would be to implement split-screen display,
preferably in a way that also allows it to be used for cutscene animations such as
pulling a switch.

**Possible mentors:** Tobbi

### Font improvements

Our current font system is using png images containing the glyphs. This has
proven to be hard to maintain and hard to understand for contributors, and has
bugs in right-to-left languages and isn't able to properly display Arabic.

The plan is to move to a TTF rendering library such as SDL\_ttf or HarfBuzz/FreeType and
integrate it into the game.

### In-game level editor

Since removing the in-game level editor in favor of the external ones, players
have complained about level editing being hard, and even the developer team has
had problems with running the editor on their computers, mostly due to portability
issues.

As such, we'd like to re-introduce an in-game level editor. Work
has started at [#269](https://github.com/SuperTux/supertux/pull/269) but it
is far from being finished

**Possible mentors:** Hume2

### OpenGL ES support

Update our `opengl` renderer option to be able to support OpenGL ES. This would
make running SuperTux on lower-spec devices more fluent, with more fun for the
player. Graphics skills are required for this task.

### Wiimote support

SuperTux does not currently support WiiMotes; this project would implement support, using the popular [Wiiuse](https://github.com/rpavlik/wiiuse) library.

### Water Physics / Sliding Physics

Penguins swim quite frequently, but so far there has not been any swimming in SuperTux. This project would add buoyancy and possibly some fluid simulation to SuperTux, allowing Tux to swim as well as any other penguin. Ideas for swimming are [here](http://supertux.lethargik.org/wiki/Swimming). Also interesting would be the ability to slide down slopes and jump off ramps.
