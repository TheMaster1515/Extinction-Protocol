"use strict";

const $ = id => document.getElementById(id);
const characterKey = "extinction.character";
let running = false;
let generation = 0;
let submitting = false;

async function request(path, data) {
  const options = data === undefined ? {} : {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  };
  const response = await fetch(path, options);
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || "Request failed.");
  return result;
}

function showError(message) {
  $("error").textContent = message;
  $("error").hidden = false;
}

function loadCharacter() {
  const saved = localStorage.getItem(characterKey);
  if (saved === null) return {};
  const character = JSON.parse(saved);
  if (!character || typeof character !== "object" || Array.isArray(character)) {
    throw new Error("The character saved in this browser is invalid.");
  }
  return character;
}

function saveCharacter(changes) {
  try {
    const character = {...loadCharacter(), ...changes};
    localStorage.setItem(characterKey, JSON.stringify(character));
  } catch (error) {
    showError("Could not save your character in this browser. Check your browser's storage settings.");
  }
}

function append(text) {
  const output = $("output");
  output.append(document.createTextNode(text));
  if (output.textContent.length > 200000) {
    output.textContent = output.textContent.slice(-150000);
  }
  output.scrollTop = output.scrollHeight;
}

async function poll(current) {
  while (running && current === generation) {
    try {
      const {events} = await request("/api/events");
      if (current !== generation) return;
      for (const event of events) {
        if (event.type === "output") append(event.text);
        else if (event.type === "character_update") saveCharacter(event.changes);
        else if (event.type === "input") {
          $("prompt").textContent = event.prompt || "Enter your response, or press Enter to continue";
          $("input-form").hidden = false;
          $("status").hidden = true;
          $("answer").focus();
        } else if (event.type === "image") {
          $("story").style.backgroundImage = `url(${JSON.stringify("/" + event.path)})`;
        } else if (event.type === "arcade") {
          $("story").hidden = true;
          $("arcade").hidden = false;
          arcade.open();
        } else if (event.type === "error") showError(event.message);
        else if (event.type === "finished") {
          running = false;
          $("input-form").hidden = true;
          $("status").hidden = false;
          $("status").textContent = "Game ended. Start over to play again.";
        }
      }
    } catch (error) {
      if (current === generation) {
        running = false;
        showError(error.message);
      }
      return;
    }
    await new Promise(resolve => setTimeout(resolve, 300));
  }
}

async function send(value) {
  if (submitting) return false;
  submitting = true;
  try {
    await request("/api/input", {value});
    return true;
  } catch (error) {
    showError(error.message);
    return false;
  } finally {
    submitting = false;
  }
}

$("start").addEventListener("click", async () => {
  $("start").disabled = true;
  $("error").hidden = true;
  try {
    await request("/api/start", {character: loadCharacter()});
    arcade.reset();
    running = true;
    generation++;
    $("welcome").hidden = true;
    $("story").hidden = false;
    $("restart").hidden = false;
    $("status").hidden = false;
    $("status").textContent = "Starting game…";
    poll(generation);
  } catch (error) {
    showError(error.message);
  } finally {
    $("start").disabled = false;
  }
});

$("restart").addEventListener("click", async () => {
  if (!confirm("Are you sure you would like to start over?")) return;
  $("restart").disabled = true;
  try {
    await request("/api/stop", {});
  } catch (error) {
    if (!error.message.includes("expired")) {
      showError(error.message);
      $("restart").disabled = false;
      return;
    }
  }
  running = false;
  generation++;
  arcade.close();
  $("output").textContent = "";
  $("answer").value = "";
  $("input-form").hidden = true;
  $("story").hidden = true;
  $("arcade").hidden = true;
  $("restart").hidden = true;
  $("restart").disabled = false;
  $("error").hidden = true;
  $("welcome").hidden = false;
});

$("input-form").addEventListener("submit", async event => {
  event.preventDefault();
  const value = $("answer").value;
  const prompt = $("prompt").textContent;
  $("input-form").hidden = true;
  $("status").hidden = false;
  $("status").textContent = "Continuing…";
  if (await send(value)) {
    append((prompt === "Enter your response, or press Enter to continue" ? "" : prompt) + value + "\n");
    $("answer").value = "";
  } else {
    $("input-form").hidden = false;
    $("status").hidden = true;
  }
});

$("arcade-finish").addEventListener("click", async () => {
  $("arcade-finish").disabled = true;
  $("arcade").hidden = true;
  $("story").hidden = false;
  $("status").hidden = false;
  $("status").textContent = "Continuing…";
  if (await send("")) {
    arcade.close();
  } else {
    $("arcade").hidden = false;
    $("story").hidden = true;
  }
  $("arcade-finish").disabled = false;
});
