function sendMail(contactForm) {
    emailjs.send("service_dhbb9pk", "template_6e1jo6f", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.projectsummary.value

    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            alert("Thanks... your Job offer has been sent. I will get back to you soon!");
        },
        function(error) {
            console.log("FAILED", error);
            alert("There was an error sending your Job offer. Please try again later.");
        }
    );
    return false;  // To block from loading a new page
}