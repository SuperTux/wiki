Summary
-------

A Candle object that was given a name can be controlled by scripts.

Instances
---------

A `Candle` is instantiated via a definition in a level. It can be accessed by its `name` in scripts and via <code>sector.<var>name</var></code> in the console.

### Example

Example of a definition:

    (candle
      (name "CANDLE1")
      (burning #f)
      (x 1632)
      (y 1088)
    )

The above object will be exposed under the name CANDLE1 in the scripting engine. Example usage:

    CANDLE1.set_burning(true);

Console usage:

    sector.CANDLE1.set_burning(false)

Methods
-------

Method                      | Explanation
----------------------------|---------------------------------------------------
`bool get_burning()`        | Returns true if candle is lighted.
`set_burning(bool burning)` | Lights candle if true; extinguishes candle if false.

Constants
---------

None
