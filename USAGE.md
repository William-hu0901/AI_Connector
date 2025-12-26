DeepSeek API Usage Guide
========================

1. Obtain DeepSeek API Key
--------------------------
To use the DeepSeek API, you need to obtain an API key first:
- Visit https://www.deepseek.com/ to register an account
- Log in and go to the developer panel
- Create a new API key and copy it for safekeeping

2. Configure API Key
------------------
Enter the obtained API key in the config.ini file:
```
[deepseek]
api_key = your_actual_deepseek_api_key_here
base_url = https://api.deepseek.com
```

3. Configure Model Parameters
---------------------------
You can configure default model parameters in config.ini:
```
[model_params]
model = deepseek-chat          # Model to use
max_tokens = 1000              # Maximum output token count
temperature = 0.7              # Temperature parameter, controls output randomness
```

4. Install Dependencies
----------------------
Run in the project directory:
```
pip install -r requirements.txt
```

5. Run the Program
-----------------
```
python deepseek_client.py
```

6. API Function Description
-------------------------
- chat_completion(): Chat completion API, used for conversation generation
- get_models(): Get list of available models
- Support for custom parameters (model, max tokens, temperature, etc.)

7. Notes
-------
- Please keep your API key secure and do not share it with others
- Be aware of API call frequency limits and costs
- Adjust the temperature parameter as needed to control output creativity