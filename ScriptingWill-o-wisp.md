Summary
-------

Will-o-Wisps, when given a name (and perhaps a [path](ScriptingPath "wikilink") too), become scriptable, much like a [platform](ScriptingPlatform "wikilink") or [tilemap](ScriptingTilemap "wikilink").

Methods
-------

Method                    | Explanation
--------------------------|----------------------------------------------------
`goto_node(int node_no)`  | Move willowisp to given node.
`start_moving()`          | Start following the path.
`stop_moving()`           | Stop following the path.
`set_state(string state)` | Set the willowisp state to one of the below values.

States
------

- stopped: willowisp doesn't move
- idle: willowisp stops tracking Tux if he is distant enough 
- move\_path: willowisp moves along the path (call `goto_node`)
- move\_path\_track: willowisp moves along path but catches Tux when he is near
- normal: “normal” mode starts tracking Tux when he is near enough
- vanish: willowisp vanishes

Constants
---------

None
