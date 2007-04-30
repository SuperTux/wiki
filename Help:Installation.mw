{{H:h|system admin toc}}
Many links on this page are red because they are the name of the article in Wikimedia. This page '''guides''' you through the process of installation of the latest stable version on '''linux'''. There is another page for installation from [[mw:Subversion|Subversion]]. The 1.6 series is the last to support versions of PHP earlier than PHP 5.

There are also guides for installing MediaWiki on '''Windows''' and IIS, which is a little harder:
* [[meta:Installing MediaWiki on Windows XP|Installing MediaWiki on Windows XP]] -> [[meta:Installing MediaWiki on Windows XP - MediaWiki 1.9.2|Installing MediaWiki on Windows XP - MediaWiki 1.9.2]]
* [[meta:Installing MediaWiki on Windows Server 2003 SP1|Installing MediaWiki on Windows Server 2003 SP1]]
* see also other guides: [[#External links]]

MediaWiki can be difficult to install for the average computer user who does not have experience with Apache, PHP and MySql. Most users who wish to use wiki software may benefit from using a free wiki host (see a [http://en.wikibooks.org/wiki/Wiki_Science:How_to_start_a_Wiki#.22Hosted_wiki.22_and_Wiki_hosts list of wiki hosts] on Wikibooks).

== Preparations ==

== Minimum system requirements ==
The recommended minimum settings is 256MB of RAM for a single-computer website, although this will not suffice for a busy public site. Some users have reported running MediaWiki on computers with as little as 48MB of RAM. 

=== Prerequisites ===
Before you can install '''MediaWiki''', there are four prerequisite components you must install. When you install these, remember to read the associated documentation. If your website is hosted for you then contact the server administrators or hosting company to ensure these are installed.  

# An '''Apache web server''', available at [http://httpd.apache.org/download.cgi the official download page].
#* MediaWiki also apparently runs under IIS 6.0, [http://www.0x50.org/ Cherokee] and [http://lighttpd.net lighttpd].
#* Sun has some [http://developers.sun.com/prodtech/webserver/reference/techart/mediawiki.html installation instructions] for running Mediawiki on the ''Sun Java System Web Server 7.0''.
# A recent version of '''PHP''', the programming language in which MediaWiki is written. This is available from the [http://www.php.net/downloads.php official download page]. As of version 1.7 '''PHP 5.x is required''' -- PHP 4.x is not supported from this version onwards.
#* See [[PHP config]] for compiling options
#* Some Linux servers may also require the equivalent MySQL package and PHP session management package; see the documentation for the operating system.
#* When installing on windows using the Microsoft installer, add the extension for your database of choice (MySQLi or PostgresSQL) to the features to be installed.  
#* If your Apache server has the [http://www.hardened-php.net/ Hardened PHP patch], you may need to edit several variables in your /etc/php.ini file if you wish to have Wiki pages with large amounts of content.  In particular, consider the settings for varfilter.max_value_length, hphp.post.max_value_length, and hphp.request.max_value_length.  The default settings may limit your pages to less than 10k or 64k in size.
#* Many people report blank pages in recent versions after submitting articles to their new wiki. A likely cause is the memory limit in default php installations (usually 8 MB). Please check your PHP and/or Apache error logs. To modify this setting edit <code>/etc/php.ini</code> and increase the "memory_limit" setting. For example to  raise it to 20 MB replace the existing text with "<code>memory_limit = 20M</code>". Make sure to restart your Apache server after you have changed this value.
# A '''MySQL database server''', which will be used to store all the text and data. This is available from the [http://dev.mysql.com/downloads/ official download page].
#* As of version 1.8, [http://www.postgres.org Postgres] is also supported. It should be noted that support for Postgres is very new and not as well tested as the MySQL equivalent.
# '''MediaWiki itself''', which is available from the [http://www.mediawiki.org/wiki/Download official download page]. Development versions are available from the [http://sourceforge.net/projects/wikipedia/ Sourceforge.net project page].

== Uploading to the server ==

=== Download and uncompress ===
[http://sourceforge.net/projects/wikipedia Download MediaWiki] to your local computer and uncompress the files, so that you can see the files and folders. This is usually done with software such as [http://www.7-zip.org/ 7-Zip] (open source software), [http://www.winzip.com/ WinZip], [http://www.rarlabs.com/ WinRAR] or [http://www.izarc.org/ IZArc] on Windows. On Linux, you can untar the file using this command:
 tar xvzf mediawiki-*.tar.'''gz'''

=== Upload ===
Upload the files to a public directory (usually '''<tt>public_html/wiki</tt>''') using an FTP client such as [http://filezilla.sourceforge.net/ FileZilla] (Open Source Software, Windows) or [http://cyberduck.ch/ Cyberduck] (OSX). If you are using a Unix server and have access to the <tt>httpd.conf</tt>, make a [[Wikipedia:Symbolic link|symbolic link]].

Change the permission settings for the "config" subdirectory so that it is writable by the webserver. If you are using FileZilla, right-click on the directory, select "attributes...", and check "Write" under "Owner". If it prompts you for a number instead or you are using a command-line interface, use '''755''' (Use '''777''' on Linux except for RedHat Linux). Alternately, you may be able to change permissions using a "control panel" provided by your web host.

Depending on the server configuration, in some cases you have to check all boxes (777) in FileZilla, to be able to run the install-script of MediaWiki.

=== Troubleshooting ===
* '''Case:''' If you are using a different FTP client than FileZilla, be sure to configure the client to ''not'' force uppercase or lowercase filenames on the webserver. MediaWiki filenames are case-sensitive.
* '''Incomplete uploads:''' The pack includes a lot of files, spread over dozens of directories. Be careful when uploading. If the transfer is interrupted, you might have missing or incomplete files. You may have to retry your upload several times, especially if you have an unreliable connection.
* '''403 Forbidden:''' If your webserver produces a "403 Forbidden error" page, then make sure your Apache '''httpd.conf''' have '''Options FollowSymLinks''' to allow symbolic links and that each directory leading up to your linked directory have '''+x''' permission for user running httpd.
* '''Internal error:''' If your webserver produces a "500 Internal Error" at the beginning of the install process, you may need to change the permissions on the config folder to 755.
* '''SELinux''': Linux distributions which support SELinux ('Security Extensions') are becoming more widespread. On such systems, PHP scripts will still be unable to write to the config directory, after you have set the normal file permissions. You will also need to use the 'chcon' command to change the SELinux file type. See [http://www.mediawiki.org/wiki/SELinux SELinux].
* If you are running the Mediawiki software on a free site that requires banners or prefix advertising, this may cause MediaWiki not to work, and appear to only generate empty pages beyond the banner advertising.  A fix for this will need to be done in the future.  In the interim the only option is to find a paid hosting site.  This may be considered a bug, and is being reported.
* '''Config directory unwritable:''' If you have changed the permissions for the config directory and still get an unwritable error try changing the owner to apache.
 chown -R apache:apache /var/www/html/mediawiki/*

=== Create a database ===

Currently, you must use either MySQL or Postgres to store the actual contents of your wiki.

====MySQL====
The MySQL database server stores the text and data of your wiki.

* If you know the '''root''' password for your database server, (the password for the user called "root") the MediaWiki setup script can automatically create a database and an account to access it.
* If you don't know the '''root''' password for your MySQL server, for example if you don't have the password because you are using a shared host, you need to create a MySQL database and a user before installing MediaWiki. You can do this using various control panels such as [[wikipedia:PhpMyAdmin|PhpMyAdmin]], which are often available from shared hosts, or you may be able to use ssh to login to your host and type the commands into a MySQL prompt. See the corresponding documentation. Alternatively, contact your host provider to have them create an account for you.

:1. Download and install [http://dev.mysql.com/downloads/mysql/5.0.html MySQL 5.0]. It should put itself in /usr/local/mysql<BR>
:2. Check and see if the database server is running ("/usr/local/mysql/bin/mysqladmin status"), If not, sudo /usr/local/mysql/bin/safe_mysqld &.<BR> (For Fedora Core 5, use /usr/bin/mysqld_safe)<BR>
:3. Set a password for the "root" account on your database server. /usr/local/mysql/bin/mysqladmin -u root password <I>yourpassword</I><BR>
:4. Set up a user in MySQL for your Wiki--do this in your terminal: /usr/local/mysql/bin/mysql -u root -p mysql<BR>
:5. This starts up the MySQL command line client. Now, do this in the client:

  create database wikidb;
  grant create, select, insert, update, delete, lock tables on wikidb.* to 'wikiuser'@'localhost' identified by 'password';
  flush privileges;
  \q


If your database is not running on the same server as your web server, you need to give the appropriate web server hostname -- mediawiki.example.com in my example -- as follows:
  grant create, select, insert, update, delete, lock tables on wikidb.* to
  'wikiuser'@'mediawiki.example.com' identified by 'password';

====Postgres====

If you are using Postgres, you will need to either have a database and user created for you, or simply supply the name of a Postgres user with "superuser" privileges to the configuration form. Often, this is the database user named '''postgres'''.

The database that MediaWiki will use needs to have both plpgsql and tsearch2 installed. The installer script will try and install plpgsql, but you may need to install tsearch2 yourself. (tsearch2 is used for searching the text of your wiki). Here's one way to do most of the setup. This is for a Unix-like system, and assumes that you have already installed the plpgsql and tsearch2 modules. In this example, we'll create a database named '''wikidb''', owned by a user named '''wikiuser''', with a password of "pgrocks". From the command-line, as the postgres user, perform the following steps.

  createuser -S -D -R -P -E wikiuser(then enter the password)
  createdb -O wikiuser wikidb
  createlang plpgsql wikidb

Adding tsearch2 to the database is not a simple step, but hopefully it will already be done for you by whatever packaging process installed the tsearch2 module. In any case, the installer will let you know right away if it cannot find tsearch2.

The above steps are not all necessary, as the installer will try and do some of them for you if supplied with a superuser name and password.

For installing tsearch2 to the wikidb database under Windows, do the following steps:
1. find tsearch2.sql (probably under .\PostgreSQL\8.x\share\contrib) and copy it to the postgresql\8.x\bin directory;
2. from a command prompt at the postgresql\8.x\bin directory, type "psql wikidb < tsearch2.sql -U wikiuser";
3. it will prompt you for the password for wikiuser;
That's it!

point 2. seems only to work on windows, cause on debian linux 4.0 (etch) only user postgres is allowed to use language c. so there it must be called by:

 su - postgres -c psql wikidb < tsearch2.sql

afterwards you must grant select rights to wikiuser to the tsearch table's and insert the correct locale.

 su - postgres
 echo 'grant select on pg_ts_cfg to wikiuser;' |psql wikidb
 echo 'grant select on pg_ts_cfgmap to wikiuser;' |psql wikidb
 echo 'grant select on pg_ts_dict to wikiuser;' |psql wikidb 
 echo 'grant select on pg_ts_parser to wikiuser;' |psql wikidb
 echo "update pg_ts_cfg set locale='en_US' where ts_name='default' and prs_name='default'"| psql wikidb
if the last line 'update' in the above box does not work try the following in the psql shell (see also in discussion):

 psql wikidb
 update pg_ts_cfg set locale = current_setting('lc_collate') where ts_name = 'default';
 \q

=== Run the installation script ===
Use your browser to visit the wiki directory on your webserver to run the installation script.  If you are running a distribution with SELinux, e.g. Fedora Core, be sure to set the context on the installation directory correctly e.g.:
 ls -aZ
 chcon -R system_u:object_r:httpd_sys_content_t wiki
If you installed into '''<tt>public_html/wiki</tt>''', this will probably be something similar to '''<tt><nowiki>http://www.yourdomain.com/wiki</nowiki></tt>'''. Depending on how you uploaded the files, you may need to visit '''<tt><nowiki>http://www.yourdomain.com/wiki/config</nowiki></tt>''' instead.
Follow the installation instructions on the installation script page. Refer to the following table if you're uncertain what to enter.
{| class="wikitable"
! Field !! Explanation
|-
| Database name
| The name of the MySQL or Postgres database you created (see [[#MySQL]])<br/>'''Note:''' If you run MySQL using a different socket file (e.g. mysql on localhost, using --socket=/tmp/mysocketfile), set the database name to:"localhost:/tmp/mysocketfile".
|-
| Database username
| The username used for accessing your wiki database.
|-
| Database password
| The user password for accessing your wiki database.
|-
| Database table prefix
| (MySQL only) An optional prefix to prepend to the name of every table that will be created within your wiki database. If you plan to have several wikis, you might want use the prefix "w1" so that all the tables associated with your first wiki will have "w1_" prepended. This allows you to install multiple wikis using the same databases by making the name unique. For example the generic name "archive" becomes "w1_archive", so that it is possible to add another database with the same table names.
|-
| Database port
| Currently only used by Postgres, this is the port number Postgres is installed at. The default value of 5432 should work for most instances. If you are connecting by using a hostname, this should be blank.
|-
| Schema for mediawiki / Schema for tsearch2
| (Postgres only) The name of the schema to put your wiki inside of. The default value of "mediawiki" should be fine for most purposes. The default value of "public" for tsearch2 should almost never have to be changed.
|-
| Superuser account / Superuser password
| The root database user and password, if you have it. If you don't have this password, leave it as it is. If you have the password, you may be able to skip the above stages of creating the database since MediaWiki will be able to do this for itself.
|}

Click the "Install!" button.

If you are using a hosting service, note that the database name and database username may have an extra prefix (normally the userid given by your hosting provider). For example, if you have created a database named db01 with username u01 and your userid is ocom (given by your hosting provider), you should enter the database name and database username as ocom_db01 and ocom_u01 respectively.

This may or may not apply to MySQL 5.x, but with MediaWiki 1.8.3 and MySQL 4.1.21 installed with UTF-8 as the default character set, there may be a MySQL error of the type "specified key was too long". One way of solving that
<ref>{{cite news | first= | last= | coauthors= | title=MediaWiki详细安装图解——常见安装问题 | date= | publisher= | url =http://www.allwiki.com/wiki/Mediawiki%E8%AF%A6%E7%BB%86%E5%AE%89%E8%A3%85%E5%9B%BE%E8%A7%A3%E2%80%94%E2%80%94%E5%B8%B8%E8%A7%81%E5%AE%89%E8%A3%85%E9%97%AE%E9%A2%98 | work = | pages = | accessdate = 2006-12-02 | language = Simplified Chinese }}</ref>
is to choose "Backwards-compatible UTF-8" in the installation script and edit the file maintenance/tables.sql so that the table causing the problem uses shorther keys. For example, if you find the error message:
<div style="border:#E08080 solid 1px;background-color:#FEE;padding:8px;">
PRIMARY KEY job_id (job_id), KEY (job_cmd, job_namespace, job_title) ) TYPE=InnoDB " failed with error code "Specified key was too long; max key length is 1024 bytes (localhost)".
</div>

Then you should find table "job" in tables.sql and modify varchar(255) to something shorther, eg varchar(242) as following. 

<pre><nowiki>
-- Jobs performed by parallel apache threads or a command-line daemon
CREATE TABLE /*$wgDBprefix*/job (
  job_id int(9) unsigned NOT NULL auto_increment,
  
  -- Command name, currently only refreshLinks is defined
  job_cmd varchar(242) NOT NULL default '',

  -- Namespace and title to act on
  -- Should be 0 and '' if the command does not operate on a title
  job_namespace int NOT NULL,
  job_title varchar(242) binary NOT NULL,

  -- Any other parameters to the command
  -- Presently unused, format undefined
  job_params blob NOT NULL default '',

  PRIMARY KEY job_id (job_id),
  KEY (job_cmd, job_namespace, job_title)
) TYPE=InnoDB;
</nowiki></pre>
  
Then you should delete tables you have made before, and then run the install script again. If you still see the same error, you can change the 255 to a even smaller number, eg varchar(150), and then repeat the above steps again. See also [http://bugzilla.wikimedia.org/show_bug.cgi?id=4445 MediaWiki bug 4445].

====Missing table prefix====

A MySQL installation of MediaWiki 1.8.2 on a shared host failed to display the '''database table prefix''' input box.  The form field was generated in the configuration page with no-display attributes.  If you experience this problem, the addition of the <tt>//</tt> characters to <tt>config/index.php</tt> as shown below will cause this field to re-materialize.  This input box is not needed unless more than one MediaWiki instance is being installed into a single database, so most installations will not need to do this, whether the field is present or not.   
<pre>
 <?php // database_switcher('mysql'); ?>
 <div class="config-input"><?php
         aField( $conf, "DBprefix", "Database table prefix:" );
 ?></div>
</pre>

Note: the problem persists in MediaWiki 1.9.3.  Subsequent experience suggests that the optional database portion of the installation form (which comes up with a yellow background for MySQL options, and blue for Postgres options) can be activated--if it does not appear on its own--with extra clicks on the database selection radio buttons (observed to work under Firefox 1.5)

== Configuration ==
=== Local settings ===
After setup, a file called '''<tt>LocalSettings.php</tt>''' is created in the "config" directory. This file contains all the information needed by MediaWiki to run. If it does not find the file in the main folder, it will launch the installation script to create a new one in the "config" directory.

# Move this file to the main wiki directory (if you installed MediaWiki to '''<tt>public_html/wiki</tt>''', move it there). '''Do not leave a copy in the config folder''', as this poses a severe security risk.
# Set stringent permissions on the '''<tt>LocalSettings.php</tt>''' file. ( chmod 600 and chown <webserver owner> )
# '''Delete''' the entire "config" directory.

=== Advanced configuration ===
For help with more advanced technical configuration, see [[Help:Configuration]] and [[Help:Administration]].

For a brief overview that addresses the empty help pages and text and layout modification, see [[Help:Installation-Software_Configuration]].

== Uninstallation ==
Removing MediaWiki entirely can be accomplished in two steps: removing the directory where MediaWiki was installed, and dropping the MediaWiki database from MySQL or Postgres.

For example, if you installed MediaWiki to '''/var/www/mediawiki-xyz''', you might do

 rm -r /var/www/mediawiki-xyz

===MySQL===

To remove the MySQL database holding your wiki, use the '''mysql''' utility to interactively connect to MySQL as a user with adequate permissions, then issue the following command at the '''mysql>''' prompt:

 DROP DATABASE wikidb;

(If you needed to retain some tables, you could also drop just some of the tables individually. See [http://mail.wikipedia.org/pipermail/mediawiki-l/2005-November/008090.html this MediaWiki-L message] for details.)

===Postgres===

To remove the Postgres database holding your wiki, run the following command:

  dropdb wikidb

You can also connect as a superuser using the '''psql''' program and issue:

  DROP DATABASE wikidb;

== See also ==
* [[mw:Help:FAQ#Installation_.26_Configuration|Installation FAQ]]
* [[Help:Upgrading MediaWiki]]
* [[MediaWiki architecture]]
* [[Postgres config]] -- more details on Postgres configuration for MediaWiki

== External links ==
*Lopez, Daniel ''Sams Teach Yourself Apache 2 in 24 Hours''.  Excellent easy to use book, the 3rd chapter, which explains how to install Apache, can be viewed on Amazon.com [http://www.amazon.com/gp/reader/0672323559/ here] ''(must register with Amazon first to view pages)''

*An [http://www.mundy.org/xp/ outdated explanation] of how to install, configure, and get Apache 1.3, MySQL 3, PHP 4 running under Windows XP in less than 30 minutes.  ('''This document is significantly out of date, having been updated October 5, 2003, but is otherwise well written!''')  For example, as of January 1, 2006:
*# It references Apache 1.3, Apache 2.2 is current.  The syntax it suggests for httpd.conf prevents Apache from restarting.
*# It references PHP 4.  PHP 5.1 is current.
*# It references MySQL 3.23.  MySQL 5.x is current.

* Life Hacker has [http://www.lifehacker.com/software/wikipedia/geek-to-live-set-up-your-personal-wikipedia-163707.php instructions] for installing MediaWiki on Windows XP.

'''Deploying MediaWiki with Sun Java System Web Server 7.0'''

* Sun has recently released their latest version of Web Server - [http://www.sun.com/download/products.xml?id=45ad781d Sun Java System Web Server 7.0](formerly known as iPlanet Enterprise Server or Sun ONE Web Server). Here is a technical [http://developers.sun.com/prodtech/webserver/reference/techart/mediawiki.html     article] on how to deploy MediaWiki with Sun Java System Web Server 7.0. Feel free to post your queries and concerns that you run into at [http://forum.java.sun.com/forum.jspa?forumID=759 Sun's Web Server Software forum]
* Also, if you need more help on how to get PHP as such working with [http://www.sun.com/download/products.xml?id=45ad781d  Sun Java System Web Server 7.0], then check out this [http://developers.sun.com/prodtech/webserver/reference/techart/php2.html article] which describes the steps involved in configuring and running PHP with Web Server 7.0. 
[[User:Natarajan|Natarajan]] 02:03, 24 January 2007 (UTC)


* A compact step-by-step guide to configure WAMP + MediaWiki is also [http://oss.segetech.com/wamp.html available].

For Windows XP, I think you may want to point users to a site similar to [http://www.apachefriends.org/en/xampp-windows.html XAMPP for Windows]. This appears to cover the basic requirements of Apache, PHP and MySQL.

'''See also''' : 
* [[Newcomers guide to installing on Windows]] 
* if you prefer IIS 6 try [[Installing MediaWiki on Windows Server 2003 SP1]]
* if you prefer IIS 5.1 try [[Installing MediaWiki on Windows XP]] 
* if you want step-by-step instruction try [[streamlined Windows Install Guide ]]
* How to [[upgrade from PHP4 to PHP5 on RedHat Enterprise Linux]] (AS4)
* [http://blog.eukhost.com/2006/10/11/apache-installation/ Apache Installation]

{{h:f|langs=|enname=Installation}}

==Reference==
<div class='references-small'>
<references/>
</div>
[[Category:Imported help]]
