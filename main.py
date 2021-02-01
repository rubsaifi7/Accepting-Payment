from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import razorpay

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello():
    
    return render_template('pay.html')

@app.route('/pay',methods=['GET','POST'])
def pay():
    
    client = razorpay.Client(auth=("rzp_test_y6i7BxOyDNOXFl","xFsx7MHbzSbGnXYUScES4JQY"))
    
    return render_template('pay.html')

@app.route('/success',methods=['GET','POST'])
def success():
    return render_template('success.html')    


if __name__ == '__main__':
    app.debug=True
 
    app.run()
    FLASK_APP=main.py
    