{{PD Help Page}}

MediaWiki '''variables''' are strings of text that output as information such as time, site details, or page names.

==Parsing==
The syntax of most variables is similar to [[Help:Templates|templates]], but capitalized to help avoid conflicts. If a template has the same name and case as a variable, the variable will be used. Usage of the template can be forced by adding the "msg:" modifier (for example, "<code><nowiki>{{msg:CURRENTYEAR}}</nowiki></code>").

Page-dependent variables will return data about the currently-viewed page, regardless of whether the variable is in the page code or a transcluded template.

==Variables==
===Date & time===
The following variables return the current date and time according to the user's timezone [[Special:Preferences|preferences]], defaulting to the UTC timezone.

Due to MediaWiki and browser caching, these variables frequently show when the page was ''cached'' rather than the current time.

{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
|-
|colspan="3"| '''Year'''
|-
| <nowiki>{{CURRENTYEAR}}</nowiki>
| {{CURRENTYEAR}}
| Year
|-
|colspan="3"| '''Month'''
|-

| <nowiki>{{CURRENTMONTH}}</nowiki> 
| {{CURRENTMONTH}}
| Month (zero-padded number)
|-
| <nowiki>{{CURRENTMONTHNAME}}</nowiki>
| {{CURRENTMONTHNAME}}
| Month (name)
|-
| <nowiki>{{CURRENTMONTHNAMEGEN}}</nowiki>
| {{CURRENTMONTHNAMEGEN}}
| Month ([http://en.wikipedia.org/wiki/genitive genitive form])
|-
| <nowiki>{{CURRENTMONTHABBREV}}</nowiki>
| {{CURRENTMONTHABBREV}}
| Month (abbreviation)
|-
|colspan="3"| '''Day'''
|-
| <nowiki>{{CURRENTDAY}}</nowiki>
| {{CURRENTDAY}}
| Day of the month (unpadded number)
|-
| <nowiki>{{CURRENTDAY2}}</nowiki>
| {{CURRENTDAY2}}
| Day of the month (zero-padded number)
|-
| <nowiki>{{CURRENTDOW}}</nowiki>
| {{CURRENTDOW}}
| Day of the week (unpadded number)
|-
| <nowiki>{{CURRENTDAYNAME}}</nowiki>
| {{CURRENTDAYNAME}}
| Day of the week (name)
|-
|colspan="3"| '''Time'''
|-
| <nowiki>{{CURRENTTIME}}</nowiki>
| {{CURRENTTIME}}
| Time (24-hour HH:mm format)
|-
| <nowiki>{{CURRENTHOUR}}</nowiki>
| {{CURRENTHOUR}}
| Hour (24-hour zero-padded number)
|-
|colspan="3"| '''Other'''
|-
| <nowiki>{{CURRENTWEEK}}</nowiki>
| {{CURRENTWEEK}}
| Week (number)
|-
| <nowiki>{{CURRENTTIMESTAMP}}</nowiki>
| {{CURRENTTIMESTAMP}}
| ISO 8601 time stamp
|}

The following variables do the same as the above, but using the site's local timezone instead of user preferences and UTC:
* <nowiki>{{LOCALYEAR}}</nowiki>
* <nowiki>{{LOCALMONTH}}</nowiki>
* <nowiki>{{LOCALMONTHNAME}}</nowiki>
* <nowiki>{{LOCALMONTHABBREV}}</nowiki>
* <nowiki>{{LOCALDAY}}</nowiki>
* <nowiki>{{LOCALDAY2}}</nowiki>
* <nowiki>{{LOCALDOW}}</nowiki>
* <nowiki>{{LOCALDAYNAME}}</nowiki>
* <nowiki>{{LOCALTIME}}</nowiki>
* <nowiki>{{LOCALHOUR}}</nowiki>
* <nowiki>{{LOCALWEEK}}</nowiki>
* <nowiki>{{LOCALTIMESTAMP}}</nowiki>

===Statistics and technical details===
====Site====
{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
|-
| <nowiki>{{SITENAME}}</nowiki>
| {{SITENAME}}
| Name of the wiki ({{mediawiki|Manual:$wgSitename|$wgSitename}})
|-
| <nowiki>{{CONTENTLANGUAGE}}</nowiki>
| {{CONTENTLANGUAGE}}
| Default interface language ({{mediawiki|Manual:$wgLanguageCode|$wgLanguageCode}})
|-
| <nowiki>{{NUMBEROFPAGES}}</nowiki>
| {{NUMBEROFPAGES}}
| Number of wiki pages
|-
| <nowiki>{{NUMBEROFARTICLES}}</nowiki>
| {{NUMBEROFARTICLES}}
| Number of pages in main namespace
|-
| <nowiki>{{NUMBEROFFILES}}</nowiki>
| {{NUMBEROFFILES}}
| Number of uploaded files
|}

====Latest revision to a page====
The following variables return data about the '''latest edit to the current page''', even if viewing an older version of the page.

{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
|-
| <nowiki>{{REVISIONID}}</nowiki>
| {{REVISIONID}}
| Unique ID
|-
| <nowiki>{{REVISIONDAY}}</nowiki>
| {{REVISIONDAY}}
| Day edit was made (unpadded number)
|-
| <nowiki>{{REVISIONDAY2}}</nowiki>
| {{REVISIONDAY2}}
| Day edit was made (zero-padded number)
|-
| <nowiki>{{REVISIONMONTH}}</nowiki>
| {{REVISIONMONTH}}
| Month edit was made (unpadded number)
|-
| <nowiki>{{REVISIONYEAR}}</nowiki>
| {{REVISIONYEAR}}
| Year edit was made
|-
| <nowiki>{{REVISIONTIMESTAMP}}</nowiki>
| {{REVISIONTIMESTAMP}}
| Timestamp as of time of edit
|}

===URL data===
====URLs====
{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
|-
| <nowiki>{{SERVER}}</nowiki>
| {{SERVER}}
| domain URL ({{mediawiki|Manual:$wgServer|$wgServer}})
|-
| <nowiki>{{SERVERNAME}}</nowiki>
| {{SERVERNAME}}
| domain name ({{mediawiki|Manual:$wgServerName|$wgServerName}})
|-
| <nowiki>{{SCRIPTPATH}}</nowiki>
| {{SCRIPTPATH}}
| relative script path ({{mediawiki|Manual:$wgScriptPath|$wgScriptPath}})
|-
| <nowiki>{{localurl:</nowiki>''pagename''<nowiki>}}</nowiki><br /><nowiki>{{localurl:pagename|</nowiki>''query string''<nowiki>}}</nowiki>
| {{localurl:pagename}}<br />{{localurl:pagename|query string}}
| relative path to title
|}

====Page names====
{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
|-
| <nowiki>{{FULLPAGENAME}}</nowiki>
| {{FULLPAGENAME}}
| Namespace and page title
|-
| <nowiki>{{BASEPAGENAME}}</nowiki>
| {{BASEPAGENAME}}
| The namespace and page title excluding the current [[Help:subpage|subpage]] ("Title" on "Title/foo")
|-
| <nowiki>{{PAGENAME}}</nowiki>
| {{PAGENAME}}
| Page title
|-
| <nowiki>{{SUBPAGENAME}}</nowiki>
| {{SUBPAGENAME}}
| The [[Help:subpage|subpage]] title ("foo" on "Title/foo")
|-
| <nowiki>{{SUBJECTPAGENAME}}</nowiki>
| {{SUBJECTPAGENAME}}
| The title of the associated content page.
|-
| <nowiki>{{TALKPAGENAME}}</nowiki>
| {{TALKPAGENAME}}
| The title of the associated talk page.
|}

The following are URL-encoded equivalents:
* <nowiki>{{FULLPAGENAMEE}}</nowiki>
* <nowiki>{{PAGENAMEE}}</nowiki>
* <nowiki>{{BASEPAGENAMEE}}</nowiki>
* <nowiki>{{SUBPAGENAMEE}}</nowiki>
* <nowiki>{{SUBJECTPAGENAMEE}}</nowiki>
* <nowiki>{{TALKPAGENAMEE}}</nowiki>

====Namespaces====
{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
|-
| <nowiki>{{NAMESPACE}}</nowiki>
| {{NAMESPACE}}
| Namespace (name)
|-
| <nowiki>{{SUBJECTSPACE}}</nowiki>
| {{SUBJECTSPACE}}
| Name of the associated content namespace
|-
| <nowiki>{{TALKSPACE}}</nowiki>
| {{TALKSPACE}}
| Name of the associated talk namespace
|}

The following are URL-encoded equivalents:
* <nowiki>{{NAMESPACEE}}</nowiki>
* <nowiki>{{SUBJECTSPACEE}}</nowiki>
* <nowiki>{{TALKSPACEE}}</nowiki>

<code><nowiki>{{ns:}}</nowiki></code> returns the localized namespace name for that number of constant. The default values are:

{| {{prettytable}}
|-
!{{Hl2}}| Usage
!{{Hl2}}| Output
|-
| <nowiki>{{ns:-2}} or {{ns:Media}}</nowiki>
| {{ns:-2}}
|-
| <nowiki>{{ns:-1}} or {{ns:Special}}</nowiki>
| {{ns:-1}}
|-
| <nowiki>{{ns:0}} or {{ns:Main}}</nowiki>
| {{ns:0}}
|-
| <nowiki>{{ns:1}} or {{ns:Talk}}</nowiki>
| {{ns:1}}
|-
| <nowiki>{{ns:2}} or {{ns:User}}</nowiki>
| {{ns:2}}
|-
| <nowiki>{{ns:3}} or {{ns:User_talk}}</nowiki>
| {{ns:3}}
|-
| <nowiki>{{ns:4}} or {{ns:Project}}</nowiki>
| {{ns:4}}
|-
| <nowiki>{{ns:5}} or {{ns:Project_talk}}</nowiki>
| {{ns:5}}
|-
| <nowiki>{{ns:6}} or {{ns:Image}}</nowiki>
| {{ns:6}}
|-
| <nowiki>{{ns:7}} or {{ns:Image_talk}}</nowiki>
| {{ns:7}}
|-
| <nowiki>{{ns:8}} or {{ns:MediaWiki}}</nowiki>
| {{ns:8}}
|-
| <nowiki>{{ns:9}} or {{ns:MediaWiki_talk}}</nowiki>
| {{ns:9}}
|-
| <nowiki>{{ns:10}} or {{ns:Template}}</nowiki>
| {{ns:10}}
|-
| <nowiki>{{ns:11}} or {{ns:Template_talk}}</nowiki>
| {{ns:11}}
|-
| <nowiki>{{ns:12}} or {{ns:Help}}</nowiki>
| {{ns:12}}
|-
| <nowiki>{{ns:13}} or {{ns:Help_talk}}</nowiki>
| {{ns:13}}
|-
| <nowiki>{{ns:14}} or {{ns:Category}}</nowiki>
| {{ns:14}}
|-
| <nowiki>{{ns:15}} or {{ns:Category_talk}}</nowiki>
| {{ns:15}}
|}

== Custom variables ==
MediaWiki also supports custom variables defined as part of extensions or specific to a particular installation.  For example, some installations  might find it helpful to have a variable that identifies the name of the sponsoring organization or the portion of the wiki URL that precedes the title if it is liable to change or more complex than <code><nowiki>http://{{SERVERNAME}}</nowiki></code>.


For more information, please see [[Manual:Variables]].

==External links==
{{meta|Help:Variable}}

{{Languages|Help:Variables}}

[[Category:Help|Variables]]
[[Category:Imported help]]
