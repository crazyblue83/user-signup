from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/validate-signup", methods=["POST"])
def validate_signup():
    return render_template('signup_form.html')    

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    
    if not username:
        username_error = "That's not a valid username."
    
    if len(username) <= 3 or len(username) > 20:
        username_error = "That's not a valid username"
        username = ''
    else:
        username = str(username)
        if " " in username:
            username_error = "That's not a valid username"
            username = ''

    if not password:
        password_error = "That's not a valid password"

    if len(password) <= 3 or len(password) > 20:
        password_error = "That's not a valid password"
        password = ''
    else:
        password = str(password)
        if " " in password:
            password_error = "That's not a valid password"
            password = ''
    if not verify:
        verify_error = "Passwords do not match."
    else:
        if str(password) != str(verify):
            verify_error = "Passwords do not match."
    
    if len(email) <= 3 or len(email) > 20:
        email_error = "That's not a valid email address."
        email = ''
    else:
        email = str(email)
        if "@" or "." not in email:
            email_error = "That's not a vaild email address."
        if " " in email:
            email_error = "That's not a valid email address."
            email = ''
    if not (username_error) and not (password_error) and not (verify_error) and not (email_error):
        username = str(username)
        return render_template('hello_greeting.html', name=username)
        
    else:
        return render_template('signup_form.html',
            username_error=username_error,
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error,
            email=email,
            username=username)

#@app.route('/valid-signup')
#def valid_signup():
#    username = request.args.get('username')
#    return '<h1>Welcome, {0}.</h1>'.format(username)

app.run()
