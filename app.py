from classifier import get_prediction
from flask import Flask,jsonify,request

app=Flask(__name__)
@app.route("predict_digit",methods=['POST'])
def predictData():
    
    image=request.files.get("digit")
    prediction=get_prediction(image)
    return jsonify({
        "prediction": prediction
    }),200
if __name__=="__main__":
    app.run(debug=True)