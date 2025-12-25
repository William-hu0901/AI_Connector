# AI_Connector

这是一个连接各种AI大模型的客户端程序，其中包含调用DeepSeek API服务的示例代码，将会不断添加其他大模型API的调用示例，并逐步形成类似AI Agent的功能。

## 使用方法

1. 在[config.ini](file:///C:/Users/delon/PycharmProjects/AI_Connector/config.ini)文件中填入你的DeepSeek API密钥：
   ```
   [deepseek]
   api_key = your_actual_deepseek_api_key_here
   base_url = https://api.deepseek.com
   ```

2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

3. 运行程序：
   ```
   python deepseek_client.py
   ```

## 功能

- 获取可用模型列表
- 调用聊天完成API
- 支持自定义对话参数（模型、最大token数、温度等）

## API密钥获取

要使用DeepSeek API，你需要：
1. 访问DeepSeek官方网站注册账户
2. 在开发者面板中获取API密钥
3. 将API密钥填入配置文件中