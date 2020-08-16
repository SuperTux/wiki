Summary
-------

A [Tilemap](Tilemap "wikilink") that was given a name can be controlled by scripts. The tilemap can be moved by specifying a [path](ScriptingPath "wikilink") for it.

Instances
---------

An instance is created by being defined in a level. It may be accessed via its `name` from scripts and via `sector.`*`name`* from the console.

### Example

Example of a definition:

<code>
` (tilemap`
`   (name `“`niftymap`”`)`
`   (path`
`     (mode `“`circular`”`)`
`     (node`
`       (x 832)`
`       (y 800)`
`       (time 10)`
`     )`
`     (node`
`       (x 832)`
`       (y 704)`
`       (time 10)`
`     )`
`   )`
`   (width …)`
`   (height …)`
`   (tiles …)`
`   (solid #t)`
` ) `
</code>

The above tilemap will be exposed under the name “niftymap” in the scripting engine. Example usage:

<code>
` niftymap.goto_node(1);`
` niftymap.fade(0.0, 10);`
</code>

This will cause the tilemap to slowly move left, fading out as it goes, and disappear completely when it reaches its destination. Never fear, though; it is still there. From the console, you can enter:

<code>

` sector.niftymap.goto_node(0);`
` sector.niftymap.fade(1.0, 15)`

</code> The tilemap will then reverse its previous actions, ending up back where it started, but it will only reach full opacity 5 seconds after it stops.

Methods
-------

| goto\_node(int node\_no)         | Move tilemap along path until at given node, then stop.                                                                                        |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| start\_moving()                  | Start moving tilemap                                                                                                                           |
| stop\_moving()                   | Stop tilemap at next node                                                                                                                      |
| fade(float alpha, float seconds) | Start fading the tilemap to opacity given by alpha. Destination opacity will be reached after seconds game seconds. Also influences solidity.  |
| set\_alpha(float alpha)          | Instantly switch tilemap's opacity to alpha. Also influences solidity.                                                                         |
| float get\_alpha()               | Return the tilemap's opacity. Note that while the tilemap is fading in or out, this will return the current alpha value, not the target alpha. |

Constants
---------

None
