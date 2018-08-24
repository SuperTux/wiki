{{Navbox Milestone 2 Design Document}}
Obsolete things from other pages. Note however that obsolete doesn't mean its useless, sometimes things are already done while other times they just haven't been properly integrated into the Milestone 2 Design Document yet and got moved here as a result of cleanup.

For the old forest page, see [[Milestone 3 Design Document]]

For the last voice meeting see: [[SuperTux Meeting 18. August 2007]]

= Things unknown =

* Who is running backups of the Wiki and SVN repository?
* Shall we switch to GPLv3? '''Not now, but maybe later'''
<math>Insert formula here</math>

= Next Meeting Agenda (7. August 2008, 18:00 GMT) =

* supertux.info status? integrate in main page?
* GP2x updates

* music submission: BlastOffTek music pack for Supertux.rar
* badguy name cleanup
* GP2x status
* large level, establishing milestone 2 'gold standard'
* editor news
* compiled data formats
* editor gui restructure

== older stuff ==

* present newly build levels
* what to do with Badguy::freeze()?
* what to do with level flipping (suggestion: ignore it)
* Wiki & SVN backup again

= Meeting Notes =

<pre>
Code:
- engine problems blending
- monster activation should be dependent on tux position and
  not on screen position (like it is now) because it should
  be independent from aspect ratio
  (Note for level designers: Think that potentially the user
  can see the whole level in front of him)
- Code for butt jump

Objects:
- new object to place images into levels (to replace info boxes):

http://pingus.seul.org/~grumbel/tmp/md5/ca5c98b54e92b1317776c49970f2bbbe-info-boxes-done-right.png

Menu System Rework:
- Scrolling level selection list
- Buttons in menus
- Add info box below menu (with explanations)

Profile system:
- create profiles
- delete profiles
- load default profile on startup

- Restart game on language change (do not put language change menu into
the
       Pause-Options menu)

Graphics:
- running animation
- butt jump animation
- improve egg graphics, so it does not seem like a "snowball"
- graphics for the stuff in "Creatures"

Behaviour:
- Angry Iceblock: like the mario blocks (in the castles)
- Owl: unclear... Carriers objects and drops them at tux somehow, but not clear.
- Canon: like in mario: shoots left/right
- MiniBomb: accelerates, follows tux (but does not jump)
- Eater: ?

Snowmen:
- take the jogger one for fall-down snowball
- take the japanese one for the gun
- take the "normal" one for stay on platform
- take the "ninja" for following tux

Enemy Code:
- support for spawning k-children in an enemy (for spitter for example)

Mods:
- we might want to support "mods". A mod is defined in that it replaces
stuff
that is already there (instead of only adding new stuff). Undecided if
we want
it and how exactly.

Controls:
- we need to support jump with up and jump with button
- support binding for left,right,up,down. allow double up+jump config

Game mechanics:
- no costs for reset points
- Mailinglist discussion: do we want reset points?
- Remove global coin counter, coin count is only per level now  (similar to collectibles)
- Add collectibles: per level, show them in the screen while playing the level
- When you find a collectible, fade in collectible count for a short time
- In pause mode show all collectible as once

Mailing lists:
- We want a separate team mailing list.
  Proposal: create supertux-user and supertux-team. make forward
  supertux-devel mails to supertux-user. supertux-team read everyone but write
  only for people with svn access...

World1:
- levels will be changed, and reworked to make use of the new features

Yeti:
- Sequence at end of castle: Tux find Yeti, Yeti jumps out of the window and  flees
</pre>

== 2008-01-31 ==

Code:
* New Badguy "Ice Crusher", falls down to crush Tux, then rises back up. Has a platform on its top
* Remove old Cannon, Dropper graphics and use new Cannon instead. Only shoots left and right
* Butt-Jump should easily be possible. Press down in midair to make Tux stop in mid-air and drop down vertically. Current effect is just fine. Don't forget to shake the camera.

Game:
* Figure out which Russian Translation to use (contact translators).
* Build test level using snow slopes.
* Do not use Ice Flower. It's not finished yet.

Graphics:
* Fix jumping Tux animation. It has weird black marks.
* Make Tux backflip animation smoother.
* New tileset for above-ground levels.
* New decorative tiles. Ice cracks, snowmen, cavemen, areas with more transparency, ...
* Frozen tree.

Misc:
* The forum of supertux.info is currently broken or unmaintained. Should we shut down the server? Contact maintainer.
* Sounds for Ice Crusher, Flying Snowball, Snowball splashing against wall. Sound of rockets exploding is too loud.
