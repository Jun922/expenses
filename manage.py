from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    content = ["hoge", "fuga", "fuge"]
    return render_template("index.html", name=name, content=content)


@app.route("/index", methods=["post"])
def post():
    content = ["hoge", "fuga", "fuge"]
    name = request.form["name"]
    content.append(name)
    return render_template("index.html", name=name, content=content)


if __name__ == "__main__":
    app.run(debug=True)