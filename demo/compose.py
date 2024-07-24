# -*- coding: utf-8 -*-
# Author: Vi
# Created on: 2024-07-23 16:42:33
# Description: Compose demo

'''
函数组合是一种编程技术，通过将多个函数组合成一个新的函数，使得输入数据可以顺序地经过这些函数的处理。这种技术有许多优点，但也有一些缺点。以下是函数组合的优缺点分析：

### 优点

1. **简洁和可读性**：
   - 通过函数组合，可以将复杂的操作分解为多个简单的函数，每个函数只关注一个任务。这使得代码更易读，更易理解。
   - 使用管道符 `|` 或其他组合操作符，可以直观地表示数据流的处理过程。

2. **模块化和复用性**：
   - 每个函数都是一个独立的模块，可以单独测试和调试。
   - 这些独立的函数可以在不同的组合中重复使用，提高代码的复用性。

3. **易于测试**：
   - 由于每个函数都是独立的单元，可以单独编写测试用例，确保每个函数的正确性。
   - 函数组合后的新函数也可以通过组合单元测试来验证。

4. **灵活性和可扩展性**：
   - 可以轻松地添加、删除或替换组合中的函数，以满足不同的需求。
   - 函数组合使得代码更具灵活性，适应变化的需求更加容易。

5. **函数式编程范式**：
   - 函数组合是函数式编程的重要特性之一，有助于实现无副作用的代码，提高代码的可靠性和可维护性。

### 缺点

1. **调试困难**：
   - 当组合的函数链较长时，如果出现错误，可能很难确定是哪个函数导致的问题。调试可能需要逐步检查每个函数的输出。

2. **性能开销**：
   - 函数组合可能会带来一些性能开销，特别是当每个函数调用都涉及到大量的数据传递时。这是因为每个函数调用都会有一定的开销。

3. **类型安全**：
   - 在动态类型语言（如 Python）中，函数组合可能会导致类型不匹配的问题。需要确保每个函数的输入和输出类型是兼容的，否则可能会导致运行时错误。

4. **复杂性增加**：
   - 虽然函数组合可以简化代码的逻辑，但在某些情况下，过度使用函数组合可能会增加代码的复杂性，特别是当组合的函数数量很多时。

5. **依赖管理**：
   - 当函数组合涉及到外部依赖时（如数据库连接、网络请求等），需要小心管理这些依赖，以避免资源泄露或不一致的状态。

### 总结

函数组合是一种强大的编程技术，能够提高代码的简洁性、可读性和复用性。然而，使用函数组合时也需要注意调试、性能、类型安全和依赖管理等问题。合理地使用函数组合，可以大大提高代码的质量和开发效率。
'''

import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_EVEN
from typing import List, Union
from functools import reduce
from functools import partial

def to_ndarray(list_of_series: Union[list, pd.Series]) -> np.ndarray:
    return np.array(list_of_series)


def to_decimal(arr: np.ndarray) -> np.ndarray:
    return arr.astype(Decimal)


def divide_by_10(arr: np.ndarray) -> np.ndarray:
    return arr * 0.1


def power_with_10(arr: np.ndarray) -> np.ndarray:
    return np.power(10, arr)


def mul10(arr: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    return 10 * arr


def round_half_even(value: float, precision: int = 1) -> float:
    """
    对给定的浮点数进行四舍五入操作，并遵循四舍五入六成双的规则。

    Args:
        value (float): 待四舍五入的浮点数。
        num: 保留的小数位数，默认值为1，即保留1位小数。

    Returns:
        float: 四舍五入后的结果。
    """
    try:
        return float(
            Decimal(value).quantize(
                Decimal(f"{10**(-precision)}"), rounding=ROUND_HALF_EVEN
            )
        )
    except:
        return "-"


def compose(*funcs):
    return lambda x: reduce(lambda v, f: f(v), funcs, x)

pre_process = compose(to_ndarray, to_decimal)
calc_Leq = compose(
    divide_by_10,
    power_with_10,
    np.mean,
    np.log10,
    mul10,
    partial(round_half_even, precision=1),
)

dbs = [61, 43, 45, 94, 56, 75]
dbs_pre = pre_process(dbs)
Leq = calc_Leq(dbs_pre)

print(Leq)
