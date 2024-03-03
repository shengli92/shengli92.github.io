---
layout: post
tags: [Unity, C#]
---
{% include JB/setup %}


## C# 随手记

#### Dictionary 

Dictionary 是C#中的一种集合类型， 用来存储键值对数据。 Dictionary经常用于管理游戏中的状态、配置数据、对象池等。 以下是一个简单示例，用来演示Dictionary的使用：

```csharp
using System.Collections.Generic;
using UnityEngine;

public class DictionaryExample : MonoBehaviour
{
    // 声明一个 Dictionary，键是字符串类型，值是整数类型
    private Dictionary<string, int> scores = new Dictionary<string, int>();

    void Start()
    {
        // 添加键值对到 Dictionary
        scores.Add("Alice", 100);
        scores.Add("Bob", 80);
        scores.Add("Charlie", 90);

        // 通过键访问值
        Debug.Log("Alice's score: " + scores["Alice"]);

        // 修改值
        scores["Bob"] = 85;

        // 遍历 Dictionary
        foreach (KeyValuePair<string, int> pair in scores)
        {
            Debug.Log(pair.Key + "'s score: " + pair.Value);
        }

        // 检查 Dictionary 中是否包含某个键
        if (scores.ContainsKey("David"))
        {
            Debug.Log("David's score: " + scores["David"]);
        }
        else
        {
            Debug.Log("David's score not found.");
        }
    }
}


```

在这个示例中，我们首先声明了一个 Dictionary<string, int> 类型的变量 scores，它用于存储玩家的得分信息。然后，我们通过 Add 方法向 scores 中添加了一些键值对。接着，我们演示了如何通过键访问值、修改值，并通过 foreach 循环遍历 Dictionary 中的所有键值对。最后，我们使用 ContainsKey 方法检查 Dictionary 中是否包含某个键。


#### System.Tuple

System.Tuple 是C#中的一种元组类型，它用于存储一组数据。元组可以是任意大小的，可以包含任意类型的对象。以下是一个简单的示例，用来演示元组的使用：
```Csharp
using System;

public class TupleExample : MonoBehaviour
{
    void Start()
    {
        // 创建一个包含两个元素的 Tuple，第一个元素是字符串，第二个元素是整数
        Tuple<string, int> person = new Tuple<string, int>("Alice", 30);

        // 获取元组的元素
        string name = person.Item1;
        int age = person.Item2;

        Debug.Log("Name: " + name + ", Age: " + age);
    }
}

```
在这个示例中，我们创建了一个包含两个元素的 Tuple，第一个元素是字符串类型的名字 "Alice"，第二个元素是整数类型的年龄 30。我们可以通过 Item1 和 Item2 属性来获取元组的各个元素。

需要注意的是，System.Tuple 在 Unity 中可用，但是它并不是 Unity 特有的功能，而是 C# 语言的一部分，可以在任何支持 .NET 的环境中使用。System.Tuple 主要用于临时的、简单的元组数据结构，如果需要更复杂的元组操作，你可能需要考虑使用自定义的数据结构或其他 .NET 提供的类型。