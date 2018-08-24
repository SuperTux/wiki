Some things about SuperTux, be it due to the code/content status of the development version or the design, really make my blood pressure skyrocket and my emotions go haywire against the other developers.

Some things, even though fixed in the current version, still make the hair at the back of my neck stand up.

== Bugs ==
The following SuperTux bugs I found particularly unnerving:
* Cloud walking: a '''''very''''' long time ago, one could pick up ice blocks, throw them, and so activate invisible blocks that were hidden inside clouds. Since the r~2926 version can't do this, I am stuck in every level that uses this (I'll use the infamous "A Path Through The Clouds" by Tobe Deprez and "Nolok's Party Pit" by Penguinmaster as examples), cursing the authors and editing the COPYING file to explicitly ''forbid making levels which require picking up Iceblocks''. (Everybody violating this part of the license will have to endure mkntfs destroying their system partition. Destroying data is sadistic, overwriting it with a Microsoft file system is outright brutal.)

== Catastrophic implementations ==
* ~r2928: The statistics subsystem is *really* badly implemented. I can't even understand what calls what without supplying a steady 1hl/h flow of caffeine to my brain.
