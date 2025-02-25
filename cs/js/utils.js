// Move to the URL
function load_page(url) {
    window.location.href=url
}

// Retrieve a cookie name
function get_cookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
        c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
        }
    }
    return "";
}

function get_timestamp() {
    var date = new Date();

    // getMonth() returns 0-11
    var month = (date.getMonth()+1);

    // getDate() returns the day of the month for some reason
    var day = date.getDate();

    // getFullYear() returns the current year
    var year = date.getFullYear()

    // getHours() returns 0-23
    // Add a zero if hours is less than 10 to maintain two digits
    var hours = (date.getHours() < 10 ? '0' : '') + date.getHours()

    // getMinutes() returns 0-59
    // Add a zero if minutes is less than 10 to maintain two digits
    var minutes = (date.getMinutes() < 10 ? '0' : '') + date.getMinutes()

    // getSeconds() returns 0-59
    // Add a zero if seconds is less than 10 to maintain two digits
    var seconds = (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()

    var timestamp = month + "-" + day + "-" + year + " " + hours + ":" + minutes + ":" + seconds;
    return timestamp
}