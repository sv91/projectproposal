# Projectproposal

Multi step form created through Django in order to serve as a proposal generator.

## Installation

Execute first the command ```pip install pip==1.4.1``` followed by ```pip install -i https://bbpteam.epfl.ch/repository/devpi/simple --pre -r "requirements.txt"```.<br />
If you don't have pip installed: [Install pip](https://pip.pypa.io/en/stable/installing/) .

Go to [Collab portal: Client creation](collab.humanbrainproject.eu/#/collab/54/nav/1051) and click on the <code>+ Create new Client</code> button.<br />
Fill the formular with those informations:
* __Name:__ 'HPC Computing Platform: Production Project Request'
* __Application type:__ Server flow
* __Authorized redirect URLs:__ 'https://localhost:8000'
* __Authorized scopes:__ openid, profile, offline_access, hbp.users
* Leave the logo as it is.

Press save and stay on the page that will appear.

Create a file 'projectproposal/projectproposal/localsettings.py' and write:
```python
import hbp_app_python_auth.settings as auth_settings
auth_settings.SOCIAL_AUTH_HBP_KEY = 'XXX'
auth_settings.SOCIAL_AUTH_HBP_SECRET = 'YYY'
```
where 'XXX' is the Client ID value from the page and 'YYY' is the Client secret value.</code>

In your terminal execute the command <code>python manage.py runsslserver</code>.<br />
If you dont have a certificate for your localhost: [Collab portal: How to set local certificate](https://developer.humanbrainproject.eu/docs/projects/HBP%20Collaboratory%20Documentation/1.2/app-developer-manual/quickstart/setup/ssl-certificate.html) <br />
Open your browser and go to [LocalHost](https://localhost:8000/formular) and authorise the client you created.

## TODO List

- [ ] Visual Design
	- [ ] .
	
- [ ] Steps
	- [ ] Step 7: Summary of step 6
	- [ ] Legal agreement
	- [ ] PDF generation and update

- [ ] Features
	- [ ] Import
	- [ ] Export
	- [ ] Delete "Add more" parts
		- [ ] Remove the formular part on the screen
		- [ ] Delete the session Variable
		- [ ] Delete the linked session Variable
		- [ ] Adapt numbering

- [ ] Information treatment
	- [ ] Standardise variable names
	- [ ] Treatment of empty values
	- [ ] Optimise the modularity of the functions

- [ ] Development
	- [ ] Continuous integration