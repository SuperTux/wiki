How to Translate
----------------

1.  Register on our On-line translation manager [1](https://www.transifex.com/projects/p/supertux/)
2.  Request à New language or join an existing one
3.  Just translate on line

If you have no internet access for translation work, then download po files from Transifex, complete them on your local system with Poedit. then upload them on transifex. If letters/alphabets are missing ask the language guru ( [[Giby|User#Giby]] ) to add it after completing all po files on Transifex.

Notes for Translators
---------------------

-   If there isn't a good translation for some term (e.g. “Credits” or “Sound”), you might consider to **simply keep it** in English. It's better to allow users to make an educated guess than to confuse them by displaying **meaningless** or garbled text.

<!-- -->

-   In English, there is only one singular second person form: “You”. If your language has more than one - a **personal** and an **impersonal** form - remember that this is a game, so you should use the personal one. Note that if it can be **omitted** your language, you should probably do so.

<!-- -->

-   Names like **SuperTux, Tux, Penny or Nolok** should not be translated. If you really think one of these is too strange for your language, first inform us on our mailing list. Names of minor characters like **Mr. Ice Block** can (and should) be translated.

<!-- -->

-   If somewhere in the game, after translating a string, it doesn't look well (**bad aligment**, overlaps other text...), let us know and we will fix it.

<!-- -->

-   Do not stick to the original text too much, just try to **capture the meaning of a phrase**. This especially true for level names, which often play on phrases only known to english speakers. In this case it's often better to make up a level name that is close to the original, but doesn't use a **wordplay**.

<!-- -->

-   Have a friend **play the game** using your translation. If any phrase needs additional explanation, consider changing it.

Tools
-----

There's a number of tools you can use to edit the .po files:

-   [KBabel](http://i18n.kde.org/tools/kbabel/) - matured KDE translation program
-   [poEdit](http://poedit.sourceforge.net/) - multi-platform po editor (runs on Windows and Unix/Linux)
-   QTranslator - comes with Qt, also multi-platform
-   (X)Emacs - commonly used for translation with the respective plugin
-   Any text editor - of course you can also simply use a text editor. Just make sure the file encoding really matches the stuff stated in the .po header.

Translations
------------

SuperTux [Milestone 2](Milestone_2 "wikilink") supports localization. This means you can play SuperTux in any of the languages supplied with the game, as well as make your own translation.

SuperTux will try to auto-detect what language to display text in. If auto-detection fails or if you want to play in a certain language, you can force SuperTux to use a specific locale by setting the LANG environment variable to the handle of your language (e.g. “en”; see the following sections for all available languages).

Setting an environment variable can be done in a number of ways, depending on your operating system.

Linux users might run

`LANG=`“`en`”` ./supertux`

Windows users might run

`set LANG=en`
`supertux.exe`

If setting the environment variable `LANG` doesn't work, you may try using the variable `SUPERTUX_LANG` instead.

Existing Translations
---------------------

Please add yourself to this list if you are working on a new translation, so that others can contact you. Please log in if you change an entry in this list.

<table>
<thead>
<tr class="header">
<th><p>Language</p></th>
<th><p>Code</p></th>
<th><p>Translator</p></th>
<th><p>In<br />
release</p></th>
<th><p>In<br />
revision</p></th>
<th><p>Comments</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Catalan</p></td>
<td><p>ca</p></td>
<td><p>Martí Bosc &lt;estopenc@hotmail.com&gt;</p></td>
<td></td>
<td><p>r4873</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Czech</p></td>
<td><p>cs</p></td>
<td><p>Ondra Hosek &lt;ondra.hosek@gmail.com&gt;</p></td>
<td><p>0.3.0</p></td>
<td><p>r4415</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>Danish</p></td>
<td><p>da</p></td>
<td><p>Anders &lt;anders@ersej.dk&gt;</p></td>
<td><p>0.3.0</p></td>
<td><p>r4415</p></td>
<td><p>100%</p></td>
</tr>
<tr class="even">
<td><p>German</p></td>
<td><p>de</p></td>
<td><p>Matthias Braun &lt;matze@braunis.de&gt;, Marek Möckel</p></td>
<td><p>0.3.0</p></td>
<td><p>r4415</p></td>
<td><p>99%</p></td>
</tr>
<tr class="odd">
<td><p>(European) Spanish</p></td>
<td><p>es</p></td>
<td><p>Fernando Carmona <ferkiwi @ gmail .com></p></td>
<td><p>0.3.0</p></td>
<td><p>r4415</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Finnish</p></td>
<td><p>fi</p></td>
<td><p>Yaniel &lt;jhs@psonet.com&gt;</p></td>
<td></td>
<td></td>
<td><p>Work in progress...</p></td>
</tr>
<tr class="odd">
<td><p>French</p></td>
<td><p>fr</p></td>
<td><p>Benjamin Leduc &amp; Leo Poughon &lt;supertux-french-translation-team@googlegroups.com&gt;</p></td>
<td><p>0.3.3</p></td>
<td><p>r6691</p></td>
<td><p>100%, in improvement</p></td>
</tr>
<tr class="even">
<td><p>Hungarian</p></td>
<td><p>hu</p></td>
<td><p>Kővágó Zoltán (DirtY iCE) &lt;DirtY.iCE.hu (AT) gmail dot com &gt;</p></td>
<td><p>0.3.0</p></td>
<td><p>r4458</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>Icelandic</p></td>
<td><p>is</p></td>
<td><p>Thorsteinn A. Malmjursson &lt;hammer.of.thor (AT) hotmail.com&gt;</p></td>
<td><p>0.3.0</p></td>
<td></td>
<td><p>Most messages translated for menus, In game messages and screens still to do. Work in progress.</p></td>
</tr>
<tr class="even">
<td><p>Italian</p></td>
<td><p>it</p></td>
<td><p>Manuela Kessler <exty at exty.ch></p></td>
<td></td>
<td><p>r5181</p></td>
<td><p>Posted to mailinglist</p></td>
</tr>
<tr class="odd">
<td><p>Japanese</p></td>
<td><p>ja</p></td>
<td><p>Timothy Goya <tuxdev103 (AT) gmail DOT com></p></td>
<td></td>
<td></td>
<td><p>Work in Progress</p></td>
</tr>
<tr class="even">
<td><p>Lithuanian</p></td>
<td><p>lt</p></td>
<td><p>Andrius Štikonas <stikonas AT gmail DOT com></p></td>
<td></td>
<td><p>r4695</p></td>
<td><p>Work in progress...</p></td>
</tr>
<tr class="odd">
<td><p>Dutch</p></td>
<td><p>nl</p></td>
<td><p>Frank van der Loo &lt;frank_l@linuxmail.org&gt;</p></td>
<td></td>
<td><p>r2430</p></td>
<td><p>Work in progress...</p></td>
</tr>
<tr class="even">
<td><p>Norwegian Nynorsk</p></td>
<td><p>nn</p></td>
<td><p>Karl Ove Hufthammer &lt;karl@huftis.org&gt;</p></td>
<td><p>0.3.0</p></td>
<td></td>
<td><p>100% complete</p></td>
</tr>
<tr class="odd">
<td><p>Norwegian Bokmål</p></td>
<td><p>nb</p></td>
<td><p>Karl Ove Hufthammer &lt;karl@huftis.org&gt;</p></td>
<td><p>0.3.0</p></td>
<td></td>
<td><p>100% complete</p></td>
</tr>
<tr class="even">
<td><p>Polish</p></td>
<td><p>pl</p></td>
<td><p>Dominik &lt;dominik232@gmail.com&gt;</p></td>
<td></td>
<td><p>r5277</p></td>
<td><p>broken</p></td>
</tr>
<tr class="odd">
<td><p>(European) Portuguese</p></td>
<td><p>pt</p></td>
<td><p>Daniela Ferraz &lt;danielaafferraz@gmail.com&gt;, Ricardo Cruz &lt;rick2@aeiou.pt&gt;, Liudas Dmitrijevas</p></td>
<td><p>0.3.3-GIT</p></td>
<td><p>c5732ec26513</p></td>
<td><p>100%</p></td>
</tr>
<tr class="even">
<td><p>(Brazilian) Portuguese</p></td>
<td><p>pt_BR</p></td>
<td><p>Daniela Ferraz &lt;danielaafferraz@gmail.com&gt;, Krishnamurti Lelis Lima Vieira Nunes, Herval Ribeiro &lt;heraze@gmail.com&gt;</p></td>
<td><p>0.3.3-GIT</p></td>
<td><p>c5732ec26513</p></td>
<td><p>100%</p></td>
</tr>
<tr class="odd">
<td><p>Romanian</p></td>
<td><p>ro</p></td>
<td><p>Dajboc Razvan &lt;razvan.net AT gmail DOT com&gt;</p></td>
<td><p>0.3.0</p></td>
<td><p>r5135</p></td>
<td><p>100% Complete</p></td>
</tr>
<tr class="even">
<td><p>Russian</p></td>
<td><p>ru</p></td>
<td><p>Constantin Baranov <const86 at avtograd dot ru> Eugen Uvin &lt;nivus.ua AT gmail DOT com&gt;</p></td>
<td><p>0.3.0</p></td>
<td><p>r5135</p></td>
<td><p>100% Complete for Supertux, editor isn't translated</p></td>
</tr>
<tr class="odd">
<td><p>Slovenian</p></td>
<td><p>sl</p></td>
<td><p>Marko Burjek <email4marko AT gmail DOT com></p></td>
<td><p>0.3.0</p></td>
<td><p>r4415</p></td>
<td><p>90%</p></td>
</tr>
<tr class="even">
<td><p>Swedish</p></td>
<td><p>sv</p></td>
<td><p>Arvid Norlander <anmaster (AT) berlios DOT de></p></td>
<td><p>0.3.0</p></td>
<td><p>r4415</p></td>
<td><p>not 100% complete</p></td>
</tr>
<tr class="odd">
<td><p>Ukrainian</p></td>
<td><p>uk</p></td>
<td><p>Eugen Uvin &lt;nivus.ua AT gmail DOT com&gt;</p></td>
<td><p>0.3.0</p></td>
<td><p>r5135</p></td>
<td><p>100% Complete for Supertux, editor isn't translated</p></td>
</tr>
<tr class="even">
<td><p>Chinese, Simplified</p></td>
<td><p>zh_CN</p></td>
<td><p>Liu Sizhuang (lsz) <oldherl &#97;t gmail &#100;ot com></p></td>
<td></td>
<td></td>
<td><p>Work in progress, 95% done for Supertux, editor isn't translated. Posted to maillist.</p></td>
</tr>
</tbody>
</table>

[Category:Developer documentation](Category:Developer_documentation "wikilink")
