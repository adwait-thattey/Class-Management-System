from flask import Flask ,render_template,request,session,redirect,url_for
#import the functions
app = Flask(__name__)

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == 'POST':
        age = request.form['age']
        name = request.form[]


        return render_template('age.html',age=age)
        
    return render_template('form.html')
    

if __name__ == "__main__":
    app.run(debug=True)