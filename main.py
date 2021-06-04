import flask
import codeforces_problem_wrapper

PROBLEM_LINK = 'https://codeforces.com/problemset/problem/'
CONTEST_LINK = 'https://codeforces.com/contest/'

app = flask.Flask(__name__)

@app.route("/",methods=['GET'])
def contest_data():
    problem_id = flask.request.args['id']
    return flask.jsonify(codeforces_problem_wrapper.parse_problem(PROBLEM_LINK + problem_id))
	
@app.route("/contest",methods=['GET'])
def contest():
	contest_id = flask.request.args['id']
	return flask.jsonify(codeforces_problem_wrapper.parse_contest(CONTEST_LINK + contest_id))
	