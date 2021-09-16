import os
import textwrap
import csv
from flask import Flask, render_template, send_from_directory, request, redirect


app = Flask(__name__)


def write_to_file(data):
    try:
        with open('database.txt', 'a') as database:
            email = data['email']
            subject = data['subject']
            message = data['message']
            database.write(f'\n{email}\t{subject}\t{message}')
    except:
        return 'Could not save to database'

def write_to_csv(data):
    try:
        with open('database.csv', 'a', newline='') as database:
            email = data['email']
            subject = data['subject']
            message = data['message']
            csv_writer = csv.writer(database, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            csv_writer.writerow([email, subject, message])
    except:
        print('Could not save to database')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')    
    else:
        return 'something went wrong, try again!'
