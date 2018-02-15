Here are some useful terms which will help you understand what people are talking about, on IRC, the mailing list or GitHub.

## Beginner Terms

### Level

A tile-base map of platforms which Tux (the player) must run and jump through. They are also littered with Badguys, and other objects

### Worldmap

A set of levels, organize into a [group of] islands.

### [Badguy](https://github.com/SuperTux/supertux/wiki/Badguys)

One of Nolok's minions, that Tux must avoid, or attempt to kill.

### Boss

A badguy which Tux must fight at the end of each island in Story Mode.

### Addon

A ZIP archive containing levels and possibly a worldmap. These can be downloaded in-game, or taken from other sources such as the forums.

### Secret Area

An area of the level which is difficult to reach, often containing a reward and a message e.g. "You have found a Secret Area"

## Advanced Terms

### [S-Expr](https://en.wikipedia.org/wiki/S-expression) (Also "sexpr", "s-expression" and even "lisp")

The file format that the game loads levels, resource definitions and sprites from.

### Sector

Levels can contain multiple areas which Tux cannot run and jump between. He has to use doors, or another way to reach these areas.

### Scripting

Levels can contain scripts which give the level creator more control over the level's objects and tiles. They are small pieces of code.
There can be script triggers, which when Tux collides with them (although invisible) the script will run.
Buttons, and other events can also run scripts

### [Squirrel](https://en.wikipedia.org/wiki/Squirrel_(programming_language))

The scripting language used by the game.
