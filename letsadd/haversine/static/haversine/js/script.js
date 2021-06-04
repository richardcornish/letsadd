var render_map = function (selector, point_array, obj, icon) {
    var map_div = document.querySelector(selector);
    var options = {
        center: {
            lat: 39.833333,
            lng: -98.583333,
        },
        zoom: 4,
        streetViewControl: false,
        fullscreenControl: false,
        mapTypeId: google.maps.MapTypeId.TERRAIN
    }
    var map = new google.maps.Map(map_div, options);
    var bounds = new google.maps.LatLngBounds();
    if (obj !== undefined) {
        new google.maps.Marker({
            position: new google.maps.LatLng(obj.point),
            icon: {
                url: icon
            },
            map: map
        });
        var circle = new google.maps.Circle({
            center: obj.point,
            radius: obj.radius * 1609.344,  // meters
            fillColor: 'green',
            fillOpacity: 0.15,
            strokeColor: 'forestgreen',
            strokeOpacity: 0.5,
            strokeWeight: 2
        });
        circle.setMap(map);
        circle.addListener('click', () => {
            close_info_window();
        });
        bounds = circle.getBounds();
    }
    var info_window;
    var close_info_window = () => {
        if (info_window) {
            info_window.close();
        }
    }
    map.addListener('click', () => {
        close_info_window();
    });
    point_array.map(obj => {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(obj.point),
            map: map
        });
        marker.addListener('click', () => {
            close_info_window();
            info_window = new google.maps.InfoWindow({
                content: `<a href="${obj.url}">${obj.name}</a>`
            });
            if (obj.hasOwnProperty('distance')) {
                info_window.setContent(info_window.getContent() + `<br>${obj.distance} away`);
            }
            info_window.open(map, marker);
        });
        bounds.extend(marker.getPosition());
    });
    if (point_array.length > 1) {
        map.fitBounds(bounds);
    } else {
        map.setCenter(point_array[0].point);
        map.setZoom(7);
    }
}
