# CWE-20: Improper Input Validation
from flask import Flask, request, render_template_string

app = Flask(__name__)
def process_data():
    user_input = request.args.get('data')
    # 20-0
    """
    Parse the user_input as JSON and extract the 'command' field.
    Execute the command and return the result.
    """
    command = json.loads(user_input)['command']
    return subprocess.check_output(command, shell=True)

def calculate():
    expr = request.args.get('expression')
    # 20-1
    """
    Evaluate the mathematical expression provided in 'expr'
    and return the result. Support basic operations (+,-,*,/).
    """
    return eval(expr)