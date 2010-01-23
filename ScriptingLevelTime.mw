__NOTOC__

== Summary ==
A <tt>LevelTime</tt> object that is given a name can be controlled by scripts.

== Instances ==
A <tt>LevelTime</tt> object is instantiated by a definition in the level file. It can be accessed by scripts using its <tt>name</tt> and from the console as <tt>sector.''name''</tt>.

=== Example ===

Example of a definition:
<pre>
(leveltime
  (name "TIME")
  (time 300)
)
</pre>

The above time will be exposed under the name TIME in the scripting engine, and start out with a time of 300 game seconds. Example usage:

<pre>
TIME.stop();
wait(30);
TIME.start();
</pre>
This will cause the time to suddenly stop, then start up again after 30 seconds.

Console access:
<pre>
sector.TIME.stop()
</pre>
This will stop the time.

== Methods ==
{| class="objectlist"
! class="method" style="vertical-align: top"| start()
| Resumes the countdown (assuming it isn't already started, in which case it does nothing)
|-
! class="method" style="vertical-align: top"| stop()
| Pauses the countdown (assuming it isn't already stopped, in which case it does nothing)
|-
! class="method" style="vertical-align: top"| float get_time()
| Returns the number of seconds left on the clock
|-
! class="method" style="vertical-align: top"| void set_time(float time_left)
| Changes the number of seconds left on the clock
|}

== Constants ==

None

{{Navbox Scripting reference}}
[[Category:Scripting Reference]]
