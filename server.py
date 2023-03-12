
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# using a secret key as we are using session to help use consistent data throuhout our routes
app.secret_key = 'La Republica Dominicana 🇩🇴'

# main page's route to display Dojo Survey 
@app.route('/')
def hello_world():
    return render_template('survey.html')

# Route is to pass our post data 
@app.route('/submit', methods=['POST'])
def submit():
    # Utilizing session to access the form data as it is returned in a dictionary 
    session['name'] = request.form['name']
    session['location'] = request.form['select_location']
    session['language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    # re-directing to our results route to avoid the re-submission of data
    return redirect ("/results")

# Helps us go to our results page 
@app.route('/results')
def surveyInfo():
    #  Rendering our results html page 
    return render_template('results.html')

# Creating this page to clear our session and delete it from our browser's cookies
@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)

