import re
from flask import * 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('cal.html')
@app.route('/calc', methods = ['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        if operation == 'addition':
            sum = float(num1)+float(num2)
            return render_template('cal.html', data=sum)
        elif operation == 'substraction':
            sub = float(num1)-float(num2)
            return render_template('cal.html', data=sub)
        elif operation == 'multiplication':
            mul = float(num1)*float(num2)
            return render_template('cal.html', data=mul)
        elif operation == 'division':
            div = float(num1)/float(num2)
            return render_template('cal.html', data=div)
        else:
            return render_template('cal.html')

if __name__ == '__main__':
    app.run(debug=True)