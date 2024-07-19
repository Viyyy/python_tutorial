# 面向对象编程

面向对象编程（Object-Oriented Programming，简称OOP）是一种编程范式，它将数据和操作数据的方法组织在一起，形成一种称为“对象”的结构。面向对象编程的核心思想是将现实世界中的事物抽象成程序世界中的对象，通过对象之间的交互来完成程序的功能。

![Go 面向对象编程篇（三）：通过组合实现类的继承和方法重写 - 极客书房](https://tse1-mm.cn.bing.net/th/id/OIP-C.t2klS103O6n00M4jUvvLzgHaE7?rs=1&pid=ImgDetMain)

## 基本概念

### 1. 类（Class）

类是面向对象编程的基础，它是一个抽象的概念，用于描述具有相同属性和方法的对象的集合。类定义了对象的蓝图，规定了对象的属性（数据）和行为（方法）。

### 2. 对象（Object）

对象是类的实例，是具体的、可操作的数据实体。每个对象都有自己的状态和行为。例如，在现实世界中，斗牛犬、小猎犬和德国牧羊犬都是“狗”这个类的实例。

> 类与对象的关系：
>
> - 类是对具体事物（对象）的抽象化。
> - 对象是类的具体化。
>
> ![Java 对象和类_举例说明java中的对象-CSDN博客](https://www.runoob.com/wp-content/uploads/2013/12/20210105-java-object-1.png)

### 3. 属性（Attribute）

属性是对象所包含的数据，用来描述对象的某些特征。在类中，属性通常被定义为变量。

### 4. 方法（Method）

方法是对象可以执行的操作，它通常表现为函数。方法是类的一部分，用于操作对象的属性或实现某些功能。

### 5. 封装（Encapsulation）

封装是指将对象的实现细节隐藏起来，仅对外暴露必要的接口。封装可以保护对象的数据不被外部直接访问，保证了数据的安全性和一致性。

### 6. 继承（Inheritance）

继承是面向对象编程中实现代码复用的机制。通过继承，子类可以继承父类的属性和方法，并可以添加新的属性和方法或覆盖（Override）父类的方法。

### 7. 多态（Polymorphism）

多态是指同一个方法在不同类型的对象上具有不同的行为。在面向对象编程中，多态通常通过继承和接口实现，使得不同的对象可以响应相同的消息，执行不同的操作。

```python
from typing import Any, List
from abc import ABC, abstractmethod

class PrinterBase:
    '''
    PrinterBase 类，所有打印机类的基类
    '''
    def __init__(self, name:str):
        self.name = name

    @abstractmethod
    def print(self, content:Any)->None:
       pass

class ColorPrinter(PrinterBase):
    '''
    ColorPrinter 类，彩色打印机类，继承 PrinterBase 类
    '''
    def __init__(self, name:str, colors:List[str]):
        super().__init__(name)
        self.colors = colors

    def print(self, content:Any)->None:
        print(f"{content} in {self.colors}")

class BlackAndWhitePrinter(PrinterBase):
    '''
    BlackAndWhitePrinter 类，黑白打印机类，继承 PrinterBase 类
    '''
    def __init__(self, name):
        super().__init__(name)

    def print(self, content:Any)->None:
        print(f"{content} in black and white")

# 实例化对象
color_printer = ColorPrinter("HP Color LaserJet MFP M281fdw", ["red", "blue", "green"])
black_and_white_printer = BlackAndWhitePrinter("Epson WorkForce 2540")

# 多态，调用不同打印机类的 print 方法
content = "Hello, world!"
color_printer.print(content)
black_and_white_printer.print(content)
```

## 面向对象编程的特点

* **模块化** ：通过类和对象将程序划分为独立的模块，提高了代码的可重用性和可维护性。
* **易扩展** ：通过继承和多态，可以方便地扩展和维护代码。
* **易理解** ：面向对象编程更接近人类思维模式，便于理解和分析问题。

## Q: 什么时候用？

- 需要代码重用、模块化设计、模拟现实世界关系以及易于维护和扩展的复杂系统开发场景时。

## Q: 什么时候不适用？

- 编写简单的脚本或工具时
- 做数据处理或转换等函数式工作时
