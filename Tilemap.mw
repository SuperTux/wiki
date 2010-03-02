'''Tilemaps''' consist of all of the ground, spikes, lava, clouds, etc. that do not move and do not interact ''actively'' with the player. Each tilemap consists of one or more [[tiles]], which each contain several attributes specified in the ''[[tileset]]''.

Tilemaps can be either ''solid'' or ''non-solid''. The player can only interact with ''solid'' tilemaps (i.e. they are used for collision detection) but not with ''non-solid'' tilemaps. Non-solid tilemaps are usually used as foreground and background layers.

Multiple tilemaps of each kind may be specified.  You can think of a ''tilemap'' as a ''layer'' of “blocks”. Each layer has an associated ''z-position'' where smaller values mean further back, larger values mean further in front.
:{| border="1"
! z-position
! Use
|-
| -100
| Default background layer
|-
| 0
| Default interactive layer
|-
| 50
| <code>LAYER_OBJECTS</code> (default [[Game objects|object]] layer)
|-
| 51
| [[Tux]], bonus blocks
|-
| 100
| Default foreground layer
|}

Tilemaps are also [[Scripting reference|scriptable]] if given a (unique) name, see [[ScriptingTilemap]].

Tilemaps may also be given a [[ScriptingPath|path]], which they will follow once scripted to do so.

Note that [[infoblock]]s, [[unstable tile]]s, [[bonus block]]s, invisible blocks that can be activated, coins, and wooden bricks are not actually part of the tilemap; after the level is parsed, the tiles with the ID's or attributes representing those objects are replaced with the objects themselves and the tiles changed to empty.

[[Category:Game Object]]
