---
layout: post
tags: [clickhouse]
---
{% include JB/setup %}


clickhouse 从 csv 导入数据示例

#### 创建表
```shell
CREATE TABLE recipes
(
    title String,
    ingredients Array(String),
    directions Array(String),
    link String,
    source LowCardinality(String),
    NER Array(String)
) ENGINE = MergeTree ORDER BY title;
```

#### 插入数据
```shell
clickhouse-client --query "
    INSERT INTO recipes
    SELECT
        title,
        JSONExtract(ingredients, 'Array(String)'),
        JSONExtract(directions, 'Array(String)'),
        link,
        source,
        JSONExtract(NER, 'Array(String)')
    FROM input('num UInt32, title String, ingredients String, directions String, link String, source LowCardinality(String), NER String')
    FORMAT CSVWithNames
" --input_format_with_names_use_header 0 --format_csv_allow_single_quote 0 --input_format_allow_errors_num 10 < full_dataset.csv
```
这是一个展示如何解析自定义 CSV，这其中涉及了许多调整。

说明：

1. 数据集为 CSV 格式，但在插入时需要一些预处理；使用表函数 input 进行预处理；
2. CSV 文件的结构在表函数 input 的参数中指定；
3. 字段 num（行号）是不需要的 - 可以忽略并从文件中进行解析；
4. 使用 FORMAT CSVWithNames，因为标题不包含第一个字段的名称，因此 CSV 中的标题将被忽略（通过命令行参数 --input_format_with_names_use_header 0）；
5. 文件仅使用双引号将 CSV 字符串括起来；一些字符串没有用双引号括起来，单引号也不能被解析为括起来的字符串 - 所以添加--format_csv_allow_single_quote 0参数接受文件中的单引号；
6. 由于某些 CSV 的字符串的开头包含 \M/ 因此无法被解析； CSV 中唯一可能以反斜杠开头的值是 \N，这个值被解析为 SQL NULL。通过添加--input_format_allow_errors_num 10参数，允许在导入过程中跳过 10 个格式错误；
7. 在数据集中的 Ingredients、directions 和 NER 字段为数组；但这些数组并没有以一般形式表示：这些字段作为 JSON 序列化为字符串，然后放入 CSV 中 - 在导入是将它们解析为字符串，然后使用 JSONExtract 函数将其转换为数组。

[详细示例见][demo1]

csv不做处理直接导入的[参考示例][demo2]

[demo1]:https://clickhouse.com/docs/zh/getting-started/example-datasets/recipes
[demo2]:https://clickhouse.com/docs/zh/getting-started/example-datasets/uk-price-paid
