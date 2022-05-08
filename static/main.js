//When the app is loaded. Click once onto the URL input field, to visualize the interactive part for the user.
$( document ).ready(function() {
  $('#s-input-field').trigger("click");
});

//Action-Listener. If something has been entered in the URL_input box, than return a prediction "malicious" or "not".
$('#s-input-field').keyup(function(){
  //store user-input
  let url_str = $('#s-input-field').val();

  //if the given url is long enough. A classification is useless in this is not the case.
  if(url_str.length<3){
    //Show placeholder text that indicates the user, that a valid url has to be typed in
    $(".results_placeholder").css("display", "block");
    $(".results").css("display", "none");
  }
  if(url_str.length>=3){ //if the url is long enough to justify a classification.
    //JSON-ify URL_String for AJAX-Call
    let url_data = {
      "url": url_str
    };

    //show loading_icon
    $('.lds-ring').css("visibility", "visible");
    //AJAX Call to Flask-API to get the ml-prediction and it's confidence.
    $.ajax({
      url: "/prediction",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify(url_data),
      dataType: 'json',
      success: function(data){
        //hide loading_ring
        $('.lds-ring').css("visibility", "hidden");
        let result_str = "";
        
        //Classified as normal URL
        if(data["prediction"] == "1"){
          result_str = 'secure';
        }
        else if(data["prediction"] == "0"){ //classified as malicious URL
          result_str = "malicious";
        }

        //Output classification in result_area
        $(".results_placeholder").css("display", "none");
        $(".results").css("display", "block");
        $('#result_area').html(result_str);

        //Output classification probability  
        let prob_str = parseFloat(data["probability_malicious"]) >= parseFloat(data["probability_normal"]) ? data["probability_malicious"] : data["probability_normal"];
        $('#result_prob').html(prob_str);
      },
      error: function(request,status, message) {
        //Debugging. Unused in production
        //console.log(request);
        //console.log(message);
        }
    });
  }
});