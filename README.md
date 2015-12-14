# Projectproposal

Multi step form created through Django in order to serve as a proposal generator.

## Installation

Execute the command <code>pip install -i https://bbpteam.epfl.ch/repository/devpi/simple --pre -r "requirements.txt"</code>.
If you don't have pip installed: https://pip.pypa.io/en/stable/installing/ .

Go to 'collab.humanbrainproject.eu/#/collab/54/nav/1051' and click on the '+ Create new Client' button.
Fill the formular with those informations:
	Name: 'HPC Computing Platform: Production Project Request'
	Application type: Server flow
	Authorized redirect URLs: 'https://localhost:8000'
	Authorized scopes: openid, profile, offline_access, hbp.users
	Leave the logo as it is.
Press save and stay on the page that will appear.

Create a file 'projectproposal/projectproposal/localsettings.py' and write:
<code>import hbp_app_python_auth.settings as auth_settings
auth_settings.SOCIAL_AUTH_HBP_KEY = 'XXX'
auth_settings.SOCIAL_AUTH_HBP_SECRET = 'YYY'</code>
where 'XXX' is the Client ID value from the page and 'YYY' is the Client secret value.</code>

In your terminal execute the command <code>python manage.py runsslserver</code>.
If you dont have a certificate for your localhost: https://developer.humanbrainproject.eu/docs/projects/HBP%20Collaboratory%20Documentation/1.2/app-developer-manual/quickstart/setup/ssl-certificate.html
Open your browser and go to 'https://localhost:8000/formular' and authorise the client you created.