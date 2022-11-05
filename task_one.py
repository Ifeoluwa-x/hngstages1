import openai
# from api_secrets import API_KEY
from flask import Flask,json,jsonify
from flask import jsonify,request
from enum import Enum





app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


class Operate(Enum):
    addition = "+"
    subtraction = "-"
    multiplication = "*"
    
    
    
    @app.route("/",  methods = ['GET'])
    def getDeets():
        return jsonify({"slackUsername":"Aribo Ifeoluwa", "backend":True, "age":24, "bio":"Hi, My name is Ifeoluwa and i'm a backend developer."})

    @app.route("/",  methods = ['POST'])
    def calculateDeets():
        res = request.json
        values = set(item.name for item in Operate) 
        sign = res['operation_type'] #"addition"
        if res['operation_type'] in values:
            operator = Operate[sign].value
            first_Num = int(res['x'])
            second_Num = int(res['y'])
            if operator == "+":
                result = first_Num + second_Num
                return jsonify({ "slackUsername": "Aribo ifeoluwa", "result": result , "operation_type": sign })
            elif operator == "-":
                result = first_Num - second_Num
                return jsonify({ "slackUsername": "Aribo ifeoluwa", "result": result , "operation_type": sign })
            else:
                result = first_Num * second_Num
                return jsonify({ "slackUsername": "Aribo ifeoluwa", "result": result , "operation_type": sign })
        else:
            openai.api_key = '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'
            req = res['operation_type']
            response = openai.Completion.create(model="text-davinci-002", prompt=req, temperature=0, max_tokens=20)
            response_Result = response['choices']
            final_text = response_Result[0]['text']
            spliter = (final_text.split())
            result = spliter[-1]
            # return final_text
        # if "+" in final_text and "sum" or "add" or "togetherness" or "together" or "plus" or "altogether" or "total"  in req:
        #     return jsonify({ "slackUsername": "Aribo ifeoluwa", "result": result , "operation_type": "addition" })
        
        if "-" in final_text and "minus" or "greater than" or "take away" or "fewer than" or "less than"or "subtract" or "decreased by" in req:
            return jsonify({ "slackUsername": "Aribo koko ifeoluwa", "result": result })
        
        elif "*" in final_text and "product" or "multiply" or "multiplied by" or "times" in req:
            return jsonify({ "slackUsername": "Aribo ifeoluwa", "result": result})
        
        else:
            return jsonify({"error":"Please the ai can't calculate this"})
            

if __name__ == "__main__":
    app.run(debug=True, port=33507)
