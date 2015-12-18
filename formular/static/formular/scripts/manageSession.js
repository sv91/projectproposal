/*
*  Set of scripts used to manage the Session Variables from the "Formular" app.
*/


/*	
*	Delete everything linked to the specified field.
*	
*	Input:
*		field: 	Name of the field to delete.
*		prefix:	Part of the field name preceding the number of the field.
*
*/
function deleteField(field, prefix)
{
	var i;
	for(i in link){
		if(link[i][0] == field){
			deleteField(link[i][1],link[i][2])
		}
	}
	
}