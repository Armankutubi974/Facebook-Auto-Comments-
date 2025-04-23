from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_TOKEN = 'YOUR_PAGE_ACCESS_TOKEN'

@app.route('/comment', methods=['POST'])
def comment():
    data = request.json
    post_id = data.get('post_id')
    message = data.get('message')

    if not post_id or not message:
        return jsonify({"error": "post_id and message are required"}), 400

    url = f'https://graph.facebook.com/{post_id}/comments'
    payload = {
        'message': message,
        'access_token': ACCESS_TOKEN
    }

    response = requests.post(url, data=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
