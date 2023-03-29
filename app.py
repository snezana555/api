from flask import Flask, request

app = Flask(__name__)


@app.route('/sum/', methods=['POST'])
def hello_world():
    print(request.json)
    a = request.json['a']
    b = request.json['b']
    return {'sum': a + b}

@app.route('/sum2/', methods=['POST'])
def hello():
    print(request.json)
    a = request.json['data']
    return {'sum': sum(a)}


@app.route('/sum3/', methods=['POST'])
def hi():
    print(request.json)
    a = request.json.get('a')
    b = request.json.get('b')
    c = request.json.get('c')
    d = request.json.get('d')
    sum = 0
    if a:
        sum += a
    if b:
        sum += b
    if c:
        sum += c
    if d:
        sum += d
    return {'sum': sum}


@app.route('/nextround/', methods=['POST'])
def nextround():
    n = request.json['n']
    k = request.json['k']
    data = request.json['data']
    res = 0

    for i in data:
        if i >= data[k-1] and i > 0:
            res += 1
    print(res)
    return {'res': res}



@app.route('/lexographically/', methods=['POST'])
def lexographically():
    a = request.json['a']
    b = request.json['b']
    if a.lower() == b.lower():
        return {'res': 0}
    if a.lower() > b.lower():
        return {'res': 1}
    if a.lower() < b.lower():
        return {'res': -1}


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host='0.0.0.0', port=5000)