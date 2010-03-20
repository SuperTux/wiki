{{Navbox Milestone 2 Design Document}}
= Actions =

The major change in the basic actions will be making running automatic. Running will automatically happen when you have walked continuously into a certain direction and will be different by a new animation. The acceleration phase will be long enough to be able to make walking-jumps. The jump height should be similar to what it is now with different height for run and jump. The current implementation of having a walk-key and [[Milestone 1|Milestone-1]]-style running by default is ''not'' the intended final behavior.
:What means "current" here? Which [[SVN]] revision are you referring to? --[[User:Octo|octo]] 08:38, 6 March 2010 (UTC)

Rationale: The run key is overlooked by many people making the game extremely frustrating and annoying for them, since it isn't obvious that there is one, the tutorial situation in the form of a high wall in Milestone1 didn't really fix the problem, since we got still plenty of questions about the situation. It also serves little purpose since more experienced players will basically always press it down, i.e. almost nobody actually walks through the game on purpose.

== Jumping ==

When standing or walking, [[Tux]] can jump ''four tiles'' high. When running or using the [[backflip]] jump, ''Tux'' can jump ''five tiles'' high.
: ''(This if from the top of my head. Please correct if this is wrong. --[[User:Octo|octo]] 08:33, 6 March 2010 (UTC))''

'''FIXME:'''
* How high, how is it influenced by running?
* How far can Tux jump, i.e. what is the widest "normal" gap width that should occur in levels?

== Running ==

Walking and running velocity and acceleration are defined in {{SvnFile|src/object/player.cpp}}. Currently those values are:

{| class="wikitable" border="1"
! Name
! Value
! Description
|-
| <code>WALK_ACCELERATION_X</code>
| 300
| acceleration in horizontal direction when walking
|-
| <code>RUN_ACCELERATION_X</code>
| 400
| acceleration in horizontal direction when running
|-
| <code>MAX_WALK_XM</code>
| 230
| maximum walk velocity (pixel/s)
|-
| <code>MAX_RUN_XM</code>
| 320
| maximum horizontal climb velocity
|-
| <code>WALK_SPEED</code>
| 100
| instant velocity when tux starts to walk
|}

'''FIXME:'''
* How fast, how does it influence jump, how long is acceleration?

== Backflip ==
The backflip is a special jump which gives Tux some extra height compared to a normal jump.
<br clear="all" />

== Flapping ==
By flapping his wings Tux is able to get a short amount of additional time in the air as well as gain a tile in height.

Reasons to have it: fits the penguin, interesting gameplay mechanic, has a reference implementation in the form of Yoshi Island

Reasons to not have it: Has been tried with not so much success

Problem: Its a "now or never" game mechanic, it changes the game to much to be introduced at a later point.

'''Will be ignored for now'''

<br clear="all" />

== Butt Jump ==
[[Image:Supertux-buttjump.png|thumbnail|right|Butt Jump]]
The Butt Jump is activated by pressing down while in the air. It causes Tux to crush down on the exact spot over which he currently is. The butt jump provides additional force that allows him to crush blocks and some kind of armored enemies.
<br clear="all" />

== Blow Flyer ==
[[Image:Tux_bubble.png|thumbnail|right|Tux in Bubble Mode]]

Tux body catches a lot of hot air and thus starts to float. This action is triggered by objects in the game world and automatically terminates after some amount of time.

Can interact with wind.

'''Will be implemented later, not a high priority item'''

<br clear="all" />

== Sliding down Slopes ==

When on a slope you can press 'duck' and then slide down the slope, killing enemies in your way.

[[Category:Development]]
