async function initializeGame() {
  const response = await fetch("/tool/rti/loadScreen");
  const data = await response.json();
  const pre = document.getElementById("game-box");

  pre.innerHTML = `
    ${data.art}
  `;

  console.log("loaded scene: " + data.name);
}

// Create a new game
async function createGame(saveName, gameData) {
  const response = await fetch("/tool/rti/createGame", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ save_name: saveName, game_data: gameData })
  });

  const data = await response.json();
  console.log("CreateGame response:", data);
}

// Save current game
async function saveGame(saveName, gameData) {
  const response = await fetch("/tool/rti/saveGame", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ save_name: saveName, game_data: gameData })
  });

  const data = await response.json();
  console.log("SaveGame response:", data);
}

// Load a saved game
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
