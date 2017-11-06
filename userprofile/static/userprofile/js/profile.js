var profile = null;
var editProfile = null;
var body = null;

function showProfile() {

    body.appendChild(profile);
    body.removeChild(editProfile);
    document.getElementById("profile_title").innerHTML = "Din profil";
}

function showEditProfile() {

    body.appendChild(editProfile);
    body.removeChild(profile);
    document.getElementById("profile_title").innerHTML = "Rediger";

}

function initProfile() {

    profile = document.getElementById("profile");
    editProfile = document.getElementById("profile_edit");
    body = document.getElementById("profile_body");
    body.removeChild(editProfile);

}

window.onload = function() {

    initProfile();
    var val_error = document.getElementById("val_error").value;
    if(val_error !== "" || val_error.length !== 0) {
        showEditProfile();
    }
};