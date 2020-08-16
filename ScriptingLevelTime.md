Summary
-------

A `LevelTime` object that is given a name can be controlled by scripts.

Instances
---------

A `LevelTime` object is instantiated by a definition in the level file. It can be accessed by scripts using its `name` and from the console as <code>sector.<var>name</var></code>.

### Example

Example of a definition:

    (leveltime
      (name "TIME")
      (time 300)
    )

The above time will be exposed under the name TIME in the scripting engine, and start out with a time of 300 game seconds. Example usage:

    TIME.stop();
    wait(30);
    TIME.start();

This will cause the time to suddenly stop, then start up again after 30 seconds.

Console access:

    sector.TIME.stop()

This will stop the time.

Methods
-------

Method                      | Explanation
----------------------------|---------------------------------------------------
`start()`                   | Resumes the countdown (assuming it isn't already started, in which case it does nothing).
`stop()`                    | Pauses the countdown (assuming it isn't already stopped, in which case it does nothing).
`float get_time()`          | Returns the number of seconds left on the clock.
`set_time(float time_left)` | Changes the number of seconds left on the clock.

Constants
---------

None
