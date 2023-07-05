---
layout: post
tags: [clickhouse]
---
{% include JB/setup %}


本次记录的是  docker 运行 clickhouse
首先使用*docker pull clickhouse/clickhouse-server*命令拉取 docker 镜像

如果不需要修改clickhouse的用户密码等，直接运行即可
```shell
docker run -it --rm --link some-clickhouse-server:clickhouse-server --entrypoint clickhouse-client clickhouse/clickhouse-server --host clickhouse-server
# OR
docker exec -it some-clickhouse-server clickhouse-client
```


如果需要设置clickhouse的用户与密码。 先要创建本地目录，用来存储容器内的配置文件等
```shell
# 创建 clickhouse 目录
mkdir -p /data/clickhouse/data/   # 创建数据目录
mkdir -p /data/clickhouse/config/ # 创建 clickhouse config目录
mkdir -p /data/clickhouse/log/    # 创建  clickhouse log 目录
```

先启动容器
```shell
docker run -d \
--name clickhouse-server \
--ulimit nofile=262144:262144 \
-p 8123:8123 \
-p 9000:9000 \
-p 9009:9009 \
clickhouse/clickhouse:latest
```

然后将容器内的配置文件copy至本地目录
```shell
docker cp clickhouse-server:/etc/clickhouse-server/config.xml  /data/clickhouse/config/config.xml

docker cp clickhouse-server:/etc/clickhouse-server/users.xml /data/clickhouse/config/users.xml
```


default 用户配置
```shell

# 生成制定密码123456
echo "123456"; echo -n "123456" | sha256sum | tr -d '-'

output% 123456
output% 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92

# 打开本地users.xml文件，将default用户设置密码为123456
vim /data/clickhouse/config/users.xml

# 将文件中<password></password>改为以下内容
<password_sha256_hex>8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92</password_sha256_hex>


# 将 default 用户改为只读
# 将 <profile>default</profile>
<profile>readonly</profile>
```


新增 root 用户
```shell
# 同样是打开 users.xml文件。 然后在default用户下添加以下内容
<root>
    <password_sha256_hex>8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92</password_sha256_hex>
    <networks incl="networks" replace="replace">
      <ip>::/0</ip>
    </networks>
    <profile>default</profile>
    <quota>default</quota>
</root>
```

设置完之后，删除临时容器 *docker rm -f clickhouse-server* 这么做是为了将容器内的配置文件copy到本地

最后部署clickhouse-server
```shell

 docker run -d \
 --name clickhouse-server \
 --ulimit nofile=262144:262144 \
 -p 8123:8123 \
 -p 9000:9000 \
 -p 9009:9009 \
 -v /data/clickhouse/data:/var/lib/clickhouse:rw \
 -v /data/clickhouse/log:/var/log/clickhouse-server:rw \
 -v /data/clickhouse/config/config.xml:/etc/clickhouse-server/config.xml \
 -v /data/clickhouse/config/users.xml:/etc/clickhouse-server/users.xml \
 clickhouse/clickhouse-server:latest
```


以上就完成了clickhouse 的用户密码配置

想要重新进入容器内的clickhouse，需要先执行
```shell
docker exec -it clickhouse-server /bin/bash
```

然后在 /bin/bash 的命令行中执行 *clickhouse-client -uroot --password* 输入密码后，就进入了clickhouse命令行