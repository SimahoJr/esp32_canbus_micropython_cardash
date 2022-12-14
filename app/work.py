from microdot import Microdot, Response, send_file
from microdot_utemplate import render_template
from can import *
import _thread, time
import ujson

app = Microdot()
Response.default_content_type = 'text/html'

# Not a problem with more memory here
@app.route('/svg/<path:path>')
def svg(request, path):
    def stream():
        # TODO:Come back here for flash size
        chunk_size = 2048
        f = open("static/icons.svg", "r")
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data
            time.sleep(0.5)
    return stream(), 200, {'Content-Type':'image/svg+xml'}

@app.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)

@app.route('/data', methods=['GET', 'POST'])
def data(req):
    ret = {}
    try:
        values = req.json
        for key, val in values.items():
            try:
                _ret = sendAndCheck(key, int(val), True)
                # TODO: str(_ret)
                ret[key] = _ret
            except Exception as e:
                print("data ret", e)
            time.sleep(0.1)
    except Exception as e:
        print("data", e)
    # print(ret)
    return ret


@app.route('/', methods=['GET', 'POST'])
def index(req):
    name = None
    if req.method == 'POST':
        name = req.form.get('name')
    return render_template('index.html')

if __name__ == '__main__':
    print("server is running port 5000")
    app.run(debug=True)
