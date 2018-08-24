{{PD Help Page}}
There are four sorts of links in MediaWiki: 
# internal links to other pages in the wiki
# external links to websites
# [[#Interwiki links|interwiki links]] (links to other wikis)
# inter-language links to other language versions of the same wiki

To add an internal link, enclose the name of the page you want to link to in double square brackets. When you save the page, you'll see the new link pointing to your page. If the page exists already, it is displayed in blue, empty pages are displayed in red. Selflinks to the current page are not transformed in URLs but displayed in bold.

The first letter of the target page is automatically capitalized and spaces are represented as underscores (typing an underscore in the link will have a similar effect as typing a space, but is not recommended, since the underscore will also be shown in the text).

== How to link ==
{| {{Prettytable}}
|-
|{{Hl3}}|'''Description'''
|{{Hl3}}|'''You type'''	
|{{Hl3}}|'''You get'''
|-
|Internal link
|<tt><nowiki>[[Main Page]]</nowiki></tt>
|[[Main Page]]
|-
|Piped link 
|<tt><nowiki>[[Main Page|different text]]</nowiki></tt>
|[[Main Page|different text]]
|-
|External link
|<tt><nowiki>http://mediawiki.org</nowiki></tt>
|http://mediawiki.org
|-
|External link,<br />
different title
|<tt><nowiki>[http://mediawiki.org MediaWiki]</nowiki></tt>
|[http://mediawiki.org MediaWiki]
|-
|External link,<br />
numbered
|<tt><nowiki>[http://mediawiki.org]</nowiki></tt>
|[http://mediawiki.org]
|-
|Anchor link 
|<tt><nowiki>[[#See also]]</nowiki></tt>
|[[#See also]]
|-
|Anchor link at another page
|<tt><nowiki>[[Help:Images#See also]]</nowiki></tt>
|[[Help:Images#See also]]
|-
|Category link
|<tt><nowiki>[[:Category:Help]]</nowiki></tt>
|[[:Category:Help]]
|-
|Internal link to image file
|<tt><nowiki>[[media:example.jpg]]</nowiki></tt>
|[[media:example.jpg]]
|-
|Internal link to pdf file
|<tt><nowiki>[[media:example.pdf]]</nowiki></tt>
|[[media:example.pdf]]
|-
|Interwiki link
|<tt><nowiki>[[Wikipedia:MediaWiki]]</nowiki></tt>
|[[Wikipedia:MediaWiki]]
|-
|mailto link
|<tt><nowiki>[mailto:info@example.org email me]</nowiki></tt>
|[mailto:info@example.org email me]
|-
|redirect
|<tt><nowiki>#REDIRECT [[Main Page]]</nowiki></tt>
| &rarr; [[Main Page]]
|}

=== More advanced ===

{| {{Prettytable}}
|-
|{{Hl3}}|'''Description'''
|{{Hl3}}|'''You type'''	
|{{Hl3}}|'''You get'''
|-
|Piped link,<br />
different title
|<tt><nowiki>[[Main Page|<span title="different title">different text</span>]]</nowiki></tt>
|[[Main Page|<span title="different title">different text</span>]]
|-
|External link,<br />
same host unnamed
|<tt><nowiki>[http://{{SERVERNAME}}/pagename]</nowiki></tt>
|[http://{{SERVERNAME}}/pagename]
|-
|mailto named with subject line and body
|<tt><nowiki>[mailto:info@example.org?Subject=URL%20Encoded%20Subject&body=Body%20Text info]</nowiki></tt>
|[mailto:info@example.org?Subject=URL%20Encoded%20Subject&body=Body%20Text info]
|}


----

{{admin tip|tip=
Which protocols (like http:) are allowed for links is controlled by the [http://www.mediawiki.org/wiki/Manual:%24wgUrlProtocols $wgUrlProtocols]<!-- deliberate use of http url, these pages get exported. Should these admin tips even be here? This is supposed to be end user help is it not? --> setting. 
}}

{{admin tip|tip=
To remove the 'external link image' from next to each of the external links, add the following to the page located at <code>MediaWiki:Monobook.css</code> on your wiki.

<pre>
#bodyContent a.external,
#bodyContent a[href ^="gopher://"] {
        background: none;
        padding-right: 0;
}
</pre>
}}

== How to avoid auto-links ==

By default, when you write a URL as is, it will be transformed to an external link.

To avoid that effect, put the URL between &lt;nowiki&gt; start & end tags as in:

 &lt;nowiki&gt;<nowiki>http://mediawiki.org</nowiki>&lt;/nowiki&gt;

== Interwiki links ==
Interwiki links are links from the local wiki to another wiki. For example you can link to the Sunflower article on wikipedia.org by typing <tt><nowiki>[[wikipedia:Sunflower]]</nowiki></tt>. This results in a link like this: [[wikipedia:Sunflower]]

Similar to internal page links, you can create piped links, with alternate link text. e.g. <tt><nowiki>[[wikipedia:Sunflower|big yellow flower]]</nowiki></tt>

Basically this is an abbreviation for longer URLs. A very similar link could be created as a normal external link by typing <tt><nowiki>[http://en.wikipedia.org/wiki/Sunflower Sunflower]</nowiki></tt>, but interwiki links allow you to type out an easy and compact link, almost as if you are linking to a page on your own wiki.

Some interesting things to note:
* Interwiki links are displayed slightly differently to external links, without the little external link icon.
* Complex page names with spaces and other characters are handled elegantly, just as they would be for an internal page link, making this more tidy than creating an external link to a full URL. For example <tt><nowiki>[[wikipedia:Sunflower County, Mississippi]]</nowiki></tt> is in some ways tidier and more elegant than the full URL : <tt>http://en.wikipedia.org/wiki/Sunflower_County%2C_Mississippi</tt>

== See also ==
* [[Help:Linked images|Linked images]]
 
{{Languages|Help:Links}}

[[Category:Help|Links]]
[[Category:Link]]
[[Category:Imported help]]
