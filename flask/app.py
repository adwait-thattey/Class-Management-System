from flask import Flask ,render_template,request,session,redirect,url_for
#import the functions
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def send():
    if request.method == 'POST':
        email = request.form['email']
        #name = request.form[]
        password = request.form['password']

        return render_template('webpage.html')
        
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)