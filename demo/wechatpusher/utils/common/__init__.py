import requests
import hashlib
import time
import uuid

def do_call(url:str, params:dict, method:str, header:dict=None)->requests.Response:
    """
    发起HTTP请求
    :param url: 请求的URL
    :param params: 请求参数
    :param method: 请求方法（GET或POST）
    :param header: 请求头，默认为None
    :return: requests.Response对象
    """
    if not header:
        header = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    if 'get' == method.lower():
        return requests.get(url, params)
    elif 'post' == method.lower():
        return requests.post(url, params, header)
    else:
        raise ValueError('Unsupported method: %s' % method)

def addAuthParams(appKey, appSecret, params):
    """
    添加鉴权参数到请求参数中
    :param appKey: 应用ID
    :param appSecret: 应用密钥
    :param params: 请求参数
    """
    q = params.get('q')
    if q is None:
        q = params.get('img')
    q = "".join(q)
    salt = str(uuid.uuid1())
    curtime = str(int(time.time()))
    sign = calculateSign(appKey, appSecret, q, salt, curtime)
    params['appKey'] = appKey
    params['salt'] = salt
    params['curtime'] = curtime
    params['signType'] = 'v3'
    params['sign'] = sign


def returnAuthMap(appKey, appSecret, q):
    """
    返回包含鉴权参数的字典
    :param appKey: 应用ID
    :param appSecret: 应用密钥
    :param q: 请求内容
    :return: 包含鉴权参数的字典
    """
    salt = str(uuid.uuid1())
    curtime = str(int(time.time()))
    sign = calculateSign(appKey, appSecret, q, salt, curtime)
    params = {'appKey': appKey,
              'salt': salt,
              'curtime': curtime,
              'signType': 'v3',
              'sign': sign}
    return params

def calculateSign(appKey, appSecret, q, salt, curtime):
    """
    计算鉴权签名
    :param appKey: 应用ID
    :param appSecret: 应用密钥
    :param q: 请求内容
    :param salt: 随机值
    :param curtime: 当前时间戳
    :return: 鉴权签名
    """
    strSrc = appKey + getInput(q) + salt + curtime + appSecret
    return encrypt(strSrc)


def encrypt(strSrc):
    """
    使用SHA256加密字符串
    :param strSrc: 待加密的字符串
    :return: 加密后的字符串
    """
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(strSrc.encode('utf-8'))
    return hash_algorithm.hexdigest()


def getInput(input):
    """
    处理输入内容，如果长度超过20，则截取前10个字符和后10个字符，并在中间插入长度
    :param input: 输入内容
    :return: 处理后的输入内容
    """
    if input is None:
        return input
    inputLen = len(input)
    return input if inputLen <= 20 else input[0:10] + str(inputLen) + input[inputLen - 10:inputLen]