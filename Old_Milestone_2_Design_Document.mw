{{Notice Milestone 3}}
:''This page described the features that once were planned for ''Milestone&nbsp;2''. However, implementing all this turned out to be impractical. In order to clean up the codebase, much of the features originally described here have been moved to [[Milestone 3 Design Document]]. The current goals for ''Milestone 2'' are documented in [[Milestone 2 Design Document]].''

= About This Page =
This document is work in progress; when finished, its purpose is to provide a final design paper for SuperTux Milestone 2. General ideas go into their respective areas on the [[game design]] pages. Please '''do not''' change anything on this page that hasn't been discussed and approved by the developers!

= [[Milestone 1 Analysis]] =

Milestone 2 will try to correct many things that were considered "bad" while retaining most things that were considered considered "good" in [[Milestone 1]]. See [[Milestone 1 Analysis]] for a detailed analysis.

= [[Game Engine]] =

SuperTux Milestone 2 will use OpenGL to draw the graphics. The features of this library will be used to enhance gameplay and visual content in several ways:

* Create dark levels that are illuminated only in certain areas (for example around Tux, lamps, lava, certain badguys etc.), see [[Lighting]]
* Colored blocks that are only visible when in the range of a light source with the same color, see [[Lighting]]
* Add atmosphere to levels using different lighting
* Zooming (in cutscenes)
* Make foreground translucent when Tux walks behind it

= New Design Document =
Most of this page has been moved to Milestone 3. See [[Milestone 2 Design Document]] for details on the current Milestone 2 plan.

= [[World 2]] =

After finishing Antarctica by beating the worlds boss, a cutscene, replacing the currently displayed text, will be shown. (For a detailed description of cutscenes, see section "Story".) Tux will then advance to [[World 2]], the forest island. Its worldmap will be built using the same, possibly enhanced, format that Antarctica uses. The worldmap will be designed as follows: The island consists of four sections. A light friendly looking forest where Tux starts his journey, a ghost forest section, and a transition between them; in the center of the island, surrounded by the ghost forest is the world's castle, called Dark Forest Keep. Levels will be spread throughout the whole island, distributed as follows: 50 per cent of the levels are inside the light section, 30 per cent inside the haunted section, with one or two levels inside the transition area. The remaining 20 per cent will take place inside the castle.

The primary goal of the forest world is to beat the boss at the final castle level. In order to get there, Tux needs to collect five keys scattered throughout the island which will open the door to the castle. Thus, the paths on the worldmap should lead into five dead-ends that hold the levels in which the key can be found. The path to the castle is accessible from after the first level. However, when Tux tries to enter the castle, he can't unlock the door without all five keys.

= Levels =
Unlike Antarctica, forest levels can have variable sizes, both horizontally and vertically. In addition to that, levels can have a number of different sectors of variable size, connected by doors, portals, script events and spawn points. Due to this variability, there is no recommended level size anymore; the "perfect size" of a level solely depends on its design.
The three different themes on forest world -light forest, ghost forest and castle- are each represented by a matching tileset. All forest levels use one of these tilesets; a general rule should be not to mix them.

Levels have the ability to autoscroll in all four directions. There is no fixed ending sequence like in Antarctica anymore; level designers can use scripts to determine the ending conditions of a level. The most common level endings will be:

* reaching a goal area somewhere in the level,
* picking up a special item (for example, one of the five keys),
* killing a certain badguy or boss.

Milestone 2 levels will try to focus on a certain theme to make each level unique in gameplay. Level events can be automated using scripts in order to create in-game cutscenes.

== Worldmap ==
Other than on the Antarctica worldmap, the levels should be placed on different paths, so that there is always a choice between at least two levels. Exceptions to this (i.e. levels with no alternative to choose from) are

* the first level,
* levels on one path that are in some way connected by story,
* the (first) transition to the ghost forest section, and
* the castle levels.

== Light Forest ==
Levels:
* Theme introduction and tutorial on new abilities
* Moving platforms
* Trampolines
* Autoscrolling
* Falling rocks
* Portable boxes, stacking
* Vertically flipped level

== Ghost Forest ==

Intro: Nolok is using some heavy magic in the castle, this will have an effect to the levels around the castle. The forest there turned into a ghost forest. Stuff will look spooky and surreal things can happen.

Gameplay: You can think of the ghost world as a 2nd dimension next to the forest. There will be some game elements that allow a transition between these 2 dimensions (or force that transition). We will also start playing with colors and light effects in the ghost forest parts. Transitions between the dimensions can happen by:

* actively walking through a portal,
* being beamed into the other world without warning, using invisible triggers, or
* being caught by special badguys (willowisp) that have the ability to carry you over to the other world.

Levels:
* Light forest to ghost forest transition, theme introduction (two levels)
* Cannons and dispensers
* Spiders

== Castle ==
* Main Hall: Theme introduction
* First Floor: Labyrinth, light switch blocks
* Tower: Rising Lava
* Attic: Boss battle

= [[Actions]] =

== Powerups ==
In Milestone 2 in general, the favourite way of enhancing Tux' abilities will be through level objects that temporarily grant Tux special abilities (see Level Objects section for more details), rather than permanent powerups like fire and ice shots. Those will still be there, but they'll remain relatively weak, so they don't get in the way of level design. An ice shot will be implemented, the fire shot's behaviour will be improved [need more detail here]. The fire shot gets a new ability to burn through specific tiles to reveal paths. These paths, however, should contain only bonus items like coins; it must be possible to finish a level without needing the fire powerup.
* Ice shot
* Fire melts ice, ice freezes water
* Super Buttjump (timed)
General idea: More level objects than powerups, they can be placed where they are needed.
Powers like fire must not get in the way of level design

== Permanent Abilities (for Big Tux) ==
* Butt Jump
* Backflip

= Level Objects =
* Coin - collect 100 coins to get an extra life.
* Bonus Block - contains powerups.
* Message Box - a special bonus block that contains a message. Implemented as telephones.
* Ambient Sound - plays a looping sound effect inside the defined range.
* Timer - adds a time limit to a level.
* Particle System - adds background visual effects like clouds, snow, and rain.
* Door - respawns Tux at a defined spawn point when activated.
* Spawn Point - defines the place where Tux appears after walking through a door.
* Bell - When touched, Tux respawns at the bell after dying.
* Trampoline - Tux can jump on them for a very high jump; can be carried around.
* Falling Block - solid block that falls down shortly after being touched.
* Powerup - an object that represents a powerup, such as egg, flower, star, extra life, or potion.
* Message Trigger - display a message as soon as Tux enters their range. Used to mark secret areas.
* Sequence Trigger - executes a script on contact.
* Moving Platform - [still needs to be defined.]
* Carryable Block - Blocks that can be carried around and stacked.
* Bubble Dispenser - Releases bubbles that Tux can use to travel upwards.
* Ice Cube/Straw Block - a block that can be destroyed by the fire shot. Appearance depends on the world it's used in.

= [[Badguys]] =
For detailed info, see the [[Badguys]] page. The following is a list of new badguys that will definitely be in Milestone 2:
* Poison Ivy
* Mr. Tree
* Mr. Rocket
* Dispenser
* Zeekling
* Kugelblitz
* Snail
* Spider

= [[Bosses]] =
* Antarctica: Yeti
* Forest: Ghost

= [[Story]]/[[Cutscenes]] =
[no final decisions yet; see the [[Cutscene Storyboard]] for ideas.]

= (Sketches) =
Here are some sketches of things explained above.

[[Image:Worldmap sketch.png]]

[[Category:Design]]
[[Category:Outdated]]
