from microdot import Microdot, Response, send_file
from microdot_utemplate import render_template
from can import *
import _thread, time

app = Microdot()
Response.default_content_type = 'text/html'

can_values = {}

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
    if req.method == 'POST':
        values = req.args.to_dict()
        sendAndCheck(can, values, 0x102, True)
    return can_values


@app.route('/', methods=['GET', 'POST'])
def index(req):
    name = None
    if req.method == 'POST':
        name = req.form.get('name')
    return render_template('index.html')

def get_values():
    while True:
        time.sleep(1)
_thread.start_new_thread(get_values, ())

if __name__ == '__main__':
    print("server is running port 5000")
    app.run(debug=True)
