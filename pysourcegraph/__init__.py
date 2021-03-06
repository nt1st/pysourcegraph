"""
This package is a way for people who contribute to software to develop an
understanding of the codebase they wish to contribute to in a visual, intuitive
manner.
"""
from .nodes import BaseNode, PackageNode, ModuleNode, ClassNode, FunctionNode,\
                   ImportNode

from .parsing import tree_builder

from .graphing import tree_to_dot
