import os
import json
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

from ..collector.amap import get_weather_by_address

MODEL_NAME = os.getenv('OPENAI_MODEL_NAME','gpt-3.5-turbo')
# 初始化OpenAI模型
LLM = ChatOpenAI(model=MODEL_NAME)

def parse_json(json_data:dict)->str:
    # 将JSON数据转换为字符串，以便GPT模型可以处理
    json_str = json.dumps(json_data, ensure_ascii=False)

    parse_json_prompt_template = ChatPromptTemplate.from_messages(
        [('system','You are good at parsing JSON data. please transfer the following JSON data to a detailed natural language description, using chinese characters.'),
        ('user', "{input}")]
    )

    parse_json_chain = parse_json_prompt_template | LLM

    result = parse_json_chain.invoke({'input': json_str})
    result = result.content
    return result

def generate(prompt:str, **kwargs)->str:
    '''
    使用llm生成文本
    '''
    # 文本生成模版
    prompt_template = PromptTemplate.from_template(prompt)

    response = LLM.invoke(prompt_template.format(**kwargs))
    result = response.content
    return result

def greet_from_weather(to_whom:str, weather_description:str)->str:
    '''
    使用llm生成问候语
    '''
    greeting_prompt = '''
        请帮我写一份温馨的早安问候，问候对象是: {to_whom}，要求如下：
        - 以信的格式完成。
        - 根据对象类型调整称呼和语气：
            - 长辈：使用“您”，语气更加礼貌，增加一句“祝您身体健康，平安健康！”
            - 朋友：语气轻松，增加一句笑话。
            - 男/女朋友：使用“亲爱的”作为开头和称呼，语气更加亲密，增加一句情话。
        - 包含当天的天气情况：{weather_description}，并给出穿衣和出行建议。
        - 可以使用emoji。
        - 结尾写一句祝福语。
        - 结尾不需要署名。
    '''
    result = generate(prompt=greeting_prompt, to_whom=to_whom, weather_description=weather_description)
    return result

def generate_weather_description(address:str)->str:
    '''
    根据地址获取天气描述
    '''
    weather_data = get_weather_by_address(address)
    weather_description = parse_json(weather_data)
    return weather_description

def greet_from_address(to_whom:str, address:str)->str:
    '''
    根据地址生成问候语
    '''
    weather = generate_weather_description(address)
    greeting = greet_from_weather(to_whom, weather)
    return greeting

