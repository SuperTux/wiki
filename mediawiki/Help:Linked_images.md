{{PD Help Page}}

[[Help:Images|Images]] on a MediaWiki wiki are designed to link to the description page, so that licensing information, upload history, contributors, and full resolution versions are immediately available to the user when he or she clicks an image. In fact, MediaWiki is designed to prevent manual manipulation of images in wikicode which may circumvent this operation: The '''<tt>&lt;img&gt;</tt>''' tag is specifically not whitelisted in the {{mediawiki|Manual:Sanitizer.php|Sanitizer}}, nor is the '''<tt>background-image</tt>''' CSS attribute.

However, there are several workarounds for those that require them.

==Vanilla install==
If you only have sysop access to the Wiki, these are your best options.

===Site CSS===
The most simplistic method, if your requirements for external images are specialized (that is, restricted to one page or one image), is to add a CSS rule to your MediaWiki:Common.css (or other CSS files, such as MediaWiki:Skinname.css or /skins/skinname/main.css, etc) giving child links of a certain class of object a background image. This method also has some security, as it requires editing the site-wide CSS files, meaning only sysops have access to modify the image shown. 

For example (red sections are parts to configure for each image):

In MediaWiki:Common.css:
 '''<tt>.imagelink_<span style="color:red;">somename</span> a {
   width:<span style="color:red;">100</span>px;
   height:<span style="color:red;">100</span>px;
   display:block;
   text-decoration:none;
   background-image: url("<span style="color:red;"><nowiki>http://fullurltoimage</nowiki></span>") 
 }</tt>'''
In your wikicode:
 '''<tt>&lt;div class="imagelink_<span style="color:red;">somename</span>"&gt;<nowiki>[[</nowiki><span style="color:red;">Some link</span>|&amp;nbsp;<nowiki>]]</nowiki>&lt;/div&gt;</tt>'''

This would give the link the background image specified, as well as the width and height of the image (which you have to set manually). To find the location of an uploaded file, go to the image description page and click the image itself, and copy the image location in the address bar. 

For example on [[:Image:Wiki.png]], the image location is http://upload.wikimedia.org/wikipedia/mediawiki/b/bc/Wiki.png (location format will differ depending on local settings), and the width and height would be set to 135px and 135px. So to make a link to the main page here using that logo, one would add to [[MediaWiki:Common.css]]:
<pre>.imagelink_wikilogo a {
  width:135px;
  height:135px;
  display:block;
  text-decoration:none;
  background-image: url("http://upload.wikimedia.org/wikipedia/mediawiki/b/bc/Wiki.png") 
}</pre>
And then use the wikicode:
<pre><div class="imagelink_wikilogo">[[MediaWiki|&amp;nbsp;]]</div></pre>

Which would give you:
<div class="imagelink_wikilogo">[[MediaWiki|&nbsp;]]</div>

You can also use a thumbnail of an image, but make sure the thumbnail is being used elsewhere, as most installations are not configured to generate thumbnails on demand.

===Inline CSS===
You can also attempt to superimpose an invisible link over an image via CSS, such as is done in [[Template:Click]]. An example of a typical click template is:
<pre><div style="position: relative; width: {{{width}}}; height: {{{height}}}; overflow: hidden;">
<div style="position: absolute; top: 0px; left: 0px; font-size: 100px; overflow: hidden; line-height: 100px; z-index: 3;">[[{{{link}}}|&amp;nbsp;&amp;nbsp;&amp;nbsp;]]</div>
<div style="position: absolute; top: 0px; left: 0px; z-index: 2;">[[Image:{{{image}}}|{{{width}}}|{{{link}}}]]</div>
</div></pre>

Known problems: It doesn't work in text-only browsers, and in screen readers for the disabled, and possibly other situations.  The technique of using [[wikipedia:CSS|CSS]] to change page content also completely breaks an article's [[wikipedia:web accessibility|web accessibility]] by contravening a [[wikipedia:WAI|WAI]] priority-one checkpoint.[http://www.w3.org/TR/WAI-WEBCONTENT/#tech-order-style-sheets]

===Redirect===
A less elegant trick is to make the image description page a redirect to the target. So for example [[:Image:Wiki.png]] would be changed to content:
<pre>#REDIRECT [[MediaWiki]]</pre>
There are several disadvantages to this:
* It doesn't always work, some installations/versions have internamespace redirects disabled.
* The image appears at the top of the article. This is because MediaWiki redirects aren't really redirects, they simply bring the target page's data to the current URL, but on image description pages this is done after the image itself is shown.
* It can only be done once per image.

==Native with configuration change==
If you have server access, but do not want to install any extensions, these solutions may work for you.
===External image syntax===
If you enable {{mediawiki|Manual:$wgAllowExternalImages|$wgAllowExternalImages}} (which allows external images from any domain) or {{mediawiki|Manual:$wgAllowExternalImagesFrom|$wgAllowExternalImagesFrom}} (which restricts the list of domains), anyone can then easily create an "external" link to an "external" image. External simply means: using the full URL rather than a local link, so you can link locally, but you need to use the full URL. The plainlinks class is used to remove the "external link" icon:

 &lt;span class="plainlinks"&gt;<span style="color:red;"><nowiki>[http://linktopage http://linktoimage]</nowiki></span>&lt;/span&gt;

So for example, were external images allowed here, you could link to the {{mediawiki|MediaWiki|main page}} with http://upload.wikimedia.org/wikipedia/mediawiki/b/bc/Wiki.png using wikicode like:

 &lt;span class="plainlinks"&gt;<nowiki>[{{fullurl:MediaWiki}} http://upload.wikimedia.org/wikipedia/mediawiki/b/bc/Wiki.png]</nowiki>&lt;/span&gt;

This has the disadvantage of not registering the link, or the image use, as well as not being easily portable to forks and mirrors.

===Raw HTML===
If you enable {{mediawiki|Manual:$wgRawHtml|$wgRawHtml}}, you can use '''<tt>&lt;img&gt;</tt>''' tags freely, but this method is highly insecure.

There are, however, some extensions to make it safer, see {{mediawiki|Manual:$wgRawHtml#Related_Extensions}} for details.

==via Extension==
If you are willing to install an extension, several extensions have been created to address this issue:
*{{mediawiki|Extension:ImageMap}} - advanced image shape-link extension, uses the html USEMAP features ''(xml tag)''
*{{mediawiki|Extension:LinkedImage}} - image links ''(XML tag)''
*{{mediawiki|Extension:Icon}} - image links ''(parser function)''

Or you can invent your own linked image syntax, by writing an extension that registers it as a parser hook. See {{mediawiki|Manual:Tag extensions}} for information on extending MediaWiki syntax.

==Other options==
If you want, you can do some more drastic things, such as modify /includes/Sanitizer.php (where the HTML tag whitelist is), and add &lt;img /&gt; to the list of allowed tags.

==See also==
*[[Help:Contents]]
*[[Help:Links]]
*[[Help:Images]]

[[Category:Help|Linked images]]
[[Category:Imported help]]
