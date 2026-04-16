from flask import Blueprint, render_template, request, redirect, session

def create_routes(auth_service):

    routes = Blueprint('routes', __name__)

    @routes.route('/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = auth_service.login(
                request.form['username'],
                request.form['password']
            )

            if user:
                session['user'] = user.username
                session['role'] = user.role

                if user.role == 'admin':
                    return redirect('/admin')
                elif user.role == 'usuario':
                    return redirect('/user')
                else:
                    return redirect('/guest')

            return "Credenciales incorrectas"

        return render_template('login.html')

    @routes.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            auth_service.register(
                request.form['username'],
                request.form['password'],
                request.form['role']
            )
            return redirect('/')

        return render_template('register.html')

    @routes.route('/admin')
    def admin():
        if 'user' not in session or session['role'] != 'admin':
            return redirect('/')
        return render_template('admin.html')

    @routes.route('/user')
    def user():
        if 'user' not in session or session['role'] != 'usuario':
            return redirect('/')
        return render_template('user.html')

    @routes.route('/guest')
    def guest():
        if 'user' not in session:
            return redirect('/')
        return render_template('guest.html')

    @routes.route('/logout')
    def logout():
        session.clear()
        return redirect('/')

    return routes
