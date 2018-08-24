__NOTOC__

== Summary ==

Will-o-Wisps, when given a name (and perhaps a [[ScriptingPath|path]] too), become scriptable, much like a [[ScriptingPlatform|platform]] or [[ScriptingTilemap|tilemap]].

== Methods ==
{| class="objectlist"
! class="method"| goto_node(int node_no)
| Move willowisp to given node.
|-
! class="method"| start_moving()
| start following the path
|-
! class="method"| stop_moving()
| stop following the path
|-
! class="method" style="vertical-align: top"| set_state(string state)
| set the willowisp state, can be:
*stopped:         willowisp doesn't move
*move_path:       willowisp moves along the path (call goto_node)
*move_path_track: willowisp moves along path but catches Tux when he is near
*normal:          "normal" mode starts tracking tux when he is near enough
*vanish:          willowisp vanishes
|}

== Constants ==

None

{{Navbox Scripting reference}}
[[Category:Scripting Reference]]
