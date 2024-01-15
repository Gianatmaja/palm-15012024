import google.generativeai as palm

from flask import Flask, request, render_template

model = { 'model': "models/chat-bison-001"}

palm.configure(api_key="AIzaSyA8A3S6pdcdEl0I0LqZ2feDyXMnN1DXRrs")

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        return(render_template("index.html", result = palm.chat(**model, messages = q).last))
    else:
        return(render_template("index.html", result = "Waiting for question..."))

if __name__ == "__main__":
    app.run()