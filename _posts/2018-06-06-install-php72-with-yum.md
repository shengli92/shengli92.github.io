---
layout: post
title: "Install PHP72 with Yum"
description: ""
category: 
tags: [php]
excrept: yum 安装php7.2方法
---
{% include JB/setup %}


### Installing PHP version 7.2

1. Turn on EPEL repo, enter:
` yum -y install epel-release`
2. Turn on Remi repo i.e.remi-php72:
`yum-config-manager --enable remi-php72`
3. Refresh repository:
`yum update`
4. Install php version 7.2. run ：
`yum install php`


### How to install PHP 7.2 on Centos 7

```
 $ yum install epel-release
 
 //turn remi repo
 $ yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
 
 // install yum-utils packages
 $ yum install yum-utils
 
 // enable remi repo, run: 
 $ yum-config-manager --enable remi-php72
 $ yum update
 
 //search for php7.2 package and modules with more command/grep command/egrep command:
 $ yum search php72 | more
 $ yum search php72 | egrep 'fpm|gd|mysql|memcache'
 
 //finally install php7.2 on centos 7.2:
 $ yum install php72
 
 // install "PHP  FastCGI Process Manager" called php72-php-fpm along with commonly used modules:
 $ yum install php72-php-fpm php72-php-gd php72-php-json php72-php-mbstring php72-php-mysqlnd php72-php-xml php72-php-xmlrpc php72-php-opcache

```
