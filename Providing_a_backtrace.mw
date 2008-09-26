This document describes how to provide a backtrace for reporting bugs when SuperTux crashes.

== SuperTux ==

# First, ensure <tt>DEBUG</tt> is enabled so SuperTux is compiled with debugging symbols.
## Run <tt>ccmake .</tt> and make sure <tt>DEBUG</tt> is set to <tt>ON</tt>. Use <tt><enter></tt> to toggle the setting.
## Press <tt>C</tt> then <tt>G</tt> to generate the new configuration and exit.
# If you haven't previously run <tt>cmake .</tt>, do so now.
# Run <tt>make</tt> to compile SuperTux
# Start SuperTux with <tt>gdb ./supertux2</tt>
# Enter <tt>run</tt> to start SuperTux. Alternatively, you can enter <tt>run <params></tt> to start SuperTux with parameters.
# When SuperTux crashes, enter <tt>bt</tt> into GDB. This will provide you with the backtrace which can be sent to the [[mailing list]] or included in a 
bug report.

=== Breakpoints ===

If you're asked to set a breakpoint, it can be done in GDB using <tt>break <filename>:<linenum></tt> before entering <tt>run</tt>
