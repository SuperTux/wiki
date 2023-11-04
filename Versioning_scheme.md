This page describes the new versioning scheme that will be used for SuperTux.

The scheme
----------

### SuperTux

Releases will have the form of `x.y.z`.

-   `x` is increased only when there is a *major* update or we reach a *major* milestone. When `x` is increased, `y` and `z` are reset to `0`
-   `y` is increased for each new regular, planned released. When `y` is increased, `z` is reset to `0`. Odd versions of `y` indicate a *development branch*. Even versions of `y` indicate a *stable branch*.
-   `z` is increased when there is a bugfix release or minor changes are made, such as a couple new features and new content (eg, new worlds or levels). For development branches, bigger changes are more likely to make it into `z`-releases.

The development branches are used to work our way to a stable release. For example, the `0.3.x` will be used to create a stable `0.4.0` ([Milestone 2](Milestone_2 "wikilink")) release.

While development releases are likely to be stable, they are more likely to receive less testing before a release, so we cannot guarantee their stability.

As a rule, `z`-releases cannot break level editor functionality in stable branches. For development branches you should check the wiki to make sure your version of the SuperTux Editor works with your version of SuperTux. To be sure, if you are using the development branch you should always be using the latest version of both SuperTux and the SuperTux Editor.

### SuperTux Editor

Releases will have the form of `x.y.z`.

-   `x` and `y` will match the `x` and `y` of the SuperTux release the editor works for.
-   `z` is increased when there is a bugfix release or minor changes made to the editor. This number does not necessarily match up with the `z` of the SuperTux release.

### Brown-paper-bag releases

A fourth decimal point number `n`, of the form `x.y.z.n`, will be used for [brown-paper-bag](http://www.answers.com/topic/brown-paper-bag-bug-computer-jargon) releases. Hopefully we never need to use this.

Release branches
----------------

### `0.1.x` releases

This is the [Milestone 1](Milestone_1 "wikilink") branch.

The `0.1.x` releases do not follow the current versioning scheme. `0.1.x` is considered a *stable branch*.

### `0.2.x` releases

There will not be any `0.2.x` releases.

### `0.3.x` releases

The `0.3.x` branch is being used to develop SuperTux 0.4.0. It is implementing the [Milestone 1.9](Milestone_1.9 "wikilink") and [Milestone 2](Milestone_2_Design_Document "wikilink") goals.

There will be no `0.3.2` release. There were some unofficial releases of SuperTux incorrectly labelled as version `0.3.2` so in order to avoid confusion there will be no official `0.3.2` release.

### `0.4.x` releases

SuperTux 0.4.0 will be the next stable ([Milestone 2](Milestone_2 "wikilink")) release.

### `SVN` “releases”

SVN builds will have version numbers of the form `x.y.z-SVN` with an optional version specifier at the end. `x.y.z` will be the latest unstable release, and the version specifier will be the result of running `svnversion`.