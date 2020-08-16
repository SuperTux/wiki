Summary
-------

Will-o-Wisps, when given a name (and perhaps a [path](ScriptingPath "wikilink") too), become scriptable, much like a [platform](ScriptingPlatform "wikilink") or [tilemap](ScriptingTilemap "wikilink").

Methods
-------

| goto\_node(int node\_no) | Move willowisp to given node.                                                     |
|--------------------------|-----------------------------------------------------------------------------------|
| start\_moving()          | start following the path                                                          |
| stop\_moving()           | stop following the path                                                           |
| set\_state(string state) | set the willowisp state, can be:                                                  
                                                                                     
  -   stopped: willowisp doesn't move                                                
  -   move\_path: willowisp moves along the path (call goto\_node)                   
  -   move\_path\_track: willowisp moves along path but catches Tux when he is near  
  -   normal: “normal” mode starts tracking tux when he is near enough               
  -   vanish: willowisp vanishes                                                     |

Constants
---------

None
