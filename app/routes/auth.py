from flask import Blueprint, request ,session, redirect, render_template, url_for, flash

auth_bp = Blueprint('auth' , __name__)

USER_CRIDINTAILS = {
    "username" : "Gaurav",
    "password" : "1234"
}

@auth_bp.route('/login', methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')      
        password = request.form.get('password')
        
        if  username == USER_CRIDINTAILS['username']  and password == USER_CRIDINTAILS['password'] :
            session['user'] = username
            flash('Login Successful', 'success')
            return redirect(url_for("tasks.view_tasks"))  # ✅ This is critical!
        else:
            flash('Invalid username or password', 'danger')
                
    return render_template('login.html')    

@auth_bp.route('/logout')
def logout():
    session.pop("user", None)
    flash('Logout successful','info')
    return redirect(url_for("auth.login")) 