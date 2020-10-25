from flask import request, redirect, flash, render_template, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.users.models import userInfo
from app.users.forms import loginForm, registerForm
from app.users import users
from app import dbase

#   Login/Register System   # 
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()

    if form.validate_on_submit():
        hashedPassword = generate_password_hash(form.password.data, method='sha256')
        username = form.username.data
        email = form.username.data
        password = hashedPassword

        newRegister = userInfo(username = username, password = password, email = email)
        dbase.session.add(newRegister)
        dbase.session.commit()
        flash("Registration Successful!")
        return redirect(url_for('users.login'))
    return render_template('registration.html', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()

    if request.method == 'POST':
        if form.validate_on_submit:
            user = userInfo.query.filter_by(username = form.username.data).first()

            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)

                    return redirect(url_for('index'))
                else:
                    flash('Invalid credentials, please try again...')
            else:
                return redirect(url_for('index'))
        
    return render_template('login.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))