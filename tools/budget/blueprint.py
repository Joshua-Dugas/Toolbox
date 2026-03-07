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

    name = request.form["name"]
    amount = float(request.form["amount"])

    expenses.append({
        "name": name,
        "amount": amount
    })

    total = sum(e["amount"] for e in expenses)

    rows = "".join(
        f"<li>{e['name']} - ${e['amount']}</li>"
        for e in expenses
    )

    return f"""
    <ul>{rows}</ul>
    <strong>Total: ${total}</strong>
    """

