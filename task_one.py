import os
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/", methods=['GET'])
def home():
    return jsonify({"slackUsername":"ifeoluwa_x",  "backend":True,  "age":24,  "bio":"Hi, My name is Ifeoluwa and i'm a backend developer."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
