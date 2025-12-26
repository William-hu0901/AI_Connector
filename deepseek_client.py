import requests
import json
import configparser
from typing import Optional, Dict, Any


class DeepSeekAPI:
    def __init__(self, config_file: str = "config.ini"):
        """
        Initialize the DeepSeek API client
        :param config_file: Configuration file path
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
        Call the DeepSeek chat completion API
        :param messages: Message list, format is [{"role": "user", "content": "message content"}, ...]
        :param model: Model to use, defaults to the model in the configuration file
        :param max_tokens: Maximum output token count, defaults to the value in the configuration file
        :param temperature: Temperature parameter, controls output randomness, defaults to the value in the configuration file
        :return: Dictionary of API response
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
            response.raise_for_status()  # Check HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return None
    
    def get_models(self) -> Optional[Dict[Any, Any]]:
        """
        Get list of available models
        :return: Dictionary of model list
        """
        url = f"{self.base_url}/models"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return None


def main():
    # 创建API客户端实例
    client = DeepSeekAPI()
    
    # Example 1: Get available model list
    print("Getting available model list...")
    models = client.get_models()
    if models:
        print("Available models:")
        for model in models.get('data', []):
            print(f"- {model['id']}")
    else:
        print("Failed to get model list")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Chat completion
    print("Performing chat completion test...")
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, briefly introduce the features of DeepSeek models in less than 200 words."}
    ]
    
    response = client.chat_completion(messages)
    if response:
        choice = response.get('choices', [{}])[0]
        message = choice.get('message', {})
        print(f"Assistant response: {message.get('content', 'No response content received')}")
    else:
        print("Chat completion request failed")
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Custom conversation
    print("Custom conversation example...")
    custom_messages = [
        {"role": "system", "content": "You are a programming assistant, specializing in helping solve programming problems."},
        {"role": "user", "content": "Write a quick sort algorithm in Python, no more than 500 characters."}
    ]
    
    response = client.chat_completion(
        messages=custom_messages,
        max_tokens=500,
        temperature=0.5
    )
    
    if response:
        choice = response.get('choices', [{}])[0]
        message = choice.get('message', {})
        print(f"Programming assistant response:\n{message.get('content', 'No response content received')}")
    else:
        print("Custom conversation request failed")
    
    print("\n" + "="*50 + "\n")
    
    # Example 4: Using default configuration parameters
    print("Using default configuration parameters...")
    config_messages = [
        {"role": "system", "content": "You are a knowledgeable assistant."},
        {"role": "user", "content": "Briefly explain the three main branches of artificial intelligence in less than 500 words."}
    ]
    
    # Don't provide parameters, use default values from configuration file
    response = client.chat_completion(config_messages)
    
    if response:
        choice = response.get('choices', [{}])[0]
        message = choice.get('message', {})
        print(f"Knowledge assistant response:\n{message.get('content', 'No response content received')}")
    else:
        print("Request with default configuration failed")


if __name__ == "__main__":
    main()