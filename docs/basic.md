# 基础语法

## 变量声明

在Python中，变量命名需要遵循以下规则：

1. **变量名必须以字母（a-z, A-Z）或下划线（_）开头** ，不能以数字开头。
2. **变量名不能包含空格** ，但可以使用下划线（_）来分隔单词，以提高可读性。
3. **变量名不能包含标点符号** ，如!、@、#、$、%、^、&、*、(、)、-、+、=、{、}、[、]、:、;、"、'、<、>、?、/、\。
4. **变量名不能是Python中的关键字** ，如 `and`, `if`, `while`, `for`, `True`, `False`等。
5. **变量名对大小写敏感** ，这意味着 `variable`和 `Variable`是两个不同的变量。

```csharp
x = 10  # 整数
y = "Hello"  # 字符串
```

> Python是动态类型的语言，不需要显式声明变量的数据类型。

> ##### ⭐好习惯：命名应该能够清晰描述变量的信息，方便其他开发者理解。

> ##### python的命名习惯：
>
> - **使用小写字母和下划线** ：对于变量和函数，使用小写字母和下划线来提高可读性
> - **使用大写字母来定义类名** ：对于类名，使用大驼峰命名法（PascalCase），即每个单词的首字母都大写。
> - **使用大写字母来定义常量** ：对于常量，使用全部大写字母，并用下划线分隔单词。
> - **私有变量和方法** ：对于类中的私有变量和方法，使用两个前导下划线。
> - **保持一致性** ：在代码库中保持一致的命名习惯。
> - **函数和方法参数** ：参数名应该小写，必要时使用下划线。

### 基本数据类型

#### 数字（Numeric Types）

1. **整数（int）** ：表示整数，没有小数点。例如：`10`, `-5`, `0`.
2. **浮点数（float）** ：表示带有小数点的数。例如：`3.14`, `-0.001`, `5.0`.
3. **复数（complex）** ：表示实部和虚部的组合，使用 `j` 或 `J` 表示虚部。例如：`2 + 3j`, `1.5 - 2.5j`.

#### 序列（Sequence Types）

1. **字符串（str）** ：表示文本数据，由一系列字符组成。例如：`"Hello, World!"`, `'Python'`.
2. **列表（list）** ：表示有序的元素集合，元素可以是不同类型。例如：`[1, 'a', 3.14, [2, 3]]`.
3. **元组（tuple）** ：表示不可变的有序元素集合，元素可以是不同类型。例如：`(1, 'a', 3.14)`.

#### 映射（Mapping Type）

1. **字典（dict）** ：表示键值对的集合，键必须是不可变类型，通常是字符串或数字。例如：`{'name': 'Alice', 'age': 30}`.

#### 集合（Set Types）

1. **集合（set）** ：表示无序且元素唯一的集合，元素通常是不可变类型。例如：`{1, 2, 3}`.
2. **冻结集合（frozenset）** ：表示不可变的集合类型。例如：`frozenset({1, 2, 3})`.

#### 布尔类型（Boolean Type）

1. **布尔（bool）** ：表示逻辑值 `True` 或 `False`。例如：`True`, `False`.

> 除了这些基本类型，Python 还有一些特殊的数据类型，如 `NoneType`，用于表示 `None` 值，这是一个特殊的常量，表示空值或无值。

```python
# 查看数据类型
x = 10
print(type(x)) # -> <class 'int'>
```

### 可变变量和不可变变量

在 Python 中，变量是对象的引用。变量本身没有类型，它们引用的对象才有类型。根据对象是否可以被修改，可以将变量分为两类：可变（mutable）和不可变（immutable）。

#### 不可变（Immutable）变量

不可变变量指的是那些一旦创建，其值就不能被更改的对象。这意味着如果尝试修改不可变对象，实际上会创建一个新的对象，并将变量指向这个新对象。

以下是一些常见的不可变类型：

- **整数（int）** ：整数类型的值一旦设定，就不能更改。

```python
   a = 10
   a = a + 1  # 这实际上是将 a 指向了一个新的整数对象 11
```

- **浮点数（float）** ：浮点数也是不可变的。

```python
   b = 3.14
   b = 2.71  # b 现在指向了新的浮点数对象 2.71
```

- **字符串（str）** ：字符串在 Python 中是不可变的。

```python
   s = "hello"
   s = s + " world"  # s 现在指向了新的字符串对象 "hello world"
```

- **元组（tuple）** ：虽然元组可以包含可变对象，但元组本身是不可变的。

```python
   t = (1, 2, [3, 4])
   t[2][0] = 5  # 这会改变列表中的元素，但不会改变元组本身
   # t[0] = 100  # 这会引发错误，因为元组是不可变的
```

#### 可变（Mutable）变量

可变变量是指那些可以被修改的对象，也就是说，可以在不创建新对象的情况下改变对象的内部状态。

以下是一些常见的可变类型：

- **列表（list）** ：列表是可变的，你可以添加、删除或修改列表中的元素。

```python
   lst = [1, 2, 3]
   lst[0] = 100  # 修改列表的第一个元素
   lst.append(4)  # 向列表中添加一个新元素
```

- **字典（dict）** ：字典也是可变的，可以添加新的键值对或修改现有的键值对。

```python
   d = {'a': 1, 'b': 2}
   d['a'] = 10  # 修改字典中的 'a' 键的值
   d['c'] = 3   # 向字典中添加一个新的键值对
```

- **集合（set）** ：集合是可变的，可以添加或删除元素。

```python
   st = {1, 2, 3}
   st.add(4)  # 向集合中添加一个新元素
   st.remove(1)  # 从集合中删除一个元素
```

> 了解变量的可变性和不可变性对于理解 Python 中的数据结构和编写高效、无错误的代码至关重要。例如，不可变对象可以作为字典的键，而可变对象则不可以。

> ##### ❗避坑：函数的形参如果是可变变量，默认值要设置为None

- 错误的：

```python
def append_to(element, to=[]):
    to.append(element)
    return to

# 调用函数
my_list = append_to(1)
print(my_list)  # 输出: [1]

another_list = append_to(2)
print(another_list)  # 输出: [1, 2]，这不是我们期望的结果

```

- 推荐的：

```python
def append_to(element, to=None):
    if to is None:
        to = []  # 创建一个新的列表
    to.append(element)
    return to

# 调用函数
my_list = append_to(1)
print(my_list)  # 输出: [1]

another_list = append_to(2)
print(another_list)  # 输出: [2]，这是期望的结果

```

## 函数声明

> 在Python中，使用def关键字来声明函数：

```python
def add(x, y):
    # 函数体
    return x + y
```

## 控制流

### **条件语句** - 使用 `if`, `elif`, `else` 关键字。

```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### **循环** - `for` 循环和 `while` 循环。

```python
# for循环
for i in range(5):
    print(i)

# while循环
while x > 0:
    print(x)
    x -= 1
```

### **异常处理** - 使用 `try` 和 `except`。

```python
try:
    # 可能引发异常的代码
    pass
except Exception as e:
    # 异常处理代码
    pass
```

## 行与缩进

|   特征/语言   |      Python      |       Java       |        C#        |
| :------------: | :--------------: | :---------------: | :---------------: |
| 代码块区分方式 |     使用缩进     | 使用大括号 `{}` | 使用大括号 `{}` |
|   行结束符号   | 不需要分号 `;` |  需要分号 `;`  |  需要分号 `;`  |

- python

```python
# Python中的单行代码
x = 10  # 这是一行Python代码，不需要分号

# Python中的代码块
def my_function():
    # 这是my_function的代码块
    y = 20  # 块内的一个代码行
    print("Hello, World!")  # 另一个代码行

if x > 10:
    # 这是一个if语句的代码块
    print("x is greater than 10")  # 块内的代码行

```

- Java

```java
// Java中的单行代码
int x = 10; // 这是一行Java代码，以分号结束

// Java中的代码块
public class MyClass {
    public static void main(String[] args) {
        // 这是main方法的代码块
        int y = 20; // 块内的一个代码行
        System.out.println("Hello, World!"); // 另一个代码行
    }
}

```

- C#

```csharp
// C#中的单行代码
int x = 10; // 这是一行C#代码，以分号结束

// C#中的代码块
public class MyClass {
    public static void Main(string[] args) {
        // 这是Main方法的代码块
        int y = 20; // 块内的一个代码行
        Console.WriteLine("Hello, World!"); // 另一个代码行
    }
}

```

## 注释

> ##### ⭐好习惯：编写注释是编程中非常重要的一个方面，它有助于他人（或未来的你）理解代码的意图和工作原理。

- 单行注释：使用井号

```python
# 这里是单行注释的内容
```

- 多行注释：使用三引号

```python
'''
这里是多行注释：
注释1
注释2
……
'''
```

- 区域划分：起始 `# region 描述`，结束 `# endregion`

```python
# region 打招呼
def hello():
  print("hello, world.")
# endregion
```

> VSCode的注释快捷键：Ctrl+/

## 类型注解：Typehint

Type hinting（类型注解）是Python 3.5及以上版本中引入的一个特性，它允许开发者在代码中指定变量的预期类型。

> ##### ⭐好习惯：使用typehint指定函数形参的类型以及函数返回的类型。

### 用途：

1. **代码可读性** ：类型注解可以帮助开发者更快地理解代码的意图和数据流。
2. **代码维护** ：在代码重构或修改时，类型注解有助于确保更改不会破坏现有的数据类型假设。
3. **静态类型检查** ：使用像 `mypy`这样的静态类型检查工具，可以在不运行代码的情况下发现潜在的类型错误。
4. **IDE支持** ：现代IDE和编辑器可以利用类型注解来提供更好的代码补全、错误提示和代码导航。

- 没有使用typehint

```python
def divice(a, b):
    '''
    计算两个数的商
    :param a: 被除数
    :param b: 除数
    :return: 商
    '''
    assert b!= 0, "除数不能为0"
    return a / b

result = divice("Hello, ", "world!")  # 类型错误，字符串不是浮点数
```

- 使用了typehint

```python
# 可以使用mypy进行静态类型检查
def divice(a:float, b:float)->float:
    '''
    计算两个数的商
    :param a: 被除数
    :param b: 除数
    :return: 商
    '''
    assert b!= 0, "除数不能为0"
    return a / b
```

```python
def print_upper(s:str)->str:
    '''
    打印字符串的大写版本
    :param s: 字符串
    :return: 字符串的大写版本
    '''
    return s.upper() # 使用了typehint，IDE会有代码补全和错误提示
```
