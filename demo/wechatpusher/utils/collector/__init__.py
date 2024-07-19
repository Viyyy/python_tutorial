import os
from dotenv import load_dotenv
from ..common import do_call

# 加载环境变量
load_dotenv()

# 获取高德地图API密钥
AMAP_API_KEY = os.getenv('AMAP_API_KEY', None)

def get_geocodes(address, key=AMAP_API_KEY)->list:
    '''
    根据地址获取地理编码
    :param address: 地址
    :param key: 高德地图API密钥
    :return: 地理编码列表
    '''
    # 获取地理编码的URL
    url = 'https://restapi.amap.com/v3/geocode/geo'
    
    # 请求参数
    params = {
        'address': address,
        'output': 'JSON',
        'key': key
    }
    
    # 发送请求并获取响应
    res = do_call(url=url, params=params, method='GET')
    
    # 解析响应
    result = res.json()
    if (info:=result.get('info')) == 'OK':
        return result['geocodes']
    else:
        assert False, f'Error: {info}'
    
def get_adcode(address, key=AMAP_API_KEY)->str:
    # 获取地理编码
    geocodes = get_geocodes(address, key)
    if geocodes:
        return geocodes[0]['adcode']
    else:
        return None
    
def get_weather(adcode:str, type_:str='all', key=AMAP_API_KEY)->dict:
    # 验证请求类型
    assert type_ in ['base', 'all']
    
    # 获取天气信息的URL
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    
    # 请求参数
    params = {
        'city': adcode,
        'key': key,
        'extensions': type_,
        'output': 'JSON'
    }
    
    # 发送请求并获取响应
    res = do_call(url=url, params=params, method='GET')
    result = res.json()
    if (info:=result.get('info')) == 'OK':
        return result['lives' if type_ == 'base' else 'forecasts'][0]
    else:
        assert False, f'Error: {info}'

def get_weather_by_address(address:str, type_:str='all', key=AMAP_API_KEY)->dict:
    # 获取行政区编码
    adcode = get_adcode(address, key)
    if adcode:
        return get_weather(adcode, type_, key)
    else:
        return None