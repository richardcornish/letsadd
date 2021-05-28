var ajax = function (input_selector, url, results_selector, error_selector) {

    var input = document.querySelector(input_selector);
    var results = document.querySelector(results_selector);
    var error = document.querySelector(error_selector);
    var no_results = 'No results.'

    var get_results = async (url) => {
        var response = await fetch(url, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest'
            }
        });
        return await response.json();
    };

    var render_results = (data, error) => {
        if (data.hasOwnProperty('object_list')) {
            error.innerHTML = '';
            if (data.object_list.length === 0) {
                results.innerHTML = `<p>${no_results}</p>`;
            } else {
                results.innerHTML = `<ul>${data.object_list.map(item => `<li><a href="${item.fields.get_absolute_url}">${item.fields.title}</a></li>`).join('')}</ul>`;
            }
        } else if (data.hasOwnProperty('errors')) {
            results.innerHTML = '';
            for (var field in data.errors) {
                var selector = document.querySelector('.error-id_' + field);
                let lis = '';
                for (var error of data.errors[field]) {
                    lis += `<li>${error}</li>`;
                }
                selector.innerHTML = `<ul>${lis}</ul>`;
            }
        };
    };

    input.addEventListener('keyup', (event) => {
        var params = new URLSearchParams();
        params.append(input.name, input.value);
        window.history.replaceState({}, '', `${location.pathname}?${params}`);
        get_results(`${url}?${params}`).then(data => {
            render_results(data, error);
        });
    });

};
