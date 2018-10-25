Developer mode enables various features intended to be used by developers of
the game, most notably various [[Cheats]]. This mode cannot be entered by means
of a graphical user interface.

SuperTux 0.3
------------

To enable developer mode, start the game with the `--developer` option.

To do this on macOS, control-click on the SuperTux.app bundle and select 'Open
Contents'. Then open the `MacOS` folder. Open a new terminal window, drag the
SuperTux binary from the `MacOS` folder in that terminal window and type
`--developer`. Hit enter to start SuperTux.

On Linux or UNIX-like systems, run `supertux2 --developer` in a terminal.

Windows users can create a shortcut to the SuperTux exe and append
`--developer` in the *Target* option of the shortcut's properties.
Alternatively you can run this from the command prompt.

The option can be made permanent with:

    (developer #t)

in the SuperTux [[Configuration File]].


SuperTux 0.1
------------

In the SuperTux 0.1 releases, this mode is called Debug Mode. Follow the
process as described above, but instead of the `--developer` option you need to
use the `--debug-mode` option. Also note that the binary is usually called
`supertux` for these releases, and *not* `supertux2`. Therefore, on Linux you
would for example actually run `supertux --debug-mode`.
