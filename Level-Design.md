These guidelines should be kept for any level that appears on the official worldmaps. Designers contributing levels to the
Contrib sections are free of regulations - that's what those sections are for. However, keep in mind that if your levels
violate too many of these suggestions people will likely find them not very fun.

To maintain a certain level of playability, official levels should be designed with these rules in mind:

# Contents
  1. [Setting](https://github.com/SuperTux/supertux/wiki/Leveldesign#Setting)
  2. [Size](https://github.com/SuperTux/supertux/wiki/Leveldesign#Size)
  3. [Difficulty](https://github.com/SuperTux/supertux/wiki/Leveldesign#Difficulty)
  4. [Enemies](https://github.com/SuperTux/supertux/wiki/Leveldesign#Enemies)
  5. [Sectors](https://github.com/SuperTux/supertux/wiki/Leveldesign#Sectors)
  6. [Tiles](https://github.com/SuperTux/supertux/wiki/Leveldesign#Tiles)
  7. [Language](https://github.com/SuperTux/supertux/wiki/Leveldesign#Language)
  8. [File Naming Conventions](https://github.com/SuperTux/supertux/wiki/Leveldesign#File-Naming-Conventions)
  9. [Other](https://github.com/SuperTux/supertux/wiki/Leveldesign#Other)

---

Setting
-------

The general rule when comming up with a setting is to decide on a style in advance and then only add what fits with that theme.
Avoid the temptation to think "more is better" by using nearly every enemy / background tile / secret type etc.

* Backgrounds: Generally try to stick to one visual theme per level. Pick one style of background tile and stick to it. Lots of
  scenery is good, but it should be consistent. Same goes for tilesets
* Enemies: Select a handful of enemies that best fit the level style and stick with those rather than using every enemy type
  available. Do not randomly mix enemies of all different kinds. Your Level should follow a certain theme and thus focus on enemies that
  fit that theme. For example, fire enemies should only appear in castle levels. In addition, don't just randomly place
  each and every type of snow enemy into a level - pick a few enemies that best fit into your level.

Size
----

Levels *must* be at least 25 tiles high. Any vertical scrolling sectors should be no narrower than 40 tiles in width to ensure
it displays well in every resolution setting currently supported by SuperTux.

Usually, levels in SuperTux are meant to be around 300 to 500 tiles in length. Around the middle a checkpoint must be placed
(preferably near harder section if possible). Levels that are more complex may be shorter to compensate the overall playtime
which is meant to be about 90 seconds per level.

An exception to this rule are either hidden bonus levels or levels that feature a theme only present in this one level (e.g.
The Crystal Mine). Those types of level are much longer featuring more complex puzzles, challenges etc. and take much longer
to beat. Additionally, more checkpoints must be placed! The total amount varies per level.

---

Difficulty
----------

The goal of *SuperTux* is to be fun, not to be hard. So the goal is to make *fun* levels, not to make them *challenging* just
for the sake of it. Remember that a player will get frustrated and annoyed if he dies more than small number of times in a level
and also keep in mind that a player will see the level for the first time when he plays it.

*Tip: If you are in doubt if a level is getting too hard, change the style of play to something that is unfamiliar to
you, invert left/right controls, play with the left hand, play only as small Tux or anything like that. If you can still
beat the level without problems and without dying, it likely is easy enough. If not, then it is likely too hard.*

---

Enemies
-------

Be mindful of how enemies react to the environment when deciding where to put them. For example, Mr. Snowball will always fall
off ledges while Mrs. Snowball will always turn around at a ledge, thus Mr. Snowball is a poor choice in a sky level where Mrs.
Snowball is much more appropriate. Enemies should not fall off the screen before players have a chance to engage them, and it
should be possible to fill out the *badguys killed* stat.

Finally avoid placing enemies where they will reach a spawn- or resetpoint. This is most important, as there should be ample time
for a player to see and assess the level before being forced to act. Levels that switch back-and-forth between sectors are also
prone to having an enemy wander into a spawn point resulting in Tux being hurt immediately after spawning - this is bad and makes
players sad.

Tiles
-----

Don't use tiles in the background that were built for the foreground. Use only special background tiles in the background.
In general, don't ever mix tilesets. Clearly distinguish between the layers - players should be able to see immediately where
they can safely walk and what is foreground and background. Secret areas can violate this.

![Styleguide on Tiles](images/Styleguide-tiles.png "Styleguide on Tiles")

When creating slopes, make sure that they are smooth and don't make sudden jumps in inclination. Note when using slopes that
some combinations are ill-fitting; ignore these artifacts as they are graphics problems, not level problems. You may want to
avoid the use of steep slopes for the time being, at least until the slope collision physics are improved some more. Along
those same lines, the placement of slopes directly next to a vertical wall currently produces some bizarre behavior and
should be avoided until the mechanics are improved.

![Styleguide on Slopes](images/Styleguide-slope.png "Styleguide on Slopes")

---

Language
--------

* All types of text should be written in American English.
* Test your level thoroughly and let friends play it. Make sure every part isn't too hard, every jump is as far as you want it
  to be, nothing can be accessed easier then you intended, and all your secrets work.

File Naming Conventions
-----------------------

When saving the level file, stick with the convention used for the worldmap. For example, *Icy Island* levels are named like this:
```example_level.stl``` The level extension is *.stl*, if you forget the extension, the level will not be recognized. If you need
an example of naming convention, look at the ```data/levels/world1``` directory.

Note: having spaces in the level names makes command-line manipulation of files for development atrocious. Use underscores in the
level names instead.

However, it's not critical that custom levels necessarily follow the same naming convention. It is nevertheless best to stick with
a non-cryptic naming scheme where it is obvious which file is for which level.

---

Sectors
-------

When making a level, use floors and ceilings where appropriate. Basic rule of thumb is that your environment should visually
make sense. For example:

- Overground areas should have a floor and no ceiling.
- Underground and interior areas should have both a floor and ceiling.
- Sky areas should have neither a floor nor ceiling.

Transitions between sectors should also make sense. Having Tux walk off a screen of overground ice and suddenly appearing in
the middle of a castle is confusing. Also one-way sector transitions should only be used where it is logical, such as dropping
down a hole. Doors should be two-way. Sectors designed to be next to each other should be able to be visually connected.

![How NOT bind sectors together](images/Nsb.png "How NOT to bind sectors together")

---

Other
-----

SuperTux is meant to be a fair and fun game, so don't create unfair configurations, like a spike on the roof as well as one on
the ground, that require way too much precision or luck and just aren't fun to play.

![How NOT to design levels](images/Howtonotdesignlevels.jpg "How NOT to design levels")

![More things to avoid](images/Hallofshame.jpg "More things to avoid")

### Other things to avoid:

1. Creating paths that are only two tiles high. Make things high
   enough that SuperTux can jump.
2. Don't create jumps that require pixel perfect precision unless it
   is for a special secret area.
3. Don't use invisible tiles for normal gameplay.
4. Keep the number of enemies that are on the screen at once small,
   it shouldn't be more then three for most cases.
5. Do not overuse switches and doors: SuperTux isn't an adventure
   game, it's a jump'n run, so make the level straightforward and
   easy to understand.
6. Avoid creating large monotonous spaces; players get tired of
   running around a huge level.
7. Try to limit the use of reset points; if you can get away with
   none whatsoever, do so.
8. Don't allow dead ends or impossible levels; either the player
   dies, or there's still a way to solve it. (Allowing the player to
   suicide from a trap works as well) Test your level thoroughly to
   find possible paths you missed before.
9. Avoid too hard or too easy levels. Too easy levels get boring very
   quickly while too hard ones can be frustrating. Levels you built
   often appear a lot easier for yourself, so be sure to let other
   people test them.
10. Secret areas should be well-hidden and not be visible on first
    sight, but can still have a visual cue that they are there. Use
    your imagination to think of new ways to create secrets - some of
    the above rules can be broken for that purpose, but be careful!
11. Avoid impossible-to-reach coins, powerups, areas, and badguys.
    Collecting everything or reaching everywhere in a level is often
    important to players. However, difficulty can be just short of
    impossible - requiring frame-by-frame accuracy is fine. (So long
    as you provide a demo to prove that it is in fact possible) This
    only applies to bonus items - players should be able to complete
    the level minus some items with only moderate difficulty.
12. Avoid using any water. Swimming and water physics have not been
    finalized, so any current water behavior is unreliable.
13. Avoid using very steep slopes or placing slopes next to vertical
    walls, the collision physics is still a bit off.
14. Don't overuse “new” things (enemies, objects, tiles): Use them
    when and where they make sense. Don't use them just because they
    are new.
15. Change gravity only when it has sense. Don't change it, when you
    want only Tux jumping higher/lower.
16. Don't mix tilesets! There shouldn't be any ice or castle tiles in a forest level,
    unless there is an obvious reason (like transition into another area).
17. Clearly distinguish between the layers - players should be able to see immediately
    where they can safely walk and what is foreground and background. Avoid placing
    bonus items (coins, boxes) in the background.
18. Be careful not to create dead ends. Test your level thoroughly to find possible
    paths you might have missed before.
19. Use everything the engine offers - but don't place it all in a single level!
20. Avoid large amounts of objects and badguys on the screen at once as it greatly
    decreases playability. Also, your level might not be playable on slower machines
    anymore.
21. Find the right difficulty! Too easy levels get boring very quickly while too hard
    ones can be frustrating. Levels you built often appear a lot easier for yourself,
    so be sure to let other people test them.
22. Don't make your level too short or too long - good size largely depends on the
    level's overall design, so there's no general "good" value. In longer levels,
    make sure there are enough reset points, so players won't have to repeat large
    portions of the level.
23. Secret areas should be well-hidden and not be visible on first sight. Use your
    imagination to think of new ways to create secrets - some of the above rules can
    be broken for that purpose, but be careful!
24. Members of the Crusher-family (Ice-, Rock- etc.) should be able to reach their
    original position and shouldn't get stuck anywhere in the middle when rising.

### General

* Beginning Safehaven: Give the player a safe space to start the beginning of each level. If a player dies less than 5 seconds after
  starting, they're more likely to quit.
* Ending Safehaven: Try to avoid putting enemies right near the exit door. Dying right at the end of a level is frustrating!
* Even Difficulty: Try to aim for a fairly even difficulty throughout level. If you want an extra difficult part, make it a sub level,
  connected by warps.
* Bonus Independent: Hidden secrets and bonuses are good, just don't generally make a level dependent on them to avoid frustration.
  A player who missed the bonus should still be able to get through (see Always Winnable below).
* Beginner Friendly: Avoid essential objectives that require very high or long jumps. Just because you can make them, doesn't mean
  everyone else wants to.
* Always Winnable: Avoid making levels potentially unwinnable if a player does something wrong. If an item is essential, it should
  come out infinitely; if a player falls off a platform, it should return; if a player walks past something important, they should
  be able to get back there.
* Indicate Direction If the way forward is not obvious, clues should be given to encourage exploration. If a player is required to
  fall off a ledge to an area below the current camera position, a visual clue should be given that it is safe, like some coins in
  the shape of an arrow.
* Off Path: Encourage exploration away from the central path with non essential bonuses.
* Enemy Visibility: Take care when using Front Passive objects to ensure they never completely cover any enemies. If you want a
  section where Tux appears behind the scenery, don't put any enemies in it.
* Easy for Kids: Use the Textbox only if necessary as a player may have a limited knowledge of the English language or even none
  at all.
* Consistently Solid: It should be obvious which parts are solid and which parts are decoration, otherwise it's very frustrating.
* Minimal Space: Always leave some free space vertically in small corridors for big Tux and never require to be small Tux to
  reach an Area. 

### Optional

* Difficulty Filler: Look at what levels exist and try to fill in the "difficulty gaps" with yours. Often this may mean creating
  easier levels.
* Clear Direction: The player should always have a clear idea of which way to go and what to do, the challenge should be in doing
  it. This is called the central path.
* Stable Only: Try and show off new features, but only ones that are in the latest stable version.
* Learning First: Make sure that there is an easy level that encourages learning any new skill safely before challenging players
  with a level where they die if they do not use that skill successfully.
* Bonus Clues: Use small clues to hint at hidden secrets (e.g. a single coin otherwise unreachable). Should be visible if player
  is paying attention but not obvious.
* Jump Backgrounds: Make sure to use background graphics wherever the player would be jumping. Without backgrounds it can be hard
  to judge your speed and position. 

### Hiding Bonuses And Secrets

Enemy Assisted:

* Distance Bounce: Bounce on an enemy to reach a distant, normally unreachable platform
* Deadly Enemy: Stand / run on an enemy that normally hurts you (e.g. Ice Crusher)
* Enemy Breakout: Enemies break open new areas (e.g. Mr. Iceblock breaks wooden crate)

Bonus/Powerup Assisted:

* Fire Flower: Throw fireball at meltbox to allow access to a new area.
* Invincibility: Stars lets the player run through obstacles that would normally kill them.
* Hidden Block: Activating an invisible bonus block is required to reach a high up area.

Landscape Based:

* Level warp: Hidden door leads to hidden areas or otherwise not accessible parts of a level.
* Non-Deadly Fall: Fall somewhere that looks deadly but revels a secret / area.
* Partially obscured: Secrets or entrances to secret areas can be partially hidden behind background objects.
* Moving Platform: Moving platforms that the player only sees if they do something unusual e.g. if they just run through an area
  they never see the platform but if he waits, it moves onscreen. 
* Skillful Maneuver: Secret is visible, but requires an unusually skillful jump / maneuver to get. 
