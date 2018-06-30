# GnuCash Portfolio Web UI

The code is written in Python on the server-side, and HTML/JavaScript/CSS on the client-side.

All the dependent libraries are listed in `requirements.txt` for Python and `package.json` for node.

## Set Up

To install the required development and runtime dependencies, run

```console
pip install -r requirements.txt
```

Npm's package.json is in the app directory. Go to app directory and run

```console
npm install
```

To compile all client-side (.scss, .js) code, run

`npm run build`

in the "app" directory. This will compile production-ready images, styles, and scripts into `/static` folder.

`npm run dev` will do the same but for development. Meaning, the source code will not be minimized and webpack will continue monitoring the folders for any changes to the source files.

### CSS

Custom SCSS is compiled with Webpack (when `npm run build` is executed).

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

### Debugging

Add `"FLASK_APP": "app/app"` to vscode Python extension settings.

# Web Application

This project contains the web application implemented in Flask. It is intended to be used as the full GUI for accepting user input (parameters) and displaying the output.

The app is located in the `/app` directory.

It is intended to run on a desktop workstation, with direct access to the GnuCash book file, stored as an SQLite database.

## Benefits

Considering several factors below, it might be preferrable to use an independent application to work with Portfolio then to provide the UI functionality through GnuCash reports using gnucash_utilities project. This approach would utilize the gnucash book/database directly.

- Ease of development  
Developing reports on piecash stack seems fairly straightforward and much simpler than Scheme, GnuCash reporting engine. The control of the output is also easier by directly editing HTML templates and CSS styles.

- Performance  
Comparing the output through GnuCash reports on Windows to the output produced using the Python stack (flask + jinja HTML output + piecash), the advantage is significantly on the side of the Python components.

# Distribution

### Test Site

```console
python setup.py sdist upload -r test
```

### Production Site

```console
python setup.py sdist upload -r pypi
```