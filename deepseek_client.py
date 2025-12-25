import requests
import json
import configparser
from typing import Optional, Dict, Any


class DeepSeekAPI:
    def __init__(self, config_file: str = "config.ini"):
        """
        初始化DeepSeek API客户端
        :param config_file: 配置文件路径
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file, encoding='utf-8')
        
        self.api_key = self.config.get('deepseek', 'api_key')
        self.base_url = self.config.get('deepseek', 'base_url')
        
        # 从配置文件中读取模型参数默认值
        self.default_model = self.config.get('model_params', 'model', fallback='deepseek-chat')
        self.default_max_tokens = self.config.getint('model_params', 'max_tokens', fallback=1000)
        self.default_temperature = self.config.getfloat('model_params', 'temperature', fallback=0.7)
        
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
    
    def chat_completion(self, messages: list, model: str = None, max_tokens: int = None, temperature: float = None) -> Optional[Dict[Any, Any]]:
        """
        调用DeepSeek聊天完成API
        :param messages: 消息列表，格式为[{"role": "user", "content": "消息内容"}, ...]
        :param model: 使用的模型，默认为配置文件中的模型
        :param max_tokens: 最大输出token数，默认为配置文件中的值
        :param temperature: 温度参数，控制输出随机性，默认为配置文件中的值
        :return: API响应的字典
        """
        url = f"{self.base_url}/chat/completions"
        
        # 使用传入的参数，如果未提供则使用配置文件中的默认值
        model = model or self.default_model
        max_tokens = max_tokens or self.default_max_tokens
        temperature = temperature or self.default_temperature
        
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()  # 检查HTTP错误
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
            return None
    
    def get_models(self) -> Optional[Dict[Any, Any]]:
        """
        获取可用模型列表
        :return: 模型列表的字典
        """
        url = f"{self.base_url}/models"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
            return None


def main():
    # 创建API客户端实例
    client = DeepSeekAPI()
    
    # 示例1: 获取可用模型列表
    print("获取可用模型列表...")
    models = client.get_models()
    if models:
        print("可用模型:")
        for model in models.get('data', []):
            print(f"- {model['id']}")
    else:
        print("获取模型列表失败")
    
    print("\n" + "="*50 + "\n")
    
    # 示例2: 聊天完成
    print("进行聊天完成测试...")
    messages = [
        {"role": "system", "content": "你是一个有用的助手。"},
        {"role": "user", "content": "你好，简单介绍一下DeepSeek模型的特点，不超过200字。"}
    ]
    
    response = client.chat_completion(messages)
    if response:
        choice = response.get('choices', [{}])[0]
        message = choice.get('message', {})
        print(f"助手回复: {message.get('content', '未获取到回复内容')}")
    else:
        print("聊天完成请求失败")
    
    print("\n" + "="*50 + "\n")
    
    # 示例3: 自定义对话
    print("自定义对话示例...")
    custom_messages = [
        {"role": "system", "content": "你是一个编程助手，专门帮助解决编程问题。"},
        {"role": "user", "content": "用Python写一个快速排序算法，不超过500字符。"}
    ]
    
    response = client.chat_completion(
        messages=custom_messages,
        max_tokens=500,
        temperature=0.5
    )
    
    if response:
        choice = response.get('choices', [{}])[0]
        message = choice.get('message', {})
        print(f"编程助手回复:\n{message.get('content', '未获取到回复内容')}")
    else:
        print("自定义对话请求失败")
    
    print("\n" + "="*50 + "\n")
    
    # 示例4: 使用默认配置参数
    print("使用默认配置参数...")
    config_messages = [
        {"role": "system", "content": "你是一个知识渊博的助手。"},
        {"role": "user", "content": "请简要说明人工智能的三个主要分支，不超过500个字。"}
    ]
    
    # 不提供参数，使用配置文件中的默认值
    response = client.chat_completion(config_messages)
    
    if response:
        choice = response.get('choices', [{}])[0]
        message = choice.get('message', {})
        print(f"知识助手回复:\n{message.get('content', '未获取到回复内容')}")
    else:
        print("使用默认配置请求失败")


if __name__ == "__main__":
    main()