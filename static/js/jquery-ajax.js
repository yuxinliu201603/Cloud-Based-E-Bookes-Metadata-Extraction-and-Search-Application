
$.ajax({
        url: 'https://inf551project-c1290.firebaseio',
        dataType: 'json',
        complete: function(data){
			var json = JSON.toString(data);
            alert(json)
        },
        success: function(json){
            alert(json)
        }


