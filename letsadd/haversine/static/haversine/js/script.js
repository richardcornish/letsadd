let opts = {
    center: {
        lat: 39.833333,
        lng: -98.583333
    },
    fullscreenControl: false,
    mapTypeId: google.maps.MapTypeId.TERRAIN,
    streetViewControl: false,
    zoom: 7
};

const meters_in = {
    km: 1000,  // meters
    mi: 1609.344  // meters
};

let park_detail = function (selector, object) {
    let mapDiv = document.querySelector(selector);
    opts.center = {
        lat: object.latitude,
        lng: object.longitude
    };
    let _map = new google.maps.Map(mapDiv, opts);
    new google.maps.Marker({
        map: _map,
        position: {
            lat: object.latitude,
            lng: object.longitude
        }
    });
};

let park_list = function (selector, object_array, point, radius, units, path) {
    let mapDiv = document.querySelector(selector);
    let _map = new google.maps.Map(mapDiv, opts);
    let bounds = new google.maps.LatLngBounds();
    let info = new google.maps.InfoWindow();
    object_array.forEach(function (obj) {
        let marker = new google.maps.Marker({
            map: _map,
            position: {
                lat: obj.latitude,
                lng: obj.longitude
            }
        });
        marker.addListener("click", function () {
            if (info) {
                info.close();
            }
            info.setContent(`<a href="${obj.get_absolute_url}">${obj.name}</a>`);
            if (obj.hasOwnProperty("distance") && units !== undefined) {
                info.setContent(info.getContent() + `<br>${obj.distance} ${units}`);
            }
            info.open(_map, marker);
        });
        bounds.extend(marker.getPosition());
        _map.fitBounds(bounds);
    });
    if (point !== undefined) {
        let _center = {
            lat: point.latitude,
            lng: point.longitude
        };
        _map.setCenter(_center);
        let marker = new google.maps.Marker({
            map: _map,
            position: _center
        });
        if (path !== undefined) {
            marker.setIcon({
                scaledSize: new google.maps.Size(27, 43),
                url: path
            });
        }
        marker.addListener("click", function () {
            if (info) {
                info.close();
            }
            info.setContent(`${point.formatted_address}`);
            info.open(_map, marker);
        });
        let circle = new google.maps.Circle({
            center: _center,
            fillColor: "orange",
            fillOpacity: 0.15,
            map: _map,
            strokeColor: "orange",
            strokeOpacity: 0.5,
            strokeWeight: 5
        });
        if (radius !== undefined && units !== undefined) {
            circle.setRadius(radius * meters_in[units]);
        }
        bounds = circle.getBounds();
        _map.fitBounds(bounds);
    }
};
