\_\_NOTOC\_\_

Summary
-------

`Camera` is an interface to manipulate the camera.

Instances
---------

An instance named `Camera` (`sector.Camera` in the console) is available. *(Note: doesn't having a class and an eponymous instance create a potential for conflicts? We should probably rename the instance or the class.)*

The *mode* of the camera is either **normal** (the camera is following the player) or **autoscroll**. In the latter mode the camera is forced along a specified [path](ScriptingPath "wikilink"). The left and right borders of the screen are solid. If the player fails to hold up with the moving camera, [Tux](Tux "wikilink") is pushed forward according to the camera movement, possibly squishing him when he is between the border of the screen and other solid objects.

### Example

`(camera`
`  (mode `“`autoscroll`”`)`
`  (path`
`    (node`
`      (x 0)`
`      (y 0)`
`      (time 250)`
`    )`
`    (node`
`      (x 19072)`
`      (y 0)`
`    )`
`  )`
`)`

Methods
-------

| shake(float time, float x, float y)      | Shakes camera in the vector specified by x and y.                                                |
|------------------------------------------|--------------------------------------------------------------------------------------------------|
| set\_pos(float x, float y)               | Moves the camera to the specified position. Warning: This function has not yet been implemented. |
| set\_mode(string modestring)             | This function sets the camera mode. Valid values for `modestring` are “`normal`” and “`manual`”. |
| scroll\_to(float x, float y, float time) | Scrolls the camera to (`x`, `y`) within `time` seconds.                                          |

Constants
---------

None

[Template:Navbox Scripting reference](Template:Navbox_Scripting_reference "wikilink")

[Category:Scripting Reference](Category:Scripting_Reference "wikilink")
