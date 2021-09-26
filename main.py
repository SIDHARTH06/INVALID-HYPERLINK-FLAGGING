from check import *
from flask import Flask, request, render_template ,request
# Flask constructor
app = Flask(__name__)
@app.route('/')
def show():
   return render_template('index.html')
@app.route('/result',methods =["GET", "POST"])
def result():
      if(request.method=="POST"):
        result = request.form.get('flink')
        valid=action(result)
        broken=actiona(result)
      return render_template("result.html",valid = valid,broke=broken)
if __name__ == '__main__':
   app.run(debug = True)




    
