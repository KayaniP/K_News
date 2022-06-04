import random
from flask import Flask, render_template
from data import states

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    newsTop=[]
    for state in states:
        for news in state.get_news():
            if news.get_top():
                newsTop.append(news)
    return render_template('card.html', states=states, newsTop=newsTop)

@app.route('/info/<int:info_id>', methods=['GET'])
def info(info_id):
     noticeState = []
     for state in states:
        for news in state.get_news():
            if news.get_id() == info_id:
                return render_template('info.html', notice=news)


     for state in states:
        for news in state.get_news():
            for notice in news:
                if notice.get_id() == info_id:
                    return render_template('info.html', notice=notice)
            
@app.route('/state/<int:state_id>', methods=['GET'])
def state(state_id):
    noticeState = []
    for state in states:
        for news in state.get_news():
            if news.get_id() == state_id:
                noticeState.append(news)
    return render_template('card.html', statesOne=noticeState, states = states )