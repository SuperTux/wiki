This is a list of potential bugs in SuperTux that I have noticed but have not taken the time to properly report.  I'm publishing it here for the sake of open development.  Others are welcome to add comments.  These descriptions are intentionally terse (that's the purpose of this page compared to the bug tracker); if you are not sure what I mean, please ask.

See also the patches in the "for-upstream" branch of https://mattmccutchen.net/private/supertux.git/ , if any.

* 2009-12-28: Coins in 1-tile gaps are collected inconsistently in Boney.M Mega Mix.  Maybe another issue with floating point error vs. x coordinate?

* 2010-01-02: After setting magnification to 125% and entering and aborting a level,  options menu incorrectly shows magnification as auto.
** OptionsMenu constructor is not selecting existing values.  (Resolution too?)

* 2010-01-11: Key levels should do statistics just like other levels, and maybe invincibility too to be safe.

* 2010-01-11: Integer screen coordinates
** Fixed in [[Template:Revision|6568]]. --[[User:Octo|octo]] 10:01, 7 March 2010 (UTC)
*** What I meant was "FIXME Force integer translation for all graphics, not just tilemaps" in src/object/tilemap.cpp . [[User:Mattmccutchen|Mattmccutchen]] 00:27, 17 March 2010 (UTC)

* 2010-01-11: What is the aspect ratio control supposed to do?  Values other than "auto" produce a display ridiculously stretched horizontally.  I guess we want 2880:900.  But why, when the window is smaller???

* 2010-01-21: Everything in the collision detection torture test
** The horizontal crush in gaps of width between 16 and 24 can happen in the tree stump in "Under Construction".  Easy to reproduce in 0.3.1, harder in the trunk where the moving tilemaps carry Tux along ([[Template:bug|269]] fixed).

* 2010-01-21: Shrink tilemaps to size

* 2010-01-22: Editor: Bad handling of dithered editor-images when zoomed out.  Need to average.

* 2010-01-22: Memory leaks...

* 2010-01-23: Position of "Best Level Statistics" in worldmap does not update correctly on window resize.

* 2010-01-24: Not sure I like the new behavior where ice blocks and snails die immediately when stomped with invincibility.

* 2010-01-24: "Short Visit to El Castillo": Upper dart trap is not operating.  Intentional?

* 2010-01-24: Editor: Clicking eye field of unfocused layer in the list cycles the visibility right away for a visible tilemap, not otherwise.  Inconsistent.

* 2010-01-27: Badguys getting stuck on slopes against walls in the second sector of "A Village in the Forest".

* 2010-01-28: Big/small Tux seems to affect position of worldmap character but not size.  That's weird.

* 2010-01-28: jump_early_apex happening during buttjumps.

* 2010-01-28: In "Find the Bigger Fish", under the pipe in the lower sector, why does the wind appear to make my low jumps /lower/?

* 2010-01-31: Editor: Typing ".3" in path node time, 0 is inserted automatically.  Distracting and mispositions cursor.  Validate on blur?

* 2010-01-31: Cannot have objects controlled by fix_old_tiles on a moving tilemap.

* 2010-02-09: In the beginning of one of the "moo" levels, a snowball's sprite is not set correctly when it is dying.

* 2010-02-09: In some forest levels, a zeekling killed exactly at ground level will sit in place for a few seconds with the original sprite.  Seen twice, may be hard to reproduce.

* 2010-02-09: "Village in the Forest": When pulling the switch, the sleeping spiky disappears as the camera pans.  Maybe a deactivation issue.

* 2010-02-09: "Kneep-deep in the Depth" should not have an end sequence trigger, for consistency with the other key levels.

* 2010-02-09: "Treasure in the skies": Climbable area extends into thin air.

* 2010-02-15: Possible to lose while winning:
** (2010-02-15 05:10:59 UTC) Forty-Two: I notice that in Light and Magic, if you reach the finish while holding a lantern, you drop it and it kills you (you lose 25 coins) although you also finish the level
** Can fall off the screen (only in pathological levels)

* 2010-02-20: Can jump over some of the exits:
** Up and Down
** Tux the Builder
** Others?

* 2010-02-24: If I hold a camera pan key (e.g., delete) when leaving a sector, the camera pan persists when re-entering the sector even if I am not holding the key.

* 2010-03-01: Hilarious glitch seen in octo's "Yoshi's Island 2".  When we change sectors while holding an ice block, the player in the first sector is still holding the ice block.  If we now return to the first sector in a different place, the ice block flies into Tux's arms.  Tracking bug for "too much sector-specific state"?

* 2010-03-01: Need to clear backflipping when starting to climb.

* 2010-03-02: Do something about missing badguys during cutscenes due to activation. [http://lists.lethargik.org/pipermail/supertux-devel-lethargik.org/2010-February/002768.html]

* 2010-03-02: While camera is in autoscroll mode, badguy activation should be based on camera instead of Tux.

* 2010-03-02: Remove hacks around camera bounding in "Village in the Forest".

* 2010-03-07: Infoblock popup is in front of pause shading, should be behind.

* 2010-03-16: Incubator level "The not so long way" uses fish in translucent water.  One can see the fish appear and disappear.  That looks bad.

* 2010-03-16: In lower-left corner of incubator level "Crystal Cataclysm", Tux sticks to the slopes in the ceiling.  The slopes may be miscoded.

* 2010-03-16: Bug tracker: There should be a "View Revisions" for deleted notes too, at least for administrators.

* 2010-03-16: CMakeLists.txt might as well use GLOB_RECURSE to specify the source files.

* 2010-03-16: [http://supertux.lethargik.org/viewvc/viewvc.cgi/trunk/supertux/ The viewvc interface] says "No admin address has been configured".

* 2010-04-01: When a sliding ice block slows down and then starts walking, it remains vertically lower than a walking ice block should be.

* 2010-04-01: "Down the Rabbit Hole": Snowshots don't belong in the forest world.  Why not restore the rockets?  The implementation was just fine.

* 2010-04-01: "Down the Rabbit Hole": Cannon gets deactivated.  Avoid that somehow.  A decent heuristic would be to keep a dispenser active as long as any of the badguys it produced is active.

* 2010-04-01: It's confusing if an ice block sliding on a long floor gets deactivated and doesn't bounce back by itself.  To avoid this, deactivate an ice block only if its latest bounce x-interval is far from the screen.

* 2010-04-02: The player should not squish badguys while the safe_timer is running.  That would improve the balance of the game.

* 2010-04-02: The silent period at the beginning of data/music/invincible.ogg is a hack that shows up if the user pauses while invincible (so the music loops), goes through a door (so the music restarts; example in "Crumbling Path"), or even runs "invincible()" in the console.  Remove the silent period, and instead don't start data/music/invincible.ogg until after data/sounds/invincible_start.ogg is finished.

* 2010-04-02: Allowing buttjump to break boxes and activate bonus blocks makes some parts of levels ''way'' too easy.  E.g., the fish puzzle in "Area 42" is trivialized.

* 2010-04-02: Falling ice blocks can nest, at the beginning of "End of the Tunnel".

* 2010-04-13: Specifying a worldmap on the command line does not work: it incurs "Insecure filename" errors from PhysFS.

* 2010-04-14: Review [http://cvs.fedoraproject.org/viewvc/rpms/supertux/devel/ Fedora's changes].
** Use the system Squirrel
** Desktop file

* 2010-04-14: Fedora nipped the 2 from supertux2 until the latest build, and I actually liked that.  The original reason for the 2 was to have separate configuration from milestone 1 ([[Template:revision|3968]]), but do we still care?  [[Template:bug|535]] might help.
