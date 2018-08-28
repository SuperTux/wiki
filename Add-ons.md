**Add-ons** are extensions for *SuperTux* which are distributed
separately from the main distribution. In most cases, they are sets of
levels contributed by users or groups of users. They may, however,
include custom [tilesets](tileset "wikilink"), which may give these
levels a very distinct look.

Add-ons can be downloaded from within *SuperTux*. Simply ensure you
have an internet connection, and select “Addons” from the main menu,
where you can choose to install the currently available add-ons.

The addons are managed in two repositories:

* https://github.com/SuperTux/addons
* https://github.com/SuperTux/addons-src

`addons` contains the `.zip` files that are downloaded by SuperTux,
while `addon-src` contains the levels in extracted form to make it
easier to modify and debug them.

The process of updating the `addons` repository is documented at:

* https://github.com/SuperTux/addons/blob/master/README.md

Manual installation
-------------------

If you cannot use the *Add-on manager* for some reason (for example if
you built *SuperTux* without *libcurl*), you can download the add-ons,
which are distributed as `.zip` files. Just copy the file(s) to your
*SuperTux 2* config directory (`~/.supertux2/` on UNIX / Linux,
`%USERPROFILE%\supertux2\` on Windows).

    $ wget -P ~/.supertux2 $ADDON_URL
