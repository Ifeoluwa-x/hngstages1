from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def home():
    return jsonify({"slackUsername":"Aribo Ifeoluwa", "backend":True, "age":24, "bio":"Hi, My name is Ifeoluwa and i'm a backend developer."})

if __name__ == "__main__":
    app.run(debug=True,host='172.19.73.242:33507', port=33507)
