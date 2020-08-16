Summary
-------

`Camera` is an interface to manipulate the camera.

Instances
---------

An instance named `Camera` (`sector.Camera` in the console) is available. *(Note: doesn't having a class and an eponymous instance create a potential for conflicts? We should probably rename the instance or the class.)*

The *mode* of the camera is either **normal** (the camera is following the player) or **autoscroll**. In the latter mode the camera is forced along a specified [path](ScriptingPath "wikilink").

### Example

    (camera
      (mode "autoscroll")
      (path
        (node
          (x 0)
          (y 0)
          (time 250)
        )
        (node
          (x 19072)
          (y 0)
        )
      )
    )

Methods
-------

Method                                    | Explanation
------------------------------------------|-------------------------------------
`shake(float time, float x, float y)`     | Moves camera to the given coordinates in <var>time</var> seconds returning quickly to the original position after that.
`set_pos(float x, float y)`               | Moves the camera to the specified absolute position. The origin is at the top left.
`set_mode(string modestring)`             | This function sets the camera mode. Valid values for <var>modestring</var> are “normal” and “manual”.
`scroll_to(float x, float y, float time)` | Scrolls the camera to the given coordinates within <var>time</var> seconds.

Constants
---------

None
