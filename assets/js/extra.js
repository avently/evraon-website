/* 
* CONSTANTS
*/
const DEBUG = false
const API_URL = DEBUG ? "http://localhost:3000/api/v1" : "https://api.evraon.com/api/v1"

/* 
* INIT
*/
function initResetPassword() {
    const form = document.querySelector("#password_reset_form");
    const success = document.querySelector("#password_reset_success");
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        const email = form.elements.email.value
        resetPassword(email, function (error, response) {
            if (!error) {
                form.style.display = "none"
                success.style.display = "block"
            } else {
                alert$.next(error)
            }
        })
    });
}

function initChangePassword() {
    const token = findGetParameter("token")
    const form = document.querySelector("#password_change_form");
    const fail = document.querySelector("#password_change_error");
    const success = document.querySelector("#password_change_success");
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        const password = form.elements.password.value
        const password_confirm = form.elements.password_confirm.value
        if (password != password_confirm || !regExpForPassword.test(password)) {
            fail.style.display = "block"
            return
        }
        fail.style.display = "none"
        if (!token) {
            alert$.next("No token was specified. Click on a link from email")
            return
        }

        changePassword(password, token, function (error, response) {
            if (!error) {
                form.style.display = "none"
                success.style.display = "block"
            } else {
                alert$.next(error)
            }
        })
    });
}

/* 
* API
*/
function resetPassword(email, done) {
    const data = {
        email: email
    }
    var xhr = new XMLHttpRequest();
    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === this.DONE) {
            if (this.status < 300)
                done(null, this.responseText)
            else
                done(parseErrorMessage(this.responseText), null)
        }
    });
    xhr.open("DELETE", API_URL + "/accounts/password");
    xhr.setRequestHeader("content-type", "application/json");
    xhr.send(JSON.stringify(data));
}

function changePassword(password, token, done) {
    const data = {
        token: token,
        password: password
    }
    var xhr = new XMLHttpRequest();
    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === this.DONE) {
            if (this.status < 300)
                done(null, this.responseText)
            else
                done(parseErrorMessage(this.responseText), null)
        }
    });
    xhr.open("PUT", API_URL + "/accounts/password");
    xhr.setRequestHeader("content-type", "application/json");
    xhr.send(JSON.stringify(data));
}

/* 
* REGEXES
*/
const regExpForPassword = /^.{8,100}$/i;

/* 
* UTILS 
*/
function findGetParameter(parameterName) {
    var result = null,
        tmp = [];
    location.search
        .substr(1)
        .split("&")
        .forEach(function (item) {
            tmp = item.split("=");
            if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
        });
    return result;
}

function parseErrorMessage(responseText) {
    let json = {}
    try {
        json = JSON.parse(responseText)
    } catch (e) {
    }
    if (json.error && json.error.message)
        return json.error.message
    else
        return responseText
}
