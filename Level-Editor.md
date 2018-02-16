## Editor Tutorials

There are various videos on the internet documenting the use of the built-in level editor. This is a list of some of the useful ones. However, due to the nature of the internet this list is probably incomplete. You're always welcome to add new ones!

- [Basic Tutorial](https://www.youtube.com/watch?v=gsuKAy18iWo) by brmbrmcar
- [Advanced Tutorial](https://www.youtube.com/watch?v=drwLEYo8EVQ) by brmbrmcar
- [Basic Tutorial (Part 1/2)](https://www.youtube.com/watch?v=mhSNateb4nI) by Oliver Buo
- [Basic Tutorial (Part 2/2)](https://www.youtube.com/watch?v=NLWhteLNcC8) by Oliver Buo
- [Advanced Tutorial (Part 1/2)](https://www.youtube.com/watch?v=WBdwwcLD-vw) by Oliver Buo
- [Advanced Tutorial (Part 2/2)](https://www.youtube.com/watch?v=UoaGDuBax6E) by Oliver Buo
- [Expert Tutorial](https://www.youtube.com/watch?v=lL3oZbPfw08) by Oliver Buo

## Sharing Levels

When you finished creating a level or even more, it is possible to share it with the SuperTux community.

### Getting the Relevant Files

You can find them at `C:\Users\YOUR-USERNAME\AppData\Roaming\SuperTux\supertux2\levels\YOUR-LEVELSETNAME\` on Windows or `/home/YOUR-USERNAME/.local/share/supertux2/levels/YOUR-LEVELSETNAME/` on Linux.
There should be some files called `level1.stl`, `level2.stl` and so on, depending on the number of levels you have created. Those files contain the actual levels you created.
If you created a worldmap, there will also be a file called `worldmap.stwm`. That file stores the content of the worldmap.

### The `info` File

Another file should be called `info` without any file ending. It contains the following code:

```
(supertux-level-subset
  (title (_ "Name that should be displayed"))
  (description (_ "A short description"))
  (levelset #f)
  (hide-from-contribs #f)
)
```

| Property             | Description                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `title`              | The name of your add-on that will be displayed to players. This can be translated with a language file.                           |
| `description`        | A short description about your add-on. Write a short summary. This can be translated with a language file.                        |
| `levelset`           | Use `#f` if you created a worldmap and `#t` if you didn't.                                                                        |
| `hide-from-contribs` | If this is set to #t, your levelset won't show up in-game. This should only be used internaly in SuperTux, so just leave it `#f`. |

### The `.nfo` File

Every add-on needs an `.nfo`-file which looks like this:

```
(supertux-addoninfo
  (id "Worldmap-ID")
  (version 1)
  (type "world")
  (title "Your Worldmap Name")
  (author "Your Name")
  (license "CC-by-sa 4.0")
)
```

| Property  | Description                                                                                                                                                                                                                        |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`      | The ID of your worldmap. You are only allowed to use letters, _ (underscore) and - (minus). To avoid having two add-ons with the same ID, call it `yourname_name-of-your-worldmap`. The `.nfo` file should be named after your ID. |
| `version` | If you updated your worldmap, count up. Only whole numbers are allowed, so don't set it to 1.1 or something.                                                                                                                       |
| `type`    | Use `world` or `worldmap` if you created a worldmap and `levelset` if you didn't.                                                                                                                                                  |
| `title`   | The title of the worldmap.                                                                                                                                                                                                         |
| `author`  | Your name/nickname.                                                                                                                                                                                                                |
| `license` | Leave it like this to allow sharing and modification of your worldmap.                                                                                                                                                             |

### Creating the Add-On Structure

If you just zip it like this, you are already able to share it, but the player has to save it in the `supertux2/levels/` directory and unpack it first.

So, create a directory called `levels/YOUR-WORLDMAP-ID/` and move the `level.stl`, `worldmap.stwm` and the `info`-file into it (but not the `.nfo`-file!). Put all graphics in an `images/` directory, all sounds into `sounds/` and music into `music/` in the same structure SuperTux uses. You can find the original graphics at  `C:\Program Files\SuperTux\data\images\` (Windows) or `/usr/share/supertux2/images/` (Linux). But be careful, as the file locations in the levels must match the directory structure you create.
The file structure should now look like this:

![](https://forum.freegamedev.net/download/file.php?id=10828)

Now the player can simply save this file in `supertux2/addons/` and enable it in-game at the "Add-ons" menu by checking the checkbox.

### Compressing the Add-On as a `.zip`-Archive

Select the levels-directory, the `.nfo`-file - and if you added additional content - those directories and compress them as a `.zip`-file.

### Uploading the Add-On

Now you can upload your file. We recommend creating a new topic [at the Add-ons forum](https://forum.freegamedev.net/viewforum.php?f=69). Describe your worldmap, and add one or two screenshots, depending on the number of levels you created. Then attach your .zip-file to the post. *Caution: Files larger than 2MB in size cannot be uploaded there.*

## Questions? Problems?

Do you still have questions? Or do you experience any problems? Just contact us and ask.
