Summary
-------

A [Moving platform](Moving_platform "wikilink") that was given a name can be controlled by scripts. It is moving along a specified [path](ScriptingPath "wikilink").

Instances
---------

An instance is created by being defined in a level. It may be accessed via its `name` from scripts and via <code>sector.<var>name</var></code> from the console.

### Example

Example of a definition:

    (platform
      (name "PLATFORM1")
      (running #f)
      (sprite "images/objects/platforms/vertical-wood.sprite")
      (path
        (mode "circular")
        (node
          (x 832)
          (y 800)
        )
        (node
          (x 832)
          (y 704)
        )
      )
    ) 
     

The above object will be exposed under the name PLATFORM1 in the scripting engine. Example usage:

      PLATFORM1.goto_node(0);
     

From console:

      sector.PLATFORM1.goto_node(1);

Methods
-------

Method                   | Explanation
-------------------------|------------------------------------------
`goto_node(int node_no)` | Advances until at given node, then stops.
`start_moving()`         | Starts advancing automatically.
`stop_moving()`          | Stops advancing automatically.
`set_action(string action, int repeat)` | Sets the sprite action.

Constants
---------

None
