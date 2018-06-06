---
layout: post
title: "OpenResty 安装全过程"
description: ""
category: 
tags: []
---
{% include JB/setup %}

###LIST OF PROBLEM I MET

1、运行`sudo yum-config-manager --add-repo https://openresty.org/yum/cn/centos/OpenResty.repo` 时，报错：yum-config-manager：command not found

**解决** 系统默认没有安装这个命令，这个命令在yum-utils 包里，可以通过yum -y install yum-utils 安装就可以了。

