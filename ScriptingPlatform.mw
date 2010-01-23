__NOTOC__

== Summary ==

A [[Moving platform]] that was given a name can be controlled by scripts. It is moving along a specified [[ScriptingPath|path]].

== Instances ==
An instance is created by being defined in a level. It may be accessed via its <tt>name</tt> from scripts and via <tt>sector.''name''</tt> from the console.

=== Example ===

Example of a definition:
 <pre>
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
 </pre>

The above object will be exposed under the name PLATFORM1 in the scripting engine. Example usage:

 <pre>
  PLATFORM1.goto_node(0);
 </pre>

From console:

<pre>
  sector.PLATFORM1.goto_node(1);
</pre>

== Methods ==
{| class="objectlist"
! class="method"| goto_node(int node_no)
| advance until at given node, then stop.
|-
! class="method"| start_moving()
| start advancing automatically
|-
! class="method"| stop_moving()
| stop advancing automatically
|}

== Constants ==

None

{{Navbox Scripting reference}}
[[Category:Scripting Reference]]
