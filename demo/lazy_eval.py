# -*- coding: utf-8 -*-
# Author: Vi
# Created on: 2024-07-23 14:46:48
# Description: Lazy evaluation demo

import sys
from pprint import pprint
from typing import Iterable, Generator
import tracemalloc

file_path = r"docs\paradigm.md"

class MemoryLogger:
    def __init__(self, do_print:bool, do_memory:bool):
        '''
        初始化 MemoryLogger 类
        :params do_print: 是否打印内存使用信息
        :params do_memory: 是否记录内存使用信息
        '''
        self.do_print = do_print
        self.do_memory = do_memory
        self.memories = [] # 记录内存分配信息
        
    def reset(self):
        '''
        重置内存使用信息
        '''
        self.memories = []
    
    def __call__(self, do_print:bool=None, do_memory:bool=None):
        """
        装饰器函数，用于查看函数运行时内存占用
        :params do_print: 是否打印内存使用信息
        :params do_memory: 是否记录内存使用信息
        """
        
        if do_print is None:
            do_print = self.do_print
            
        if do_memory is None:
            do_memory = self.do_memory
            
        if not do_print and not do_memory:
            return lambda func: func  # 无需记录内存，直接返回原函数

        def wrapper(func):
            def inner(*args, **kwargs):
                tracemalloc.start()  # 启动内存跟踪功能
                tracemalloc.reset_peak()  # 重置内存使用峰值
                
                result = func(*args, **kwargs)  # 调用被装饰的函数，并保存结果

                current, peak = tracemalloc.get_traced_memory()# 获取当前内存使用量和峰值内存使用量

                tracemalloc.stop()  # 停止内存跟踪
                
                # 打印当前内存使用量，峰值内存使用量，和 tracemalloc 的内存使用量
                usage_dict = {
                    "Function": func.__name__,
                    "Current(Bytes)": current,
                    "Peak(Bytes)": peak,
                    "Return(Bytes)": sys.getsizeof(result),
                    "Return Type": type(result).__name__,
                }
                
                # usage_dict = {
                #     "函数名": func.__name__,
                #     "当前使用内存": current,
                #     "峰值使用内存": peak,
                #     "结果大小": sys.getsizeof(result),
                #     "结果类型": type(result).__name__,
                # }
                
                if do_print: 
                    print("-" * 80)  # 打印分隔线
                    pprint(usage_dict, sort_dicts=False)
                
                if do_memory:
                    self.memories.append(usage_dict)

                return result  # 返回函数的结果

            return inner  # 返回内部函数

        return wrapper  # 返回装饰器函数

memory_logger = MemoryLogger(do_print=False, do_memory=True)

@memory_logger()
def read_filelines(file_path: str) -> Iterable:
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.readlines()
    return contents


@memory_logger()
def read_file(file_path: str) -> Generator:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line

def print_lines(lines: Iterable):
    for line in lines:
        a = line.strip()
        
@memory_logger()
def read_and_use_filelines(file_path: str)->None:
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.readlines()
    for line in contents:
        a = line.strip()
     
@memory_logger()
def read_and_use_file(file_path: str)->None:
    def __read_file(file_path: str)->Generator:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                yield line
    
    for line in __read_file(file_path):
        a = line.strip()

def print_size(obj):
    print(f"{sys.getsizeof(obj)=}, {type(obj)=}")


def main():
    result1 = read_file(file_path)
    print_lines(result1)
    result2 = read_and_use_file(file_path)

    result3 = read_filelines(file_path)
    print_lines(result3)
    result4 = read_and_use_filelines(file_path)
    
    import pandas as pd
    
    df = pd.DataFrame(memory_logger.memories)
    print(df.head())


if __name__ == "__main__":
    main()
