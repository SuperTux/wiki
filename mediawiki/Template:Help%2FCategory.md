<noinclude>
[[Template:#ifexist: Template:PD Help Page/{{SUBPAGENAME]]|[[Template:PD Help Page/{{SUBPAGENAME]] }}|[[Template:PD Help Page]] }}

This template is to be transcluded in '''public domain''' help pages to categorize those pages.

== Example ==

 <nowiki>[[Template:</nowiki>{{PAGENAME]]|MediaWiki Introduction|lang=zh}}

 <nowiki>[[Template:</nowiki>{{PAGENAME]]|MediaWiki Introduction}}

Default value of [[Template:{lang]]} will be <nowiki>[[Template:SUBPAGENAME]]</nowiki> (which will be "fr", "ja", "th", for, "Page/fr", "Page/ja", "Page/th", respectively).

If you want to specify the sort key, you may instead use the form <nowiki>[[Category:Cat name[[Template:Lang subpage]]|sort key]]</nowiki>.
This template is equivalent to <nowiki>[[Category:Cat name[[Template:Lang subpage]]|[[Template:En pagename]]]]</nowiki>, but it compute <nowiki>[[Template:If en|...]]</nowiki> two times, while this template compute <nowiki>[[Template:If en|...]]}</nowiki> only once.

[[Category:Internationalization templates|Category/Help]]

</noinclude>
{{Help/If en|
[[Category:[[Template:{1|<nowiki>{{{1]]}</nowiki>}}}|[[Template:PAGENAME]]]]|
[[Category:[[Template:{1|<nowiki>{{{1]]}</nowiki>}}}/[[Template:{lang|{{SUBPAGENAME]] }}}|[[Template:BASEPAGENAME]]]]}}<noinclude>[[Category:Imported help]]</noinclude>
