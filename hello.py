import MySQLdb
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello():
	db = MySQLdb.connect(host="10.19.251.50",    # your host, usually localhost
                     user="root",         # your username
                     passwd="sxcloud",  # your password
                     db="test")        # name of the data base

	cur = db.cursor()
	cur.execute("SELECT * FROM heat_map limit 10")
	#entries = [dict(longitude=row[0], latitude=row[1],count=int(row[2]) for row in cur.fetchall()]
	return render_template('hello.html', entries=cur.fetchall())

@app.route('/heatmap')
def heatmap():
	db = MySQLdb.connect(host="10.19.251.50",    # your host, usually localhost
                     user="root",         # your username
                     passwd="sxcloud",  # your password
                     db="test")        # name of the data base

	cur = db.cursor()
	cur.execute("SELECT * FROM heat_map limit 10")
	return render_template('heatmap.html',entries=cur.fetchall())

if __name__ == '__main__':
    app.run(debug=True)