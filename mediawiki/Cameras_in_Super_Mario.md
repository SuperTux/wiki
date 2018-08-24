== Super Mario World ==

=== Horizontal Movement ===

The camera seems to know 2 modes when scrolling horizontal: Left and Right scrolling mode. In both modes Mario is kept a little bit away from the middle of the screen:

[[Image:marioscroll1.jpg]]


When Mario walks into the direction opposite from the scrolling direction the camera stands still until he reaches ~65% of the screen. Then the camera makes a fast linear movement into the other camera mode.

[[Image:marioscrollchange.jpg]]

=== Vertical Movement ===

The basic rule here is that the camera tries to keep Mario in the middle vertically:

[[Image:marioscrollvert1.jpg]]


However when Mario jumps, the camera is NOT following him vertically as long as he doesn't fall deeper as the high where he started the jump. However this exception does not apply for trampoline jumps.

So normally if you jump up on some tiles, the camera moves from step to step each time Mario is on ground again.

== Yoshis Island ==

[[Image:yoshiscroll.jpg]]

=== Horizontal Movement ===

Here also exists a left and a right scroll mode. The game tries to keep Yoshi at 1/3rd of the screen. Switching between camera modes happens instantly this time as soon as Yoshi changes the direction in which he looks. The camera then starts to move linear and relatively slowly into the other direction. This move into the other direction gets faster if Yoshi actually starts moving.

Most of the time the mode is determined entirely by which direction Yoshi is facing, however there is actually a third stopped camera mode. This mode seems to be activated if a second direction change occurs before the scrolling camera has reached its final position. In other words if two direction changes are made relatively close together.

Once the camera has stopped Yoshi will be on one half of the screen. I will call this half of the screen the Yoshi side and the other half the non-Yoshi side. If Yoshi walks in the direction of the non-Yoshi side, scrolling seems to resume as soon as he reaches the 50% point. If Yoshi walks away from the non-Yoshi side I am still unclear as to when scrolling resumes. There seems to be a little bit of a buffer most of the time.

=== Vertical Movement ===

Basically the same rules as in Super Mario World apply here
