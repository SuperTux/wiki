{{PD Help Page}}'''wikidb''' is the default [[MySQL]] database for the wiki.
The number of tables depends on the set-up.  The ''content'', or ''wikitexts'' are stored in table "[[text]]".  The revisions are stored in table "[[revision]]".  The user status (e.g. [[sysop]], [[bureaucrat]], [[checkuser]], etc) are stored in [[user_groups]].

The following is an example on the windows command line, of [[mediawiki-1.11.0]], with [[extension:CheckUser]] and [[extension:semantic MediaWiki]] installed. 

== list of tables ==
<pre>
K:\usr\local\mysql\bin>mysql -uUSERNAME -pPASSWORD
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4 to server version: 5.0.17

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| phpmyadmin         |
| wikidb             |
+--------------------+
4 rows in set (0.64 sec)

mysql> use wikidb;
Database changed
mysql> show tables;
+----------------------+
| Tables_in_wikidb     |
+----------------------+
| archive              |
| categorylinks        |
| cu_changes           |
| externallinks        |
| filearchive          |
| hitcounter           |
| image                |
| imagelinks           |
| interwiki            |
| ipblocks             |
| job                  |
| langlinks            |
| logging              |
| math                 |
| objectcache          |
| oldimage             |
| page                 |
| page_restrictions    |
| pagelinks            |
| querycache           |
| querycache_info      |
| querycachetwo        |
| recentchanges        |
| redirect             |
| revision             |
| searchindex          |
| site_stats           |
| smw_attributes       |
| smw_longstrings      |
| smw_nary             |
| smw_nary_attributes  |
| smw_nary_longstrings |
| smw_nary_relations   |
| smw_relations        |
| smw_specialprops     |
| smw_subprops         |
| templatelinks        |
| text                 |
| trackbacks           |
| transcache           |
| user                 |
| user_groups          |
| user_newtalk         |
| watchlist            |
+----------------------+
44 rows in set (0.03 sec)

mysql>
mysql> select * from user_groups;
+---------+------------+
| ug_user | ug_group   |
+---------+------------+
|       1 | bureaucrat |
|       1 | checkuser  |
|       1 | sysop      |
|       2 | sysop      |
+---------+------------+
4 rows in set (0.36 sec)

mysql>

</pre>
== granting and removing rights  ==
Following from above, we may grant and then remove checkuser rights to user 2 by:
<pre>

mysql> insert user_groups (ug_user,ug_group) values (2,'checkuser');
Query OK, 1 row affected (0.01 sec)

mysql> select * from user_groups;
+---------+------------+
| ug_user | ug_group   |
+---------+------------+
|       1 | bureaucrat |
|       1 | checkuser  |
|       1 | sysop      |
|       2 | checkuser  |
|       2 | sysop      |
+---------+------------+
5 rows in set (0.01 sec)

mysql> delete from user_groups where (ug_user,ug_group) = (2,'checkuser');
Query OK, 1 row affected (0.02 sec)

mysql> select * from user_groups;
+---------+------------+
| ug_user | ug_group   |
+---------+------------+
|       1 | bureaucrat |
|       1 | checkuser  |
|       1 | sysop      |
|       2 | sysop      |
+---------+------------+
4 rows in set (0.00 sec)

mysql>
</pre>

== to read the checkuser logs ==
<pre>
mysql> SELECT * FROM cu_changes;
</pre>

== to check the latest contributions from ip-address '127.0.0.1' ==
<pre>
mysql>SELECT * FROM recentchanges WHERE rc_ip='127.0.0.1' ORDER BY rc_id DESC LIMIT 7
</pre>
And I shall leave the results to your imagination.
[[Category:Imported help]]
