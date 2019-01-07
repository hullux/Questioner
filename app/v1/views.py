# @app.route("/",methods=['GET','POST'])
# def index():
# 	return render_template('index.html')

# @app.route("/signup",methods=['GET','POST'])
# def signup():
# 	form = RegistrationForm()
# 	if form.validate_on_submit():
# 		flash("Account successfully created for {}! ".format(form.username.data), "success")
# 		return redirect(url_for('index'))
# 	return render_template('signup.html',form=form)
# @app.route("/login",methods=['GET','POST'])
# def login():
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		flash("login successful, redirecting to home page ...", "success")
# 		return redirect(url_for('index'))
# 	return render_template('login.html',form=form)
# if __name__ == "__main__":
# 	app.run(debug=True)