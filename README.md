
# remove-spaces

一个超轻量的 Python 脚本，用来批量去掉当前文件夹下所有文件名里的空格。

## 使用方法

1. 下载 `remove spaces.py`。
2. 把它放到需要处理的文件夹里。
3. 双击运行脚本。
4. 所有文件名中的空格会被移除。  
   - 如果新文件名已存在，脚本会自动在后面加 `_1`, `_2` 来避免覆盖。

## 示例

原始文件夹：
```
hello world.txt
my file.docx
```

运行后：
```
helloworld.txt
myfile.docx
```

## 环境要求
- Python 3.x（推荐 3.7+）
- 支持 Windows、macOS、Linux
