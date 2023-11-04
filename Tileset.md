SuperTux [tilemaps](tilemap "wikilink") are composed from tiles,
little 32x32 pixel wide images. These tiles are defined in an
[[S-Expression]] based file, [data/images/tiles.strf](Template:SvnFile
"wikilink").

These tilesets are included into the level by a `tileset` entry.

A `tile` has an ID number a set of images (it's an animated tile if it
has more than 1 image) and contains a set of attributes like solid,
icy, anim-fps...

Example
-------

An example of a simple solid tile looks like this:

     (tile
       (id 7)
       (solid #t)
       (images
         "tiles/snow/snow1.png"
       )
     )

An animated waterfall tile (animation played with 10 fps):

     (tile
       (id 175)
       (images
         "tiles/waterfall/trans1-1-1.png"
         "tiles/waterfall/trans1-1-2.png"
         "tiles/waterfall/trans1-1-3.png"
         "tiles/waterfall/trans1-1-4.png"
       )
       (water #t)
       (anim-fps 10)
     )

It's also possible to extract parts of bigger images to create tiles.
This extracts the upper left edge of the foresttiles-1.png file:

     (tile
       (id 1000)
       (images
         (region "tiles/forest/foresttiles-1.png" 0 0 32 32)
       )
     )

Note that in [Milestone 2](Milestone_2 "wikilink"), the last variant
is deprecated in favor of a more compact approach at defining multiple
tiles:

     (tiles
       (width 3)
       (height 4)
       (ids  7  8  9
            13 14 15
            10 11 12
            16 17 18)
       (attributes 0 0 0
                   1 1 1
                   1 1 1
                   0 0 0)
       (image "tiles/snow/convex.png")
     )

In this example, a block of 3x4 tiles will be extracted from an image
with only the middle rows solid. To ignore a portion of the image, use
an id of 0 in the appropriate place.

More complex variants are also supported:

     (tiles
       (width 11)
       (height 4)
       (ids
         7  8  9  0    1826 1827 0    1837 1838 1843 1844
         13 14 15 1829 1830 1831 1832 1839 1840 1845 1846
         10 11 12 1833 1834 1835 1836 1841 1842 1847 1848
         16 17 18 0    0    0    0    0    0    1849 1850
       )
       (attributes
         0 0 0 0  0  0  0  0  0  0  0
         1 1 1 17 17 17 17 17 17 17 17
         1 1 1 1  1  1  1  1  1  17 17
         0 0 0 0  0  0  0  0  0  1  1
       )
       (datas
         0 0 0 0  0  0  0  0 0 0  0
         0 0 0 18 34 32 16 2 0 66 48
         0 0 0 0  0  0  0  0 0 50 64
         0 0 0 0  0  0  0  0 0 0  0
       )
       (image "tiles/snow/convex.png")
     )

17 is used for slopes, and the appropriate data/slope-type is put in
datas. Alternately, you could go minimalist with no data or
attributes:

     (tiles
       (width  12)
       (height 14)
       (ids
          2212 2213 2214 2215 2216 2217 2218 2219 2220 2221 2222 2223
          2224 2225 2226 2227 2228 2229 2230 2231 2232 2233 2234 2235
          2236 2237 2238 2239 2240 2241 2242 2243 2244 2245 2246 2247
          2248 2249 2250 2251 2252 2253 2254 2255 2256 2257 2258 2259
          2260 2261 2262 2263 2264 2265 2266 2267 2268 2269 2270 2271
          2272 2273 2274 2275 2276 2277 2278 2279 2280 2281 2282 2283
          2284 2285 2286 2287 2288 2289 2290 2291 2292 2293 2294 2295
          2296 2297 2298 2299 2300 2301 2302 2303 2304 2305 2306 2307
          2308 2309 2310 2311 2312 2313 2314 2315 2316 2317 2318 2319
          2320 2321 2322 2323 2324 2325 2326 2327 2328 2329 2330 2331
          2332 2333 2334 2335 2336 2337 2338 2339 2340 2341 2342 2343
          2344 2345 2346 2347 2348 2349 2350 2351 2352 2353 2354 2355
          2356 2357 2358 2359 2360 2361 2362 2363 2364 2365 2366 2367
          2368 2369 2370 2371 2372 2373 2374 2375 2376 2377 2378 2379
       )
       (image "tiles/castle/background.png")
     )

Tile attributes
---------------

Tiles can have the following attributes:

| Name       | Value           | Description                                                                                                                                                                                                      | Data field                                                                                    |
|------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| solid      | `0x0001` / 1    | defines if the tile should be considered for collision detection                                                                                                                                                 |                                                                                               |
| unisolid   | `0x0002` / 2    | the tile will only be considered for collision detection when tux is falling down. That is you can jump through the tile from below but not fall through it. Must be used in conjunction with attribute *solid*. |                                                                                               |
| brick      | `0x0004` / 4    | A brick that can be destroyed by jumping under it                                                                                                                                                                |                                                                                               |
| goal       | `0x0008` / 8    | The level should be finished when touching a goaltile.                                                                                                                                                           | 0 Trigger *endsequence*, 1 Finish level instantly                                             |
| slope-type | `0x0010` / 16   | The tile is a slope. Must be combined with *solid*.                                                                                                                                                              | Type of slope (deformation). [See below](#Slope_types "wikilink") for possible values.        |
| fullbox    | `0x0020` / 32   | Bonusbox                                                                                                                                                                                                         | Content of the box., 1 Coin, 2 Egg / fireflower, 3 Star, 4 Tux Doll (1 up), 5 Egg / iceflower |
| coin       | `0x0040` / 64   | The tile is a coin                                                                                                                                                                                               |                                                                                               |
| ice        | `0x0100` / 256  | the tile will be slippery                                                                                                                                                                                        |                                                                                               |
| water      | `0x0200` / 512  | The tile is a water tile (needed for [fish](fish "wikilink") enemy)                                                                                                                                              |                                                                                               |
| hurts      | `0x0400` / 1024 | The tile will hurt you when you hit it                                                                                                                                                                           |                                                                                               |

Data section
------------

Each `tile` definition can have a `data` section (“`datas`” when using
the `tiles` definition). This section is used when the
yes/no-information usually stored in the *attributes* definition isn't
appropriate for the type of information. Currently, this section is
only used to store *slope* data.

Each type of information stored in the data section needs to reserve a
range of values for itself. The slope information, for example, uses
the values zero through 67 (64+3), so the mask is at least `0x007f`.
To allow for future extension, the mask `0x00ff` has been reserved.

| Name              | Mask                          | Meaning                                                                                           |
|-------------------|-------------------------------|---------------------------------------------------------------------------------------------------|
| Slope information | `0x00ff` (actually: `0x0073`) | Valid only when the *solid* attribute is set. See [\#Slope types](#Slope_types "wikilink") below. |

### Slope types

![](images/Slopes.png "Slopes.png")

![Circle showing the 20 different valid slope data values.](images/Slope-data.png "fig:Circle showing the 20 different valid slope data values.") The *deformation* means the following. The “circle” on the right shows the 20 different possibilities.

| Name    | Value | Meaning                                  |
|---------|-------|------------------------------------------|
| Deform1 | 16    | Only the lower half of the tile is used. |
| Deform2 | 32    | Only the upper half of the tile is used. |
| Deform3 | 48    | Only the left half of the tile is used.  |
| Deform4 | 64    | Only the right half of the tile is used. |

The important part is that the deformation determines which part of
the tile is used and not the actual *form* of the tile. For example,
the `0+48` tile is a (steep, south-west) *triangle*, while `2+48` is a
(steep, south-east) *trapezoid*.

### Example

The following defines several tiles, some of which are slopes. Their
slope information is stored in the *datas* section.

      (tiles
        (width 11)
        (height 4)
        (ids
          7  8  9  0    1826 1827 0    1837 1838 1843 1844
          13 14 15 1829 1830 1831 1832 1839 1840 1845 1846
          10 11 12 1833 1834 1835 1836 1841 1842 1847 1848
          16 17 18 0    0    0    0    0    0    1849 1850
        )
        (attributes
          0 0 0 0  0  0  0  0  0  0  0
          1 1 1 17 17 17 17 17 17 17 17
          1 1 1 1  1  1  1  1  1  17 17
          0 0 0 0  0  0  0  0  0  1  1
        )
        (datas
          0 0 0 0  0  0  0  0 0 0  0
          0 0 0 18 34 32 16 2 0 66 48
          0 0 0 0  0  0  0  0 0 50 64
          0 0 0 0  0  0  0  0 0 0  0
        )
        (image "tiles/snow/convex.png")
      )

Adding new tiles
----------------

You can simply add new tiles with your favourite text editor. However
we also provide an easy to use editor to make this task easier
(especially extracting regions of bigger images). You can find it in
the *tools/tilemanager* directory. It's a mono/gtk\# app so you have
to have these 2 things installed and should invoke make in that
directory then. It'll create *tilemanager.exe* which you can then
start with mono like this:

    mono tilemanager.exe

NOTE: You should be careful when choosing tile ids to not overwrite
existing tiles. You should also keep in mind that existing levels will
break if you change tile numbers later (the levels just save a big a
list of numbers that reference the tile file).

**WARNING**: Unfortunately the tilemanage application is broken at the
moment and does not work correctly! You'll destroy several tile
attributes like slopes and some of the tiles created from multiple
images, when opening and saving a tileset with the editor!

Testing
-------

Simply open the flexlay or ST\# editor and the new tiles should
appear.

Trickery
--------

Note that some tiles aren't actually used in-game. Right after the
level is loaded, various tiles in the solid tilemaps are replaced with
objects. These include all with the coin, fullbox, brick, or goal
attributes, and tile id 112 (invisible block). But the game doesn't
end there. It also adds light sources to torches and lava, which are
then hidden unless the level uses a lightmap.