"use strict";

const arcade = (() => {
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  const status = document.getElementById("arcade-status");
  const start = document.getElementById("arcade-start");
  const pause = document.getElementById("arcade-pause");
  const initialsForm = document.getElementById("arcade-initials-form");
  const initialsInput = document.getElementById("arcade-initials");
  const images = {};
  const names = ["background.jpg", "player.png", "enemy.png", "prize.png", "blaster.png", "friend.png", "asteroid.png", "enemy_blaster.png"];
  const sounds = {};
  const GAME_OVER_FLASH_MS = 1800;
  const RETRO_FONT = '"Retro", monospace';
  for (const name of names) {
    const image = new Image();
    image.src = "/arcade/images/" + name;
    images[name.split(".")[0]] = image;
  }
  for (const name of ["arcade", "blaster", "prize", "destruction"]) {
    sounds[name] = new Audio("/arcade/sounds/" + name + ".mp3");
  }
  sounds.arcade.loop = true;
  sounds.arcade.volume = 0.4;
  const keys = new Set();
  let active = false;
  let playing = false;
  let paused = false;
  let pausedAt = 0;
  let pausedDuration = 0;
  let gameOverPhase = null;
  let gameOverStarted = 0;
  let initials = "";
  let frame = 0;
  let lastTime = 0;
  let lastShot = 0;
  let score = 0;
  let lives = 3;
  let invulnerableUntil = 0;
  let player;
  let objects;
  let shots;
  let enemyShots;
  let highScores = [];

  function sound(name) {
    const audio = sounds[name].cloneNode();
    audio.play().catch(() => {});
  }

  function drawImage(name, object) {
    const image = images[name];
    if (image.complete && image.naturalWidth) ctx.drawImage(image, object.x, object.y, object.w, object.h);
  }

  function overlap(a, b) {
    return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
  }

  function spawn(kind, width, height, speed, y) {
    objects.push({kind, x: Math.random() * (1000 - width), y, w: width, h: height, speed, shot: lastTime});
  }

  function shoot() {
    if (lastTime - lastShot < 500) return;
    lastShot = lastTime;
    shots.push({x: player.x + 53, y: player.y, w: 19, h: 78});
    sound("blaster");
  }

  function gameOver() {
    playing = false;
    gameOverPhase = "flash";
    gameOverStarted = lastTime;
    initials = "";
    sounds.arcade.pause();
    status.textContent = "Game over!";
    start.hidden = true;
    pause.hidden = true;
    initialsForm.hidden = true;
  }

  async function submitHighScore() {
    if (gameOverPhase !== "initials" || initials.length !== 3) return;
    gameOverPhase = "saving";
    status.textContent = "Saving your high score…";
    drawInitialsScreen();
    try {
      const response = await fetch("/api/high-scores", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name: initials, score})
      });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "Unable to save high scores.");
      if (gameOverPhase !== "saving") return;
      highScores = result.scores;
      gameOverPhase = "highScores";
      initialsForm.hidden = true;
      drawHighScores();
      start.textContent = "Play again";
      start.hidden = false;
      status.textContent = `Game over! Score: ${score}. High scores saved. Play again or return to the story.`;
    } catch (error) {
      if (gameOverPhase !== "saving") return;
      gameOverPhase = "initials";
      initialsForm.hidden = false;
      initialsInput.disabled = false;
      initialsInput.focus();
      drawInitialsScreen();
      status.textContent = `Could not save your score: ${error.message} Press Enter to retry.`;
    }
  }

  function loseLife() {
    if (!playing || lastTime < invulnerableUntil) return;
    lives -= 1;
    invulnerableUntil = lastTime + 2000;
    player.x = 437;
    player.y = 400;
    sound("destruction");
    if (lives <= 0) gameOver();
  }

  function update(dt) {
    const step = Math.min(dt / (1000 / 60), 3);
    const speed = 6 * step;
    player.x = Math.max(0, Math.min(875, player.x + (keys.has("ArrowRight") - keys.has("ArrowLeft")) * speed));
    player.y = Math.max(0, Math.min(475, player.y + (keys.has("ArrowDown") - keys.has("ArrowUp")) * speed));
    if (keys.has("x")) shoot();
    for (const shot of shots) shot.y -= 18 * step;
    for (const shot of enemyShots) shot.y += 9 * step;
    for (const object of objects) {
      object.y += object.speed * step;
      if (object.kind === "enemy" && lastTime - object.shot > 3000) {
        object.shot = lastTime;
        enemyShots.push({x: object.x + 40, y: object.y + 100, w: 19, h: 78});
      }
    }
    const collision = {x: player.x + 32, y: player.y + 22, w: 60, h: 80};
    for (const object of objects) {
      if (object.dead) continue;
      if ((object.kind === "enemy" || object.kind === "asteroid") && overlap(collision, object)) {
        object.dead = true;
        loseLife();
        if (!playing) return;
        continue;
      }
      if (object.kind === "prize" && overlap(player, object)) {
        object.dead = true;
        score += 10;
        sound("prize");
      }
      if (object.kind === "enemy" || object.kind === "asteroid") {
        for (const shot of shots) {
          if (!shot.dead && overlap(shot, object)) {
            shot.dead = true;
            object.dead = true;
            score += object.kind === "enemy" ? 75 : 20;
            sound("destruction");
            break;
          }
        }
      }
    }
    const hitShot = enemyShots.find(shot => !shot.dead && overlap(player, shot));
    if (hitShot) {
      hitShot.dead = true;
      loseLife();
      if (!playing) return;
    }
    objects = objects.filter(object => !object.dead && object.y < 700);
    shots = shots.filter(shot => !shot.dead && shot.y + shot.h > 0);
    enemyShots = enemyShots.filter(shot => !shot.dead && shot.y < 700);
    if (Math.random() < 1 - Math.pow(1 - 0.001, step)) spawn("enemy", 100, 100, 1, -200);
    if (Math.random() < 1 - Math.pow(1 - 0.005, step)) spawn("asteroid", 100, 100, 3, -1000);
    if (Math.random() < 1 - Math.pow(1 - 0.02, step)) spawn("prize", 50, 50, 2, -2000);
    if (Math.random() < 1 - Math.pow(1 - 0.01, step)) spawn("friend", 100, 100, 5, -1000);
  }

  function draw() {
    ctx.fillStyle = "#05080f";
    ctx.fillRect(0, 0, 1000, 600);
    drawImage("background", {x: 0, y: 0, w: 1000, h: 1200});
    for (const object of objects) drawImage(object.kind, object);
    for (const shot of shots) drawImage("blaster", shot);
    for (const shot of enemyShots) drawImage("enemy_blaster", shot);
    if (lastTime >= invulnerableUntil || Math.floor(lastTime / 100) % 2 === 0) {
      drawImage("player", player);
    }
    ctx.fillStyle = "white";
    ctx.font = `28px ${RETRO_FONT}`;
    ctx.textAlign = "left";
    ctx.fillText(`Score: ${score}`, 10, 35, 480);
    ctx.textAlign = "right";
    ctx.fillText(`Lives: ${lives}`, 990, 35, 480);
  }

  function drawHighScores() {
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, 1000, 600);
    ctx.fillStyle = "white";
    ctx.textAlign = "center";
    ctx.font = `48px ${RETRO_FONT}`;
    ctx.fillText("GAME OVER", 500, 100);
    ctx.font = `28px ${RETRO_FONT}`;
    ctx.fillText(`Final score: ${score}`, 500, 155);
    ctx.font = `36px ${RETRO_FONT}`;
    ctx.fillText("HIGH SCORES", 500, 230);
    ctx.font = `28px ${RETRO_FONT}`;
    highScores.forEach((entry, index) => {
      ctx.fillText(`${index + 1}. ${entry.name} ${entry.score}`, 500, 290 + index * 48);
    });
  }

  function drawGameOver(time) {
    const showText = Math.floor((time - gameOverStarted) / 250) % 2 === 0;
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, 1000, 600);
    if (!showText) return;
    ctx.fillStyle = "white";
    ctx.textAlign = "center";
    ctx.font = `64px ${RETRO_FONT}`;
    ctx.fillText("GAME OVER", 500, 300);
  }

  function drawInitialsScreen() {
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, 1000, 600);
    ctx.fillStyle = "white";
    ctx.textAlign = "center";
    ctx.font = `48px ${RETRO_FONT}`;
    ctx.fillText("GAME OVER", 500, 115);
    ctx.font = `28px ${RETRO_FONT}`;
    ctx.fillText(`Final score: ${score}`, 500, 175);
    ctx.fillText("Enter three initials for the high score", 500, 270);
    ctx.font = `56px ${RETRO_FONT}`;
    ctx.fillText(initials.padEnd(3, "_").split("").join(" "), 500, 365);
    ctx.font = `22px ${RETRO_FONT}`;
    ctx.fillText("Type letters, then press Enter", 500, 435);
  }

  function tick(time) {
    if (!active || paused) return;
    time -= pausedDuration;
    if (playing) {
      const delta = lastTime ? time - lastTime : 0;
      lastTime = time;
      update(delta);
      if (playing) draw();
      else if (gameOverPhase === "flash") drawGameOver(time);
      if (playing || gameOverPhase === "flash") frame = requestAnimationFrame(tick);
      return;
    }
    if (gameOverPhase !== "flash") return;
    if (time - gameOverStarted >= GAME_OVER_FLASH_MS) {
      gameOverPhase = "initials";
      status.textContent = "Enter three initials for your high score, then press Enter.";
      initialsForm.hidden = false;
      initialsInput.disabled = false;
      initialsInput.focus();
      drawInitialsScreen();
      return;
    }
    drawGameOver(time);
    frame = requestAnimationFrame(tick);
  }

  function begin() {
    if (!active) return;
    player = {x: 437, y: 400, w: 125, h: 125};
    objects = [];
    shots = [];
    enemyShots = [];
    score = 0;
    lives = 3;
    invulnerableUntil = 0;
    paused = false;
    pausedDuration = 0;
    gameOverPhase = null;
    initials = "";
    initialsInput.value = "";
    initialsInput.disabled = false;
    initialsForm.hidden = true;
    lastTime = 0;
    lastShot = -500;
    keys.clear();
    playing = true;
    start.hidden = true;
    pause.hidden = false;
    pause.textContent = "Pause";
    status.textContent = "Good luck!";
    sounds.arcade.currentTime = 0;
    sounds.arcade.play().catch(() => {
      status.textContent = "Good luck! Audio is unavailable in this browser.";
    });
    frame = requestAnimationFrame(tick);
  }

  function togglePause() {
    if (!active || !playing) return;
    paused = !paused;
    keys.clear();
    if (paused) {
      pausedAt = performance.now();
      cancelAnimationFrame(frame);
      sounds.arcade.pause();
      ctx.fillStyle = "#000b";
      ctx.fillRect(0, 0, 1000, 600);
      ctx.fillStyle = "white";
      ctx.textAlign = "center";
      ctx.font = `48px ${RETRO_FONT}`;
      ctx.fillText("PAUSED", 500, 300);
      pause.textContent = "Resume";
      status.textContent = "Paused. Press P or Resume to continue.";
    } else {
      pausedDuration += performance.now() - pausedAt;
      pause.textContent = "Pause";
      status.textContent = "Good luck!";
      sounds.arcade.play().catch(() => {
        if (active && playing && !paused) status.textContent = "Good luck! Audio is unavailable in this browser.";
      });
      frame = requestAnimationFrame(tick);
    }
  }

  initialsInput.addEventListener("input", () => {
    initials = initialsInput.value.replace(/[^a-z]/gi, "").toUpperCase().slice(0, 3);
    initialsInput.value = initials;
    drawInitialsScreen();
  });
  initialsForm.addEventListener("submit", event => {
    event.preventDefault();
    if (initials.length !== 3) {
      status.textContent = "Enter three letters for your initials.";
      return;
    }
    initialsInput.disabled = true;
    initialsForm.hidden = true;
    submitHighScore();
  });

  start.addEventListener("click", begin);
  pause.addEventListener("click", togglePause);
  document.addEventListener("keydown", event => {
    if (!active || !playing) return;
    if (event.key.toLowerCase() === "p") {
      event.preventDefault();
      if (!event.repeat) togglePause();
      return;
    }
    if (paused) return;
    if (["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "x", "X"].includes(event.key)) {
      event.preventDefault();
      keys.add(event.key.toLowerCase() === "x" ? "x" : event.key);
    }
  });
  document.addEventListener("keyup", event => keys.delete(event.key.toLowerCase() === "x" ? "x" : event.key));
  window.addEventListener("blur", () => keys.clear());
  for (const button of document.querySelectorAll("[data-key]")) {
    button.addEventListener("pointerdown", event => {
      if (!active || !playing || paused) return;
      event.preventDefault();
      button.setPointerCapture(event.pointerId);
      keys.add(button.dataset.key);
    });
    button.addEventListener("pointerup", () => keys.delete(button.dataset.key));
    button.addEventListener("pointercancel", () => keys.delete(button.dataset.key));
    button.addEventListener("lostpointercapture", () => keys.delete(button.dataset.key));
  }

  return {
    reset() {
      highScores = [];
      gameOverPhase = null;
      initials = "";
    },
    open() {
      active = true;
      gameOverPhase = null;
      pause.hidden = true;
      start.hidden = false;
      start.textContent = "Play";
      status.textContent = "Press Play to begin.";
      initialsForm.hidden = true;
      ctx.fillStyle = "#05080f";
      ctx.fillRect(0, 0, 1000, 600);
    },
    close() {
      active = false;
      playing = false;
      paused = false;
      gameOverPhase = null;
      initialsForm.hidden = true;
      pause.hidden = true;
      cancelAnimationFrame(frame);
      keys.clear();
      sounds.arcade.pause();
    }
  };
})();
