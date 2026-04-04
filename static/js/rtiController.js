async function initializeGame() {
  gameData = await fetchGameState();
  renderScene(gameData);
}

async function fetchGameState() {
  const response = await fetch("/tool/rti/loadScreen");
  const gameData = await response.json();
  return gameData;
}

async function renderScene(gameData) {
  //-----redner Ascii Art-----
  const ac = document.getElementById("ascii-container");
  ac.innerHTML = `${gameData.screen}`;

  //-----render buttons----- 
  const bc = document.getElementById("button-container");
  //We want to clear the previous screens buttons 
  bc.replaceChildren();

  //Setting the id = action allows us to send the action taken to the backend
  gameData.actions.forEach(action => {
    const btn = document.createElement("button");
    bc.appendChild(btn);
    btn.innerText = action;
    btn.setAttribute("id", action);
  });

  //-----redner text block-----
  const tc = document.getElementById("text-container");
  tc.innerText = gameData.text;
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
