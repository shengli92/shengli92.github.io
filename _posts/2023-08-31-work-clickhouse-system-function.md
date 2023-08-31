---
layout: post
tags: [clickhouse, system function]
---
{% include JB/setup %}


示例sql
```clickhouse
select t.install_date                                                                    as date,
       toDecimal64(sum(f_net_revenue(t.revenue, t.revenue_ads, t.net_ratio)) / 10000, 4) as revenue_net,
       toDecimal64(sum(t.cost) / 10000, 4)                                               as cost
from app.v_mkt_roi_no_click_v1 t
where t.install_date between '2023-07-01' and '2023-07-31'
  and app_id = 'paradiseisland.global.prod'
  and f_select_facebook(t.media_source, t.app_id, t.install_date,
                        ['graininess','date','type','country_equal','campaign_equal','sorts','selectedTableColumns','page_size','app_id']) =
      1
group by t.install_date as date
having  cost >= 0
limit 1000
;
```

其中的 f_net_revenue, f_select_facebook 是系统定义的function。 存在system function里， 我理解的function是预定义的一些方法，具体查询时，可以通过function 对sql进行一些简化， 类似于clickhouse系统定义的function toDate(), today()等。
创建function的sql如下：
```clickhouse
CREATE OR REPLACE FUNCTION z_test
AS (
revenue
,revenue_ads
,net_ratio
) -> CASE
  WHEN revenue_ads is NULL then revenue * if(net_ratio>0,toDecimal64(net_ratio,4),toDecimal64(0.7,4))
  ELSE (revenue-revenue_ads) * if(net_ratio>0,toDecimal64(net_ratio,4),toDecimal64(0.7,4)) + revenue_ads
END
;
```


查看function的sql如下：
```clickhouse
select * from system.functions
WHERE name LIKE 'f\_%' or name LIKE 're\_%'
    and origin = 'SQLUserDefined'
ORDER BY name
;
```


删除function的sql如下：
```clickhouse
drop function z_test;
```