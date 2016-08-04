
function submit_clicked(event) {
  console.log("Clicked!!");
  event.preventDefault();
  var content = $('select').val(); //.val allows you to
  $.post(
    "post_1",
    select, //This is the answer that you get from the user
    handle_response  //This function is only called when you recieve a response
    // "this is the content"
  );
}

function handle_response(data) {
  console.log(data);              //This lets the server post information on the console as well.
  $('#result').text(data);
  $('#result').show();
}


function associate_events() {
  $('#submit').click(submit_clicked);
}

$(document).ready(associate_events);
