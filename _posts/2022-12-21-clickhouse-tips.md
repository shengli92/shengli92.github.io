---
layout: post
title: "工作踩坑既要"
description: ""
category: Clickhouse
tags: [clickhouse, 共享锁，排他锁]
---


#### Clickhouse 同步远程数据表内容
```clickhouse

set max_memory_usage=21474836480;
set max_partitions_per_insert_block=10000;
set connect_timeout_with_failover_ms=10000;

INSERT INTO php_clickhouse.material_info_new
SELECT *
FROM remote('${REMOTE}:9000', ${SCHEMA},
            ${TABLE}, ${USER}, ${PWD})
```
