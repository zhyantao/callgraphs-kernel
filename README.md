# CPP Code Analyzer

## Usage

```bash
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
python tests/test_pycallgraphviz.py

# 安装编译环境
sudo apt remove llvm* clang* libclang*
sudo apt install graphviz llvm-12* clang-12* libclang-12* cmake
sudo ln -s /usr/bin/clang-12 /usr/bin/clang
sudo ln -s /usr/bin/opt-12 /usr/bin/opt
```