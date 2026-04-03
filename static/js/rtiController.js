async function initializeGame() {
  const response = await fetch("/tool/rti/loadScreen");
  const data = await response.json();
  const ac = document.getElementById("ascii-container");
  const mc = document.getElementById("menu-container")
  ac.innerHTML = `
    ${data.screen}
  `;

  mc.innerHTML = "";

  data.actions.forEach(action => {

    const li = document.createElement("li");

    li.textContent = action;

    mc.appendChild(li);

  });
}

async function createGame(saveName, gameData) {
  const response = await fetch("/tool/rti/createGame", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ save_name: saveName, game_data: gameData })
  });

  const data = await response.json();
  console.log("CreateGame response:", data);
}

async function saveGame(saveName, gameData) {
  const response = await fetch("/tool/rti/saveGame", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ save_name: saveName, game_data: gameData })
  });

  const data = await response.json();
  console.log("SaveGame response:", data);
}

async function loadGame(saveName) {
  const response = await fetch(`/tool/rti/loadGame/${saveName}`);
  const data = await response.json();

  if (data.status === "success") {
    console.log("Loaded game data:", data.game_data);
    return data.game_data;
  } else {
    console.warn(data.message);
    return null;
  }
}
