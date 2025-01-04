from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast

js_code = """
function exampleFunction() {
    if (condition) {
        // code
    }
    for (let i = 0; i < 10; i++) {
        // code
    }
    while (condition) {
        // code
    }
}
"""

parser = Parser()
tree = parser.parse(js_code)

for node in nodevisitor(tree):
    if isinstance(node, ast.FunctionDeclaration):
        print('FunctionDeclaration:', node.identifier.name)
    elif isinstance(node, ast.IfStatement):
        print('IfStatement found')
    elif isinstance(node, ast.ForStatement):
        print('ForStatement found')
    elif isinstance(node, ast.WhileStatement):
        print('WhileStatement found')