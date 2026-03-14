from flask import Blueprint, render_template, request, jsonify

budget = Blueprint(
    "budget",
    __name__,
    template_folder="."
)



#This is just some crappy starter code for a placeholder. Eventually this will be more robust and will have save functionality
expenses = {}


@budget.route("/")
def ui():
    return render_template("template.html", expenses=expenses)


@budget.route("/add", methods=["POST"])
def add():
    data = request.json
    name = data["name"]
    amount = float(data["amount"])
    
    expenses[name] = amount

    print(f"adding expense: {name} with the amount of {amount}")
    print(f"Total expenses: {expenses}")
    return jsonify({
        "name": name,
        "amount": amount,
        "total": get_total()
    })

@budget.route("/delete", methods=["DELETE"])
def delete():
    data = request.json
    name = data["name"]
    amount = float(data["amount"])

    expenses.pop(data["name"])

    print(f"Deleting expense of name {data["name"]}")
    print(f"Total expenses: {expenses}")
    return jsonify({
        "name": name,
        "amount": amount,
        "total": get_total()
    })

def get_total():
    return sum(expenses.values())

    

