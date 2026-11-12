"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

function browser(storage = new Map(), failWrites = false, events = [{type: "finished"}]) {
  const elements = new Map();
  const requests = [];
  const sandbox = {
    document: {
      getElementById(id) {
        if (!elements.has(id)) {
          elements.set(id, {
            hidden: false, value: "", textContent: "", style: {}, handlers: {},
            addEventListener(type, handler) { this.handlers[type] = handler; },
            focus() {},
            append() {}
          });
        }
        return elements.get(id);
      }
    },
    localStorage: {
      getItem(key) { return storage.has(key) ? storage.get(key) : null; },
      setItem(key, value) {
        if (failWrites) throw new Error("storage unavailable");
        storage.set(key, value);
      }
    },
    fetch: async (url, options) => {
      requests.push({url, options});
      return {
        ok: true,
        json: async () => url === "/api/events" ? {events} : {}
      };
    },
    arcade: {reset() {}, close() {}, open() {}},
    setTimeout,
    confirm: () => true
  };
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync(path.join(__dirname, "../web/app.js"), "utf8"), sandbox);
  return {sandbox, elements, requests, storage};
}

test("character saves are isolated and survive a page reload", async () => {
  const computer = browser();
  const phone = browser();
  vm.runInContext('saveCharacter({Name: "Alice", Age: "25", Colony: "America", Job: "Pilot"})', computer.sandbox);
  vm.runInContext('saveCharacter({Name: "Bob", Age: "30", Colony: "China"})', phone.sandbox);
  const reloaded = browser(computer.storage);
  vm.runInContext('saveCharacter({Person: "Friend"})', reloaded.sandbox);
  await reloaded.elements.get("start").handlers.click();
  await phone.elements.get("start").handlers.click();
  assert.deepEqual(JSON.parse(reloaded.requests[0].options.body).character, {
    Name: "Alice", Age: "25", Colony: "America", Job: "Pilot", Person: "Friend"
  });
  assert.deepEqual(JSON.parse(phone.requests[0].options.body).character, {
    Name: "Bob", Age: "30", Colony: "China"
  });
});

test("storage failures are reported without replacing existing data", () => {
  const storage = new Map([["extinction.character", '{"Name":"Alice"}']]);
  const tab = browser(storage, true);
  vm.runInContext('saveCharacter({Name: "Bob"})', tab.sandbox);
  assert.equal(storage.get("extinction.character"), '{"Name":"Alice"}');
  assert.match(tab.elements.get("error").textContent, /Could not save your character/);
  assert.equal(tab.elements.get("error").hidden, false);
});

test("game character updates are saved to the browser", async () => {
  const tab = browser(new Map(), false, [
    {type: "character_update", changes: {Name: "Alice", Age: "25", Colony: "America"}},
    {type: "character_update", changes: {Job: "Pilot"}},
    {type: "finished"}
  ]);
  await tab.elements.get("start").handlers.click();
  await new Promise(resolve => setImmediate(resolve));
  assert.deepEqual(JSON.parse(tab.storage.get("extinction.character")), {
    Name: "Alice", Age: "25", Colony: "America", Job: "Pilot"
  });
});

test("chapter 8 unlock survives reload and stays separate between browsers", async () => {
  const computer = browser(new Map(), false, [
    {type: "chapter8_unlocked"},
    {type: "finished"}
  ]);
  const phone = browser();
  await computer.elements.get("start").handlers.click();
  await new Promise(resolve => setImmediate(resolve));
  const reloaded = browser(computer.storage);
  await reloaded.elements.get("start").handlers.click();
  await phone.elements.get("start").handlers.click();
  assert.equal(JSON.parse(reloaded.requests[0].options.body).chapter8Unlocked, true);
  assert.equal(JSON.parse(phone.requests[0].options.body).chapter8Unlocked, false);
});

test("chapter unlock storage failure is reported", async () => {
  const tab = browser(new Map(), true, [
    {type: "chapter8_unlocked"},
    {type: "finished"}
  ]);
  await tab.elements.get("start").handlers.click();
  await new Promise(resolve => setImmediate(resolve));
  assert.match(tab.elements.get("error").textContent, /Could not save.*Chapter 8/i);
});
