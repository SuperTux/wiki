Summary
-------

A [Thunderstorm](Thunderstorm "wikilink") object that was given a name can be controlled by scripts.

Instances
---------

A `Thunderstorm` is initialised by a definition in the level. It can be accessed via its `name` in scripts and <code>sector.<var>name</var></code> in the console.

### Example

Example of a definition:

    (thunderstorm
      (name "ELIZA")
      (running #f)
    )

The above object will be exposed under the name ELIZA in the scripting engine. Example usage:

    ELIZA.thunder();
    wait(2);
    ELIZA.lightning();

In the console:

    sector.ELIZA.electrify()

Methods
-------

| start()     | Start playing thunder and lightning at configured interval   |
|-------------|--------------------------------------------------------------|
| stop()      | Stop playing thunder and lightning at configured interval    |
| thunder()   | Play thunder                                                 |
| lightning() | Play lightning, i.e. call flash() and electrify()            |
| flash()     | Display a nice flash                                         |
| electrify() | Electrify water throughout the whole sector for a short time |

Constants
---------

None
