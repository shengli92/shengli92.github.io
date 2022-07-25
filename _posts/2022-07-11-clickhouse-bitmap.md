---
layout: post
title: "Clickhouse Bitmap"
description: "位图的且或操作"
category: clickhouse
tags: [clickhouse, bitmap]
---


#### Clikhouse Bitmap


##### 创建位图表
```clickhouse
DROP TABLE IF EXISTS user_tag_bitmap;
CREATE TABLE IF NOT EXISTS user_tag_bitmap
(
    etl_time   DateTime('UTC') DEFAULT now() COMMENT 'etl时间',
    app_id      String,
    tag_name   String,
    tag_value  String,
    fp_id      AggregateFunction(groupBitmap, UInt64)
    ) ENGINE = ReplacingMergeTree(etl_time)
    ORDER BY (app_id, tag_name, tag_value)
    SETTINGS index_granularity = 8192;
```

##### 从 user_tags 表中添加数据到到bitmap表
```clickhouse
insert into user_tag_bitmap
select now()                                   as etl_time,
       app_id,
       tag_name,
       tag_value,
       groupBitmapState(toUInt64OrZero(fp_id)) as ids
from user_tag
group by app_id, tag_name, tag_value;
```

##### (A 或 B) 且 ( C 或 D)
```clickhouse
select bitmapCardinality(bitmapAnd(
        groupBitmapAndStateIf(fp_id
            , (tag_name = 'last_launch_time' and tag_value = '>7天') -- A
                                  or (tag_name = 'last_launch_time' and tag_value = '3~7天') -- B
            )
    , groupBitmapOrStateIf(fp_id
            , (tag_name = 'charge_price_30d' and tag_value = '小R') -- C
                               or (tag_name = 'charge_price_30d' and tag_value = '大R') -- D
            )
    )) as cnt
from user_tag_manager.user_tags_bitmap
;
```


##### (C 或 D)
```clickhouse
select bitmapCardinality(bitmapOr(
        groupBitmapAndStateIf(fp_id
            , (tag_name = 'charge_price_30d' and tag_value in ('小R')) -- C
            )
    , groupBitmapAndStateIf(fp_id
            , (tag_name = 'charge_price_30d' and tag_value = '大R') -- D
            )
    )) as cnt
from user_tag_manager.user_tags_bitmap
;
```


##### (B 且 C)
```clickhouse
select bitmapCardinality(bitmapAnd(
        groupBitmapAndStateIf(fp_id
            , (tag_name = 'last_launch_time' and tag_value = '3~7天') -- B
            )
    , groupBitmapAndStateIf(fp_id
            , (tag_name = 'charge_price_30d' and tag_value = '小R') -- C
            )
    )) as cnt
from user_tag_manager.user_tags_bitmap
;
```


##### A 且 ( C 或 D)
```clickhouse
select bitmapCardinality(bitmapAnd(
        groupBitmapOrStateIf(fp_id
            , (tag_name = 'last_launch_time' and tag_value = '>7天') -- A
            )
    , groupBitmapOrStateIf(fp_id
            , (tag_name = 'charge_price_30d' and tag_value = '小R') -- C
                               or (tag_name = 'charge_price_30d' and tag_value = '大R') -- D
            )
    )) as cnt
from user_tag_manager.user_tags_bitmap
;
```



#### 2022-07-25 更新

##### A 且 B: 
```clickhouse
-- 返回 命中的count
with
    groupBitmapOrStateIf(z, (tag_id = 'tag_id')) as A
        , groupBitmapOrStateIf(z, (tag_id = 'tag_id2')) as B
        , bitmapAnd(A, B) as AandB
select bitmapCardinality(AandB)
from bitmap_table;

-- 返回结果集用：bitmapToArray()
```


##### A 或 B：
```clickhouse
with
    groupBitmapOrStateIf(z, (tag_id = 'tag_id')) as A
        , groupBItmapOrStateIf(z, (tag_id = 'tag_id2')) as B
        , bitmapOr(A, B) as AorB
select bitmapCardinality(AorB)
from bitmap_table;
```


##### A 且 B不存在：
```clickhouse
-- 先获取A 异或 B，得到不属于A且不属于B的集合。 
-- 然后 用 A 集合去和步骤1获取的集合取交集。 获取到属于A集合，但不属于B集合的部分
with
    groupBitmapOrStateIf(z, (tag_id = 'tag_id')) as A
        , groupBitmapOrStateIf(z, (tag_id = 'tag_id')) as B
        , bitmapXor(A, B) as AxorB
        , bitmapAnd(A, AxorB) as A_B
select bitmapCardinality(A_B)
from bitmap_table;
```


##### (A 或 B) 且 C
```clickhouse
with
    groupBitmapOrStateIf(z, (tag_id = 'tag1')) as A
        , groupBitmapOrStateIf(z, (tag_id = 'tag2')) as B
        , groupBitmapOrStateIf(z, (tag_id = 'tag3')) as C
        , bitmapOr(A, B) as AorB
        , bitmapAnd(AorB, C) as AorBandC
select bitmapCardinality(AorBandC)
from bitmap_table;
```



