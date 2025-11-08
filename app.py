from flask import Flask, request, render_template, make_response, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

# Employee database with different passwords
EMPLOYEES = {
    "1": {"name": "John Smith", "role": "Intern", "salary": "30,000", "clearance": "low", "password": "welcome123"},
    "2": {"name": "Sarah Johnson", "role": "Developer", "salary": "75,000", "clearance": "medium", "password": "devpass456"},
    "3": {"name": "Mike Chen", "role": "Manager", "salary": "120,000", "clearance": "high", "password": "mgmt789"},
    "4": {"name": "Tony Stark", "role": "CEO", "salary": "500,000,000", "clearance": "maximum", "password": "ceo_topsecret", "flag": "npflag{1d0r_4cc3ss_v10l4t10n_ftw}"},
    "5": {"name": "Pepper Potts", "role": "COO", "salary": "250,000", "clearance": "maximum", "password": "coo_secure"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    
    # Check if employee exists
    if username in EMPLOYEES:
        # Verify password for the specific employee
        if password == EMPLOYEES[username]['password']:
            resp = make_response(redirect(f'/employee/{username}'))
            resp.set_cookie('user_id', username)
            return resp
        else:
            # Password mismatch error
            return render_template('login_error.html', username=username), 401
    
    # Employee ID not found
    return render_template('employee_not_found.html', username=username), 404

@app.route('/employee/<employee_id>')
def employee_profile(employee_id):
    # IDOR VULNERABILITY: No authorization check!
    # Users can access any employee profile by changing the ID in URL
    employee = EMPLOYEES.get(employee_id)
    
    if not employee:
        return "Employee not found", 404
    
    return render_template('employee_profile.html', employee=employee)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)