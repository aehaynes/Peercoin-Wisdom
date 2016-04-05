from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chart')
def chartpage():
    pair = ""
    return render_template('chart.html',pair=pair)

@app.route('/Discussion')
def chartpage():
    pair = ""
    return render_template('discussion.html',pair=pair)

@app.route('/PeerReview')
def chartpage():
    pair = ""
    return render_template('peerreview.html',pair=pair)

@app.route('/Resources')
def chartpage():
    pair = ""
    return render_template('resources.html',pair=pair)

@app.route('/Explorer')
def chartpage():
    pair = ""
    return render_template('explorer.html',pair=pair)

@app.route('/Assets')
def chartpage():
    pair = ""
    return render_template('assets.html',pair=pair)





@app.route('/signup', methods=['POST'])
def signup():
    session['username'] = request.form['username']
    session['message'] = request.form['message']
    return redirect(url_for('message'))

@app.route('/message')
def message():
    if not 'username' in session:
        return abort(403)
    return render_template('message.html', username=session['username'], 
                                           message=session['message'])

if __name__ == '__main__':
    app.run()
