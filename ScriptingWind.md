Summary
-------

A Wind object that was given a name can be controlled by scripts.

Instances
---------

A `Wind` is instantiated by a definition in the level file. It can be accessed by scripts using its `name` and from the console as <code>sector.<var>name</var></code>.

### Example

Example of a definition:

    (wind
      (name "WIND1")
      (blowing #f)
      (speed-x 0)
      (speed-y -600)
      (acceleration 3)
      (width 32)
      (height 64)
      (x 783)
      (y 768)
    )

The above object will be exposed under the name WIND1 in the scripting engine. Example usage:

    WIND1.start();

Console access:

    sector.WIND1.stop()

Methods
-------

| start() | start blowing |
|---------|---------------|
| stop()  | stop blowing  |

Constants
---------

None
