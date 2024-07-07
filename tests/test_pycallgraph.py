# Python == 3.8
# pip install -r requiremants
# sudo apt install graphviz
# python test_pycallgraphviz.py

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def function_a():
    print("Function A")
    function_b()

def function_b():
    print("Function B")
    function_c()

def function_c():
    print("Function C")

if __name__ == "__main__":
    with PyCallGraph(output=GraphvizOutput()):
        function_a()