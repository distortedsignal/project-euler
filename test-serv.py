from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello, World!"

@app.route('/problem001/')
def problem1():
	from problem001.problem import simpleSolution as s
	return str(s())

@app.route('/problem002/')
def problem2():
	from problem002.problem import simpleSolution as s
	return str(s())

@app.route('/problem003/')
def problem3():
	from problem003.problem import nuancedSolution as s
	return str(s())

@app.route('/problem054/')
def problem54():
	from problem054.problem import simpleSolution as s
	return str(s())

@app.route('/problem058/')
def problem58():
	from problem058.problem import simpleSolution as s
	return str(s())

@app.route('/problem059/')
def problem59():
	from problem059.problem import simpleSolution as s
	return str(s())

@app.route('/problem076/')
def problem76():
	from problem076.problem import simpleSolution as s
	return str(s())

@app.route('/problem079/')
def problem79():
	from problem079.problem import simpleSolution as s
	return str(s())

@app.route('/problem082/')
def problem82():
	from problem082.problem import simpleSolution as s
	return str(s())

@app.route('/problem083/')
def problem83():
	from problem083.problem import simpleSolution as s
	return str(s())

@app.route('/problem102/')
def problem102():
	from problem102.problem import simpleSolution as s
	return str(s())

if __name__ == "__main__":
	app.run()