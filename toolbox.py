from flask import Flask, render_template 
from tools.budget.routes import budget
from tools.memoryVerse.routes import memoryVerse

app = Flask(__name__)

@app.route("/")
def dashboard():
    print("Toolbox Initializing \n Welcome to the dashboard!")
    return render_template("dashboard.html")

#register blueprints here
app.register_blueprint(budget, url_prefix="/tool/budget")

app.register_blueprint(memoryVerse, url_prefix="/tool/memoryVerse")

#Maybe change this port in future
if __name__ == "__main__":
    app.run(port=5002)
    

