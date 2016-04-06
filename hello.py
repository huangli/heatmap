import MySQLdb
import json
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
	return render_template('hello.html', entries=json.dumps(cur.fetchall()))

# static heat map
@app.route('/heatmap')
def heatmap():
	db = MySQLdb.connect(host="10.19.251.50",    # your host, usually localhost
                     user="root",         # your username
                     passwd="sxcloud",  # your password
                     db="test")        # name of the data base

	cur = db.cursor()
	cur.execute("SELECT * FROM heat_map ")
	points = json.dumps(cur.fetchall())
	cur.close()
	db.close
	return render_template('heatmap.html',entries=points)

# test animation 
@app.route('/animation')
def animation():
	db = MySQLdb.connect(host="10.19.251.50",    # your host, usually localhost
                     user="root",         # your username
                     passwd="sxcloud",  # your password
                     db="test")        # name of the data base

	cur = db.cursor()
	cur.execute("SELECT * FROM heat_map ")
	points = json.dumps(cur.fetchall())
	cur.close()
	db.close
	return render_template('animation.html',entries=points)

# convert wgs84 to baidu longtitude,latitude	
@app.route('/convert')
def convert():
	db = MySQLdb.connect(host="10.19.251.50",    # your host, usually localhost
                     user="root",         # your username
                     passwd="sxcloud",  # your password
                     db="test")        # name of the data base

	cur = db.cursor()
	cur.execute("SELECT * FROM heat_map_201603 limit 10")
	entries = json.dumps(cur.fetchall())
	# cur.close()
	# db.close
	return render_template('convert.html',entries=entries)

# insert data into database
@app.route('/insert', methods=['GET', 'POST'])
def insert():
	db = MySQLdb.connect(host="10.19.251.50",    # your host, usually localhost
                     user="root",         # your username
                     passwd="sxcloud",  # your password
                     db="test")        # name of the data base
	cur = db.cursor()
	# write data
	points = request.get_json()
	try:
		for i in range(10):
			sql = "insert into baidu_location(longitude, latitude, baidu_longitude,baidu_latitude) \
					values('%f','%f','%f','%f')" % \
					(points[i]["lng"], points[i]["lat"], points[i]["b_lng"],points[i]["b_lat"])  
			cur.execute(sql)   
			db.commit()
	except Exception, e:
		raise e
	cur.close()
	db.close()
	return render_template('message.html',entries=points)

# arcgis testing
@app.route('/arcgis')
def arcgis():
	return render_template('arcgis.html')

@app.route('/layer')
def layer():
	return render_template('layer.html')

if __name__ == '__main__':
    app.run(debug=True)