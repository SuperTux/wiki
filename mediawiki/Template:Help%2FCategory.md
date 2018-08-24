<noinclude>
{{#ifexist: Template:PD Help Page/{{SUBPAGENAME}}|{{PD Help Page/{{SUBPAGENAME}} }}|{{PD Help Page}} }}

This template is to be transcluded in '''public domain''' help pages to categorize those pages.

== Example ==

 <nowiki>{{</nowiki>{{PAGENAME}}|MediaWiki Introduction|lang=zh}}

 <nowiki>{{</nowiki>{{PAGENAME}}|MediaWiki Introduction}}

Default value of {{{lang}}} will be <nowiki>{{SUBPAGENAME}}</nowiki> (which will be "fr", "ja", "th", for, "Page/fr", "Page/ja", "Page/th", respectively).

If you want to specify the sort key, you may instead use the form <nowiki>[[Category:Cat name{{Lang subpage}}|sort key]]</nowiki>.
This template is equivalent to <nowiki>[[Category:Cat name{{Lang subpage}}|{{En pagename}}]]</nowiki>, but it compute <nowiki>{{If en|...}}</nowiki> two times, while this template compute <nowiki>{{If en|...}}}</nowiki> only once.

[[Category:Internationalization templates|Category/Help]]

</noinclude>
{{Help/If en|
[[Category:{{{1|<nowiki>{{{1}}}</nowiki>}}}|{{PAGENAME}}]]|
[[Category:{{{1|<nowiki>{{{1}}}</nowiki>}}}/{{{lang|{{SUBPAGENAME}} }}}|{{BASEPAGENAME}}]]}}<noinclude>[[Category:Imported help]]</noinclude>
