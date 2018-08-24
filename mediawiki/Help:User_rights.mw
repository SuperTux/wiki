{{PD Help Page}}

'''User rights''' are specific access and ability permissions that can be assigned to customizable groups, which can then be assigned to (or removed from) users through the [[Special:Userrights]] interface. For example, the default ''bureaucrat'' group enables the use of the User rights interface.

This feature was introduced in MediaWiki 1.5; see [http://meta.wikimedia.org/wiki/Setting_user_rights_in_MediaWiki setting user rights in MediaWiki] on the Meta-wiki for earlier methods.

==Managing groups==
A default MediaWiki installation assigns certain rights to default groups (see below). You can change the default rights by declaring the {{mediawiki|Manual:$wgGroupPermissions|$wgGroupPermissions array}} in {{mediawiki|LocalSettings.php}} with the syntax "<code>$wgGroupPermissions[&lsquo;''group''&rsquo;][&lsquo;''right''&rsquo;] = ''boolean'';</code>". To change permissions for all groups, use "*" as the group. For example, to disable editing for all users, add "<code>$wgGroupPermissions['*']['edit'] = false;</code>".

In addition to the default groups, you can arbitrarily create new groups using the same array. For example:
<source lang="php">
$wgGroupPermissions['ninja']['bot']    = true;
$wgGroupPermissions['ninja']['block']  = true;
$wgGroupPermissions['ninja']['delete'] = true;
</source>

===Rights and groups===
The following user rights are available:
{| {{prettytable}}
|-
!{{hl2}} | Right
!{{hl2}} | Description
|-
|{{hl3}} colspan="2"| '''Reading'''
|- 
| read
| allows viewing pages not defined in {{mediawiki|Manual:$wgWhitelistRead|$wgWhitelistRead}}.
|-
|{{hl3}} colspan="2"| '''Editing'''
|-
| edit
| allows [[help:editing|editing]] unprotected pages.
|-
| createpage
| allows the creation of new pages (requires the ''edit'' right).
|-
| createtalk
| allows the creation of new talk pages (requires the ''edit'' right).
|-
| move
| allows renaming page titles.
|-
| createaccount
| allows the creation of new user accounts.
|-
| upload
| allows the creation of new images and files.
|-
| reupload
| allows overwriting existing images and files.
|-
| reupload-shared
| allows replacing images and files from a shared repository (if one is set up) with local files.
|-
| upload_by_url
| allows uploading by entering the URL of an external image.
|-
|{{hl3}} colspan="2"| '''Management'''
|-
| delete
| allows the deletion of edits and pages.
|-
| undelete
| allows viewing and restoring deleted edits and pages.
|-
| deletedhistory
| allows viewing deleted revisions, but not restoring.
|-
| protect
| allows locking a page to prevent edits, and editing locked pages.
|-
| block
| allows the blocking of IP addresses, CIDR ranges, and registered users. Block options include preventing editing and registering new accounts, and autoblocking other users on the same IP address.
|-
| blockemail
| allows preventing use of the [[Special:Emailuser]] interface when blocking.
|-
| userrights
| allows the use of the user rights interface, which allows the assignment or removal of groups to any user.
|-
| rollback
| allows one-click reversion of edits.
|-
| patrol
| allows marking edits as legitimate ({{mediawiki|Manual:$wgUseRCPatrol|$wgUseRCPatrol}} must be ''true'').
|-
| editinterface
| allows editing the [[Special:Allmessages|MediaWiki namespace]], which contains {{mediawiki|Manual:Interface|interface messages}}.
|-
| editusercssjs 
| allows editing user's monobook.css, monobook.js, ... subpages.<br/>''(MediaWiki 1.12, so not yet available for non-Wikimedia sites)''
|-
|{{hl3}} colspan="2"| '''Administration'''
|-
| siteadmin
| allows locking and unlocking the database (which blocks all interactions with the web site except viewing).
|-
| import
| allows user to [http://meta.wikimedia.org/wiki/Help:Import import pages] from another wiki.
|-
| importupload
| allows user to [http://meta.wikimedia.org/wiki/Help:Import import pages] from XML files.
|-
| trackback
| allows removal of [http://www.sixapart.com/pronet/docs/trackback_spec trackbacks] (if {{mediawiki|Manual:$wgUseTrackbacks|$wgUseTrackbacks}} is ''true'').
|-
| unwatchedpages
| allows access to [[Special:Unwatchedpages]], which lists pages that no user has watchlisted.
|-
|{{hl3}} colspan="2"| '''Technical'''
|-
| bot
| hides edits from recent changes lists and watchlists by default (can optionally be viewed).
|-
| purge
| allows purging a page without a confirmation step ({{mediawiki|Manual:URL|URL parameter}} "<code>&action=purge</code>").
|-
| minoredit
| allows marking an edit as 'minor'.
|-
| nominornewtalk
| blocks new message notification when making minor edits to user talk pages (requires ''minor edit'' right).
|-
| ipblock-exempt
| makes user immune to blocks applied to his IP address.
|-
| proxyunbannable
| makes user immune to the open proxy blocker, which is disabled by default ({{mediawiki|Manual:$wgBlockOpenProxies|$wgBlockOpenProxies}}).
|-
| autopatrol
| automatically marks all edits by the user as patrolled ({{mediawiki|Manual:$wgUseRCPatrol|$wgUseRCPatrol}} must be ''true'').
|}

The following groups are available:
{| {{prettytable}}
|-
!{{hl2}} | Group
!{{hl2}} | Description
|-
| *
| all users (including anonymous).
|-
| user
| registered accounts.
|-
| autoconfirmed
| registered accounts at least as old as {{mediawiki|Manual:$wgAutoConfirmAge|$wgAutoConfirmAge}} and having at least as many edits as {{mediawiki|Manual:$wgAutoConfirmCount|$wgAutoConfirmCount}}.
|-
| emailconfirmed
| registered accounts with confirmed email addresses.
|-
| bot
| accounts with the ''bot'' right (intended for automated scripts).
|-
| sysop
| users who by default can delete and restore pages, block and unblock users, et cetera.
|-
| bureaucrat
| users who by default can change other users' rights.
|}

===Default rights===
The default rights are defined in [http://svn.wikimedia.org/viewvc/mediawiki/trunk/phase3/includes/DefaultSettings.php?view=markup DefaultSettings.php]. MediaWiki 1.11alpha defines the following:
<source lang="php">
/**
 * Permission keys given to users in each group.
 * All users are implicitly in the '*' group including anonymous visitors;
 * logged-in users are all implicitly in the 'user' group. These will be
 * combined with the permissions of all groups that a given user is listed
 * in in the user_groups table.
 *
 * Functionality to make pages inaccessible has not been extensively tested
 * for security. Use at your own risk!
 *
 * This replaces wgWhitelistAccount and wgWhitelistEdit
 */
$wgGroupPermissions = array();

// Implicit group for all visitors
$wgGroupPermissions['*'    ]['createaccount']   = true;
$wgGroupPermissions['*'    ]['read']            = true;
$wgGroupPermissions['*'    ]['edit']            = true;
$wgGroupPermissions['*'    ]['createpage']      = true;
$wgGroupPermissions['*'    ]['createtalk']      = true;

// Implicit group for all logged-in accounts
$wgGroupPermissions['user' ]['move']            = true;
$wgGroupPermissions['user' ]['read']            = true;
$wgGroupPermissions['user' ]['edit']            = true;
$wgGroupPermissions['user' ]['createpage']      = true;
$wgGroupPermissions['user' ]['createtalk']      = true;
$wgGroupPermissions['user' ]['upload']          = true;
$wgGroupPermissions['user' ]['reupload']        = true;
$wgGroupPermissions['user' ]['reupload-shared'] = true;
$wgGroupPermissions['user' ]['minoredit']       = true;
$wgGroupPermissions['user' ]['purge']           = true; // can use ?action=purge without clicking "ok"

// Implicit group for accounts that pass $wgAutoConfirmAge
$wgGroupPermissions['autoconfirmed']['autoconfirmed'] = true;

// Implicit group for accounts with confirmed email addresses
// This has little use when email address confirmation is off
$wgGroupPermissions['emailconfirmed']['emailconfirmed'] = true;

// Users with bot privilege can have their edits hidden
// from various log pages by default
$wgGroupPermissions['bot'  ]['bot']             = true;
$wgGroupPermissions['bot'  ]['autoconfirmed']   = true;
$wgGroupPermissions['bot'  ]['nominornewtalk']  = true;
$wgGroupPermissions['bot'  ]['autopatrol']      = true;

// Most extra permission abilities go to this group
$wgGroupPermissions['sysop']['block']           = true;
$wgGroupPermissions['sysop']['createaccount']   = true;
$wgGroupPermissions['sysop']['delete']          = true;
$wgGroupPermissions['sysop']['deletedhistory']     = true; // can view deleted history entries, but not see or restore the text
$wgGroupPermissions['sysop']['editinterface']   = true;
$wgGroupPermissions['sysop']['editusercssjs']   = true;
$wgGroupPermissions['sysop']['import']          = true;
$wgGroupPermissions['sysop']['importupload']    = true;
$wgGroupPermissions['sysop']['move']            = true;
$wgGroupPermissions['sysop']['patrol']          = true;
$wgGroupPermissions['sysop']['autopatrol']      = true;
$wgGroupPermissions['sysop']['protect']         = true;
$wgGroupPermissions['sysop']['proxyunbannable'] = true;
$wgGroupPermissions['sysop']['rollback']        = true;
$wgGroupPermissions['sysop']['trackback']       = true;
$wgGroupPermissions['sysop']['upload']          = true;
$wgGroupPermissions['sysop']['reupload']        = true;
$wgGroupPermissions['sysop']['reupload-shared'] = true;
$wgGroupPermissions['sysop']['unwatchedpages']  = true;
$wgGroupPermissions['sysop']['autoconfirmed']   = true;
$wgGroupPermissions['sysop']['upload_by_url']   = true;
$wgGroupPermissions['sysop']['ipblock-exempt']    = true;
$wgGroupPermissions['sysop']['blockemail']      = true;

// Permission to change users' group assignments
$wgGroupPermissions['bureaucrat']['userrights'] = true;

// Experimental permissions, not ready for production use
//$wgGroupPermissions['sysop']['deleterevision'] = true;
//$wgGroupPermissions['bureaucrat']['hiderevision'] = true;

/**
 * The developer group is deprecated, but can be activated if need be
 * to use the 'lockdb' and 'unlockdb' special pages. Those require
 * that a lock file be defined and creatable/removable by the web
 * server.
 */
# $wgGroupPermissions['developer']['siteadmin'] = true;
</source>

==Examples==
===Anonymous users cannot view pages===
This example will disable viewing of all pages not listed in {{mediawiki|Manual:$wgWhitelistRead|$wgWhitelistRead}}, then re-enable for registered users only.
<source lang="php">
$wgGroupPermissions['*']['read']    = false;
$wgGroupPermissions['user']['read'] = true;
</source>

===Anonymous users cannot edit===
This example will disable editing of all pages, then re-enable for registered users only.
<source lang="php">
$wgGroupPermissions['*']['edit']    = false;
$wgGroupPermissions['user']['edit'] = true;
</source>

==See also==
* [[Manual:$wgNamespaceProtection]]
* [[Manual:Preventing access]] (examples)
* [[Extension:Lockdown]]

{{languages|Help:User rights}}

{{DEFAULTSORT:User rights}}
[[Category:Help]]
[[Category:Special Pages]]
[[Category:Imported help]]
