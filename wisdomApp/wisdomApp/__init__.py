from flask import Flask, render_template, url_for, redirect, abort,request,session
from subprocess import PIPE,Popen
from block_frame import blkCount, getBlock, getDifficulty, showChain, to_html
import pandas
import subprocess

ppcoind_path = "/home/peer/ppcoin/src/ppcoind"


app = Flask(__name__)
<<<<<<< HEAD
app.config['SECRET_KEY'] = '71472D2BB01783E5C6D65667E7F0B066AC7D343CF6129432169E3B99E6307SAE';


=======
app.config['SECRET_KEY'] = '';
>>>>>>> d164116109e49269809131e3507278a9f2bffd13

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/chart/<exchange>/<pair>')
def chartpage(exchange,pair):
    return render_template("chart.html",exchange=exchange,pair=pair)

@app.route('/Journal')
def journal():
    user= ""
    return render_template('journal.html',user=user)

@app.route('/PeerReview')
def peerreview():
    pair = ""
    return render_template('peerreview.html',pair=pair)

@app.route('/Resources')
def resources():
    pair = ""
    return render_template('resources.html',pair=pair)

@app.route('/Explorer/')
def explorer():
    return render_template('explorer.html')

@app.route('/PSA')
def assets():
    pair = ""
    return render_template('PSA.html',pair=pair)

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
