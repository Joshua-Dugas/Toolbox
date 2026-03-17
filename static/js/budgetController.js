//TODO:Extreme repetition, need to find way to combine method
async function init(){
  await loadExpenses();
  await loadIncomes();
  populateBreakdownTable();
}

async function populateBreakdownTable(){

  let expenseTotal = parseFloat(
    document.getElementById("expense-total-amount").innerText.replace("$", "")
  );

  let incomeTotal = parseFloat(
    document.getElementById("income-total-amount").innerText.replace("$", "")
  );

  let netTotal = incomeTotal - expenseTotal;

  document.getElementById("bd-income-total-amount").innerText = `$${incomeTotal.toFixed(2)}`;
  document.getElementById("bd-expense-toal-amount").innerText = `$${expenseTotal.toFixed(2)}`;
  document.getElementById("net-amount").innerText = `$${netTotal.toFixed(2)}`;
}

async function loadExpenses() {
    const response = await fetch("/tool/budget/expenses/getData");
    const expenses = await response.json();

    const table = document.getElementById("expense-list");
    const totalRow = document.getElementById("expense-total-row");

    let total = 0;

    for (const [name, amount] of Object.entries(expenses)) {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${name}</td>
            <td>$${Number(amount).toFixed(2)}</td>
        `;

        row.addEventListener("click", selectRow);

        table.insertBefore(row, totalRow);

        total += Number(amount);
    }
    //loads value for breakdown talbe 
    document.getElementById("expense-total-amount").innerText =
        `$${total.toFixed(2)}`;
}

async function loadIncomes() {
    const response = await fetch("/tool/budget/income/getData");
    const incomes = await response.json();

    const table = document.getElementById("income-list");
    const totalRow = document.getElementById("income-total-row");

    let total = 0;

    for (const [name, amount] of Object.entries(incomes)) {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${name}</td>
            <td>$${Number(amount).toFixed(2)}</td>
        `;

        row.addEventListener("click", selectRow);

        table.insertBefore(row, totalRow);

        total += Number(amount);
    }

    document.getElementById("income-total-amount").innerText =
        `$${total.toFixed(2)}`;
}

async function addIncome(){
   const name = document.getElementById("income-name").value.trim();
   const amount = document.getElementById("income-amount").value;

    if (!name || !amount) {
        alert("Please enter both a name and amount.");
        return;
    }

    // Prevent duplicates already in the table
    const rows = document.querySelectorAll("#income-list tr");

    for (const row of rows) {
        if (row.id === "income-total-row") continue;

        const existingName = row.children[0].innerText.trim();

        if (existingName.toLowerCase() === name.toLowerCase()) {
            alert(`Expense "${name}" already exists!`);
            return;
        }
    }

    const response = await fetch("/tool/budget/income/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            amount: amount
        })
    });

    const data = await response.json();

    const table = document.getElementById("income-list");
    const totalRow = document.getElementById("income-total-row");

    const row = document.createElement("tr");

    row.innerHTML = `
        <td>${data.name}</td>
        <td>$${Number(data.amount).toFixed(2)}</td>
    `;

    row.addEventListener("click", selectRow);

    table.insertBefore(row, totalRow);

    document.getElementById("income-total-amount").innerText =
        `$${Number(data.total).toFixed(2)}`;

    // Clear inputs
    document.getElementById("income-name").value = "";
    document.getElementById("income-amount").value = "";
}


async function addExpense() {
    const name = document.getElementById("name").value.trim();
    const amount = document.getElementById("amount").value;

    if (!name || !amount) {
        alert("Please enter both a name and amount.");
        return;
    }

    // Prevent duplicates already in the table
    const rows = document.querySelectorAll("#expense-list tr");

    for (const row of rows) {
        if (row.id === "total-row") continue;

        const existingName = row.children[0].innerText.trim();

        if (existingName.toLowerCase() === name.toLowerCase()) {
            alert(`Expense "${name}" already exists!`);
            return;
        }
    }

    const response = await fetch("/tool/budget/expenses/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            amount: amount
        })
    });

    const data = await response.json();

    const table = document.getElementById("expense-list");
    const totalRow = document.getElementById("total-row");

    const row = document.createElement("tr");

    row.innerHTML = `
        <td>${data.name}</td>
        <td>$${Number(data.amount).toFixed(2)}</td>
    `;

    row.addEventListener("click", selectRow);

    table.insertBefore(row);

    document.getElementById("total-amount").innerText =
        `$${Number(data.total).toFixed(2)}`;

    // Clear inputs
    document.getElementById("name").value = "";
    document.getElementById("amount").value = "";
}

function selectRow(event) {
    const rows = document.querySelectorAll("#expense-list tr");
    rows.forEach(r => r.classList.remove("selected"));

    const row = event.currentTarget;
    if (row.id !== "total-row") {
        row.classList.add("selected");
    }
}

async function deleteExpense() {
    const selected = document.querySelector("#expense-list .selected");
    if (!selected) return alert("Select a row first");
    
    const name = selected.children[0].innerText;
    const amount = selected.children[1].innerText.replace("$", "");

    const response = await fetch("/tool/budget/expenses/delete", {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, amount })
    });
    
    const data = await response.json();
    console.log(data);
    document.getElementById("total-amount").innerText = `$${data.total}`;
    
    if (response.ok) {
        selected.remove();
    }
}

async function deleteIncome(){
    const selected = document.querySelector("#income-list .selected");
    if (!selected) return alert("Select a row first");
    
    const name = selected.children[0].innerText;
    const amount = selected.children[1].innerText.replace("$", "");

    const response = await fetch("/tool/budget/income/delete", {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, amount })
    });
    
    const data = await response.json();
    console.log(data);
    document.getElementById("income-total-amount").innerText = `$${data.total}`;
    
    if (response.ok) {
        selected.remove();
    }
}

init()

