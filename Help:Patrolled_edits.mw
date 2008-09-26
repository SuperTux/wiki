{{PD Help Page}}
<div style="float:right;">__TOC__</div>
'''Patrolled edits''' are a feature which allows specific users to mark items in recent changes as having been "patrolled" or "approved". By default this is only available if you have [[Help:Sysops and permissions|sysop permissions]]

This feature is useful when reviewing recent changes for undesirable edits, link spam and vandalism. This allows people (those who can see it) to coordinate their patrolling activity, such that edits gets checked over once, but with less wasted effort (different people checking the same edit)

== Marking edits as patrolled ==

; To mark an edit as patrolled

#Access [[Special:Recentchanges]]
#:Changes which are not patrolled will be indicated with a red exclamation mark
#Click the ({{mediawiki|m:Help:Diff|diff}}) link next to an edit
#To mark the edit as patrolled, click the ''mark as patrolled'' link

== Customization ==

=== Enabling/disabling ===

Patrolled edits are enabled by default in MediaWiki 1.4. In MediaWiki 1.5 and later, set '''[[Manual:$wgUseRCPatrol|$wgUseRCPatrol]]''' in {{mediawiki|Manual:Configuration settings|LocalSettings.php}}.

<code>$wgUseRCPatrol = true;</code>

=== Permissions ===

==== 1.4 ====

In MediaWiki 1.4, patrolled edits are enabled for all users. To restrict this to sysops, set '''[[Manual:$wgOnlySysopsCanPatrol|$wgOnlySysopsCanPatrol]]''' in {{mediawiki|Manual:Configuration settings|LocalSettings.php}}.

<code>$wgOnlySysopsCanPatrol = true;</code>

==== 1.5+ ====

In MediaWiki 1.5 and later, patrolled edits are enabled for sysops. Use the '''[[Manual:$wgGroupPermissions|$wgGroupPermissions]]''' configuration variable for this.

For instance, to create a ''patrollers'' group:

<code>$wgGroupPermissions['patrollers']['patrol'] = true;</code>

=== Automatic patrolling ===
In MediaWiki 1.6 through 1.8, there is a [[Help:preferences|user preference]] available to users who are able to mark edits as patrolled. When set, this causes their edits to be patrolled automatically.

This option is not available if patrolled edits are switched off.

In MediaWiki 1.9 this user preference has been removed and replaced by a new "autopatrol" right, assigned only to sysops by default. Also, users cannot mark their own edits as patrolled.

=== Marker ===

The formatting of the unpatrolled edit marker can be altered using CSS. The exclamation mark displayed on the Recent changes log is styled using the <code>span.unpatrolled</code>.

{{Languages|Help:Patrolled edits}}
[[Category:Help|Patrolled edits]]
[[Category:Imported help]]
