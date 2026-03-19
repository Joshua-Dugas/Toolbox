from flask import Blueprint, render_template, request, jsonify
import json
from pathlib import Path

budget = Blueprint(
    "budget",
    __name__,
    template_folder="."
)

#TODO:There is some extreme repition in here. Need to figure out how to combine some of these methods

EXP_DATA_FILE = Path("data/expenses.json")
INC_DATA_FILE = Path("data/income.json")

@budget.route("/")
def ui():
    expenses = load_expenses()
    return render_template("budget.html", expenses=expenses)

# If file doesnt exist make it, if file is empty then catch exception
def load_expenses():
    if not EXP_DATA_FILE.exists():
        EXP_DATA_FILE.parent.mkdir(exist_ok=True)
        with open(EXP_DATA_FILE, "w") as f:
            json.dump({}, f)
        return {}

    try:
        with open(EXP_DATA_FILE) as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def load_incomes():
    if not INC_DATA_FILE.exists():
        INC_DATA_FILE.parent.mkdir(exist_ok=True)
        with open(INC_DATA_FILE, "w") as f:
            json.dump({}, f)
        return {}

    try:
        with open(INC_DATA_FILE) as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_expense(data):
    with open(EXP_DATA_FILE, "w") as e:
        json.dump(data, e, indent=2)

def save_income(data):
    with open(INC_DATA_FILE, "w") as i:
        json.dump(data, i, indent=2)

#----------EXPENSES----------
@budget.route("/expenses/getData", methods=["GET"])
def load_expense_data():
    expenses = load_expenses()
    print(expenses)
    return jsonify(expenses)

@budget.route("/expenses/add", methods=["POST"])
def add_expense():
    expenses = load_expenses()

    data = request.json
    name = data["name"]
    amount = float(data["amount"])
    allotment = data["allotment"]
    expenses[name] = {
        "amount": amount,
        "allotment": allotment
        }

    total = 0;

    for i in expenses.values():
        total += float(i["amount"])
    

    save_expense(expenses)
    print(expenses)

    return jsonify({
        "name": name,
        "amount": amount,
        "allotment": allotment,
        "total": total
    })

@budget.route("/expenses/delete", methods=["DELETE"])
def delete_expense():
    expenses = load_expenses()

    data = request.json
    name = data["name"]
    
    total = 0;
    for i in expenses.values():
        total += float(i["amount"])

    expenses.pop(name)

    save_expense(expenses)

    print(f"Deleting expense of name {name}")
    print(f"Total expenses: {expenses}")
    
    return jsonify({
        "name": name,
        "total": total
    })

#------------INCOME--------------
@budget.route("/income/getData")
def load_income_data():
    incomes = load_incomes()
    return jsonify(incomes)

@budget.route("/income/add", methods=["POST"])
def add_income():
    incomes = load_incomes()
    data = request.json
    name = data["name"]
    amount = float(data["amount"])
    incomes[name] = amount 

    save_income(incomes)
    
    return jsonify({
        "name": name,
        "amount": amount,
        "total": sum(incomes.values())
    })

@budget.route("/income/delete", methods=["DELETE"])
def delete_income():
    incomes = load_incomes()

    data = request.json
    name = data["name"]

    incomes.pop(name)

    save_income(incomes)


    return jsonify({
        "name": name,
        "total": sum(incomes.values())
    })



    

