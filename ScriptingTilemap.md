Summary
-------

A [Tilemap](Tilemap "wikilink") that was given a name can be controlled by scripts. The tilemap can be moved by specifying a [path](ScriptingPath "wikilink") for it.

Instances
---------

An instance is created by being defined in a level. It may be accessed via its `name` from scripts and via <code>sector.<var>name</var></code> from the console.

### Example

Example of a definition:

    (tilemap
      (name "niftymap")
      (path
        (mode "circular")
        (node
          (x 832)
          (y 800)
          (time 10)
        )
        (node
          (x 832)
          (y 704)
          (time 10)
        )
      )
      (width …)
      (height …)
      (tiles …)
      (solid #t)
    ) 

The above tilemap will be exposed under the name “niftymap” in the scripting engine. Example usage:

    niftymap.goto_node(1);
    niftymap.fade(0.0, 10);

This will cause the tilemap to slowly move left, fading out as it goes, and disappear completely when it reaches its destination. Never fear, though; it is still there. From the console, you can enter:

    sector.niftymap.goto_node(0);
    sector.niftymap.fade(1.0, 15)

 The tilemap will then reverse its previous actions, ending up back where it started, but it will only reach full opacity 5 seconds after it stops.

Methods
-------

Method                                     | Explanation
-------------------------------------------|------------------------------------
`goto_node(int node_no)`                   | Moves tilemap along path until at given node, then stop.
`start_moving()`                           | Starts moving tilemap.
`stop_moving()`                            | Stops tilemap at next node.
`int get_tile_id(int x, int y)`            | Returns the id of the tile at the given coordinates or <output>0</output> if out of bounds. The origin is at the top left.
`int get_tile_id_at(float x, float y)`     | Wrapper for `get_tile_id` that subtracts an offset and divides the arguments by 32 first.
`change(int x, int y, int newtile)`        | Changes tile at given coordinates to <var>newtile</var>.
`change_at(float x, float y, int newtile)` | Wrapper for `change` that subtracts an offset and divides the arguments by 32 first.
`float get_alpha()`                        | Returns the tilemap's opacity. Note that while the tilemap is fading in or out, this will return the current alpha value, not the target alpha.
`set_alpha(float alpha)`                   | Instantly switches tilemap's opacity to <var>alpha</var>. Also influences solidity.
`fade(float alpha, float seconds)`         | Fades the tilemap to opacity given by <var>alpha</var> in <var>seconds</var> seconds. Also influences solidity.
`tint_fade(float seconds, float red, float greens, float blue, float alpha)` | Fade to given tint color in <var>seconds</var> seconds. The tint is applied on all tiles on the tilemap.
`set_solid(bool solid)`                    | If `false` is given, Tux cannot interact with the tilemap. Make sure every sector has at least one solid tilemap.

Constants
---------

None
