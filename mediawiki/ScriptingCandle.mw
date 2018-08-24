__NOTOC__

== Summary ==

A Candle object that was given a name can be controlled by scripts.

== Instances ==
A <tt>Candle</tt> is instantiated via a definition in a level. It can be accessed by its <tt>name</tt> in scripts and via <tt>sector.''name''</tt> in the console.

=== Example ===

Example of a definition:
<pre>
(candle
  (name "CANDLE1")
  (burning #f)
  (x 1632)
  (y 1088)
)
</pre>

The above object will be exposed under the name CANDLE1 in the scripting engine. Example usage:

<pre>
CANDLE1.set_burning(true);
</pre>

Console usage:

<pre>
sector.CANDLE1.set_burning(false)
</pre>

== Methods ==
{| class="objectlist"
! class="method"| get_burning()
| returns true if candle is lighted
|-
! class="method"| set_burning(bool burning)
| true: light candle, false: extinguish candle
|}

== Constants ==

None

{{Navbox Scripting reference}}
[[Category:Scripting Reference]]
