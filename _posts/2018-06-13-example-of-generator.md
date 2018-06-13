---
layout: post
title: "example of generator"
description: ""
category: 
tags: []
---
{% include JB/setup %}


### Example. CSV generator

```
    <?php
        function getRows($files)
        {
            $handle = fopen($file, 'rb');
            if($handle === false) {
                throw new Exception();
            }
            while (feof($handle) === false) {
                yield fgetcsv($handle);
            }
            fclose($handle);
        }
        
        foreach( getRows('data.csv') as $row) {
            print_r($row);
        }
```

### <span id="feof">feof</span>
 feof - 测试文件指针是否到了文件结束的位置
 
 **用法**
 
    `bool feof( resource $handle )`

 **参数**
 
    handle  文件指针必须是有效的，必须指向由fopen() 或 fsockopen() 成功打开的文件(并还未由fclose()关闭)
    
    
    
### <span id="fgetcsv">fgetcsv</span>
 fgetcsv() - 从文件指针中读入一行并解析CSV字段，与fgets()类似，不同的是 fgetcsv() 解析读入的行并找出CSV格式的字段，然后返回一个包含这些字段的数组
 
**语法**

fgetcsv(file, length, separator, enclosure)
 
 | 参数 | 描述 |
 | --- | --- |
 | file | 必需。规定要检查的文件 |
 | length | 可选。 规定行的最大长度。必须大于CVS文件内的最长的一行。|
 | separator | 可选。设置字段分界符（只允许一个字符），默认值为逗号 | 
 | enclosure | 可选。 设置字段环绕符（只允许一个字符），默认值为双引号 | 
 
 ![avatar](/assets/images/fgetcsv1.jpg)
 ![fgetcsv2](/assets/images/fgetcsv2.jpg)
 