DeepSeek API 使用说明
===================

1. 获取DeepSeek API密钥
--------------------
要使用DeepSeek API，您需要首先获取API密钥：
- 访问 https://www.deepseek.com/ 注册账户
- 登录后进入开发者面板
- 创建新的API密钥并复制保存

2. 配置API密钥
--------------
将获取的API密钥填入config.ini文件中：
```
[deepseek]
api_key = your_actual_deepseek_api_key_here
base_url = https://api.deepseek.com
```

3. 配置模型参数
--------------
您可以在config.ini中配置默认的模型参数：
```
[model_params]
model = deepseek-chat          # 使用的模型
max_tokens = 1000              # 最大输出token数
temperature = 0.7              # 温度参数，控制输出随机性
```

4. 安装依赖
----------
在项目目录中运行：
```
pip install -r requirements.txt
```

5. 运行程序
----------
```
python deepseek_client.py
```

6. API功能说明
-------------
- chat_completion(): 聊天完成API，用于对话生成
- get_models(): 获取可用模型列表
- 支持自定义参数（模型、最大token数、温度等）

7. 注意事项
----------
- 请妥善保管您的API密钥，不要将其分享给他人
- 注意API调用的频率限制和费用
- 根据需要调整temperature参数来控制输出的创造性