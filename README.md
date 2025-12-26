# AI_Connector

This is a client program that connects to various AI large models, including sample code for calling the DeepSeek API service. It will continuously add examples for calling other large model APIs and gradually form AI Agent-like functionality.

## Usage

1. Enter your DeepSeek API key in the [config.ini](file:///C:/Users/delon/PycharmProjects/AI_Connector/config.ini) file:
   ```
   [deepseek]
   api_key = your_actual_deepseek_api_key_here
   base_url = https://api.deepseek.com
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the program:
   ```
   python deepseek_client.py
   ```

## Features

- Get list of available models
- Call chat completion API
- Support for custom conversation parameters (model, max tokens, temperature, etc.)

## API Key Acquisition

To use the DeepSeek API, you need to:
1. Register an account on the DeepSeek official website
2. Obtain an API key from the developer panel
3. Enter the API key in the configuration file