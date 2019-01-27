So you've finished the story mode, and the contrib levels and you want more?
Or you're sick of the in-game worlds and want something new and fresh?
Well, lucky for you, there are:

Add-Ons
=======

**Add-ons** are extensions for *SuperTux* which are distributed
separately from the main game. 

In most cases, they are sets of levels contributed by users or groups of
users in the form of a levelset or an addon (or in some, mutliple levelsets
or worldmaps.)

Some addons may, however, include custom [[tilesets|Tileset]], which may
give them a very distinct look, in terms of tiles, levels, backgrounds,
objects, etc.

Just beware that some add-ons are unstable and may include features that
aren't ready for the main game! Also, add-ons vary in difficulty; some are
*VERY* difficult! You have been warned!

Getting and Playing add-ons
---------------

Add-ons can be downloaded from within *SuperTux*, or from the SuperTux
forum. 

***From In-Game***

To download add-ons from within the game, simply ensure you have an
internet connection, and select “Addons” from the main menu, where you
can choose to install the currently available add-ons.

Once installed, make sure they are enabled and they should show up in
your contributed levels.

***From the Forum***

To get add-ons from the SuperTux forum, just click this link:

[SuperTux Forum](https://forum.freegamedev.net/viewforum.php?f=66)

Once you're there, explore around and find some that seem interesting.

Then, download that add-on and move it's zip file from your downloads
folder to your SuperTux data folder. Then, when you find the data folder,
place the add-on in the add-on folder, enable it in-game, and it should
appear in the contributed levels.

Debugging In-Game Addons
------------------------

The in-game addons are managed in two repositories:

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

Creating Add-Ons
================

Now you're unhappy with the current add-ons, or you feel there aren't enough? Or maybe you want to be creative and make your own levels?

Levels are created in different ways depending on which version you are using, as the format changed between 0.1.x and 0.3.x. 0.3.x has a separate editor and game. 0.5.x + has a built in editor, and 0.6.x has a different format from the previous two. Anyway, these will create some .stl files for you to enjoy.

### SuperTux 0.1.x

Create as many levels as you want using the built-in editor. Try reading the editor help first by pressing F1.

#### Creating Worldmaps

There's another editor from <http://roofrabbit.com/supertux.html#editor> written in VB that you can use to create worldmaps, or you could try to use [FlexLay](http://flexlay.berlios.de).

### SuperTux 0.3.x

Download the SuperTux Editor from [Download/Unstable](Download/Unstable "wikilink"). The [Editor FAQ](Editor_FAQ "wikilink") might be helpful. Alternately, you could create 0.1.x levels and then modify them using a text editor or the [Scheme converter script](http://supertux.lethargik.org/svn/supertux/trunk/supertux/tools/levelconverter-0.1.3_0.2.0.scm) into version 2 levels. See the [File formats](File_formats "wikilink") page for details.

### SuperTux 0.5.x +

In-Game, you can make levels by accessing the editor from the main menu. Each version of the game after this version adds new features to the editor, and 0.6.0+ levels have a slightly different syntax.

Packaging Levels
----------------

Once you've made these beautiful levels, you want to let the world see them. Just follow these easy steps, which will make archives usable directly as addons for 0.3.x and allow one-step unpacking in 0.1.x:

-   Pick a “meaningful name”. This name will be used as file and directory name - the user won't get in touch with it. So pick a short but descriptive name. Your name or acronym should be sufficient, for example. Here, we will use *my-levels* as example.
-   Create a new directory hierarchy: `levels/`*`my-levels`*
-   Copy your levels (\*.stl files) into your that folder.
-   If you made a [worldmap](worldmap "wikilink"), you have to put it
    -   **0.1:** in `levels/worldmaps/` as *`my-levels`*`.stwm`, or
    -   **0.3:** in your `levels/`*`my-levels`*`/` as `worldmap.stwm`.
-   To make it an addon, create a *`my-levels`*`.nfo` text file in the top level of your directory hierarchy and fill it with the following information. See the [\#.nfo files](#.nfo_files "wikilink") section below for details.

`(supertux-addoninfo`
` (kind `“`<Type:`` ``Level,`` ``Level`` ``Subset,`` ``World,`` ``...>`”`)`
` (title "`

<Title Here>
")

` (author `“<Your name here>”`)`
` (license `“<Pick a license; all official levels are at least GPL 2 / CC-by-sa >”`)`
` (http-url `“<Place where you plan to upload it>”`)`
` (file `“<Name of your directory>`.zip`”`)`
`)`

-   So that it shows up in the “Contrib Levels” menu, you need to create an `levels/`*`my-levels`*`/info` file. You really only need this:

`(supertux-world`
` (title (_ `“<Name as will appear in menu>”`))`
` (description `“`<Description`` ``of`` ``your`` ``levels>`”`)`
` (hide-from-contribs #f)`
` (levelset `<Do you have a worldmap? Yes ⇒ #f, No ⇒ #t>`)`
`)`

-   Use a ZIP utility to package up your directory into `my-levels.zip`.
-   Once you're done, your tree should look like this:

**0.1:**

`my-levels.zip`
`!`
`+-- levels/`
`!   !`
`!   +-- my-levels/`
`!   !   !`
`!   !   +-- `*`*.stl`*
`!   !   +-- info`
`!   !`
`!   +-- worldmaps/`
`!       !`
`!       +-- my-levels.stwm`
`!`
`+-- my-levels.nfo`

**0.3:**

`my-levels.zip`
`!`
`+-- levels/`
`!   !`
`!   +-- my-levels/`
`!       !`
`!       +-- `*`*.stl`*
`!       +-- info`
`!       +-- worldmap.stwm`
`!`
`+-- my-levels.nfo`

-   You've made a package. Now log on to [IRC](Contact#IRC "wikilink") and let us know about your addition! :)

### .nfo files

An **.nfo file** is a file in the typical Lisp-syntax which describes your add-on in some detail. It can originate from two locations:

-   As the file *`my-levels`*`/`*`my-levels`*`.nfo` within your add-on.
-   As a text-file retrieved from an URL.

#### Valid keys

  
*(As of [6398](Template:Revision "wikilink"))*

kind  
Type of your add-on. This is used when displaying information about your add-on to the user. If in doubt, use “Levels” here.

title  
Title (name) of your add-on

author  
Your name

license  
License under which your levels are provided. “GPL 2+ / CC-by-sa 3.0” is the preferred license for *SuperTux* content.

http-url  
URL pointing to this add-on, i.e. the .zip-file. Used for downloading the add-on based on the information provided in the (separate) info file.

file  
Filename used to store the add-on. Be conservative and use “*my-levels*.zip”. This field is intended to be used when the info file is downloaded from a URL.

md5  
MD5-sum of your .zip-file. This field only makes sense when downloading the info file from an URL.

Installing Levels
-----------------

This is the hard part. People don't follow these guidelines, because they didn't exist, and so make lots of strange directory layouts. But there are some general rules:

-   If it's advertised as a 0.3.x addon, it probably is. To install this, just unpack it in your supertux data directory, or better yet put it in your .supertux2 directory. (See [Console](Console "wikilink") for the location; it's the directory with the config file in it) Starting with Subversion [5458](Template:revision "wikilink"), you can also put the archives into the data folder without bothering to unpack them.
-   If they followed these instructions for 0.1.x, you can still just unpack the archive into the supertux data directory.
-   For other levels, you'll have to install them manually. Unpack the archive to a convenient location. If there's a README file, see if it has instructions for installation and follow those.
-   If there's no README file, try following the packaging instructions above, skipping the zipping instructions. Then you can copy the stuff in your layout directly into the supertux data directory.

TODO
----

This doesn't tell you all there is to know about modifying SuperTux; check back from time to time for updates. If you are knowledgeable about the following things, try adding them to this tutorial:

-   Intros or extros for levels
-   Scripting .nut files
-   Adding new images or sounds
-   Replacing game files
-   Installing a new supertux executable

<Category:Development>
