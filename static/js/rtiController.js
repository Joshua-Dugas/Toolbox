async function initializeGame() {
  const response = await fetch("/tool/rti/loadScreen");
  const data = await response.json();
  const pre = document.getElementById("game-box");

  pre.innerHTML = `
    ${data.art}
  `;

  console.log("loaded scene: " + data.name);
}
