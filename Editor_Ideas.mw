{{Attention|s=This page is mainly for developers. Users: Please mark your comments so that we can see that you are users or use the talk page.}}

This page is about ideas that aren't ready to go into bug tracker as feature requests yet and they might be discarded (quite more likely than those that make it into the bug tracker).


== QA checks ==
Currently we have a function to check for invalid tile IDs in a sector (right click on sector tab to find it), although it is useful it could be extended to more things.
Some examples are:
* Change the check for invalid tile IDs in a sector to also highlight the bad ones.
* Check that there is a sector called "main" that contains a spawnpoint called "main" as well.
* Check that there is at least one spawn point in each sector and that something calls it.
* Check for other common issues (mainly issues that can happen in converted levels from 0.1.x and issues due to changes in the game/editor to find and fix all affected levels and such)
* Check for "bad" tile combinations, for example: if we have a grass top tile the tile below it should be a specific one, note that we must check in all tilemaps for this.
* Refactor endseq tiles into Sequence Triggers.
* Batch checking all levels in a directory (command line?).

=== Ideas for (possible) implementation ===
Some main class and other classes that in some way register with it and is called as needed, either an event/delegate scheme (parameter could be current level, application interface and/or other stuff depending on how we do it). A more complex way, but that would be better if we want a method to auto-fix (simpler) issues as well, would be based on interfaces like (in pseudo-code):
 interface QAChecker {
   public bool Check(Level level, IQAReporter QAReporter);
   public bool CanFix { get; }
   public bool Fix(Level level, IQAReporter QAReporter);
 }
Where IQAReporter would be some interface to show dialogs about errors and such. The methods could return true/false for if the check found problems, and for the Fix method, if the fix did succeed. CanFix would be if this QA checking class can fix issues as well as detect them. Note that this is just a quick mockup of it, and it is possible that it wouldn't work at all.
