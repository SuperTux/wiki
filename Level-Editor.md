## Editor Tutorials

There are various videos on the internet documenting the use of the built-in level editor. This is a list of some of the useful ones. However, due to the nature of the internet this list is probably incomplete. You're always welcome to add new ones!

- [Basic Tutorial](https://www.youtube.com/watch?v=gsuKAy18iWo) by brmbrmcar
- [Advanced Tutorial](https://www.youtube.com/watch?v=drwLEYo8EVQ) by brmbrmcar
- [Basic Tutorial (Part 1/2)](https://www.youtube.com/watch?v=mhSNateb4nI) by Oliver Buo
- [Basic Tutorial (Part 2/2)](https://www.youtube.com/watch?v=NLWhteLNcC8) by Oliver Buo
- [Advanced Tutorial (Part 1/2)](https://www.youtube.com/watch?v=WBdwwcLD-vw) by Oliver Buo
- [Advanced Tutorial (Part 2/2)](https://www.youtube.com/watch?v=UoaGDuBax6E) by Oliver Buo
- [Expert Tutorial](https://www.youtube.com/watch?v=lL3oZbPfw08) by Oliver Buo

## Share Levels

When you finished a level or even more, there is an easy way to share it to the SuperTux community.

### Step 1) Go to the SuperTux folder and check if all files are there.
You can find them at C:\Users\YOUR-USERNAME\AppData\Roaming\SuperTux\supertux2\levels\YOUR-LEVELSETNAME\ on Windows or /home/YOUR-USERNAME/.local/share/supertux2/levels/YOUR-LEVELSETNAME/ on Linux.
There should be some files called level1.stl, level2.stl and so on, depending on the number of levels you have created. Additionally, there will be a file called worldmap.stwm, if you made a world.
The last file should be called "info" without any file ending. It contains the following code:

(supertux-level-subset</br>
(title (_ "Name that should be displayed"))</br>
(description (_ "A short description"))</br>
(levelset #f)</br>
(hide-from-contribs #f)</br>
)

Title: The name of your add-on that should be displayed.</br>
Description: A short description about your add-on. For example you can type in your nickname or the difficulty of your levels.</br>
Levelset: Use #f if you created a worldmap and #t if you didn't.</br>
Hide-from-contribs: If this is set to #t, your levelset won't show up in-game. So just leave it #f.

If you are adding textures, you have to pack your levels as an add-on, otherwise just go on to step 2.
An add-on needs a .nfo-file which looks like this:

(supertux-addoninfo</br>
  (id "Worldmap-ID")</br>
  (version 1)</br>
  (type "world")</br>
  (title "Your Worldmap Name")</br>
  (author "Your Name")</br>
  (license "CC-by-sa 4.0")</br>
)

ID: The ID of your worldmap. You are only allowed to use letters, _ (underscore) and - (minus). To avoid having two add-ons with the same ID, call it "yourname_name-of-your-worldmap". The .nfo file should be named after your ID.</br>
Version: If you updated your worldmap, count up. Only whole numbers are allowed, so don't set it to 1.1 or something.</br>
Type: Use "world" or "worldmap" if you created a worldmap and "levelset" if you don't.</br>
Title: The title of the worldmap.</br>
Author: Your name/nickname.</br>
License: Leave it like this to allow sharing and modification of your worldmap.

Put the images in an image folder in the same way the normal SuperTux images are. You can find them at C:\Program Files\SuperTux\data\images\ (Windows) or /usr/share/supertux2/images/ (Linux). The levels, the worldmap and the "info"-file must be in a folder called levels/WORLDMAP-ID/ and the WORLDMAP-ID.nfo mustn't be placed in any folder. It should look like this example add-on:

![](https://forum.freegamedev.net/download/file.php?id=10828)

### Step 2) Compress it as a .zip-archive
If you don't add any textures, select all files (Ctrl+A) and compress them as a .zip-archive.
However, if you are adding textures, select the "levels" folder, the "images" folder and the "WORLDMAP-ID.nfo" and compress them as a .zip-archive.

### Step 3) Upload
Just sign in at [FreeGameDev.net](https://forum.freegamedev.net/index.php) and create a new topic [at the Add-ons forum](https://forum.freegamedev.net/viewforum.php?f=69). Describe your worldmap, and add one or two screenshots, depending on the number of levels you created. Then attach your .zip-file to the post. __Caution: Files larger than 2MB in size cannot be uploaded.__

## Questions?

Do you still have questions? Visit the [SuperTux forum on FreeGameDev](https://forum.freegamedev.net/viewforum.php?f=66) and ask!
