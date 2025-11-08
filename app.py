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
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Stark Industries - Secure Portal</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&display=swap');
            
            body { 
                background: linear-gradient(135deg, #0a0a2a, #1a1a4a, #2a2a6a);
                color: #00f0ff; 
                font-family: 'Orbitron', sans-serif;
                margin: 0;
                padding: 0;
                min-height: 100vh;
                overflow-x: hidden;
            }
            
            .glow-container {
                position: relative;
                max-width: 900px;
                margin: 50px auto;
                background: rgba(10, 15, 30, 0.95);
                padding: 40px;
                border-radius: 20px;
                border: 1px solid #00f0ff;
                box-shadow: 0 0 50px rgba(0, 240, 255, 0.3),
                            inset 0 0 30px rgba(0, 240, 255, 0.1);
                backdrop-filter: blur(10px);
            }
            
            .stark-header {
                text-align: center;
                margin-bottom: 40px;
                position: relative;
            }
            
            .stark-header h1 {
                font-size: 3.5em;
                font-weight: 900;
                margin: 0;
                background: linear-gradient(45deg, #00f0ff, #ff0080);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 30px rgba(0, 240, 255, 0.5);
                letter-spacing: 3px;
            }
            
            .stark-header::after {
                content: '';
                position: absolute;
                bottom: -20px;
                left: 25%;
                width: 50%;
                height: 3px;
                background: linear-gradient(90deg, transparent, #00f0ff, #ff0080, transparent);
                border-radius: 2px;
            }
            
            .login-form {
                background: rgba(20, 25, 45, 0.8);
                padding: 30px;
                border-radius: 15px;
                border: 1px solid rgba(0, 240, 255, 0.3);
                margin: 30px 0;
                position: relative;
                overflow: hidden;
            }
            
            .login-form::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(0, 240, 255, 0.1), transparent);
                transition: 0.5s;
            }
            
            .login-form:hover::before {
                left: 100%;
            }
            
            input, button {
                padding: 15px 20px;
                margin: 10px 0;
                border: 1px solid #00f0ff;
                background: rgba(10, 15, 25, 0.8);
                color: #00f0ff;
                border-radius: 8px;
                font-family: 'Orbitron', sans-serif;
                font-size: 14px;
                width: 100%;
                box-sizing: border-box;
                transition: all 0.3s ease;
            }
            
            input:focus {
                outline: none;
                border-color: #ff0080;
                box-shadow: 0 0 20px rgba(255, 0, 128, 0.3);
                background: rgba(20, 10, 25, 0.9);
            }
            
            button {
                background: linear-gradient(45deg, #00f0ff, #0080ff);
                color: #0a0a2a;
                border: none;
                font-weight: 700;
                cursor: pointer;
                text-transform: uppercase;
                letter-spacing: 2px;
                margin-top: 20px;
            }
            
            button:hover {
                background: linear-gradient(45deg, #ff0080, #ff4000);
                box-shadow: 0 0 30px rgba(255, 0, 128, 0.5);
                transform: translateY(-2px);
            }
            
            .hologram-text {
                background: linear-gradient(45deg, #00f0ff, #80ff00, #ff0080);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 500;
            }
            
            .security-level {
                display: inline-block;
                padding: 5px 15px;
                background: rgba(255, 0, 128, 0.2);
                border: 1px solid #ff0080;
                border-radius: 20px;
                font-size: 0.8em;
                margin-left: 10px;
            }
            
            .scanning-line {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 2px;
                background: linear-gradient(90deg, transparent, #00f0ff, transparent);
                animation: scan 3s linear infinite;
            }
            
            .error-message {
                background: rgba(255, 0, 0, 0.2);
                border: 1px solid #ff0000;
                padding: 15px;
                border-radius: 8px;
                margin: 15px 0;
                text-align: center;
            }
            
            @keyframes scan {
                0% { top: 0; }
                50% { top: 100%; }
                100% { top: 0; }
            }
            
            .particles {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: -1;
            }
            
            .particle {
                position: absolute;
                width: 2px;
                height: 2px;
                background: #00f0ff;
                border-radius: 50%;
                animation: float 20s infinite linear;
            }
            
            @keyframes float {
                0% { transform: translateY(100vh) translateX(0); opacity: 0; }
                10% { opacity: 1; }
                90% { opacity: 1; }
                100% { transform: translateY(-100vh) translateX(100px); opacity: 0; }
            }
        </style>
    </head>
    <body>
        <div class="particles" id="particles"></div>
        <div class="glow-container">
            <div class="scanning-line"></div>
            <div class="stark-header">
                <h1>STARK INDUSTRIES</h1>
                <p class="hologram-text">SECURE EMPLOYEE PORTAL v4.0</p>
                <p>Advanced Biometric Authentication System</p>
            </div>
            
            <div class="login-form">
                <h3 class="hologram-text">⟠ EMPLOYEE LOGIN</h3>
                <form action="/login" method="POST">
                    <input type="text" name="username" placeholder="⟸ EMPLOYEE ID" required>
                    <input type="password" name="password" placeholder="⟸ SECURITY PASSPHRASE" required>
                    <button type="submit">⏻ INITIATE AUTHENTICATION</button>
                </form>
                <p style="text-align: center; margin-top: 20px; font-size: 0.9em;">
                    <span class="hologram-text">INTERN ACCESS:</span><br>
                    ID: <strong>1</strong> | PASSPHRASE: <strong>welcome123</strong>
                </p>
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <p style="font-size: 0.8em; opacity: 0.7;">
                    ⚠️ UNAUTHORIZED ACCESS WILL BE LOGGED AND REPORTED<br>
                    🔒 MULTI-LAYER SECURITY PROTOCOL ACTIVE
                </p>
            </div>
        </div>

        <script>
            // Create floating particles
            for (let i = 0; i < 50; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + 'vw';
                particle.style.animationDelay = Math.random() * 20 + 's';
                particle.style.opacity = Math.random() * 0.5;
                document.getElementById('particles').appendChild(particle);
            }
        </script>
    </body>
    </html>
    '''

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
            return '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Authentication Failed</title>
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&display=swap');
                    body { 
                        background: linear-gradient(135deg, #0a0a2a, #1a1a4a, #2a2a6a);
                        color: #00f0ff; 
                        font-family: 'Orbitron', sans-serif;
                        margin: 0;
                        padding: 20px;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        min-height: 100vh;
                    }
                    .error-container {
                        background: rgba(255, 0, 0, 0.1);
                        border: 1px solid #ff0000;
                        padding: 40px;
                        border-radius: 15px;
                        text-align: center;
                        max-width: 500px;
                    }
                </style>
            </head>
            <body>
                <div class="error-container">
                    <h1 style="color: #ff0000;">❌ AUTHENTICATION FAILED</h1>
                    <p>Security passphrase mismatch for Employee ID: {}</p>
                    <p>Access denied. This attempt has been logged.</p>
                    <a href="/" style="color: #00f0ff; text-decoration: none;">← Return to Login</a>
                </div>
            </body>
            </html>
            f''', 401
    
    # Employee ID not found
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Employee Not Found</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&display=swap');
            body { 
                background: linear-gradient(135deg, #0a0a2a, #1a1a4a, #2a2a6a);
                color: #00f0ff; 
                font-family: 'Orbitron', sans-serif;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .error-container {
                background: rgba(255, 100, 0, 0.1);
                border: 1px solid #ff8000;
                padding: 40px;
                border-radius: 15px;
                text-align: center;
                max-width: 500px;
            }
        </style>
    </head>
    <body>
        <div class="error-container">
            <h1 style="color: #ff8000;">🔍 EMPLOYEE NOT FOUND</h1>
            <p>No employee record found for ID: {}</p>
            <p>Please verify your employee identification number.</p>
            <a href="/" style="color: #00f0ff; text-decoration: none;">← Return to Login</a>
        </div>
    </body>
    </html>
    f''', 404

@app.route('/employee/<employee_id>')
def employee_profile(employee_id):
    # IDOR VULNERABILITY: No authorization check!
    # Users can access any employee profile by changing the ID in URL
    employee = EMPLOYEES.get(employee_id)
    
    if not employee:
        return "Employee not found", 404
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Employee Profile - {employee['name']}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&display=swap');
            
            body {{ 
                background: linear-gradient(135deg, #0a0a2a, #1a1a4a, #2a2a6a);
                color: #00f0ff; 
                font-family: 'Orbitron', sans-serif;
                margin: 0;
                padding: 0;
                min-height: 100vh;
            }}
            
            .glow-container {{
                position: relative;
                max-width: 900px;
                margin: 50px auto;
                background: rgba(10, 15, 30, 0.95);
                padding: 40px;
                border-radius: 20px;
                border: 1px solid #00f0ff;
                box-shadow: 0 0 50px rgba(0, 240, 255, 0.3),
                            inset 0 0 30px rgba(0, 240, 255, 0.1);
                backdrop-filter: blur(10px);
            }}
            
            .profile-header {{
                text-align: center;
                margin-bottom: 30px;
                position: relative;
            }}
            
            .profile-header h1 {{
                font-size: 2.5em;
                font-weight: 700;
                margin: 0;
                background: linear-gradient(45deg, #00f0ff, #80ff00);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            
            .data-panel {{
                background: rgba(20, 25, 45, 0.8);
                padding: 25px;
                border-radius: 12px;
                border: 1px solid rgba(0, 240, 255, 0.3);
                margin: 20px 0;
            }}
            
            .flag-panel {{
                background: linear-gradient(45deg, rgba(0, 255, 0, 0.2), rgba(0, 200, 0, 0.3));
                border: 2px solid #00ff00;
                padding: 20px;
                border-radius: 10px;
                margin: 25px 0;
                text-align: center;
            }}
            
            .clearance-badge {{
                display: inline-block;
                padding: 8px 20px;
                background: linear-gradient(45deg, #ff0080, #ff4000);
                color: white;
                border-radius: 20px;
                font-weight: 700;
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <div class="glow-container">
            <div class="profile-header">
                <h1>👤 EMPLOYEE PROFILE</h1>
                <div class="clearance-badge">CLEARANCE: {employee['clearance'].upper()}</div>
            </div>
            
            <div class="data-panel">
                <h3>⟠ PERSONAL DATA</h3>
                <p><strong>NAME:</strong> {employee['name']}</p>
                <p><strong>ROLE:</strong> {employee['role']}</p>
                <p><strong>ANNUAL SALARY:</strong> ${employee['salary']}</p>
                <p><strong>SECURITY LEVEL:</strong> {employee['clearance'].upper()}</p>
            </div>
            
            {'<div class="flag-panel"><h2>🚩 CLASSIFIED DATA ACCESSED</h2><h3>FLAG: ' + employee['flag'] + '</h3></div>' if 'flag' in employee else ''}
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="/" style="color: #00f0ff; text-decoration: none; padding: 10px 20px; border: 1px solid #00f0ff; border-radius: 5px;">⟸ RETURN TO PORTAL</a>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)