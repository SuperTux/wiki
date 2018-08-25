'''Unstable tiles''' are a special kind of [[tile]] on which [[Tux]] can stand only for a limited time. After that, the block starts to dissolve and&nbsp;/ or to fall down.

The sprites for unstable tiles may have four ''actions'':
; normal
: Displayed until [[Tux]] steps on the tile.
; shake
: The tile shakes but is still solid.
; dissolve
: The tile is dissolving. After the animation for this action is done, the tile will be set non-solid.
; fall-down
: Gravity is enabled for this tile and it will begin to fall down.
Each of the actions ''shake'', ''dissolve'' and ''fall-down'' is optional. If a sprite doesn't have the ''dissolve'' action, the till will still be solid when the ''fall-down'' action is executed (Donut Tile style). If the tile doesn't have a ''fall-down'' action, it will be removed after the ''dissolve'' animation is done (Giana Sisters style).

[[Category:Game Object]]
