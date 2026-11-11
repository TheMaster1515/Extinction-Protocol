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
arrow keys and X to move and fire in the arcade; press P or use the Pause
button to pause and resume. Touch controls are also available. You can return
to the story using the button below the game.
After losing all lives, enter three initials and press Enter or click **Save
score** to add your score to the high-score list.

Each player gets a separate temporary story session. Character details are saved
in the browser on that device, separately for each browser and website address.
Designing a new character replaces the name, age, and colony; the friend, ship,
and job remain until new choices are made.
Choose **Start at a level** to go straight to chapter selection using the saved
character, or **Design your character** to enter new details. If no character
is saved, missing details are shown as Unknown and age is 0.
The old shared `files/character.txt` and `files/job.txt` are left untouched and
are not imported into browser saves. Clearing browser storage or using private
browsing may remove your character. The desktop game continues to use its local
character file.
Arcade high scores are shared and saved in `files/HighScores.txt` on the server. Story progress is
lost when starting over, reloading and starting a new game, server restarts,
or 30 minutes without an active page. Browser character saves survive reloads
and server restarts. High scores may be lost when the server restarts or
redeploys if its filesystem is ephemeral. The server supports up to 20 simultaneous sessions. Run only one
server process, because sessions are held in that process's memory.

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
