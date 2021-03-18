Since the game has been abandoned and picked up by varying people/teams over the years many core aspects, design elements
became a mish mash of ways to insure retrocompatibility. Understandable, but it is only causing more inconsistencies and
confusion as development goes on. Like a vicious circle.

With the release of **v0.7** we will freeze development on the game for a while to tackle all of the possible wrong designs
that we kept only for retrocompatibility. Fixing them will then be the main focus for **v0.7.1** after which development
will resume as normal.

The following list will contain every single flaw we could find. It is yet not complete as we are still scanning through
the game's files.

- *If you discovered any flaws yourself, we would like to encourage you to [notify us](https://www.supertux.org/contact.html).
  Thank you in advance!*

# Contents
1. [Code](#code)
2. [Graphics](#graphics)
3. [Data Sorting](#data-sorting)

### Other considerations
1. [Auto-converter](#auto-converter)
2. [Versioning](#versioning)


Code
----

* [ ] (insert task here)

---

Graphics
--------

* [ ] Remove duplicate graphics and tile IDs
* [ ] Get rid of old and unused graphics
    - Does not including the retro category!

---

Data Sorting
------------

* [ ] Rename `ice_world.strf` to `worldmap.strf` 
    - Old `worldmap.strf` shall become `deprecated.srtf` if not fully removed
* [ ] Relocate explosion graphics to `images/particles/` instead of `images/object/`

---

Other considerations
====================

### Auto-converter

Each "milestone" of no-retrocompatibility could come with a tool which would automatically detect the version of the game
used to edit a certain level, and would make the necessary modifications to convert old content to the new engine. Upon
opening a level using a deprecated feature, the editor will ask the user if they want to convert the level to the newer
features, and warn them of features that will be dropped if any of them has no equivalent in the newer version.

In case there are multiple "milestones", each converter should only care about converting from the newly deprecated version
to the latest version; if necessary, the game keep all converters through time and uses them in a chain.

### Versioning

Although it is possible to detect incompatibilities inside the levels directly (e. g. if a wordmap uses `worldmap.strf` and
uses tile ID 9, that's an ID used only in the deprecated version, so this level needs to be converted), there should also be
a new versioning system inside the level files, which would hold a number to be incremented each time a deprecation happens.

This would make it easier to know how levels would need to be updated. Levels without version number would be assumed to be pre-0.7.0.
