Even though it's still unclear whether SuperTux will be accepted into
[GSoC 2016](https://summerofcode.withgoogle.com/), this page should serve as a
list of potential ideas for students. This is not an exact plan, and changes can
be proposed. The page can also be used to coordinate mentor assignments.

### Multi-Player mode

A long-requested feature from the user community is having more than two people
playing the game. The project would include adding the ability for two instances
of a Player inside the game, and the student would ideally add the possibility
to add more than one input device to the game, as the two players need to be
able to play at the same time.

**Possible mentors:** Tobbi

### Font improvements

Our current font system is using png images containing the glyphs. This has
proven to be hard to edit and hard to understand for contributors, and has
even introduced a few bugs or wasn't able to properly display serveral characters.

The plan is to move to a TTF rendering library such as SDL\_ttf or FreeType and
integrate it into the game.

### In-game level editor

Since removing the in-game level editor in favor of the external ones, players
have complained about level editing being hard, and even the developer team has
had problems with running the editor on their computers, mostly due to portability
issues.

As such, we'd like to re-introduce an in-game level editor. Even though work
has already started at [#269](https://github.com/SuperTux/supertux/pull/269), it
is far from being finished

**Possible mentors:** Hume2

### OpenGL ES support

Update our `opengl` renderer option to be able to support OpenGL ES. This would
make running SuperTux on lower-spec devices more fluent, with more fun for the
player. Graphics skills are required for this task.
