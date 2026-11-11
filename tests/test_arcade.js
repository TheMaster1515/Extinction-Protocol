"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

function createArcade() {
  let time = 0;
  let nextFrame = 0;
  let randomCall = 0;
  const frames = new Map();
  const text = [];
  const documentHandlers = {};
  const ctx = {
    fillRect() {},
    drawImage() {},
    fillText(value, x, y, maxWidth) {
      text.push({value, x, y, maxWidth, align: this.textAlign});
    }
  };
  function element() {
    return {
      hidden: false, value: "", handlers: {},
      addEventListener(type, handler) { this.handlers[type] = handler; },
      focus() {}
    };
  }
  const start = element();
  const pause = element();
  const status = element();
  const form = element();
  const initials = element();
  const elements = {
    canvas: {getContext: () => ctx},
    "arcade-start": start,
    "arcade-pause": pause,
    "arcade-status": status,
    "arcade-initials-form": form,
    "arcade-initials": initials
  };
  class ImageStub {}
  class AudioStub {
    cloneNode() { return new AudioStub(); }
    play() { return Promise.resolve(); }
    pause() {}
  }
  const math = Object.create(Math);
  math.random = () => (++randomCall % 2 ? 0 : 0.5);
  const sandbox = {
    document: {
      getElementById: id => elements[id],
      addEventListener(type, handler) { documentHandlers[type] = handler; },
      querySelectorAll: () => []
    },
    window: {addEventListener() {}},
    Image: ImageStub,
    Audio: AudioStub,
    Math: math,
    performance: {now: () => time},
    requestAnimationFrame(handler) {
      frames.set(++nextFrame, handler);
      return nextFrame;
    },
    cancelAnimationFrame(id) { frames.delete(id); }
  };
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync(path.join(__dirname, "../web/arcade.js"), "utf8"), sandbox);
  vm.runInContext("arcade.open()", sandbox);
  start.handlers.click();
  return {
    start, pause, status, text, frames,
    advance(milliseconds) { time += milliseconds; },
    tick(milliseconds = 1000 / 60) {
      time += milliseconds;
      const callbacks = [...frames.values()];
      frames.clear();
      callbacks.forEach(callback => callback(time));
    },
    key(key, repeat = false) {
      documentHandlers.keydown({key, repeat, preventDefault() {}});
    },
    close() { vm.runInContext("arcade.close()", sandbox); }
  };
}

test("lives and score are anchored inside separate canvas regions", () => {
  const game = createArcade();
  game.tick();
  const score = game.text.find(item => item.value === "Score: 0");
  const lives = game.text.find(item => item.value === "Lives: 3");
  assert.deepEqual([score.x, score.align, score.maxWidth], [10, "left", 480]);
  assert.deepEqual([lives.x, lives.align, lives.maxWidth], [990, "right", 480]);
});

test("pause freezes frames and respawn protection until resumed", () => {
  const game = createArcade();
  for (let i = 0; i < 1000 && !game.text.some(item => item.value === "Lives: 2"); i++) {
    game.tick();
  }
  assert.ok(game.text.some(item => item.value === "Lives: 2"));
  game.key("p");
  assert.equal(game.pause.textContent, "Resume");
  assert.equal(game.frames.size, 0);
  assert.ok(game.text.some(item => item.value === "PAUSED"));
  game.key("p", true);
  assert.equal(game.pause.textContent, "Resume");
  game.advance(10000);
  game.pause.handlers.click();
  assert.equal(game.pause.textContent, "Pause");
  for (let i = 0; i < 30; i++) game.tick();
  assert.equal(game.text.some(item => item.value === "Lives: 1"), false);
  for (let i = 0; i < 150 && !game.text.some(item => item.value === "Lives: 1"); i++) {
    game.tick();
  }
  assert.ok(game.text.some(item => item.value === "Lives: 1"));
  game.close();
  assert.equal(game.frames.size, 0);
  assert.equal(game.pause.hidden, true);
});
