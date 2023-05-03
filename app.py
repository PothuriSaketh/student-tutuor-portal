from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder='template')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/student_portal', methods=['GET', 'POST'])
def student_portal():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate username and password here
        return redirect(url_for('student_dashboard'))
    return render_template('student_portal.html')
@app.route('/tutor_portal', methods=['GET', 'POST'])
def tutor_portal():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate username and password here
        return redirect(url_for('tutor_dashboard'))
    return render_template('tutor_portal.html')
@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')
@app.route('/tutor_dashboard')
def tutor_dashboard():
    return render_template('tutor_dashboard.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)