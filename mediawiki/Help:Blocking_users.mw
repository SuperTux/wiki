{{PD Help Page}}
'''Blocking users''' is an action that [[Help:Sysops and permissions|sysops]] can perform upon users or IP addresses to prevent them from editing the wiki.

==Blocking==
Blocking users is fairly straightforward, visit [[Special:BlockIP]] and follow these steps:

# '''IP Address or username''': Enter in the username, IP address, or [[Help:Range blocks|IP range]] to block in the "User" field. If blocking a username, make sure to check the spelling since nonexistent users can be blocked as well. Instead of typing this information in manually, it is also possible to click on a "block" link in recent changes, contributions pages, or history pages, which will automatically fill in this field with the appropriate username or IP address. A "Block this user" link is also present in the toolbox when viewing User and User talk pages.
# '''Expiration''': Select when the block should expire from the drop-down, or manually type in an expiration time of the block. When manually typing in a time, follow the [http://www.gnu.org/software/tar/manual/html_node/Date-input-formats.html GNU standard format]. The default options in the drop-down may be modified at [[MediaWiki:Ipboptions]].
# '''Reason (optional)''': The reason selected from the drop-down combined with the other/additional reason specified will be used as the message displayed to the blocked user when they try to edit. The default reasons in the drop-down may be modified at [[MediaWiki:Ipbreason-dropdown]].
# '''Select additional block options (optional)''': Depending on if a username or IP is being blocked and other options that may have been enabled, some or all of these options will be displayed on the form. Please see the [[#Configuration|configuration]] section for information of how to enable or disable some of the following options.
#* ''Block anonymous users only'': This option is only available when blocking an IP address. When selected, registered users who try to edit using a blocked IP address will still be able to edit. Otherwise, they will be unable to edit as well.
#* ''Prevent account creation'': Selecting this option will prevent the blocked username or IP address from creating new accounts.
#* ''Automatically block the last IP address used by this user, and any subsequent IPs they try to edit from'': This option is only available when blocking a username. When selected, the user's IP will become "autoblocked" (these show up as numbers such as #17 on [[Special:IPBlockList|the active block list]]) for a short period of time and any other IP addresses that the blocked user tries to edit from will be blocked as well.
#* ''Prevent user from sending e-mail'': This option is only available when blocking a username. When this option is selected, the user will be unable to use the [[Special:EmailUser]] interface.
#* ''Hide username from the block log, active block list and user list'': When selected, the blocked username or IP address will not be added to the [[Special:Log/block|block log]], the [[Special:IPBlockList|active block list]], or the [[Special:ListUsers|user list]]. Other users with the ability to view these hidden entries will still be able to see and unblock the username or IP address. This option is not enabled in a default installation of MediaWiki, see the [[#Configuration|configuration]] section for information on how to enable it if this functionality is desired.
#* ''Watch this user's user and talk pages'': When selected, this adds the blocked user's user page and user talk page to your watchlist.
# Double-check everything you entered and click on '''Block this user'''. A message should appear saying if the block was successful or unsuccessful.

==Unblocking==
To unblock a username or IP address, go to the [[Special:IPBlockList|active block list]] and click on the (unblock) link next to the user or IP you wish to unblock. Then, enter in an optional reason and click on the unblock button. A message should appear saying if the unblock was successful or unsuccessful.

==What it means to be blocked==
Blocked users are unable to [[Help:Editing pages|edit pages]], [[Help:Managing files|upload files]], [[Help:Moving a page|move pages]], and perform other actions that additional {{mediawiki|Manual:User rights|user rights}} would grant. Sysops or others with access to the blocking and unblocking interface may still block and unblock others (including themselves) while blocked.

Depending on the [[#Configuration|site configuration]], blocked users may still be allowed to edit their own user talk page.

==Configuration==
The configuration options below can be set in {{mediawiki|Manual:LocalSettings.php|LocalSettings.php}} and can be used to enable or disable certain aspects of the blocking interface.

* <code>{{mediawiki|Manual:$wgSysopUserBans|$wgSysopUserBans}}</code> controls the ability for sysops to block usernames. This is true by default.
* <code>{{mediawiki|Manual:$wgSysopRangeBans|$wgSysopRangeBans}}</code> controls the ability for sysops to block ranges of IP address. This is true by default.
* <code>{{mediawiki|Manual:$wgAutoblockExpiry|$wgAutoblockExpiry}}</code> controls how many seconds need to pass until a block on an "autoblocked" IP address will expire. The default is 86400 seconds, which is the same as 24 hours (one day)
* <code>{{mediawiki|Manual:$wgBlockAllowsUTEdit|$wgBlockAllowsUTEdit}}</code> controls whether or not a blocked user is able to edit their own user talk page. This is false by default.
* <code>{{mediawiki|Manual:$wgSysopEmailBans|$wgSysopEmailBans}}</code> and the ''blockemail'' {{mediawiki|Manual:User rights|user right}} control the ability for sysops to prevent users from using the [[Special:EmailUser]] interface. <code>$wgSysopEmailBans</code> is true by default.
* The ''hideuser'' user right controls the ability for sysops to prevent a blocked user from appearing in the block log, the active block list, and the user list.

==See Also==
*{{mediawiki|Manual:Block and unblock}}

{{Languages|Help:Blocking users}}
[[Category:Help|Blocking users]]
[[Category:Imported help]]
