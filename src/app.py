from flask import Flask
from flask import request
import json

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():    
    json_text = json.dumps(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todos.append(json.loads(request.data))
    return json.dumps(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)    
    return json.dumps(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)