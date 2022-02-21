const getPlaces = async () => (
  fetch('http://127.0.0.1:8000/contact/api/places?format=json')
    .then(response => response.json())
    .then(data => data)
);

async function initMap() {
  const places = await getPlaces();
  const placeInfo = document.querySelector('.place-info');
  const warsaw = {lat: 52.237049, lng: 21.017532};
  const map = new google.maps.Map(document.getElementById('map'), {
    zoom: 5,
    center: warsaw,
  });

  placeInfo.innerHTML = `
          <h2>${places[0]['street']}</h2>
          <h3>${places[0]['zip_code']} ${places[0]['city']}, ${places[0]['country']}</h3>
          `;

  places.forEach(place => {
    const marker = new google.maps.Marker({
        position: {
          lat: parseFloat(place.latitude),
          lng: parseFloat(place.longitude)
        },
        map: map,
      }
    );

    marker.addListener('click', () => {
      map.setZoom(12);
      map.setCenter({
        lat: parseFloat(place.latitude),
        lng: parseFloat(place.longitude)
      });

      placeInfo.innerHTML = `
          <h2>${place['street']}</h2>
          <h3>${place['zip_code']} ${place['city']}, ${place['country']}</h3>
            `;
    });
  });
}
