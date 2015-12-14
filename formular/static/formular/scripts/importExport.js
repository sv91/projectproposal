/*
*  Set of scripts used for the export and import of the values from the "Formular" app.
*/


/*	
*	Getting rid of all the ugly characters and of the fields that we don't need 
*	such as the sessionId.
*	
*	Input:
*str: 	String to clean.
*
*	Return:
*The cleaned version of the input string.
*/
function cleanString(str)
{
	var clean = str.replace(/{u'/g,"{'");
	clean = clean.replace(/\[u'/g,"['");
	clean = clean.replace(/, u'/g,", '");
	clean = clean.replace(/<MultiValueDict: /g,"");
	clean = clean.replace(/'csrfmiddlewaretoken': \[[^\]]*\],/,"");
	clean = clean.replace(/'proposal_wizard-current_step': \['[0-9]*'\]}>,/,"");
	return clean;
}

/*	
*	Creating a file containing some specified text and a link to that file in  
*	order to download it.
*	
*	Input:
*textToWrite: 	The desired content of the file to download.
*/
function extract(textToWrite)
{
	var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'});
	var fileNameToSaveAs = "ProjectProposal.txt";

	var downloadLink = document.createElement("a");
	downloadLink.download = fileNameToSaveAs;
	if (window.URL != null)
	{
		// Chrome allows the link to be clicked
		// without actually adding it to the DOM.
		downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
	}
	else
	{
		// Firefox requires the link to be added to the DOM
		// before it can be clicked.
		downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
		downloadLink.onclick = destroyClickedElement;
		downloadLink.style.display = "none";
		document.body.appendChild(downloadLink);
	}
	downloadLink.click();
}

/*	
*	Function to fill the form by using an imported file.
*/
function importOld()
{
	var filePath = document.getElementById('load');
	var fileToLoad = filePath.files[0];

	var fileReader = new FileReader();
	fileReader.onload = function(fileLoadedEvent) 
	{
		var textFromFileLoaded = fileLoadedEvent.target.result;
		copyToSession(textFromFileLoaded);
		alert('The file was successfully imported');
	};
	fileReader.readAsText(fileToLoad, "UTF-8");
}

/*
* 	Look for the specified key and return the value associated.
*
* 	Input:
*val:	Key to look for.
*txt:	String in which the function should look for the key.
*
*	Return:
*The value associated to the key.
*/
function getValueOf(val,txt)
{
	var pos = 0;
	var result = "";
	var lookFor = "'"+ val +"': ['";
	if(txt.indexOf(lookFor) > -1){
		var temp = "";
		pos = txt.indexOf(lookFor) + lookFor.length;
		while(txt.charAt(pos) != "'" && txt.charAt(pos+1) != "]"){
			temp += txt.charAt(pos);
			pos ++;
		}
		result = temp;
	} 
	return result;
}

/*
* 	Look for the next useful key of the format "[0-9]-[]"
*
* 	Input:
*pos:	Position where to start the look up.
*txt:	String in which the function should look for the key.
*
*	Return:
*The next key.
*/
function getNextKey(posi,txt)
{	
	var pos = posi;
	var found = false;
	var result = "";
	while (!found || pos== txt.length) {
		var lookFor = "'";
		var temp = "";

		if(txt.indexOf(lookFor,pos) > -1){
			pos = txt.indexOf(lookFor,pos) + lookFor.length;
			while(txt.charAt(pos) != "'" || pos== txt.length){
				temp += txt.charAt(pos);
				pos ++;
			}
			if(temp.indexOf("-") == 1){
				result = temp;
				found = true;
			}
			pos ++;
		}
		else {
			found = true;
		} 
	}
	return [result,pos];
}

/*
* 	Get the values out of the JSON text and create the associated session variables.
*
* 	Input:
*txt:	The JSON to transform into session variables.
*/
function copyToSession(txt)
{
	pos = 0;
	while (true) {
		keyArray = getNextKey(pos,txt);
		key = keyArray[0];
		if(key == "" || key == undefined){
			break;
		}
		pos = keyArray[1];
		val = getValueOf(key,txt);
		sessionStorage.setItem(key,val);
	}
}

/*
 * Method that verify if any session variable are set for the list of project and import it.
*/
function importAddMore(k,type) {
	var i = 0;
	if(type == ""){
		// Check the number of project forms
		var form_idx = parseInt(document.getElementById('id_form-TOTAL_FORMS').value);
	}
    else {
    	// Check the number of project forms
    	var form_idx = parseInt(document.getElementById('id_form_'+type+'-TOTAL_FORMS').value);
    	i = type.length + 1;
    }
    var form_num = k.charAt(10+i);
    if (k.charAt(11+i)!='-'){
      	form_num += k.charAt(11+i);
   	}
	form_num = parseInt(form_num);
   	// While the Id of the project is bigger that the 'TOTAL_FORMS' value
   	// creates additional forms.
   	while (form_idx <= form_num){
   		addMore(type);
   		form_idx += 1;
   	}
   	var field = document.getElementById(k.substring(2));
   	field.value = sessionStorage.getItem(k);
}

/*
* Save all the values for each project in the session Storage.
*/
function saveValues(step){
	if(step == 0){
		saveValue('id_0-grant', 0);
	}
	if(step == 1){
    	var form_idx = document.getElementById('id_form-TOTAL_FORMS').value;
		for(i=0; i<form_idx; i++){
			saveValue('id_form_'+i+'-project_title', 1);
			saveValue('id_form_'+i+'-funding_agency', 1);
			saveValue('id_form_'+i+'-starting_date', 1);
			saveValue('id_form_'+i+'-end_date', 1);
			saveValue('id_form_'+i+'-description', 1);
		}
	}
	if(step == 2){
		saveValue('id_2-pi', 2);
		saveValue('id_2-cpi', 2);
		saveValue('id_name_1', 2);
		saveValue('id_name_2', 2);
	}
	if(step == 3){
		var check = document.getElementById('id_3-task-0');
		var selected = '';
		var cI = 0;
		while(check!=undefined){
			cI++;
			selected += check.value+';';
			check = document.getElementById('id_3-task-'+cI);
		}
		sessionStorage.setItem('3-id_3-task',selected);
    	var form_idxP = document.getElementById('id_form_publi-TOTAL_FORMS').value;
		for(i=0; i<form_idxP; i++){
			saveValue('id_form_publi-'+i+'-name', 3);
			saveValue('id_form_publi-'+i+'-link', 3);
		}
	}
	if(step == 4){
    	var form_idx = document.getElementById('id_form-TOTAL_FORMS').value;
		for(i=1; i<form_idx; i++){
			saveValue('id_form-'+i+'-member', 4);
			saveValue('id_form-'+i+'-name', 4);
		}
	}
	if(step == 5){
		var deli_idx = document.getElementById('id_form_delivrable-TOTAL_FORMS').value;
		for(i=1; i<parseInt(deli_idx)+1; i++){
			saveValue('id_form_delivrable_'+i+'-date',5);
			saveValue('id_form_delivrable_'+i+'-description',5);
			saveValue('id_form_delivrable_'+i+'-cycle',5);
			saveValue('id_form_delivrable_'+i+'-storage',5);
			var hr_idx = document.getElementById('id_form_delivrable_'+i+'-HR-TOTAL_FORMS').value;
			for(j=0; j<hr_idx; j++){
				saveValue('id_form_delivrable_'+i+'-HR_'+j+'-member',5);
				saveValue('id_form_delivrable_'+i+'-HR_'+j+'-role',5);
				saveValue('id_form_delivrable_'+i+'-HR_'+j+'-pm',5);
				saveValue('id_form_delivrable_'+i+'-HR_'+j+'-description',5);
			}
		}
	}
	if(step == 6){
    	var form_idx = document.getElementById('id_form_delivrable-TOTAL_FORMS').value;
		for(i=0; i<form_idx; i++){
			saveValue('id_form_delivrable-'+i+'-cycle', 6);
			saveValue('id_form_delivrable-'+i+'-storage', 6);
		}
	}
}
	
/*
* Save the value in the session Storage.
*/
function saveValue(id,step){
	var doc = document.getElementById(id);
	var val = doc.value;
	var key = step + '-' + id;
	sessionStorage.setItem(key,val);
}


function loadSessionValues(){
	var step = document.getElementById('id_proposal_wizard-current_step').value;
	for (var k in sessionStorage){
		if (k.charAt(0)!=step){
			continue;
		}
    	if ((k.charAt(0)==step) && (k.indexOf("id_form-")==-1) && (k.indexOf("id_form_")==-1)) {
         	try{
        	 	var field = document.getElementById('id_' + k);
         		field.value = sessionStorage.getItem(k);
         	} catch(err) {
         	}
    	}
    	if (k.charAt(0)==step && k.indexOf("id_form-")>-1){
			try{
				importAddMore(k,"");
			} catch(err) {
         	}
		}
		if (k.charAt(0)==step && k.indexOf("id_form_")>-1){
			try{
				var pos = k.indexOf("id_form_") + 8;
				var type = "";
				while (k.charAt(pos) != '-'){
					type += k.charAt(pos);
					pos++;
				}
				importAddMore(k, type);
			} catch(err) {
         	}
		}
	}
}