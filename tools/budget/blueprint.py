from flask import Blueprint, render_template, request

budget = Blueprint(
    "budget",
    __name__,
    template_folder="."
)



#This is just some crappy starter code for a placeholder. Eventually this will be more robust and will have save functionality
expenses = []


@budget.route("/")
def ui():
    return render_template("template.html", expenses=expenses)


@budget.route("/add", methods=["POST"])
def add():

    name = request.form["Expense Name"]
    amount = request.form["Expense Amount"]

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

    return f"""
    <tr>
        <td>{name}</td>
        <td>${amount}</td>
    </tr>
    """

