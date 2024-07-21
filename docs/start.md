# 编程环境

## 环境与包管理

### 环境管理

- conda：使用conda创建不同版本的独立环境
- venv：使用python自带的venv创建当前版本的环境

> windows: anaconda
>
> linux/mac: miniconda

### 包管理

配置镜像源：[pypi | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

> ##### ⭐好习惯：每个项目都写好一个requirements.txt，保证项目的可维护性、可移植性和稳定性。

使用pip导出

```auto
pip freeze > requirements.txt
```

使用conda导出环境配置

```auto
conda env export > environment.yml
# 恢复环境
# conda env create -f environment.yml
```

## 代码编辑器的选择

> 推荐VSCode：轻量化，扩展性强，自由度高。
>
> ![1721359109037](image/start/1721359109037.png)

> ##### ❗ 避坑：VSCode选择 `System`版本，如果是 `User`版本有时会出现权限不足的情况。

### VSCode vs Pycharm

|          特点/功能          |      Visual Studio Code (VSCode)      |                 PyCharm                 |
| :--------------------------: | :------------------------------------: | :-------------------------------------: |
|       **开发商**       |               Microsoft               |                JetBrains                |
|    **操作系统支持**    |         Windows, macOS, Linux         |          Windows, macOS, Linux          |
|     **开源/闭源**     | 部分开源（核心是开源的，部分插件不是） |                  闭源                  |
|        **价格**        |        免费（部分插件可能收费）        |        社区版免费，专业版需付费        |
|     **安装包大小**     |           较小，插件按需安装           |         较大，包含许多内置功能         |
|      **用户界面**      |              简洁，现代化              |               丰富，专业               |
|      **插件生态**      |         非常丰富，社区支持强大         |          较丰富，但不及VSCode          |
|    **智能代码补全**    |  有，依赖于插件（如Python extension）  |             内置，非常强大             |
|      **代码调试**      |       支持调试，有专门的调试界面       |      强大的调试功能，包括远程调试      |
|      **版本控制**      |              内置Git支持              |      内置Git和其他版本控制系统支持      |
|      **代码重构**      |           依赖插件，功能有限           |             内置，功能全面             |
|      **项目管理**      |       依赖插件进行项目管理和识别       |       内置项目管理和虚拟环境支持       |
|      **单元测试**      |              通过插件支持              |            内置单元测试支持            |
|     **数据库工具**     |              通过插件支持              |         内置数据库工具和SQL支持         |
| **科学计算和数据分析** |       通过插件支持（如Jupyter）       | 对科学计算友好，有专门的Scientific Mode |
|        **性能**        |           轻量级，启动速度快           |      功能丰富，启动和运行可能较慢      |

### Jupyter Notebook/lab

> **Jupyter**在需要交互性、展示性和即时反馈的场景下非常有用

#### 数据分析和探索

* 当你需要快速探索数据集，执行数据分析，或者进行数据可视化时。
* 当你想要立即看到代码执行的输出结果，以便实时调整你的分析策略。

#### 教育和教学

* 当你在教授编程或数据科学课程，并希望学生能够通过交互式的方式学习。
* 当你需要创建包含代码、解释文本、图像和数学公式的教学材料。

#### 研究和学术

* 当你在进行科学研究，需要记录实验步骤、代码和结果，以便于复现和分析。
* 当你需要将研究过程和发现整合成报告或论文。

#### 快速原型开发

* 当你在开发复杂系统之前，需要快速构建和测试某个算法或模型的原型。
* 当你需要将代码和其输出结果（如图表）结合起来，以验证想法或展示概念。

#### 文档和展示

* 当你需要创建包含代码和执行结果的文档，以展示项目或研究成果。
* 当你需要向非技术背景的受众展示技术内容，并且希望他们能够理解代码的执行过程。

## 推荐的VSCode插件

- `Office Viewer(Markdown Editor)`：用于markdown编辑
- `Remote - SSH`：用于远程开发
- `SQLite Viewer`：用于查看sqlite数据库
- `vscode-drawio`: 用于绘制流程图、技术路线图等结构化图

### 格式化插件

- `Black formatter`

需要在VSCode的 `settings.json`里配置：

```json
"[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
```

### AI编程助手

- `GitHub Copilot`
- `Fittencode`，可以使用微信登陆
