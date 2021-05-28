let ajax = (input_selector, url, results_selector, error_selector) => {

    let input = document.querySelector(input_selector);
    let results = document.querySelector(results_selector);
    let errors = document.querySelector(error_selector);
    let no_results = "No results.";

    let get_results = async (url) => {
        let response = await fetch(url, {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest"
            }
        });
        return response.json();
    };

    let render_results = (data, errors) => {
        if (data.hasOwnProperty("object_list")) {
            errors.innerHTML = "";
            if (data.object_list.length === 0) {
                results.innerHTML = `<p>${no_results}</p>`;
            } else {
                results.innerHTML = `<ul>${data.object_list.map(obj => `<li><a href="${obj.fields.get_absolute_url}">${obj.fields.title}</a></li>`).join("")}</ul>`;
            }
        }
        if (data.hasOwnProperty("errors")) {
            results.innerHTML = "";
            Object.keys(data.errors).forEach((field) => {
                let errors_field = document.querySelector(".errors-id_" + field);
                errors_field.innerHTML = `<ul>${data.errors[field].map(error => `<li>${error}</li>`).join("")}</ul>`;
            });
        }
    };

    input.addEventListener("keyup", (event) => {
        let params = new window.URLSearchParams();
        params.append(input.name, input.value);
        window.history.replaceState({}, "", `${location.pathname}?${params}`);
        get_results(`${url}?${params}`).then((data) => {
            render_results(data, errors);
        });
    });

};
