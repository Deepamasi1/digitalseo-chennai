from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Webhooks with Python'

@app.route('/my_webhook', methods=['POST'])
def return_response():
    print(request.json);
    return Response(status=200)

@app.route('/githubIssue',methods=['POST'])
def githubIssue():
    data = request.json
    print(f'Issue {data["issue"]["title"]} {data["action"]}')
    print(f'{data["issue"]["body"]}')
    print(f'{data["issue"]["url"]}')
    return data

if __name__ == "__main__": app.run()
