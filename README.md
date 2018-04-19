# gnucash-portfolio-webui

GnuCash Portfolio Web UI

The code is written in Python on the server-side, and HTML/JavaScript/CSS on the client-side.

All the libraries are listed in `requirements.txt` for Python and `package.json` for node.

To install the required development and runtime dependencies, run

```
pip install -r requirements.txt
npm install
```

Npm's package.json is in the app directory.

To compile all client-side (.scss, .js) code, run

`npm run build`

in the "app" directory. This will compile production-ready images, styles, and scripts into `/static` folder.

`npm run dev` will do the same but for development. Meaning, the source code will not be minimized and webpack will continue monitoring the folders for any changes to the source files.

### CSS

Custom SCSS is compiled with Webpack (`npm run build`).

Vendor CSS is bundled with Flask Assets automatically when the site starts.

### JS

Custom JavaScript code is compiled through Webpack.

Vendor libraries are currently bundled through Flask Assets. It collects the vendor code from installed development node modules. Make sure all the npm dependencies are installed in order for this to work.
The bundle will be built automatically during the app runtime. No additional actions required by the user.

## Development

For development, run the web site:
`py app`

and compile and monitor the client-side code with

`npm run dev`

## Running

How to run the web app.

### First-Time Setup

- Config:
  In order to run the app, copy `config/settings.json.template` into `config/settings.json`. The options can be customized via the Settings link in the web app.

### Execution

All the functionality is provided through a web UI. To run, simply run the app with Python. Running

`py app`

from the root folder will do.

There are several ways to run the web app:

1. Run `py app` directly,
2. Run the "run" task from VS Code,
3. Run "run.py run" (This script was created so that the app could be debugged with Python extension for Visual Studio Code).

### Lint

- run `pylint app/` to run lint on the web app,

# Web Application

This project contains the web application implemented in Flask. It is intended to be used as the full GUI for accepting user input (parameters) and displaying the output.

The app is located in the `/app` directory.

It is intended to run on a desktop workstation, with direct access to the GnuCash book file, stored as an SQLite database.
