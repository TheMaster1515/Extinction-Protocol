"use strict";

const arcade = (() => {
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  const status = document.getElementById("arcade-status");
  const start = document.getElementById("arcade-start");
  const images = {};
  const names = ["background.jpg", "player.png", "enemy.png", "prize.png", "blaster.png", "friend.png", "asteroid.png", "enemy_blaster.png"];
  const sounds = {};
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
  let frame = 0;
  let lastTime = 0;
  let lastShot = 0;
  let score = 0;
  let player;
  let objects;
  let shots;
  let enemyShots;
  let highScore = 0;

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
    highScore = Math.max(highScore, score);
    sound("destruction");
    sounds.arcade.pause();
    status.textContent = `Game over! Score: ${score}. Session high score: ${highScore}. Play again or return to the story.`;
    start.textContent = "Play again";
    start.hidden = false;
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
        gameOver();
        return;
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
    if (enemyShots.some(shot => overlap(player, shot))) {
      gameOver();
      return;
    }
    objects = objects.filter(object => !object.dead && object.y < 700);
    shots = shots.filter(shot => !shot.dead && shot.y + shot.h > 0);
    enemyShots = enemyShots.filter(shot => shot.y < 700);
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
    drawImage("player", player);
    ctx.fillStyle = "white";
    ctx.font = "28px monospace";
    ctx.fillText(`Score: ${score}`, 10, 35);
    ctx.fillText("Lives: 1", 820, 35);
  }

  function tick(time) {
    if (!active || !playing) return;
    const delta = lastTime ? time - lastTime : 0;
    lastTime = time;
    update(delta);
    draw();
    if (playing) frame = requestAnimationFrame(tick);
  }

  function begin() {
    if (!active) return;
    player = {x: 437, y: 400, w: 125, h: 125};
    objects = [];
    shots = [];
    enemyShots = [];
    score = 0;
    lastTime = 0;
    lastShot = -500;
    keys.clear();
    playing = true;
    start.hidden = true;
    status.textContent = "Good luck!";
    sounds.arcade.currentTime = 0;
    sounds.arcade.play().catch(() => {
      status.textContent = "Good luck! Audio is unavailable in this browser.";
    });
    frame = requestAnimationFrame(tick);
  }

  start.addEventListener("click", begin);
  document.addEventListener("keydown", event => {
    if (!active || !playing) return;
    if (["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "x", "X"].includes(event.key)) {
      event.preventDefault();
      keys.add(event.key.toLowerCase() === "x" ? "x" : event.key);
    }
  });
  document.addEventListener("keyup", event => keys.delete(event.key.toLowerCase() === "x" ? "x" : event.key));
  window.addEventListener("blur", () => keys.clear());
  for (const button of document.querySelectorAll("[data-key]")) {
    button.addEventListener("pointerdown", event => {
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
      highScore = 0;
    },
    open() {
      active = true;
      start.hidden = false;
      start.textContent = "Play";
      status.textContent = "Press Play to begin.";
      ctx.fillStyle = "#05080f";
      ctx.fillRect(0, 0, 1000, 600);
    },
    close() {
      active = false;
      playing = false;
      cancelAnimationFrame(frame);
      keys.clear();
      sounds.arcade.pause();
    }
  };
})();
