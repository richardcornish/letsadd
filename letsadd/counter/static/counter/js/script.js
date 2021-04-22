var ajax = function (selector, url, csrf_token) {

    var form = document.querySelector(selector);

    form.addEventListener("submit", function (event) {

        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
        xhr.setRequestHeader("X-CSRFToken", csrf_token);
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        xhr.onreadystatechange = function () {

            // Success
            if (this.readyState === 4 && this.status === 200) {

                // Add click
                var ul = document.querySelector(".click-list");
                var li = document.createElement("li");
                var json = JSON.parse(this.response);
                var date = new Date(json.fields.timestamp);
                li.textContent = date.toISOString();
                ul.insertBefore(li, ul.firstChild);

                // Increment counter
                var length = document.querySelector(".click-list-length");
                var integer = parseInt(length.textContent, 10) + 1;
                length.textContent = integer.toString();
                var pluralize = document.querySelector(".click-list-length-pluralize");
                pluralize.textContent = (integer === 1 ? "" : "s");
            }

        };

        // Failure
        xhr.onerror = function () {
            var div = document.querySelector(".errors");
            div.innerHTML("<p>An error occurred. " + this.status + " " + this.statusText + "</p>");
        };

        // Send
        var data = new FormData(form);
        xhr.send(data);

        // Stop default submission
        event.preventDefault();

    }, false);

};
