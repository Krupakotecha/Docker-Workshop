from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def input_page() :
	return render_template('input_page.html')

@app.route('/result', methods = ['POST', 'GET'])
def result() :
	if request.method == 'POST' :
		string = request.form['input_string']
		file_name = 'output/' + 'strings' + '.txt'
		f = open(file_name, "a")
		f.write(string + "\n")
		f.close()
		return render_template('result.html', input_string = string)

if __name__ == '__main__' :
	app.run(debug = True, host = '0.0.0.0')
