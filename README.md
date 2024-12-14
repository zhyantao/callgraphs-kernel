# CPP Code Analyzer

目标：B/S 架构、无需安装、运行在浏览器上。

开发工具：TypeScript, React & Webpack, IndexedDB & localStorage, Excalidraw

TODO:

- [ ] 绘制前端页面，可以上传源代码，并保存到数据库
- [ ] 可以从数据库中取出源代码，并原模原样地加载出来
- [ ] 读取其中一个文件，按照函数，列出每个函数调用的次级函数
- [ ] 读取多个文件，整理函数之间的调用关系，并绘制出图
- [ ] 将绘制出来的图，保存到数据库，下次可以打开
- [ ] 根据图形，使用 LLM 分析每个函数的作用
- [ ] 当下次有 BUG 时，可以分析出调用链，并给出建议

## Usage

```bash
git clone --recursive https://github.com/zhyantao/code-analyzer.git
# git submodule update --init

# 添加 PPA (Personal Package Archives) 源，此源可安装多个 Python 版本
sudo add-apt-repository ppa:deadsnakes/ppa

# 制定需要安装的 Python 版本号
PYTHON_VERSION=python3.8

# 安装另一个版本的 Python
sudo apt install $PYTHON_VERSION

# 使用新版本的 Python
$PYTHON_VERSION -m venv $PYTHON_VERSION --without-pip
source $PYTHON_VERSION/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | $PYTHON_VERSION
pip install -r requirements.txt
python tests/test_pycallgraph.py

# 安装编译环境
sudo apt remove llvm* clang* libclang*
sudo apt install graphviz llvm-12* clang-12* libclang-12* cmake
sudo ln -s /usr/bin/clang-12 /usr/bin/clang
sudo ln -s /usr/bin/opt-12 /usr/bin/opt
```
