#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# June 2017
# Flask User Sign-up re: LaunchCode
# Rubric: http://education.launchcode.org/web-fundamentals/assignments/user-signup/


from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["POST", "GET"])
def index():

    username = ''
    email = ''
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    title = 'Login'

    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']

        if not username:
            username_error = "That's not a valid username."

        if (len(username) <= 3) or (len(username) > 20) or (" " in username):
            username_error = "That's not a valid username"
            username = ''

        if (not password) or (len(password) <= 3) or (len(password) > 20) or (" " in password):
            password_error = "That's not a valid password"

        if (not verify_password) or (password != verify_password):
            verify_password_error = "Passwords do not match."

        if (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
            email_error = "That's not a valid email address."
            email = ''

        if (not username_error) and (not password_error) and (not verify_password_error) and (not email_error):
            return redirect("/welcome?username={0}".format(username))
        
    return render_template('signup_form.html', title=title, username=username, email=email,
                           username_error=username_error, password_error=password_error,
                           verify_password_error=verify_password_error, email_error=email_error)


@app.route("/welcome")
def valid_login():
    title = 'Welcome!'
    username = request.args.get("username")
    return render_template('hello_greeting.html', title=title, username=username)


if __name__ == '__main__':
    app.run()
