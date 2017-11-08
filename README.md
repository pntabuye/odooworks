# odooworks
# This repo holds my Odoo Modules
#
1. Python Env setup
1.1 Get Python 3.6.x
1.2 create an odooworks directory to host everything
1.3 Make this odooworks directory your make python environment
since we have both Python 2.7 and 3.6 we make sure to call pip3
> pip3 install virtualenv
Then we populate it with a new localized python distro.
> virtualenv ./odooworks
and final we switch to the new venv by activating it
> . ./bin/activate

2. Dependencies:
2.1 PostgreSQL (10.x)
We get it from homebrew on Mac OS X
> brew install postgresql
Or we pull the latest prod release grade on Window$
On Win32 the PostgreSQL service is installed
On MacOS X in have to set up ruby gem "lunchy" to start/stop it at will
> mkdir -p ~/Library/LaunchAgents
> cp /usr/local/Cellar/postgresql/10/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents/
> launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist

2.2 Node JS
On Mac OS X, we already have node due to Atom. However we can refrech our cellar pull
> brew install node
Don't forget to pull the less style compiles
2.3 Extra libraries
Odoo needs image manipulation libs that need to be pulled separately:
> brew install freetype jpeg libpng libtiff webp xz

3. Install Odoo packages
3.1 On Window$:
Use the latest packeged MSI. The wizzard will help configuring the whole thing
3.2 On Mac OS X:
We clone the latest master from github
> git clone git@github.com:odoo/odoo.git 
This will create an odoo-11.0 right under ./odooworks

4. Starting Odoo
3.1 On Window$:
We start the service
3.2 On Mac OS X:
Command line inside the activated venv:
> ./odoo-bin --addons-path=addons,../mymodules
This command line ran from the root of odoo-11.0 folder uses the path to the root directory of our modules.









