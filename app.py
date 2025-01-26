from flask import Flask, render_template
import requests,random 


app = Flask(__name__)

@app.route('/')
def index():
    #get meme from api
    response = requests.get('https://api.imgflip.com/get_memes').json()
    if response['success']:
        random_number = random.randint(0, 100)
        memes = response['data']['memes']
        meme = memes[random_number]  
        response = {'url': meme['url'], 'name': meme['name']}
    else:
        response = {'url': '', 'name': 'No meme found'}
    return render_template('index.html', response=response,meme=meme)

app.run(debug=True,host="0.0.0.0",port="80")