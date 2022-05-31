**Add-ons** are extensions for *SuperTux* which are distributed
separately from the main distribution. In most cases, they are sets of
levels contributed by users or groups of users. They may, however,
include custom [tilesets](Tileset), which may give these
levels a very distinct look.

Add-ons can be downloaded from within *SuperTux*. Simply ensure you
have an internet connection, and select “Add-ons” from the main menu,
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
`%APPDATA%\SuperTux\supertux2\` on Windows).

    $ wget -P ~/.supertux2 $ADDON_URL

Creating Addons
===============

So you've played SuperTux, beating all the levels, including the bonus levels, and now you want more.

You can either install addons, or create your own. If you wish to create your own addons, the following instructions are for you:

Creating Levels
---------------

Levels are created in different ways depending on which version you are using, as the format changed between 0.1.x, 0.3.x and 0.5.x. Also, 0.3.x has a separate editor and game. Anyway, these will create some .stl files for you to enjoy.

<details>
<summary><b>SuperTux 0.1.x</b></summary>
<br>
Create as many levels as you want using the built-in editor. Try reading the editor help first by pressing F1.
   
#### Creating Worldmaps

You could try to use [FlexLay](http://flexlay.berlios.de) for creating worldmaps.

</details>

<details>
<summary><b>SuperTux 0.3.x</b></summary>
<br>
Download the SuperTux Editor. The Editor FAQ might be helpful. Alternately, you could create 0.1.x levels and then modify them using a text editor or the Scheme converter script into version 2 levels. See the [File formats](File_formats) page for details.

<br>
</details>

### SuperTux 0.5.x to newest

You can use the in-game level editor to create levels and worldmaps.

Packaging Addons
----------------

Once you've made these beautiful levels, you want to let the world see them.

### Automatically packaging addons

Since SuperTux 0.6.3, you can package addons in one click, using the "Package Add-on" option in the main level editor menu.

### Manually packaging addons

1. Pick a “meaningful name”. This name will be used as file and directory name - the user won't get in touch with it. So pick a short but descriptive name. Your name or acronym should be sufficient, for example. Here, we will use *my-levels* as example.
2. Create a new directory hierarchy: `levels/`*`my-levels`*
3. Copy your levels (\*.stl files) into your that folder.
4. If you made a worldmap, you have to put it n your `levels/`*`my-levels`*`/` as `worldmap.stwm`.
5. To make it an addon, create a *`my-levels`*`.nfo` text file in the top level of your directory hierarchy, and fill it in with the information, listed in [NFO files](#nfo-files).
6. So that it shows up in the “Contrib Levels” -> "Community Contrib Levels" menu, you need to create a `levels/`*`my-levels`*`/info` file. Its contents should look like this:

```
(supertux-level-subset
  (title "<Name as will appear in menu>")
  (description "<Description of your levels>")
  (hide-from-contribs #f)
  (levelset `<Do you have a worldmap? Yes ⇒ #f, No ⇒ #t>`)
  (contrib-type "community")
)
```

7. Use a ZIP utility to package up your directory into `my-levels.zip`.

NFO files
---------

Addon .nfo files look like this:

```
(supertux-addoninfo
  (id "octo-levels")
  (version 1)
  (type "worldmap")
  (title "Octo's Levels")
  (author "Octo")
  (license "GPL 2+ / CC-by-sa 3.0")
)
```

The `id` is a identifier for this addon, it has to be unique across
all addons, as it is used to compare the addons with new ones from
other sources to find updates. It is recomment to use something like
"{author}-{title}". The `id` must be all lowercase and only contain
characters of the set "[a-z][0-9]-", underscore is not allowed as it
is used for the version number.

The `version` number is a simple integer, it should be increased each
time the addon is changed.

The `type` gives an indication of what is contained within the addon,
valid values are "worldmap", "world", "levelset". At the moment this
is only a description for the user and doesn't have any impact on how
the addon is handled.

The .nfo file itself needs to be stored in the top-level directory of
the addon and should be named by the unique id of the addon, i.e.
`/octo-levels.nfo` in this example.

TODO
----

This doesn't tell you all there is to know about modifying SuperTux; check back from time to time for updates. If you are knowledgeable about the following things, try adding them to this tutorial:

-   Intros or extros for levels
-   Scripting .nut files
-   Adding new images or sounds
-   Replacing game files
-   Installing a new supertux executable
