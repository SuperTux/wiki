{{PD Help Page}}

This page explains the image syntax when editing the wiki. Before using images, your wiki must have file uploads enabled (see the {{mediawiki|Manual:Configuring_file_uploads|technical manual}} for details) and you have to [[Help:Managing files|upload a file]].

__TOC__
{| {{Prettytable}}
|-
|{{Hl3}}|'''Description'''
|{{Hl3}}|'''You type''' 
|{{Hl3}}|'''You get'''
|-
|Embed image<br /> (with alt text)
|
<code><nowiki>[[Image:Example.jpg|Sunflowers]]</nowiki></code>
|
[[Image:Example.jpg|Sunflowers]]
|-
|Link to description page
|
<code><nowiki>[[:Image:Example.jpg]]</nowiki></code><br />
<code><nowiki>[[:Image:Example.jpg|Sunflowers]]</nowiki></code>
|
[[:Image:Example.jpg]]<br />
[[:Image:Example.jpg|Sunflowers]]
|-
|Link directly to file
|
<code><nowiki>[[Media:Example.jpg]]</nowiki></code><br />
<code><nowiki>[[Media:Example.jpg|Sunflowers]]</nowiki></code>
|
[[Media:Example.jpg]]<br />
[[Media:Example.jpg|Sunflowers]]
|-
|Thumbnail<br /> (centered, 100 pixels<br /> wide, with caption)
|
<code><nowiki>[[Image:Example.jpg|center|thumb|100px|Sunflowers]]</nowiki></code>
|
[[Image:Example.jpg|center|thumb|100px|Sunflowers]]
|-
|Border<br /> (100 pixels) <br /> Results in a very small gray border
<!-- Note: because the fine gray border can not be seen when used on Image:Exaple.jpg (sunflowers image), an image with a white background is used -->
|
<code><nowiki>[[Image:Example-white-bg.jpg|border|100px]]</nowiki></code>
|
[[Image:Example-white-bg.jpg|border|100px]]
|-
|Frameless<br />Like thumbnail, respect user preferences for image width but without border and no right float.
|
<code><nowiki>[[Image:Example.jpg|frameless]]</nowiki></code>
|
[[Image:Example.jpg|frameless]]
|}

== Syntax ==
The full syntax for displaying an image is:
 <code><nowiki>[[Image:{name}|{options}]]</nowiki></code>
Where options can be zero or more of the following, separated by pipes:
*<code>thumb</code>, <code>thumbnail</code>, or <code>frame</code>: Controls how the image is formatted
*<code>left</code>, <code>right</code>, <code>center</code>, <code>none</code>: Controls the alignment of the image on the page
*<code>baseline</code>, <code>sub</code>, <code>super</code>, <code>top</code>, <code>text-top</code>, <code>middle</code>, <code>bottom</code>, <code>text-bottom</code>: Controls the vertical alignment of the image on the page
*<code>{width}px</code>: Resizes the image to the given width in pixels
*<code>{caption text}</code>: Must not end with "px"
* Special cases:
** <code>page=1</code>: displays the specified page when showing a djvu file.

The options can be given in any order. If a given option does not match any of the other possibilities, it is assumed to be the caption text. Caption text can contain wiki links or other formatting.

== Other files ==
You can link to an external file using the same syntax used for linking to an external web page. 
*<code><nowiki>[http://url.for/some/image.png]</nowiki></code>
Or with different text:
*<code><nowiki>[http://url.for/some/image.png link text here]</nowiki></code>

If it is enabled on your wiki (see {{mediawiki|Manual:$wgAllowExternalImages}}), you can also embed external images. To do that, simply insert the image's url:
*<code><nowiki>http://url.for/some/image.png</nowiki></code>

== Gallery of images ==
It's easy to make a gallery of thumbnails with the <code><nowiki><gallery></nowiki></code> tag. The syntax is:
<pre>
<gallery>
Image:{filename}|{caption}
Image:{filename}|{caption}
{...}
</gallery>
</pre>
Captions are optional, and may contain wiki links or other formatting.

for example:
<pre>
<gallery>
Image:Example.jpg|Item 1
Image:Example.jpg|a link to [[Help:Contents]]
Image:Example.jpg
Image:Example.jpg
Image:Example.jpg|''italic caption''
Image:Example.jpg|on page "{{PAGENAME}}"
</gallery>
</pre>
is formatted as:
<gallery>
Image:Example.jpg|Item 1
Image:Example.jpg|a link to [[Help:Contents]]
Image:Example.jpg
Image:Example.jpg
Image:Example.jpg|''italic caption''
Image:Example.jpg|on page "{{PAGENAME}}"
</gallery>

== See also ==
* [[Help:Linked images|Linked images]]

==External Link==
* [[wikipedia:Project:Extended image syntax|Wikipedia:Extended image syntax]]

{{Languages|Help:Images}}

[[Category:Help|Images]]
[[Category:Imported help]]
