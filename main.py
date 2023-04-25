# # imported Flask class from flask module
# from flask import Flask

# # create an instance of the Flask class
# app = Flask(__name__)

# def make_bold(function):
#     def wrapper():
#         return f"<b>{function()}</b>"
#     return wrapper

# def make_emphasis(function):
#     def wrapper():
#         return f"<em>{function()}</em>"
#     return wrapper

# def make_underlined(function):
#     def wrapper():
#         return f"<u>{function()}</u>"
#     return wrapper

# # use the route() decorator to tell Flask what URL should trigger our function
# @app.route("/")
# @make_bold
# @make_emphasis
# @make_underlined
# def hello_world():
#     return "<h1>Hello, World!</h1>"

# # use the route() decorator to tell Flask what URL should trigger our function
# @app.route("/<name>")
# def greet(name):
#     return f"<h1>Hello {name}!</h1>"

# # check if the executed file is the main program and run the app
# if __name__ == "__main__":
#     app.run(debug=True)

