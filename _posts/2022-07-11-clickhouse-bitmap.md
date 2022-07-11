#### Clikhouse Bitmap


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


