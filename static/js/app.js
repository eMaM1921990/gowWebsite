/**
 * Created by emam on 23/07/16.
 */
function updateFeeds(){
        $.ajax({
		url : "/remove_areas/",
		type : "POST",
		dataType : "text",
        data:{
          id:areaId,
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value

        },

		success : function(responseText) {
            removeRow(rowId);
            alert(responseText);
		},
		error : function(xhr, errmsg, err) {
			console.log(errmsg);

		}
	});


}