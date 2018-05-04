from flask import Flask, render_template, request
'''
This is the primary app, or "server" .py file. Flask links the .html files through routes. render_template is used to
navigate between the html files. Request is used to pull data from the forms on the form.html page.

Guide to HTML:
1. home.html - the home page, has a "jumbotron" style to display whatever the FFA would like to display.
2. layout.html - flask uses this to set a template for all of the webpages. In this app, it is the navbar on all pages.
3. form.html - Has the html registry page that gives the data to our .csv file.
4. reroute.html - I used this as a way to show that the registry was successful, it has a quick button to return to the form.html

Lastly in the folder is ffaregistry.csv, it contains the data saved from form.html broken down line by line.

'''

app = Flask(__name__)

'''
Below are the routes that will navigate the pages. Also to call the post function in the /reroute route.
'''
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')


'''
Below is the POST function. On the page form.html, when the user hits the submit button it activates the POST method.
Each of the text fields and select fields are saved in a variable within the function.
Instead of a database, we used a CSV file to save the .csv file to save data.
On the .csc file 'ffaregistry.csv' it will list the contents of the fields line by line for easy copy and paste.
'''

@app.route('/reroute', methods=['POST'])
def reply():
    student1 = request.form['s1']
    student2 = request.form['s2']
    student3 = request.form['s3']
    student4 = request.form['s4']
    student5 = request.form['s5']
    student6 = request.form['s6']
    student7 = request.form['s7']
    student8 = request.form['s8']
    subject = request.form['subject_input']
    school = request.form['school_input']


    if request.method == "POST":
        f = open('ffaregistry.csv', 'a')
        f.write(','.join([school, subject, student1, student2, student3, student4, student5, student6, student7, student8 + '\n']))

        return render_template('reroute.html')



if __name__ == '__main__':
    app.run(debug=True)

