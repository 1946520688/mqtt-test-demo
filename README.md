# MQTT Test Demo

## 项目简介
这是一个基于 Python 的 MQTT 协议测试与设备模拟示例项目，用于演示物联网设备连接、消息发布订阅、状态上报、消息接收等常见测试场景。

本项目适合用于展示以下能力：
- MQTT 协议基础理解
- IoT 设备通信测试思路
- Python 测试脚本编写能力
- 设备状态模拟与验证能力

## 技术栈
- Python 3
- paho-mqtt

## 测试场景
- 连接 MQTT Broker
- 订阅指定 Topic
- 发布设备状态消息
- 接收并解析消息内容
- 模拟设备上线
- 模拟设备清扫中状态上报
- 模拟设备回充状态上报

## 项目结构
```text
mqtt-test-demo/
├── README.md
├── requirements.txt
├── publisher.py
├── subscriber.py
└── device_simulator.py
