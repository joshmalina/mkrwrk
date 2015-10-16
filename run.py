# import forecast
# import rforest
from flask import Flask, json
from decorators import crossdomain
app = Flask(__name__)


# @app.route('/forecast')
# @crossdomain(origin='http://localhost:9000')
# def index():	
# 	forest = rforest.forest(train=False)
# 	frcast = forecast.forecast(forest.X_train.columns, forest.rf)
# 	#return flask.json.jsonify({'predictions':frcast.df})
# 	return json.jsonify(frcast.df)

@app.route('/')
def f():
	return 'cats'

if __name__ == '__main__':
	app.run(debug=True)
