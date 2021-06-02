var render_map = function (selector) {
    map = new google.maps.Map(document.querySelector(selector), {
        center: {
            lat: 39.83333,
            lng: -98.58333
        },
        zoom: 4,
    });
}
