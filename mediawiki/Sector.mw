Each level that is version 2 is divided into one or more sectors. [[Tux]] is always in a sector, initially the "main" sector. Other sectors can be accessed through the [[Console]] or any other method of running scripts, using the [[ScriptingLevel|Level]].spawn method, or by creating a [[Door]] that specifies a different sector.

Each sector contains its own private squirrel table, which all object/sector scripts are run with as the root table. This allows you to write tilemap1.fade(1.0,1.0), for example, instead of accessing it through the sector member of the ordinary root table (which console scripts, for example, are run in). One problem with this is that you cannot store cross-sector data without using the special syntax of ::parent.x to create global variables. However, this is still not satisfactory, as the variables remain too long, extending over the entire length of the game.

[[Category:Game Design]]
