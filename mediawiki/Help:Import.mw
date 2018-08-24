{{H:h|moderator toc}}

Depending on the project settings, sysops can import files: it is in the list of special pages, or [[Special:Import]] can be used. However, on many Wikimedia wikis it is '''currently disabled by default''' and gives "No transwiki import sources have been defined and direct history uploads are disabled." However, pages from [[foundation:]] can be imported to Meta. The act of importing is added to the page history and to [[Special:Log/import]].

How to export, and the format of exported pages, is described at [[Help:export]]. Normally any user can export wiki pages to a file, but to import pages into a wiki from a file, you must have 'Sysop' privileges on that wiki. So if you have your own MediaWiki installation, then you should be able to see the 'Special:Import' page there.

To import wiki pages from your file, simply click browse to locate the file on your local filesystem. 

After importing, you should be able to see any new pages which were in the file. Where pages had the same name as existing pages in the wiki, the pages will be overwritten by the content from the file if the timestamp of the article is newer. If an error ocurred during the import, e.g. due to badly formatted XML in the file, then you may find the import is partially complete (some pages imported, but not all). Since pages are overwritten, attempting the import again should not be a problem.

If you included history information when you performed the export, then you should also see information about the edits in the 'history' of the imported pages, and in the user contributions. The edits will not show up in 'recent changes' (neither positioned at the time of the original edit, nor at the time of importing).

=== Editing the import file ===
Because of the simple readable file format the XML file can easily be edited between exporting and importing. This should be done with caution and integrity, one can make antedated edits and use false user names, and in combination with deletion, one can "[[w:en:historical revisionism|change history]]". Applications of this editing include:
*adding a note to the edit summary about the importing
*changing user names and/or page names to avoid name conflicts (just between the title tags and between the username tags or also in links and signatures)
*changing namespace names into the generic or the applicable ones (ditto)
Note that if two versions of the page have the same timestamp (because one was uploaded with the same timestamp as a preexisting version), the later (imported) version will show up in the edit history but not in the article itself.

=== Merging Histories and Other Complications ===
If the import includes history information, and the edits involved a user name which in the importing project is used by somebody else, then the occurrences of the user name in the XML file should first be replaced by another name to avoid ambiguity. If the user name was not used yet in the importing project then the user contributions are available anyway, although an account is not automatically created.

Just like when a page is referred to in a link, and/or put in a URL, generic namespace names are automatically converted, and if a prefix is not a namespace name the page will arrive in the main namespace. However, e.g. "Meta:" may be ignored (dropped) on a project that uses that prefix for interwiki linking. It may be desirable to change it in the XML file to "Project:" before importing.

If a page name exists already, importing revisions of a page with that name causes the page histories to be merged. Note that after inserting a revision between two existing revisions in the page history, the change made by the user who made the next edit seems different from what it actually has been: to see the actual change made by the user one has to take the diff between the two already existing revisions, not the diff with respect to the inserted one. Therefore this should not be done except to reconstruct the true page history.

An edit summary may refer to, and possibly link to, another page. This may be confusing when the page has been imported but the target page has not.

The edit summary does not automatically show that the page has been imported, but that can be added to the edit summaries in the XML file before importing. That can avoid some potential sources of ambiguity and/or confusion. When editing the XML file with find/replace, note that adding a text to the edit summaries requires distinguishing between edits which already have an edit summary, hence comment tags in the XML file, and those without these tags. If there are multiple pairs of comment tags, only the last one is effective.

=== Large-scale Transfer ===
For a large-scale transfer, somebody with sufficient system privileges can move data within the server, which is more practical than sending large XML files from the server to a user's local computer and then back to the server.

Large files may be rejected for two reasons.  The PHP upload limit, found in PHP configuration file php.ini
<pre>
 ; Maximum allowed size for uploaded files.
 upload_max_filesize = 20M
</pre>

And also the hidden variable limiting the size in the input form.  Found in the mediawiki source code, ''includes/SpecialImport.php''
<pre>   <input type='hidden' name='MAX_FILE_SIZE' value='20000000' /> </pre>

==See also==

* [http://meta.wikimedia.org/wiki/Data_dumps data dumps] describes the maintenance script <tt>maintenance/importDump.php</tt> which provides an alternate import mechanism, but hasn't always remained in working order with recent MediaWiki releases  

{{h:f|enname=Import}}
[[Category:Imported help]]
