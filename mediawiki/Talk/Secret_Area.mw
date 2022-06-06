Instead of changing the way Secret Area work, just use another sector for your well hidden secret area and beam tux in and out using a script.

Do you know how hard it actually is make teleportation work smoothly?  Look in the ML for my "Lost Woods" concept level, change the music for the ambientsound, and play it.  I still haven't gotten it totally smooth.  Most teleport usage has a fade-in/fade-out, or a lightning strike as misdirection.  You really do not want to fade-in/fade-out, and lightning may not be appropriate.  Oh yeah, sign your comments with four tildes. --[[User:Tuxdev|Tuxdev]] 16:30, 26 Jul 2006 (BST)

== Secret area are counted ==

''"The Secret Area Trigger is used to mark secret areas, at the moment it doesn't do more then writing a message, it however could also be used to count the number of secrets the player has found in a world (even so that is probally better done with special coins or items to collect)."''
:This is wrong, those areas are counted. Look for a string like "Secrets found 1/2" at the end of a level. --[[User:AnMaster|AnMaster]] 16:34, 26 Jul 2006 (BST)

== Rectangular secretarea-triggers might not be flexible enough ==

Why not just use polygons or maybe name secret areas so that several secert areas with the same name are treated as one area? I dislike using tiles for it. --[[User:AnMaster|AnMaster]] 20:09, 27 Jul 2006 (BST)

== About secret tilemaps ==

Current implementation of secret areas uses level-wide maps which are faded on entering. This might be a problem for filesize in huge levels, especially when multiple secret maps are present. I think a smaller and positionable tilemap object (to be merged with the secret area object) might be useful:

  (secretarea
    (x number) (y number) ;coord of top left corner
    (message "message") ;message on trigger
    (width number) (height number) ;width and height (in tiles?)
    (tiles 0 0 0 ...) ;tiles like in tilemap
  )

--Shylence 14:41, 23 Oct 2006 (CEST)

: The current implementation allows secret areas to fade away a tilemap when the secret area is entered. This mechanism, however, is not restricted to tilemaps which are as big as the whole sector. IIRC tilemaps can have any size and be positioned freely, it's just not possible to create such tilemaps with the editor yet. --[[User:195.158.178.69|195.158.178.69]] 16:49, 23 Oct 2006 (CEST)

== can't find  ==

can't find a secret area in "don't miss your ride" on dungeon Island, can someone help me?
