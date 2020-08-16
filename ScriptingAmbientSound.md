Summary
-------

An ambient sound that was given a name can be controlled by scripts.

Instance
--------

An `AmbientSound` is instantiated by placing a definition inside a level. It can then be accessed by its `name` from a script or via <code>sector.<var>name</var></code> from the console.

### Example

In the level file:

    (ambient_sound
      (name "niagara")
      (x 10)
      (y 20)
      (width 100)
      (height 51)
      (distance_factor 0.5)
      (distance_bias 0)
      (sample "waterfall.wav")
      (volume 1)
    )

In a script:

    niagara.set_pos(0, 0);

In the console:

    sector.niagara.set_pos(18, 35)

Methods
-------

| set\_pos(float x, float y) | Sets the position of the ambient sound |
|----------------------------|----------------------------------------|
| get\_pos\_x()              | Returns the x coordinate.              |
| get\_pos\_y()              | Returns the y coordinate.              |

Constants
---------

-   *None*
