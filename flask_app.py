from flask import Flask, render_template, request
from account_data import main_account_info, find_coordinates, build_map

app = Flask(__name__, template_folder='/home/damoklov/mysite')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/find_account", methods=["POST"])
def find_account():
	acct = request.form.get("account")
	if not acct:
		return render_template("failed.html")
	else:
		f = open('account.txt', 'w', encoding='utf-8', errors='ignore')
		f.write(acct)
		f.close()
		name_location_icon_set = main_account_info()
		name_coordinates_icon_set = find_coordinates(name_location_icon_set)
		build_map(name_coordinates_icon_set)
		return render_template("map.html")


@app.errorhandler(500)
def page_not_found(e):
    return render_template('failed.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('failed.html'), 404

@app.errorhandler(401)
def page_not_found(e):
    return render_template('failed.html'), 401

