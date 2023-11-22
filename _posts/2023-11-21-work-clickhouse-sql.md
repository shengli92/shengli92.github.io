---
layout: post
tags: [clickhouse, system function]
---
{% include JB/setup %}


### 记一条有趣的sql
```clickhouse
with '2023-11-14' as day1,
    '2023-11-15' as day2,

    summary as (
        select down.install_date                      as install_date,
               down.os                                as os,
               total.new_installs                     as total_new_installs,
               total.new_installs - down.new_installs as except_new_installs,
               down.new_installs                      as single_new_installs
        from (
                 select t.install_date, sum(t.new_installs) as new_installs
                 from app.v_mkt_roi_no_click_v1 t
                 where t.install_date in ('2023-11-14', '2023-11-15')
                   and app_id = 'paradiseisland.global.prod'
                   and media_source not in ('Facebook-New')
                 group by install_date
                 ) total
                 join (
            select install_date, os, sum(t.new_installs) as new_installs
            from app.v_mkt_roi_no_click_v1 t
            where t.install_date in ('2023-11-14', '2023-11-15')
              and app_id = 'paradiseisland.global.prod'
              and media_source not in ('Facebook-New')
            group by install_date, os
            ) down on total.install_date = down.install_date
    ),
    summary_day1 as (
        select *
        from summary
        where install_date in (day1)
    ),
    summary_day2 as (
        select *
        from summary
        where install_date in (day2)
    )


select os,
       t1.single_new_installs,
       t2.single_new_installs,

       t1.except_new_installs,
       t2.except_new_installs,

       t1.total_new_installs,
       t2.total_new_installs,
       f_divide_or_zero(t1.except_new_installs * (t2.total_new_installs - t1.total_new_installs),
                        (t1.total_new_installs * (t2.except_new_installs - t1.except_new_installs))) - 1 as weight

from summary_day1 t1
         join summary_day2 t2
              on t1.os = t2.os
order by weight desc
limit 10
;
```