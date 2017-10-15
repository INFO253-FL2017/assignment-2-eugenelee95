function write_comment(blogname) {
    var name = document.getElementsByName("name")[0].value;
    var message = document.getElementsByName("message")[0].value;
    if (message != "" && name != "") {
        document.getElementById("comments").innerHTML += name + ": " + message + "<br>"
        localStorage.setItem(blogname, document.getElementById("comments").innerHTML);
    }
    return false
}

function contact_us() {
    var name = document.getElementsByName("name")[0].value;
    var subject = document.getElementsByName("subject")[0].value;
    var message = document.getElementsByName("message")[0].value;

    var response = "";
    if (name === "") {
        response = response.concat("name, ");
    }
    if (subject === "") {
        response = response + "subject, ";
    }
    if (message === "") {
        response = response + "message, ";
    }
    if (response != "") {
        document.getElementById("response").innerHTML = "Please fill in the following fields: " + response.slice(0, -2);
        return false;
    } else {
        return true;
    }
}