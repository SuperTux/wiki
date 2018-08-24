Sometimes it is desirable to transform existing maps in some special ways. Things that come to mind are:

* Change maps after a certain event (remember SMW with the big ! blocks and the stuff that happened after beating the star world?)
* Flipping a map upside down
* Maybe we could have an extra-hard mode that adds additional badguys for supertux experts...

These transformers would be applied directly after a map has been loaded. It should be possible to make them dependent on some conditions being met. On the implementation side this would mean that you can add a list of map transformers to each map file. This would also be a good candidate to be scriptable. Eventually, the level editor should support creating and editing those scripts.

[[Category:Game Engine]]
