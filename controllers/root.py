# from flask import render_template
from main import app
from core import view


@app.route("/")
def home():
    return view()


@app.route('/hello/')
def hello():
    #return jinja2_env.get_template(view_path).render(model)
    # import pdb
    # pdb.set_trace()
    # module_name = caller.f_globals['__name__']      # returns 'modules.default_routes'
    # package_name = caller.f_globals['__package__']  # returns 'modules'
    # return view()
    return view()


# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)