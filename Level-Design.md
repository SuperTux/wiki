These guidelines should be kept for any level that appears on the official worldmaps. Designers contributing levels to the
Contrib sections are free of regulations - that's what those sections are for. However, keep in mind that if your levels
violate too many of these suggestions people will likely find them not very fun.

SuperTux is meant to be a fair and fun game, so in order to maintain a certain level of playability, official levels should
be designed with these rules in mind:

# Contents
  1. [Setting](https://github.com/SuperTux/supertux/wiki/Level-Design#Setting)
  2. [Size](https://github.com/SuperTux/supertux/wiki/Level-Design#Size)
  3. [Difficulty](https://github.com/SuperTux/supertux/wiki/Level-Design#Difficulty)
  4. [Enemies And Obstacles](https://github.com/SuperTux/supertux/wiki/Level-Design#Enemies-And-Obstacles)
  5. [Tiles And Backgrounds](https://github.com/SuperTux/supertux/wiki/Level-Design#Tiles-And-Backgrounds)
  6. [Sectors And Trasitioning](https://github.com/SuperTux/supertux/wiki/Level-Design#Sectors-And-Transitioning)
  7. [File Naming Conventions](https://github.com/SuperTux/supertux/wiki/Level-Design#File-Naming-Conventions)
  8. [Other](https://github.com/SuperTux/supertux/wiki/Level-Design#Other)

*If you are looking for guidelines outside of level making see [Thematic Guideline](https://github.com/SuperTux/supertux/wiki/Thematic-Guideline)!*

---

Setting
-------

The general rule when comming up with a setting is to decide on a style in advance and then only add what fits with that theme.
Avoid the temptation to think "more is better" by using nearly every enemy / background tile / secret type etc.

* Generally try to stick to one visual theme per level. Pick one style of background tile and stick to it. Lots of scenery is
  good, but it should be consistent. Same goes for tilesets. Don't mix tilesets! There shouldn't be any ice or castle tiles in
  a forest level, unless there is an obvious reason (like transition into another area).
* Select a handful of enemies that best fit the level style and stick with those rather than using every enemy type available.
  Do not randomly mix enemies of all different kinds. Your Level should follow a certain theme and thus focus on enemies that
  fit that theme. For example, fire enemies should only appear in castle levels. In addition, don't just randomly place each
  and every type of snow enemy into a level - pick a few enemies that best fit into your level.

Size
----

Levels **must** be at least 25 tiles high. Any vertical scrolling sectors should be no narrower than 40 tiles in width to ensure
it displays well in every resolution setting currently supported by SuperTux.

Usually, levels in SuperTux are meant to be around 300 to 500 tiles in length. Around the middle a checkpoint must be placed
(preferably near harder section if possible). Levels that are more complex may be shorter to compensate the overall playtime
which is meant to be about 90 seconds per level.

An exception to this rule are either hidden bonus levels or levels that feature a theme only present in this one level (e.g.
The Crystal Mine). Those types of level are much longer featuring more complex puzzles, challenges etc. and take much longer
to beat. Additionally, more checkpoints must be placed! The total amount varies per level.

Difficulty
----------

The goal of SuperTux is to be fun, not to be hard. So the goal is to make *fun* levels, not to make them *challenging* just
for the sake of it. Remember that a player will get frustrated and annoyed if he dies more than small number of times in a level
and also keep in mind that a player will see the level for the first time when he plays it. Try to aim for a fairly even difficulty
throughout a level. Too easy levels get boring very quickly while too hard ones can be frustrating. Levels you built often appear a
lot easier for yourself, so be sure to let other people test them.

*Tip: If you are in doubt if a level is getting too hard, change the style of play to something that is unfamiliar to
you, invert left/right controls, play with the left hand, play only as small Tux or anything like that. If you can still
beat the level without problems and without dying, it likely is easy enough. If not, then it is likely too hard.*

---

Enemies And Obstacles
---------------------

Be mindful of how enemies react to the environment when deciding where to put them. For example, Mr. Snowball will always fall
off ledges while Mrs. Snowball will always turn around at a ledge, thus Mr. Snowball is a poor choice in a sky level where Mrs.
Snowball is much more appropriate. Enemies should not fall off the screen before players have a chance to engage them, and it
must be possible to fill out the *badguys killed* stat.

Also, avoid large amounts of objects and badguys on the screen at once as it greatly decreases playability. Also, your level
might not be playable on slower machines anymore. Keep the number of enemies that are on the screen at once small, it shouldn't
be more then three for most cases.

Don't create unfair configurations, like a spike on the roof as well as one on the ground, that require way too much precision
or luck and just aren't fun to play.

![How NOT to design levels](images/Howtonotdesignlevels.jpg "How NOT to design levels")

Finally avoid placing enemies where they will reach a spawn- or resetpoint. This is most important, as there should be ample time
for a player to see and assess the level before being forced to act. Levels that switch back-and-forth between sectors are also
prone to having an enemy wander into a spawn point resulting in Tux being hurt immediately after spawning - this is bad and makes
players sad.

![More things to avoid](images/Hallofshame.jpg "More things to avoid")

Tiles And Backgrounds
---------------------

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

Sectors And Trasitioning
------------------------

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

Other
-----

### Language

* All types of text should be written in American English.
* Test your level thoroughly and let friends play it. Make sure every part isn't too hard, every jump is as far as you want it
  to be, nothing can be accessed easier then you intended, and all your secrets work.

### Hiding Bonuses And Secrets

For Story Mode, each level must feature at least on secret area. Secret areas should be well-hidden and not be visible on first sight,
but can still have a visual cue that they are there. Use your imagination to think of new ways to create secrets - some of the above
rules can be broken for that purpose, but be careful!

Use small clues to hint at hidden secrets (e.g. a single coin otherwise unreachable). They should be visible if player is paying attention
but not obvious.

Here are some ways you could hide a bonus or secret area:

**Enemy Assisted**

* Distance Bounce: Bounce on an enemy to reach a distant, normally unreachable platform
* Deadly Enemy: Stand / run on an enemy that normally hurts you (e.g. Ice Crusher)
* Enemy Breakout: Enemies break open new areas (e.g. Mr. Iceblock breaks wooden crate)

**Object/Powerup Assisted**

* Fire Flower: Throw fireball at meltbox to allow access to a new area.
* Air Flower: Glide over long distances to reach a far off section of the level
* Invincibility: Stars lets the player run through obstacles that would normally kill them.
* Hidden Block: Activating an invisible bonus block is required to reach a high up area.
* Stacking Blocks: A high up area that be reached by stacking blocks.

**Other Methods**

* Level Warp: Hidden doors or other teleportation methods that lead to hidden areas or
  otherwise not accessible parts of a level.
* Non-Deadly Fall: Fall somewhere that looks deadly but revels a secret / area.
* Partially obscured: Secrets or entrances to secret areas can be partially hidden behind
  background objects.
* Moving Platform: Moving platforms that the player only sees if they do something unusual
  e.g. if they just run through an area they never see the platform but if he waits, it
  moves onscreen. 
* Skillful Maneuver: Secret is visible, but requires an unusually skillful jump or maneuver
  to get it. 

### Other things to consider:

* Creating paths that are only two tiles high. Make things high enough that SuperTux can jump.
* Don't create jumps that require pixel perfect precision unless it is for a special secret area. Always leave some room for error!
* Don't use invisible tiles for normal gameplay.
* Do not overuse switches and doors: SuperTux isn't an adventure game, it's a jump'n run, so make the level straightforward and
  easy to understand.
* Avoid creating large monotonous spaces; players get tired of running around a huge level.
* Don't allow dead ends or impossible levels; either the player dies, or there's still a way to solve it or return (allowing the player to
  suicide from a trap works as well). Test your level thoroughly to find possible paths you missed before.
* Avoid impossible-to-reach coins, powerups, areas, and badguys. Collecting everything or reaching everywhere in a level is often
  important to players. However, difficulty can be just short of impossible - requiring frame-by-frame accuracy is fine. (So long
  as you provide a demo to prove that it is in fact possible) This only applies to bonus items - players should be able to complete
  the level minus some items with only moderate difficulty.
* Avoid using any water. Swimming and water physics have not been finalized, so any current water behavior is unreliable.
* Don't overuse “new” things (enemies, objects, tiles): Use them when and where they make sense. Don't use them just because they
  are new. Use everything the engine offers - but don't place it all in a single level!
* Change gravity only when it has sense. Don't change it, when you want only Tux jumping higher/lower.
* Use everything the engine offers - but don't place it all in a single level!
* Members of the Crusher-family (Ice-, Rock- etc.) should be able to reach their original position and shouldn't get stuck anywhere
  in the middle when rising.
* Beginning Safehaven: Give the player a safe space to start the beginning of each level. If a player dies less than 5 seconds after
  starting, they're more likely to quit.
* Ending Safehaven: Try to avoid putting enemies right near the exit door. Dying right at the end of a level is frustrating!
* Bonus Independent: Hidden secrets and bonuses are good, just don't generally make a level dependent on them to avoid frustration.
  A player who missed the bonus should still be able to get through.
* Always Winnable: Avoid making levels potentially unwinnable if a player does something wrong. If an item is essential, it should
  come out infinitely; if a player falls off a platform, it should return; if a player walks past something important, they should
  be able to get back there.
* Beginner Friendly: When introducing a mechanic make sure to give the player a little play area to try it out before challenging
  players with a level where they die if they do not use that skill successfully.
* Clear Direction: The player should always have a clear idea of which way to go and what to do, the challenge should be in doing
  it. This is called the central path.
* If the way forward is not obvious, clues should be given to encourage exploration. If a player is required to fall off a ledge
  to an area below the current camera position, a visual clue should be given that it is safe, like some coins in
  the shape of an arrow.
* Encourage exploration away from the central path with non essential bonuses. Rewards for exploration are always nice.
* Enemy Visibility: Take care when using Front Passive objects to ensure they never completely cover any enemies. If you want a
  section where Tux appears behind the scenery, don't put any enemies in it.
* Use the Textbox only if necessary as a player may have a limited knowledge of the English language or even none at all.
* Never require to be small Tux to reach an Area.
* Do not use deadly-falls to disguise a secret unless there is an obvious hint that suggests to jump down there.
* No secret areas right above a Crusher behind the ceiling. Leave at least a gap of two tiles between the Crusher and ceiling
  as well as hints that there actually is a secret. Make sure players can tell whether or not they get crushed riding the Crusher.
