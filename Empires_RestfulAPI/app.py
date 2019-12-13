import json
from flask import Flask, jsonify, render_template, request, Response


app = Flask(__name__)


with open('Empires.JSON') as json_data:
    d = json.load(json_data)
    list_of_empires = []
    for data in d['empires']:
    	list_of_empires.append(data)

with open('Army.JSON') as army_data:
	a = json.load(army_data)
	list_of_armies = []
	for army in a['armies']:
		list_of_armies.append(army)
	print("list_of_armies: ", list_of_armies)

@app.route('/', methods =['GET'])
def home():
	return render_template("index.html")

@app.route('/empires', methods =['GET'])
def all_empires():
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(d)
	return render_template("index.html",list_data=list_of_empires)

@app.route('/empires/<string:empire_id>', methods =['GET'])
def empire_by_id(empire_id):
	emp = [empires for empires in list_of_empires if empires['empireid'] == empire_id]
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(emp)
	return render_template("index.html",list_data=emp)

@app.route('/empires/<string:empire_id>/army', methods =['GET'])
def army_by_empire_id(empire_id):
	empire_army = [armies for armies in list_of_armies if armies['empireid'] == empire_id]
	# print("empire_army: ", str(empire_army))
	army = empire_army[0]['army']
	# print("empire_army: ", str(army))
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(empire_army)
	return render_template("index.html", list_army_data=army, empire_id=empire_id)

@app.route('/empires/<string:empire_id>/army/<string:army_id>', methods =['GET'])
def army_by_empire_id_army_id(empire_id, army_id):
	empire_army = [armies for armies in list_of_armies if armies['empireid'] == empire_id]
	# print("empire_army: ", str(empire_army))
	# print("empire_army[0]: ", str(empire_army[0]))
	# print("army: ", str(empire_army[0]['army']))
	arm = [army for army in empire_army[0]['army'] if army['armyid'] == army_id]
	print("single arm: ", arm)
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(arm)
	return render_template("index.html", list_army_data=arm, empire_id=empire_id)

if __name__ == '__main__':
	 app.run(host='localhost', port=5000)