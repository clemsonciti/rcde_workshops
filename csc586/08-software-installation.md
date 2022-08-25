
# Software Installation and Configuration


```{dropdown} 1. Launch your CloudLab experiment

- Instantiate an experiment from the CloudLab profile created last week
- SSH into the experiment once it is ready.

```

```{dropdown} 2. Overview

- The purpose of this document is to create a LAMP (Linux/Apache/MySQL/Php) 
installation on your experiment. 
- With this in place, we'll also install two common LAMP applications:
  - `phpMyAdmin`: a web app for managing MySQL databases
  - `Drupal`: a content management system.
- More passwords:
  - The `MySQL` installation needs an administrative (root) password to get started. 
  This is an important one, but we will make it so that you, with machine root access, 
  do not have to remember it.
  - `phpMyAdmin` has its own administrative database/user/password; fortunately you do not need to remember this password.
  - `Drupal` also has its own administrative database/user/password which you don't have to remember. 
  Drupal also requires a site administrator login/password, which you **do** have to remember. 

```

```{dropdown} 3. MySQL

- Run the following commands

~~~
$ bash
$ wget --no-check-certificate https://www.cs.wcupa.edu/lngo/data2/mysql-apt-config_0.8.17-1_all.deb
$ sudo dpkg -i mysql-apt-config_0.8.17-1_all.deb
~~~


::::{admonition} Configuring mysql-apt-config
:class: dropdown

- Press the `Tab` key to go to `Ok`, then press `Enter`

:::{image} ../fig/csc586//08-software/mysql-01.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::
::::


~~~
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
$ sudo apt-get update
$ sudo apt install -y mysql-community-server
~~~

::::{admonition} Configuring mysql-community-server
:class: dropdown

- Select and enter a root password
- Press the `Tab` key to go to `Ok`, then press `Enter`
- Re-enter the above password when asked again, then `Tab` to `Ok` and `Enter`. 

:::{image} ../fig/csc586//08-software/mysql-02.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

- Select `User Strong Password Encryption (RECOMMENDED)`
- Press the `Tab` key to go to `Ok`, then press `Enter`

:::{image} ../fig/csc586//08-software/mysql-03.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

- Run the following command and provide the password to test the MySQL server:
  - `mysql -u root -p`
  - To quit MySQL, type `\q`

:::{image} ../fig/csc586//08-software/mysql-04.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

- Create a file named `.my.cnf` (run `sudo nano /root/.my.cnf`)directly inside `/root` with the following content:

~~~
[client]
user=root
password=”MYSQL_ROOT_PASS”
~~~

- Test the effectiveness of this passwordless setup

~~~
$ sudo su
$ mysql
\q
$ exit
$ sudo -H mysql
\q
~~~

:::{image} ../fig/csc586//08-software/mysql-05.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

::::


```


```{dropdown} 4. Apache

- Run the following commands

~~~
$ sudo apt install -y  apache2 php libapache2-mod-php php-cli php-mysql php-cgi php-curl php-json php-apcu php-gd php-xml php-mbstring
~~~

- Test the installation once it is completed by open a web browser and go to your 
CloudLab experiment’s host name (the same one that you SSH to)

:::{image} ../fig/csc586//08-software/apache-01.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

- The Apache service is one which needs to be `reset` often because of configuration 
changes. Control the Apache server is done as a SysV service which is based on the `systemctl` command:

~~~
$ sudo systemctl  COMMAND  apache2.service
~~~

or, more simply:

~~~
$ sudo systemctl  COMMAND  apache2
~~~

where COMMAND can be: `status`, `start`, `stop`, `restart`, `reload`.

- If something goes wrong, the first place to look is usually this log file: `/var/log/apache2/error_log`
- This error log file is readable by you, a system admin, without invoking `sudo`. Often a useful thing to do 
is to `follow the tail` of this file as messages are generated with using the `tail -f` command:

~~~
$ tail -f /var/log/apache2/error_log
~~~

- If you make a configuration change, you can test its effectiveness by running this prior to attempting to 
reset the service.

~~~
$ sudo apachectl configtest
~~~

- Apache understands user sites as the automatic association of a special directory owned by you 
(by default, `~/public_html`) to the URL `http://hostname/~LOGIN`

~~~
$ mkdir ~/public_html
~~~

- User directories are not enabled by default. To enable the Apache userdir module by:

~~~
$ sudo a2enmod userdir
$ sudo systemctl reload apache2
~~~

- The first command simply creates a symbolic link. Check it yourself:

~~~
$ ll /etc/apache2/mods-enabled/userdir.*
~~~

- Visit `http://hostname/~LOGIN`
  - Does it work?
  - Why?

- Run `$ sudo nano /etc/apache2/mods-available/userdir.conf`
  - Make the appropriate changes or additions
  - Save and reload
  - Try visiting the site again

```


```{dropdown} 5. PHP

- To enable PHP, edit the file `/etc/apache2/mods-enabled/php7.4.conf`
- Comment out the last five lines as per the instructions in the comments
- Restart apache2
- Create a file named `hello.php` in your `public_html` directory with the following contents:

~~~
<?php
echo "Hello from PHP";
?>
~~~

- Refresh your home page and view this file. 


```



```{dropdown} 6. PHP/phpmyadmin

- Run the following command to install `phpmyadmin`

~~~
$ sudo apt-get install -y phpmyadmin
~~~

- Press the `Space` button to check `apache2`, then `Tab` to move to `Ok` and press `Enter`. 

:::{image} ../fig/csc586//08-software/phpmyadmin-01.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

- Accept default `Yes` answer on `Configuring database for phpadmin with dbconfig-common`.
- Select and enter a password for `phpmyadmin`.
  - Press the `Tab` key to go to `Ok`, then press `Enter`
- Re-enter the above password for confirmation, then `Tab` to `Ok` and `Enter`. 
- Provide the password of account `root` for MySQL (from the MySQL installation). 
  - Press the `Tab` key to go to `Ok`, then press `Enter`

:::{image} ../fig/csc586//08-software/phpmyadmin-02.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::


:::{image} ../fig/csc586//08-software/phpmyadmin-03.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::


```



```{dropdown} 7. Drupal

- Run the following commands

~~~
$ sudo su
$ cd
$ wget https://ftp.drupal.org/files/projects/drupal-9.4.2.tar.gz
~~~

- Find your machine simple hostname
  - Going forward, `MACHINE` will refer to the outcome of this command.  
~~~
$ hostname -f | awk -F\. '{print $1}'
~~~

- Find your machine full hostname
  - Going forward, `HOSTNAME` will refer to the outcome of this command.  
~~~
$ hostname -f
~~~

- Think of a password for your drupal database. 
  - Going forward, `DRUPAL_DB_PASS` will refer to this value. 

~~~
$ mysql
mysql> create database drupal;
mysql> create user drupal@localhost identified by "DRUPAL_DB_PASS";
mysql> grant all on drupal.* to drupal@localhost;
mysql> quit;
~~~

- Install drupal

~~~
$ tar xzf drupal-9.4.2.tar.gz
$ mv drupal-9.4.2 /var/www/html/$(hostname -f | awk -F\. '{print $1}')_drupal
~~~

- Visit `http://HOSTNAME/MACHINE_drupal` to start the browser-based configuration process 
for Drupal. 

- On first windows, select language `English` and click `Save and Continue`. 
- Next, select `Standard` then click `Save and Continue`. 
- We need to address two errors and one warnings.

:::{image} ../fig/csc586//08-software/drupal-01.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::


::::{admonition} Error: File system 
:class: dropdown

~~~
$ clear
$ cd /var/www/html/$(hostname -f | awk -F\. '{print $1}')_drupal
$ pwd
$ apt install -y acl
$ mkdir sites/default/files
$ setfacl -m g:www-data:rwx sites/default/files
~~~

- Scroll to bottom of page, click `try again` to confirm that the `File system`
 error message is gone.

:::{image} ../fig/csc586//08-software/drupal-02.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::
::::

::::{admonition} Error: Settings File 
:class: dropdown

- Confirm that you are still inside the drupal directory. 

~~~
$ pwd
$ cp sites/default/default.settings.php sites/default/settings.php
$ setfacl -m g:www-data:rw sites/default/settings.php
~~~

- Scroll to bottom of page, click `try again` to confirm that the `Settings File`
 error message is gone.

:::{image} ../fig/csc586//08-software/drupal-03.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::
::::


::::{admonition} Warnings: Clean URLS 
:class: dropdown

- Confirm that you are still inside the drupal directory. 

~~~
$ pwd
$ a2enmod rewrite
$ mv .htaccess /etc/apache2/conf-available/drupal.conf
~~~

- Edit `/etc/apache2/conf-available/drupal.conf` and add 
`<Directory /var/www/html/MACHINE_drupal>` as first line and `</Directory>` as last line.

~~~
$ a2enconf drupal
$ systemctl reload apache2
~~~


- Scroll to bottom of page, click `try again` to confirm that the warning
 error message is gone and the configuration has moved on to the next step. 

:::{image} ../fig/csc586//08-software/drupal-04.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::
::::

- Provide the authentication for the `drupal` username and database table as created 
earlier. 
- Wait for the installation to complete. 
- For configuration:
  - `Site name`: MACHINE
  - `Site email address`: your email address. 
  - Other options can be selected as you see fit. 

- **Challenge**: Create a first page via Drupal and display the content. 

```