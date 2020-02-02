// $(function(){
    var startTime = new Date("Feb 27, 2020 10:00:00").getTime();
    var endTime = new Date("Feb 27, 2020 16:00:00").getTime();
    var eventName = "O'Day";
    // Pass in the starting time and ending time of the event.
    // Update the count down every 1 second
    var x = setInterval(function() {
        // alert("hi");

        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distanceToStart = startTime - now;
        var distanceToEnd = endTime - now;
        var target = null;
        

        if (distanceToEnd <= 0) {
            clearInterval(x);
            document.getElementById("countdown-widget").innerHTML = "";
            return;
        }
        else if (distanceToStart <= 0) {
            document.getElementById("countdown-text").innerHTML = "Event in progress:";
            target = distanceToEnd;
        } else {
            document.getElementById("countdown-text").innerHTML = "Countdown to next event:";
            target = distanceToStart;
        }
        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(target / (1000 * 60 * 60 * 24));
        var hours = Math.floor((target % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((target % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((target % (1000 * 60)) / 1000);

        // Display the result in the element with id="demo"
        document.getElementById("countdown-timer").innerHTML = days + "  :  " + ("0" + hours).slice(-2) + "  :  "
        + ("0" + minutes).slice(-2) + "  :  " + ("0" + seconds).slice(-2);

    }, 1000);
// });