Summary
-------

A ScriptedObject is basically a SuperTux object that can be scripted to move around and animate.

Instances
---------

ScriptedObjects are created by being defined in level files. Each scripted object will be exposed under its name to the scripting engine. Access through the console is realised via the `sector` object.

### Example

Example of a definition:

      (scriptedobject
        (x 2291)
        (y 1275)
        (name "SUPERTUX")
        (sprite "images/creatures/tux_big/tux.sprite")
        (layer 100)
        (visible #t)
        (physic-enabled #t)
        (solid #t)
      ) 
     

The above object will be exposed under the name `SUPERTUX` in the scripting engine. Example usage:

      // This script will make tux look and walk left/right (this should make him appear
      //   "upset")
      SUPERTUX.set_action("stand-right");
      wait(2);
      SUPERTUX.set_velocity(200,0);
      wait(0.3);
      SUPERTUX.set_velocity(0,0);
      wait(0.4);
      SUPERTUX.set_action("stand-left");
      SUPERTUX.set_velocity(-200,0);
      wait(0.3);
     

The object can be accessed from the console `sector.SUPERTUX`.

Methods
-------

| set\_action(string animation)          | Activates the sprite's action specified in `animation`.                                                   |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------|
| get\_action()                          | Returns the name of the sprite's current action.                                                          |
| move(float x, float y)                 | Moves the object by `x` units to the right and `y` down relative to its current position.                 |
| set\_pos(float x, float y)             | Basically identical to `move`, except its relativity to the sector origin.                                |
| get\_pos\_x()                          | Returns the X coordinate of the object's position.                                                        |
| get\_pos\_y()                          | Returns the Y coordinate of the object's position.                                                        |
| set\_velocity(float x, float y)        | Makes the object move in a certain direction (with a certain speed) given by the `x` and `y` coordinates. |
| get\_velocity\_x()                     | Returns the X coordinate of the object's velocity.                                                        |
| get\_velocity\_y()                     | Returns the Y coordinate of the object's velocity.                                                        |
| enable\_gravity(bool gravity\_enabled) | Shows or hides the object according to the value of `gravity_enabled`.                                    |
| gravity\_enabled()                     | Returns true if the object's gravity is enabled, false otherwise.                                         |
| set\_visible(bool visible)             | Shows or hides the object according to the value of `visible`.                                            |
| is\_visible()                          | Returns true if the object is visible, false otherwise.                                                   |
| set\_solid(bool solid)                 | Makes the object solid according to the value of `solid`.                                                 |
| is\_solid()                            | Returns true if the object is solid, false otherwise.                                                     |
| get\_name()                            | Returns the name of the object                                                                            |

Constants
---------

None
