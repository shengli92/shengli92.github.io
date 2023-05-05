---
layout: post
tags: [mysql]
---
{% include JB/setup %}


#### TABLE重命名
```mysql
RENAME TABLE old_table_name TO new_table_name
```



#### 往json数组里添加元素
##### json_array_append 往json数组中追加元素, **$**参数指permissions本身，也可以通过下标$[1]指定第几项，但是下标不能为负数，也不能超过array长度
```mysql
-- 查询
select json_array_append(permissions, '$', 'PAGE-CREATIVE-KANBAN-OVERVIEW') from users where id =1;

-- 更新
update users set permissions = json_array_append(permissions, '$', 'PAGE-CREATIVE-KANBAN-OVERVIEW') where id = 1;
```

##### json_array_insert 往json数组前插入元素，**$**参数指permissions本身，也可以通过下标$[1]指定第几项，但是下标不能为负数，可以超过array长度，超过表示插入到最后