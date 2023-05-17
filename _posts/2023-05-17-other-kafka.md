---
layout: post
tags: [kafka]
---
{% include JB/setup %}


### 基础概念
kafka体系架构包含若干个 Producer， Broker，Consumer 以及一个ZooKeeper集群。 
ZooKeeper 是kafka 用来负责集群元数据的管理、控制器的选举等操作。
Producer 将消息发送到Broker
Broker负责将收到的消息存储到磁盘中
Consumer 负责从 Broker 订阅并消费消息
