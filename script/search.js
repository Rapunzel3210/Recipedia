// function submit_clicked(event) {
//   console.log("Clicked!!");
//   event.preventDefault();
//   var data = {};
//   var content = $('select').val(); //.val allows you to
//   console.log (content)
//   handle_response(content)
  // $.post(  This is sending
  //   "recipe_results",
  //   content, //This is the answer that you get from the user (data)
  //   handle_response  //This function is only called when you recieve a response, it will handle the response
  //   // "this is the content"
  // );
// }
//
// function handle_response(data) { This is recieving
//   console.log(data);              //This lets the server post information on the console as well.
//   $('#result').html(data);
//   $('#result').show();
// }
//
//
// function associate_events() {
//   $('#submit').click(submit_clicked);
// }
//
// $(document).ready(associate_events);

// Send a dictionary

// JSON.stringify(dictionary)
// IN Python from a string to a dictionary first I have to import json then to json.loads(self.request.body)
// import json
// self.response.headers['Content-Type']
//  = "application/json"
// self.response.write(json.dumps(my dict))
