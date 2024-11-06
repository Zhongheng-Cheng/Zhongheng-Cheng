from flask import Flask, Response
import requests

app = Flask(__name__)

def getBadge():
    url_answer_book = 'https://answerbook.david888.com/?lang=en'
    response = requests.get(url_answer_book)
    data = response.json()
    answer_raw = data['answer']
    answer = answer_raw.replace("_", "__").replace("-", "--").replace(" ", "_")
    
    url_badge = f'https://img.shields.io/badge/Book_of_Answers-{answer}-blue'
    
    badge_response = requests.get(url_badge)
    svg_text = badge_response.text

    response = Response(svg_text, mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response


@app.route('/')
def serve_html():
    return getBadge()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)

