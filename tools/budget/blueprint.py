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

    
    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)


    total = sum(e["amount"] for e in expenses)
    
    #hx-swap-oob replaces the value of whatever you pass in as the id 
    #So in our case we replace the total field everytime we add expenses with the new total 
    return f"""
    <tr>
    <td>{name}</td>
    <td>${amount}</td>
    </tr>
    <td id="total-amount" hx-swap-oob="true">${total}</td> 
    """


