//TODO: add delete logic | Add actual memory interaction 

async function init() {
  loadVerses();
}

async function addVerse() {
  const verseHeader = document.getElementById("bk-ch-vs").value.trim();
  const verseBody = document.getElementById("vs-text").value.trim();

  if (!verseHeader || !verseBody) {
    alert("Please populate both fields");
    return;
  }

  //TODO: add dupe prevention once population is fleshed out 

  const response = await fetch("/tool/memoryVerse/verse/add", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      header: verseHeader,
      body: verseBody
    })
  });

  const data = await response.json();
  const verseList = document.getElementById("verse-list");
  const listEntry = document.createElement("li");

  listEntry.innerHTML = `
    <li>${data.header}: "${data.body}"</li>
  `;

  verseList.append(listEntry);


  // Clear inputs
  document.getElementById("bk-ch-vs").value = "";
  document.getElementById("vs-text").value = "";
}

async function loadVerses() {
  const response = await fetch("/tool/memoryVerse/verse/getData");
  const verses = await response.json();
  console.log(verses);

  const verseList = document.getElementById("verse-list");

  for (const [header, verse] of Object.entries(verses)) {
    body = verse.body;
    const listEntry = document.createElement("li");

    listEntry.innerHTML = `
    <li>${header}: "${body}"</li>
  `;

    verseList.append(listEntry);
  }
}

init();
