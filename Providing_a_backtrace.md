This document describes how to provide a backtrace for reporting bugs when SuperTux crashes.

SuperTux
--------

1.  First, ensure `DEBUG` is enabled so SuperTux is compiled with debugging symbols.
    1.  Run `ccmake .` and make sure `DEBUG` is set to `ON`. Use <enter> to toggle the setting.
    2.  Press `C` then `G` to generate the new configuration and exit.
2.  If you haven't previously run `cmake .`, do so now.
3.  Run `make` to compile SuperTux
4.  Start SuperTux with `gdb ./supertux2`
5.  Enter `run` to start SuperTux. Alternatively, you can enter `run `<params> to start SuperTux with parameters.
6.  When SuperTux crashes, enter `bt` into GDB. This will provide you with the backtrace which can be sent to the [mailing list](mailing_list "wikilink") or included in a

bug report.

### Breakpoints

If you're asked to set a breakpoint, it can be done in GDB using `break `<filename>`:`<linenum> before entering `run`
