{{PD Help Page}}

'''Magic words''' are strings of text that MediaWiki associates with a return value or function, such as time, site details, or page names. This page is about usage of standard magic words; for a technical reference, see {{mediawiki|Manual:Magic words}}.

==General notes==
* '''Inheritance:''' page-dependent magic words will affect or return data about the current page, regardless of whether it is in the page code or a transcluded template.

==Behaviour switches==
A behaviour switch controls the layout or behaviour of the page and can often be used to specify desired omissions and inclusions in the content. They are usually written as an upercase word wrapped with double underscores.

{| {{prettytable}}
|-
!{{Hl2}}| Word
!{{Hl2}}| Description
!{{Hl2}}| Versions
|-
|{{Hl3}} colspan="3"| '''Table of contents'''
|-
| <nowiki>__NOTOC__</nowiki>
| Hides the table of contents (TOC).
|
|-
|<nowiki>__FORCETOC__</nowiki>
| Forces the table of content to appear at its normal position (above the first header).
|
|-
| <nowiki>__TOC__</nowiki>
| Places a table of contents at the word's current position (overriding <nowiki>__NOTOC__</nowiki>). If this is used multiple times, the table of contents will appear at the first word's position.
|
|-
|{{Hl3}} colspan="3"| '''Editing'''
|-
| <nowiki>__NOEDITSECTION__</nowiki>
| Hides the section edit links beside headings.
|
|-
| <nowiki>__NEWSECTIONLINK__</nowiki>
| Adds a link (([[MediaWiki:Addsection|"+" by default]]) beside the "edit" tab for adding a new section on a non-talk page (see {{mediawiki|m:Help:Section#Adding a section at the end}}).
| 1.7+
|-
|{{Hl3}} colspan="3"| '''Categories'''
|-
| <nowiki>__NOGALLERY__</nowiki>
| Used on a category page, replaces thumbnails in the category view with normal links.
| 1.7+
|-
| <nowiki>__HIDDENCAT__</nowiki>
| Used on a category page, hides the category from the lists of categories in its members and parent categories (there is an option in the [[Help:Preferences|user preferences]] to show them).
| 1.13+
|-
| <nowiki>{{DEFAULTSORT:xyz}}</nowiki>
| Used on a categorized page, sets a default [[Help:Categories|category sort key]].
| 1.10+
|-
|{{Hl3}} colspan="3"| '''Language conversion'''
|-
| <nowiki>__NOCONTENTCONVERT__</nowiki><br /><nowiki>__NOCC__</nowiki>
| On wikis with language variants, don't perform any content language conversion (character and phase) in article display; for example, only show Chinese (zh) instead of variants like zh_cn, zh_tw, zh_sg, or zh_hk.
|
|-
| <nowiki>__NOTITLECONVERT__</nowiki><br /><nowiki>__NOTC__</nowiki>
| On wikis with language variants, don't perform language conversion on the title (all other content is converted).
|
|-
|{{Hl3}} colspan="3"| '''Page formatting'''
|-
| <nowiki>{{DISPLAYTITLE:xyz}}</nowiki>
| Format the current page's title header. The value must be equivalent to the default title: only capitalization changes and replacing spaces with underscores. It can be disabled or enabled by {{mediawiki|Manual:$wgAllowDisplayTitle|$wgAllowDisplayTitle}}; disabled by default before 1.10+, enabled by default thereafter.
| 1.7+
|-
| <nowiki>__END__</nowiki>
| Explicitly marks the end of the article, to prevent MediaWiki from removing trailing whitespace. Removed in {{mediawiki|rev:19213|19213}}.
| 
|-
|{{Hl3}} colspan="3"| '''Other'''
|-
| <nowiki>__START__</nowiki>
| No effect.
|
|- 
|  <nowiki>__NOINDEX__</nowiki>
| Tell search engines not to index the page (ie, do not list in search engines' results).
| {{mediawiki|rev:37973|1.13+}}
|-
|  <nowiki>__INDEX__</nowiki>
| Tell search engines to index the page (overrides {{mediawiki|Manual:$wgArticleRobotPolicies|$wgArticleRobotPolicies}}, but not robots.txt).
| 1.13+
|-
|  <nowiki>__STATICREDIRECT__</nowiki>
| On redirect pages, don't allow MediaWiki to automatically update the link when someone moves a page and checks "Update any redirects that point to the original title".
| {{mediawiki|rev:37928|1.13+}}
|-
| <nowiki>#REDIRECT [[Page name]]</nowiki>
| Causes the current page to [[Help:Redirects|redirect]] viewers to another page.
|}

==Variables and parser functions==
Variables return information about the current page, wiki, or date. Their syntax is similar to [[Help:Templates|templates]], but capitalized to help avoid conflicts. If a template has the same name and case as a variable, the variable will be used. Usage of the template can be forced by adding the "msg:" modifier (for example, "<code><nowiki>{{msg:CURRENTYEAR}}</nowiki></code>"). In some cases, adding parameters will force the parser to treat a variable as a template; for example, <code><nowiki>{{CURRENTDAYNAME|x}}</nowiki></code> tries to transclude "Template:CURRENTDAYNAME".

Parser functions are very similar to variables, but operate on user input instead of the current page. The first parameter is delimited by a colon (:) instead of a pipe (|). (This page does not document custom parser functions added by the {{mediawiki|Extension:ParserFunctions|ParserFunctions extension}}.)

===Date & time===
The following variables return the current date and time according to the user's timezone [[Special:Preferences|preferences]], defaulting to the UTC timezone.

Due to MediaWiki and browser caching, these variables frequently show when the page was ''cached'' rather than the current time.

{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
!{{Hl2}}| Versions
|-
|{{Hl3}} colspan="4"| '''Year'''
|-
| <nowiki>{{CURRENTYEAR}}</nowiki>
| {{CURRENTYEAR}}
| Year
|
|-
|{{Hl3}} colspan="4"| '''Month'''
|-
| <nowiki>{{CURRENTMONTH}}</nowiki> 
| {{CURRENTMONTH}}
| Month (zero-padded number)
|
|-
| <nowiki>{{CURRENTMONTHNAME}}</nowiki>
| {{CURRENTMONTHNAME}}
| Month (name)
|
|-
| <nowiki>{{CURRENTMONTHNAMEGEN}}</nowiki>
| {{CURRENTMONTHNAMEGEN}}
| Month ([http://en.wikipedia.org/wiki/genitive genitive form])
|
|-
| <nowiki>{{CURRENTMONTHABBREV}}</nowiki>
| {{CURRENTMONTHABBREV}}
| Month (abbreviation)
| 1.5+
|-
|{{Hl3}} colspan="4"| '''Day'''
|-
| <nowiki>{{CURRENTDAY}}</nowiki>
| {{CURRENTDAY}}
| Day of the month (unpadded number)
|
|-
| <nowiki>{{CURRENTDAY2}}</nowiki>
| {{CURRENTDAY2}}
| Day of the month (zero-padded number)
| 1.6+
|-
| <nowiki>{{CURRENTDOW}}</nowiki>
| {{CURRENTDOW}}
| Day of the week (unpadded number)
|
|-
| <nowiki>{{CURRENTDAYNAME}}</nowiki>
| {{CURRENTDAYNAME}}
| Day of the week (name)
|
|-
|{{Hl3}} colspan="4"| '''Time'''
|-
| <nowiki>{{CURRENTTIME}}</nowiki>
| {{CURRENTTIME}}
| Time (24-hour HH:mm format)
|
|-
| <nowiki>{{CURRENTHOUR}}</nowiki>
| {{CURRENTHOUR}}
| Hour (24-hour zero-padded number)
|
|-
|{{Hl3}} colspan="4"| '''Other'''
|-
| <nowiki>{{CURRENTWEEK}}</nowiki>
| {{CURRENTWEEK}}
| Week (number)
|
|-
| <nowiki>{{CURRENTTIMESTAMP}}</nowiki>
| {{CURRENTTIMESTAMP}}
| [[wikipedia:ISO 8601|ISO 8601]] time stamp
| 1.7+
|}

The following variables do the same as the above, but using the site's local timezone instead of user preferences and UTC:
* <nowiki>{{LOCALYEAR}}</nowiki>
* <nowiki>{{LOCALMONTH}}</nowiki>
* <nowiki>{{LOCALMONTHNAME}}</nowiki>
* <nowiki>{{LOCALMONTHNAMEGEN}}</nowiki>
* <nowiki>{{LOCALMONTHABBREV}}</nowiki>
* <nowiki>{{LOCALDAY}}</nowiki>
* <nowiki>{{LOCALDAY2}}</nowiki>
* <nowiki>{{LOCALDOW}}</nowiki>
* <nowiki>{{LOCALDAYNAME}}</nowiki>
* <nowiki>{{LOCALTIME}}</nowiki>
* <nowiki>{{LOCALHOUR}}</nowiki>
* <nowiki>{{LOCALWEEK}}</nowiki>
* <nowiki>{{LOCALTIMESTAMP}}</nowiki>

===Technical metadata===
Revision variables return data about the '''latest edit to the current page''', even if viewing an older version of the page.
{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
!{{Hl2}}| Versions
|-
|{{Hl3}} colspan="4"| '''Site'''
|-
| <nowiki>{{SITENAME}}</nowiki>
| {{SITENAME}}
| The wiki's site name ({{mediawiki|Manual:$wgSitename|$wgSitename}}).
|
|-
| <nowiki>{{CURRENTVERSION}}</nowiki>
| {{CURRENTVERSION}}
| The wiki's MediaWiki version.
| 1.7+
|-
| <nowiki>{{CONTENTLANGUAGE}}</nowiki>
| {{CONTENTLANGUAGE}}
| The wiki's default interface language ({{mediawiki|Manual:$wgLanguageCode|$wgLanguageCode}})
| 1.7+
|-
|{{Hl3}} colspan="4"| '''Latest revision to current page'''
|-
| <nowiki>{{REVISIONID}}</nowiki>
| {{REVISIONID}}
| Unique ID
| 1.5+
|-
| <nowiki>{{REVISIONDAY}}</nowiki>
| {{REVISIONDAY}}
| Day edit was made (unpadded number)
| 1.8+
|-
| <nowiki>{{REVISIONDAY2}}</nowiki>
| {{REVISIONDAY2}}
| Day edit was made (zero-padded number)
| 1.8+
|-
| <nowiki>{{REVISIONMONTH}}</nowiki>
| {{REVISIONMONTH}}
| Month edit was made (unpadded number)
| 1.8+
|-
| <nowiki>{{REVISIONYEAR}}</nowiki>
| {{REVISIONYEAR}}
| Year edit was made
| 1.8+
|-
| <nowiki>{{REVISIONTIMESTAMP}}</nowiki>
| {{REVISIONTIMESTAMP}}
| Timestamp as of time of edit
| 1.8+
|}

===Statistics===
Numbers returned by these variables contain number separators, but can return raw numbers with the ":R" flag (for example, <code><nowiki>{{NUMBEROFPAGES}}</nowiki></code> = {{NUMBEROFPAGES}} and <code><nowiki>{{NUMBEROFPAGES:R}}</nowiki></code> = {{NUMBEROFPAGES:R}}). Use "|R" for magic words that require a parameter like PAGESINCATEGORY (for example <code><nowiki>{{PAGESINCATEGORY:Help}}</nowiki></code> and <code><nowiki>{{PAGESINCATEGORY:Help|R}}</nowiki></code>).
{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
!{{Hl2}}| Versions
|-
|{{Hl3}} colspan="4"| '''Entire wiki'''
|-
| <nowiki>{{NUMBEROFPAGES}}</nowiki>
| {{NUMBEROFPAGES}}
| Number of wiki pages.
| 1.7+
|-
| <nowiki>{{NUMBEROFARTICLES}}</nowiki>
| {{NUMBEROFARTICLES}}
| Number of pages in main namespace.
|
|-
| <nowiki>{{NUMBEROFFILES}}</nowiki>
| {{NUMBEROFFILES}}
| Number of uploaded files.
| 1.5+
|-
| <nowiki>{{NUMBEROFEDITS}}</nowiki>
| {{NUMBEROFEDITS}}
| Number of page edits.
| {{mediawiki|rev:21319|1.10+}}
|-
| <nowiki>{{NUMBEROFUSERS}}</nowiki>
| {{NUMBEROFUSERS}}
| Number of registered users.
| 1.7+
|-
| <nowiki>{{NUMBEROFADMINS}}</nowiki>
| {{NUMBEROFADMINS}}
| Number of users in the ''sysop'' {{mediawiki|Manual:User rights|group}}.
| 1.7+
|-
| <nowiki>{{NUMBERINGROUP:groupname}}</nowiki>
| {{NUMBERINGROUP:bureaucrat}} <br /><nowiki>({{NUMBERINGROUP:bureaucrat}} used here)</nowiki>
| Number of users in a specific {{mediawiki|Manual:User rights|group}}.
| {{mediawiki|rev:40116|1.14+}}
|-
|{{Hl3}} colspan="4"| '''Per namespace'''
|-
| <nowiki>{{PAGESINNS:2}}</nowiki><br /><nowiki>{{PAGESINNAMESPACE:2}}</nowiki>
| {{PAGESINNS:2}}<br />{{PAGESINNAMESPACE:2}}
| Number of pages in the given [[Help:Namespaces|namespace]] (replace 2 with the relevant namespace ID). Disabled by default, enable with {{mediawiki|Manual:$wgAllowSlowParserFunctions|$wgAllowSlowParserFunctions}}.
| 1.7+
|-
|{{Hl3}} colspan="4"| '''Other'''
|-
| <nowiki>{{PAGESINCATEGORY:Help}}</nowiki><br /><nowiki>{{PAGESINCAT:Help}}</nowiki>
| {{PAGESINCATEGORY:Help}}<br />{{PAGESINCAT:Help}}
| Number of pages in the given [[Help:Categories|category]] (replace "Help" with the relevant category name).
| {{mediawiki|rev:32932|1.13+}}
|-
| <nowiki>{{PAGESIZE:Help:Magic_words}}</nowiki>
| {{PAGESIZE:Help:Magic_words}}
| Returns the byte size of the specified page.
| {{mediawiki|rev:33551|1.13+}}
|}

===URL data===
====URLs====
{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
!{{Hl2}}| Versions
|-
| <nowiki>{{SERVER}}</nowiki>
| {{SERVER}}
| domain URL ({{mediawiki|Manual:$wgServer|$wgServer}})
|
|-
| <nowiki>{{SERVERNAME}}</nowiki>
| {{SERVERNAME}}
| domain name ({{mediawiki|Manual:$wgServerName|$wgServerName}})
|
|-
| <nowiki>{{SCRIPTPATH}}</nowiki>
| {{SCRIPTPATH}}
| relative script path ({{mediawiki|Manual:$wgScriptPath|$wgScriptPath}})
|
|-
| <nowiki>{{localurl:</nowiki>''page name''<nowiki>}}</nowiki><br /><nowiki>{{localurl:page name|</nowiki>''query string''<nowiki>}}</nowiki>
| {{localurl:page name}}<br />{{localurl:page name|query string}}
| relative path to title
|
|-
| <nowiki>{{fullurl:</nowiki>''page name''<nowiki>}}</nowiki><br /><nowiki>{{fullurl:page name|</nowiki>''query_string''<nowiki>}}</nowiki>
| {{fullurl:page name}}<br />{{fullurl:page name|query_string}}
| absolute path to title
| 1.5+
|-
| <nowiki>{{filepath:Wiki.png}}</nowiki>
| {{filepath:Wiki.png}}
| The absolute URL to a media file.
| {{mediawiki|rev:25854|1.12+}}
|-
| <nowiki>{{urlencode:x y z}}</nowiki>
| <code>{{urlencode:x y z}}</code>
| The input encoded for use in URLs.
| {{mediawiki|rev:14273|1.7+}}
|-
| <nowiki>{{anchorencode:x y z}}</nowiki>
| <code>{{anchorencode:x y z}}</code>
| The input encoded for use in URL section anchors (after the '#' symbol in a URL).
| {{mediawiki|rev:16279|1.8+}}
|}

====Page names====
{| {{prettytable}}
|-
!{{Hl2}}| Variable
!{{Hl2}}| Output
!{{Hl2}}| Description
!{{Hl2}}| Versions
|-
| <nowiki>{{FULLPAGENAME}}</nowiki>
| {{FULLPAGENAME}}
| Namespace and page title.
| 1.6+
|-
| <nowiki>{{PAGENAME}}</nowiki>
| {{PAGENAME}}
| Page title.
|
|-
| <nowiki>{{BASEPAGENAME}}</nowiki>
| {{BASEPAGENAME}}
| Page title excluding the current [[Help:Subpages|subpage]] and namespace ("Title" on "Title/foo").
| 1.7+
|-
| <nowiki>{{SUBPAGENAME}}</nowiki>
| {{SUBPAGENAME}}
| The [[Help:Subpages|subpage]] title ("foo" on "Title/foo").
| 1.6+
|-
| <nowiki>{{SUBJECTPAGENAME}}</nowiki>
| {{SUBJECTPAGENAME}}
| The namespace and title of the associated content page.
| 1.7+
|-
| <nowiki>{{TALKPAGENAME}}</nowiki>
| {{TALKPAGENAME}}
| The namespace and title of the associated talk page.
| 1.7+
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
!{{Hl2}}| Versions
|-
| <nowiki>{{NAMESPACE}}</nowiki>
| {{NAMESPACE}}
| Namespace (name)
|-
| <nowiki>{{SUBJECTSPACE}}</nowiki><br /><nowiki>{{ARTICLESPACE}}</nowiki>
| {{SUBJECTSPACE}}<br />{{ARTICLESPACE}}
| Name of the associated content namespace
| 1.7+
|-
| <nowiki>{{TALKSPACE}}</nowiki>
| {{TALKSPACE}}
| Name of the associated talk namespace
| 1.7+
|}

The following are URL-encoded equivalents:
* <nowiki>{{NAMESPACEE}}</nowiki>
* <nowiki>{{SUBJECTSPACEE}}</nowiki>
* <nowiki>{{TALKSPACEE}}</nowiki>

<code><nowiki>{{ns:}}</nowiki></code> returns the localized namespace name for that number constant. The default values are:
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
| <nowiki>{{ns:0}}</nowiki>
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

===Formatting===
{| {{prettytable}}
!{{Hl2}}| Usage
!{{Hl2}}| Output
!{{Hl2}}| Description
!{{Hl2}}| Version
|-
|-
| <nowiki>{{lc:XYZ}}</nowiki>
| {{lc:XYZ}}
| The lowercase input.
| 1.5+
|-
| <nowiki>{{lcfirst:XYZ}}</nowiki>
| {{lcfirst:XYZ}}
| The input with the first character lowercase.
| 1.5+
|-
| <nowiki>{{uc:xyz}}</nowiki>
| {{uc:xyz}}
| The uppercase input.
| 1.5+
|-
| <nowiki>{{ucfirst:xyz}}</nowiki>
| {{ucfirst:xyz}}
| The input with the first character uppercase.
| 1.5+
|-
| <nowiki>{{formatnum:-987654321.654321}}</nowiki>
| {{formatnum:-987654321.654321}}
| The input with decimal and decimal group separators, and localized digit script, according to the wiki's default locale.
| 1.7+
|-
| <nowiki>{{padleft:xyz|5|_}}</nowiki><br /><nowiki>{{padleft:xyz|5}}</nowiki>
| {{padleft:xyz|5|_}}<br />{{padleft:xyz|5}}
| The input (first parameter) padded on the left side to the specified width (second parameter) using the specified character (third parameter). If a padding character isn't specified, '0' is used by default.<br />'''bug:''' multibyte characters are interpreted as two characters, which can skew width. These also cannot be used as padding characters.
| 1.8+
|-
| <nowiki>{{padright:xyz|5|_}}</nowiki><br /><nowiki>{{padright:xyz|5}}</nowiki>
| {{padright:xyz|5|_}}<br />{{padright:xyz|5}}
| Identical to padleft, but adds padding characters to the right side.
|-
| <nowiki>{{DIRMARK}}</nowiki><br /><nowiki>{{DIRECTIONMARK}}</nowiki>
| {{DIRMARK}}<br />{{DIRECTIONMARK}}
| Outputs a unicode-directional mark that matches the wiki's default language's direction (<code>&amp;lrm;</code> on left-to-right wikis, <code>&amp;rlm;</code> on right-to-left wikis), useful in text with multi-directional text.
| 1.7+
|-
| <nowiki>{{plural:2|is|are}}</nowiki>
| {{plural:2|is|are}}
| Outputs the correct given pluralization form (parameters except first) depending on the count (first parameter). Plural transformations are used for languages like Russian based on "count mod 10".
|}

===Miscellaneous===
{| {{prettytable}}
!{{Hl2}}| Usage
!{{Hl2}}| Output
!{{Hl2}}| Description
!{{Hl2}}| Version
|-
| <nowiki>{{#language:eo}}</nowiki> 
| {{#language:eo}}
| The native name for the given language code.
| 1.7+
|-
| <nowiki>{{#special:userlogin}}</nowiki>
| {{#special:userlogin}}
| The localized name for the given canonical Special: page.
| {{mediawiki|rev:17321|1.9+}}
|-
| <nowiki>{{#tag:tagname}}</nowiki><br /><nowiki>{{#tag:tagname|inner content|parameter=value|parameter2=value}}</nowiki>
| ''(depends on parser tag)''
| Alias for XML-style parser or extension tags, but parsing wiki code. Attribute values can be passed as parameter values ('<code><nowiki><tagname attribute="value"></nowiki></code>' &rarr; '<code><nowiki>{{#tag:tagname|attribute=value}}</nowiki></code>'), and inner content as an unnamed parameter ('<code><nowiki><tagname>content</tagname></nowiki></code>' &rarr; '<code><nowiki>{{#tag:tagname|content}}</nowiki></code>').
| [[rev:29482|1.12+]]
|}

{{languages}}

[[Category:Help|{{PAGENAME}}]]
[[Category:Time|{{PAGENAME}}]]
[[Category:Magic words|{{PAGENAME}}]]
[[Category:Imported help]]
