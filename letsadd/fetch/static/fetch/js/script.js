let ajax = function (input_selector, url, results_selector, error_selector) {

    let input = document.querySelector(input_selector);
    let results = document.querySelector(results_selector);
    let error = document.querySelector(error_selector);
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

    let render_results = (data, error) => {
        if (data.hasOwnProperty("object_list")) {
            error.innerHTML = "";
            if (data.object_list.length === 0) {
                results.innerHTML = `<p>${no_results}</p>`;
            } else {
                results.innerHTML = `<ul>${data.object_list.map(item => `<li><a href="${item.fields.get_absolute_url}">${item.fields.title}</a></li>`).join("")}</ul>`;
            }
        }
        if (data.hasOwnProperty("errors")) {
            results.innerHTML = "";
            Object.keys(data.errors).forEach((field) => {
                let selector = document.querySelector(".error-id_" + field);
                let lis = "";
                data.errors[field].forEach((error) => {
                    lis += `<li>${error}</li>`;
                });
                selector.innerHTML = `<ul>${lis}</ul>`;
            });
        }
    };

    input.addEventListener("keyup", (event) => {
        let params = new window.URLSearchParams();
        params.append(input.name, input.value);
        window.history.replaceState({}, "", `${location.pathname}?${params}`);
        get_results(`${url}?${params}`).then((data) => {
            render_results(data, error);
        });
    });

};
