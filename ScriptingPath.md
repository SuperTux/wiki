A **Path** is a series of points that can be followed by some objects. This way controlled movement can be implemented, like opening doors, moving platforms, traps, etc.

Synopsis
--------

    (path
      (mode "circular")
      (node
        (x 800)
        (y 96)
        (time 0.3)
      )
      (node
        (x 832)
        (y 96)
        (time 1.0)
      )
    )

Syntax
------

A path consists of a *mode* setting and one or more *nodes*.

### Mode

The *mode* specifies the behavior at the end of the path when automatic movement is activated, i.e. the object is going to all nodes in order one by one (rather than being told to go to a specific node and stay there). It takes one string argument with the following possible values:

-   **circular:**
    After reaching the last node go directly back to the first node, forming a circle.
-   **pingpong:**
    After reaching the last node go back the path, visiting all nodes in reverse order. This is especially useful for moving platforms that go back and forth a specific path.
-   **oneshot:**
    When reaching the last node, stay there.
-   **unordered:**
    Travels to a random node and never stops. Goes directly to given node when not running.

**Example:**

    (mode "circular")

### Nodes

Nodes are points in the level along which the associated object moves. They have the following attributes:

-   **x:**
    x-coordinate of the point in *pixels*.
-   **y:**
    y-coordinate of the point in *pixels*.
-   **time:** *(optional)*
    Time it takes to move to the *next* point in seconds. Defaults to one second.

**Example:**

    (node
      (x 42)
      (y 23)
      (time 1.337)
    )

Scripting
---------

Objects a path is associated with usually provide the following methods:

Method                   | Explanation
-------------------------|------------------------------------------------------
`goto_node(int node_no)` | Advances until at given node, then stops. The index of the first node is 0.
`start_moving()`         | Starts advancing automatically.
`stop_moving()`          | Stops advancing automatically.

Used by
-------

-   [Camera](ScriptingCamera "wikilink") (*autoscroll* mode)
-   [Platform](ScriptingPlatform "wikilink")
-   [Tilemap](ScriptingTilemap "wikilink")
-   [Will-o-wisp](ScriptingWill-o-wisp "wikilink")
