from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

#register blueprints here
from tools.budget.blueprint import budget
app.register_blueprint(budget, url_prefix="/tool/budget")

#Maybe change this port in future
if __name__ == "__main__":
    app.run(port=58080)
    

