# Extinction Protocol

A text-based sci-fi adventure with a Chapter 8 arcade game.

## Play in a browser

The website uses Python's standard library and does not require additional
packages. From the project folder, run:

```sh
python3 web_server.py
```

Open https://extinction-protocol.onrender.com/. The website uses the
existing story and images, and a browser version of the arcade game. Use the
arrow keys and X to move and fire in the arcade; touch controls are also
available. You can return to the story using the button below the game.

Each player gets a separate temporary session. Progress and arcade high scores
are not saved permanently; starting over, reloading and starting a new game,
server restarts, or 30 minutes without an active page can lose progress. The
server supports up to 20 simultaneous sessions. Run only one server process,
because sessions are held in that process's memory.

## Deploy to Render

Push the project to GitHub. In Render, choose **New → Web Service**, connect
the repository and select the branch to deploy. Choose Python as the language,
leave the build command empty (or use `true` if the field is required), and set
the start command to:

```sh
python3 web_server.py
```

The server listens on Render's `PORT`. Deploy the service and open its
`onrender.com` address. Render's free services may spin down after inactivity,
which ends active sessions. Don't use multiple instances or workers without
replacing the in-memory session manager.

## Desktop version

The original desktop launcher is `TextBaseGame.sh`. It requires Python,
Pygame, and OpenCV, and is separate from the website.
