import ast
import astor
import os
from graph import PythonDocstringGenerator


def add_placeholder_docstring(node: ast.FunctionDef) ->ast.FunctionDef:
    """Adds a placeholder docstring to a function node."""
    result = PythonDocstringGenerator(node=node).run()
    node.body.insert(0, ast.Expr(value=result['comment']))
    return node


def analyze_and_modify_file(filename):
    """Analyzes a single Python file and adds placeholder docstrings where necessary."""
    with open(filename, 'r') as file:
        content = file.read()
    tree = ast.parse(content)
    modified = False
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and not ast.get_docstring(node):
            issues.append(
                f"Added placeholder docstring for function '{node.name}' in file '{filename}'."
                )
            add_placeholder_docstring(node)
            modified = True
    if modified:
        with open(filename, 'w') as file:
            file.write(astor.to_source(tree))
    return issues


def main():
    all_issues = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                print(f'Analyzing file {file}...')
                filepath = os.path.join(root, file)
                all_issues.extend(analyze_and_modify_file(filepath))
    with open('code_analysis_report.txt', 'w') as report:
        if all_issues:
            report.write('The following modifications were made:\n')
            for issue in all_issues:
                report.write(issue + '\n')
        else:
            report.write(
                'All functions already had docstrings. No modifications needed.'
                )


if __name__ == '__main__':
    main()
