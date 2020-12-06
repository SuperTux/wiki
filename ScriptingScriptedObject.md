Summary
-------

A ScriptedObject is basically a SuperTux object that can be scripted to move around and animate.

Instances
---------

ScriptedObjects are created by being defined in level files. Each scripted object will be exposed under its name to the scripting engine. Access through the console is realised via the `sector` object.

### Example

Example of a definition:

    (scriptedobject
      (x 50)
      (y 50)
      (name "SUPERTUX")
      (sprite "images/creatures/tux/tux.sprite")
    )
   
The above object will be exposed under the name `SUPERTUX` in the scripting engine. Example usage:

    // This script will make tux look and walk left/right (this should make him
    // appear "upset")
    SUPERTUX.set_action("big-stand-right");
    wait(2);
    SUPERTUX.set_velocity(200,0);
    wait(0.3);
    SUPERTUX.set_velocity(0,0);
    wait(0.4);
    SUPERTUX.set_action("big-stand-left");
    SUPERTUX.set_velocity(-200,0);
    wait(0.3);
     

The object can be accessed from the console as `sector.SUPERTUX`.

Methods
-------

Method                                 | Explanation
---------------------------------------|----------------------------------------
`set_action(string animation)`         | Activates the sprite's action specified in <var>animation</var>.
`string get_action()`                  | Returns the name of the sprite's current action.
`move(float x, float y)`               | Moves the object by <var>x</var> units to the right and <var>y</var> down relative to its current position.
`set_pos(float x, float y)`            | Basically identical to `move`, except its relativity to the sector origin.
`float get_pos_x()`                    | Returns the X coordinate of the object's position.
`float get_pos_y()`                    | Returns the Y coordinate of the object's position.
`set_velocity(float x, float y)`       | Makes the object move in a certain <var>x</var> and <var>y</var> direction (with a certain speed).
`float get_velocity_x()`               | Returns the X coordinate of the object's velocity.
`float get_velocity_y()`               | Returns the Y coordinate of the object's velocity.
`enable_gravity(bool gravity_enabled)` | Enables or disables gravity according to the value of <var>gravity_enabled</var>.
`bool gravity_enabled()`               | Returns true if the object's gravity is enabled, false otherwise.
`set_visible(bool visible)`            | Shows or hides the object according to the value of <var>visible</var>.
`bool is_visible()`                    | Returns true if the object is visible, false otherwise.
`set_solid(bool solid)`                | Changes the solidity according to the value of <var>solid</var>.
`bool is_solid()`                      | Returns true if the object is solid, false otherwise.
`string get_name()`                    | Returns the name of the object.

Constants
---------

None
