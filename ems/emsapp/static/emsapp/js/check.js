$(document).ready(function() {
	console.log('load check.js ok');
});

function blankCheck(id) {
  if($('#'+id).val() == null) {
 	console.log('blank');
  } else {
	console.log('not blank '+$('#'+id).val()+' finish');
  }
}

