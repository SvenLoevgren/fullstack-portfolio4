$(document).ready(function() {
    $("form").submit(function(e) {
      e.preventDefault();
      $.ajax({
        type: "POST",
        url: "/booking/",
        data: $(this).serialize(),
        success: function(data) {
          if (data["success"]) {
            // Display confirmation message in a pop-up dialog
            alert("Booking confirmed!");
            // Redirect to the home page
            window.location.replace("{% url 'fastfood_home' %}");
          } else {
            alert("Booking failed!");
          }
        },
        error: function(data) {
          alert("An error occurred while processing your request.");
        }
      });
    });
  });
  