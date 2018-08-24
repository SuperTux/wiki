{{Navbox Milestone 2 Design Document}}
These guidelines should be kept for any level that appears in the main SuperTux level sequence. Any deviation should be rare and with great consideration (for example for a secret area).  Designers making custom levels intended for an [[Add-on]] or Bonus Island are free of regulations - that's what those sections are for.  However, keep in mind that if your levels violate too many of these suggestions people will likely find them not very fun.

== Setting ==

In [[Milestone 2]], will have [[Icy Island]] as game discovering area,  the island already present in [[Milestone 1]]. It has a snow and ice setting, so please use the appropriate [[tile]]s only. Most of them are in the "Snow" and "Blocks" groups in the level editor. There are numerous other tiles currently available in the editor, but they are either either not finalized (e.g. ice mountain) or not appropriate for ''Icy Island''.  In that first world, only basic elements should be found. 
It will present a revised [[Forest]], where more elaborate elements may be found. The Boss have to be designed. 
And eventually a third world (proposed to be [[Tropical_Island]]) with the Fun Pif quest. Please Note that Neither art or code is ready yet for this part, then you shall not design any level with their elements already available.

== Difficulty ==

The goal of ''SuperTux'' is to be fun, not to be hard. So the goal is to make ''fun'' levels, not to make them ''challenging''. Remember that a player will get frustrated and annoyed if he dies more than small number of times in a level and also keep in mind that a player will see the level for the first time when he plays it.

'''Tip:''' If you are in doubt if a level is getting too hard, change the style of play to something that is unfamiliar to you, invert left/right controls, play with the left hand, play only as small Tux or anything like that. If you can still beat the level without problems and without dying, it likely is easy enough. If not, then it is likely too hard.

== Enemies ==

Do not randomly mix enemies of all different kinds.  Level should follow a certain theme and thus focus on enemies that fit that theme.  For example, fire enemies should only appear in castle levels.  In addition, don't just randomly place each and every type of snow enemy into a level- pick a few enemies that best fit into your level.

Be mindful of how enemies react to the environment when deciding where to put them.  For example, snowball will always fall off ledges while smartball will always turn around at a ledge, thus snowball is a poor choice in a sky level where smarball is much more appropriate.  Enemies should not fall off the screen before players have a chance to engage them, and it should be possible to fill out the ''badguys killed'' stat.  Finally avoid placing enemies where they will reach a spawn point.  This is most important around the level start and reset points, as there should be ample time for a player to see and assess the level before being forced to act.  Levels that switch back-and-forth between sectors are also prone to having an enemy wander into a spawn point resulting in Tux being hurt immediately after spawning- this is bad and makes players sad.

== Slopes ==

When creating slopes, make sure that they are smooth and don't make sudden jumps in inclination.  Note when using slopes that some combinations are ill-fitting; ignore these artifacts as they are graphics problems, not level problems.  You may want to avoid the use of steep slopes for the time being, at least until the slope collision physics are improved some more.  Along those same lines, the placement of slopes directly next to a vertical wall currently produces some bizarre behavior and should be avoided until the mechanics are improved.

[[Image:Styleguide_slope.png|Styleguide Slope]]

== Tiles ==

Don't use tiles in the background that were built for the foreground. Use only special background tiles in the background. In general, don't ever mix tilesets. Clearly distinguish between the layers - players should be able to see immediately where they can safely walk and what is foreground and background. Secret areas can violate this.

[[Image:Styleguide_tiles.png|Styleguide Tiles]]

== Size ==

Levels ''must'' be at least 25 tiles high, and using at least 32 tiles is recommended. Levels should be between 250 and 350 tiles long.<br />(A couple of levels in [[Icy Island]] are over 500&nbsp;tiles long – newer levels should not be this long and it's possible we'll split up those long levels in the future.)<br />Any vertical scrolling sector should be no narrower than 40 tiles wide to ensure it displays well in every resolution setting currently supported by SuperTux.

== File Naming Conventions ==

When saving the level file, stick with the convention used for the worldmap.  For example, ''Icy Island'' levels are named like this:  ''02 - example level.stl'' where the number (02 in the example) showing what order you play the levels, and the level name are separated by a hyphen.  The level extension is ''.stl'', if you forget the extension, the level will not be recognized.  If you need an example of naming convention, look at the data/levels/world1 directory.  If level order does not matter, or is unknown, the number and hyphen can be omitted.

Note: having spaces in the level names makes command-line manipulation of files for development atrocious, there should probably be a discussion about changing the convention to use underscores in the level names instead.

However, it's not critical that custom levels necessarily follow the same naming convention.  It is nevertheless best to stick with a non-cryptic naming scheme where it is obvious which file is for which level.

== Sectors ==

[[Image:nsb.png|thumbnail|right|How NOT bind sectors together]]
When making a level, use floors and ceilings where appropriate. Basic rule of thumb is that your environment should visually make sense.  For example:
* Overground areas should have a floor and no ceiling.
* Underground/cave and interior areas should have both a floor and a ceiling.
* Sky area should have neither a floor nor ceiling.

Transitions between sectors should also make sense.  Having Tux walk off a screen of overground ice and suddenly appearing in the middle of a castle is confusing.  Also one-way sector transitions should only be used where it is logical, such as dropping down a hole.  Doors should be two-way.  Sectors designed to be next to each other should be able to be visually connected.

== Other ==

SuperTux is meant to be a fair and fun game, so don't create unfair configurations, like a spike on the roof as well as one on the ground, that require way too much precision or luck and just aren't fun to play.

[[Image:Howtonotdesignlevels.jpg|right|thumb|200px|How '''NOT''' to design levels]]
[[Image:Hallofshame.jpg|right|thumb|200px|More things to avoid]]

Other things to avoid:

# Creating paths that are only two tiles high, make things high enough that SuperTux can jump.
# Don't create jumps that require pixel perfect precision unless it is for a special secret area.
# Don't use invisible tiles for normal gameplay.
# Keep the number of enemies that are on the screen at once small, it shouldn't be more then three for most cases.
# Do not overuse switches and doors: SuperTux isn't an adventure game, it's a jump'n run, so make the level straightforward and easy to understand.
# Avoid creating large monotonous spaces; players get tired of running around a huge level.
# Try to limit the use of reset points; if you can get away with none whatsoever, do so.
# Don't allow dead ends or impossible levels; either the player dies, or there's still a way to solve it. (Allowing the player to suicide from a trap works as well) Test your level thoroughly to find possible paths you missed before.
# Avoid too hard or too easy levels. Too easy levels get boring very quickly while too hard ones can be frustrating. Levels you built often appear a lot easier for yourself, so be sure to let other people test them.
# Secret areas should be well-hidden and not be visible on first sight, but can still have a visual cue that they are there. Use your imagination to think of new ways to create secrets - some of the above rules can be broken for that purpose, but be careful!
# Avoid impossible-to-reach coins, powerups, areas, and badguys. Collecting everything or reaching everywhere in a level is often important to players. However, difficulty can be just short of impossible - requiring frame-by-frame accuracy is fine. (So long as you provide a demo to prove that it is in fact possible) This only applies to bonus items - players should be able to complete the level minus some items with only moderate difficulty.
# Avoid using any water. Swimming and water physics have not been finalized, so any current water behavior is unreliable.
# Avoid using very steep slopes or placing slopes next to vertical walls, the collision physics is still a bit off.
# Don't overuse "new" things (enemies, objects, tiles): Use them when and where they make sense. Don't use them just because they are new.
# Change gravity only when it has sense. Don't change it, when you want only Tux jumping higher/lower.

<br clear="all"/>

== External Links ==
* Secret Maryo Chronicles has some at http://secretmaryo.org/wiki/index.php?title=Level_Design_Guidelines

[[Category:Development]]
