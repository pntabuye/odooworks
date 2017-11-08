odooworks
---

This repo holds my Odoo Modules


1 Python Env setup

1.1. Get Python 3.6.x

1.2. create an odooworks directory to host everything

Make this odooworks directory your make python environment
since we have both Python 2.7 and 3.6 we make sure to call pip3

        pip3 install virtualenv

Then we populate it with a new localized python distro.

        virtualenv ./odooworks

and final we switch to the new venv by activating it

        . ./bin/activate

2 Dependencies:

2.1 PostgreSQL (10.x)

We get it from homebrew on Mac OS X

        brew install postgresql

Or we pull the latest prod release grade on Window$
On Win32 the PostgreSQL service is installed
On MacOS X in have to set up ruby gem "lunchy" to start/stop it at will

        mkdir -p ~/Library/LaunchAgents
        cp /usr/local/Cellar/postgresql/10/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents/
        launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist

Configure PostgreSQL
* host: localhost
* Port: 5432
* username: odooadm
* password: odoosrvpwd


2.2 Node JS

On Mac OS X, we already have node due to Atom. However we can refrech our cellar pull

        brew install node

Don't forget to pull the less style compiles

2.3 Extra libraries

Odoo needs image manipulation libs that need to be pulled separately:

        brew install freetype jpeg libpng libtiff webp xz

3 Install Odoo packages

3.1 On Window$:

Use the latest packaged MSI binary `"odoo_11.0.latest.exe"`. The wizzard will help configuring the whole thing:
* Choose English and start setup process
* Agree to License doc
* Chose to install Odoo Server
* install in "C:\Program Files (x86)\Odoo 11.0" ( 700 MB )

3.2 On Mac OS X:

We clone the latest master from github

        git clone git@github.com:odoo/odoo.git

This will create an odoo-11.0 right under ./odooworks

4 Starting Odoo

4.1 On Window$:

We start the service using services.msc

4.2 On Mac OS X:

Command line inside the activated venv:

        ./odoo-bin --addons-path=addons,../mymodules

This command line ran from the root of odoo-11.0 folder uses the path to the root directory of our modules.

5 Creating a new database

* Master Password: odooadmpwd
* Database Name: odoodbone
* email: pntabuye@gmail.com
* password: muyange73
* language: English
* Coutry: Belgium

We do not load demo data and we create the initial DB

Note: original master password is `admin`. in Windows you are prompted ti change it upon first connect to odoo. Otherwise the master password is
placed in `odoo-server.conf` file and you can reset it manually.

6 Creating an oddo app or module

We build a base directory for holding our module and buid a template project using the `scaffold`sub command:

        mkdir odooworks/mymodules
        odoo-bin scofolld musicregister odooworks/mymodules
