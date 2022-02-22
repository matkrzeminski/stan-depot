const getPlaces = async () => (
  fetch('http://127.0.0.1:8000/contact/api/places?format=json')
    .then(response => response.json())
    .then(data => data)
    .catch(error => [{
      "id":0,
      'street': 'Złota 59',
      'zip_code': '00-120',
      'city': 'Warszawa',
      'country': 'Polska',
      'latitude': '52.2302445',
      'longitude': '21.0039142'
    }])
);

async function initMap() {
  const places = await getPlaces();
  const placeInfo = document.querySelector('.place-info');
  const warsaw = {lat: 52.237049, lng: 21.017532};
  const map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: warsaw,
    minZoom: 3,

  });

  placeInfo.firstElementChild.textContent = `${places[0]['street']}`;
  placeInfo.lastElementChild.textContent = `${places[0]['zip_code']} ${places[0]['city']}, ${places[0]['country']}`;


  places.forEach(place => {
    if (place.latitude === "" || place.longitude === "") return
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

      placeInfo.firstElementChild.textContent = `${place['street']}`;
      placeInfo.lastElementChild.textContent = `${place['zip_code']} ${place['city']}, ${place['country']}`;
    });
  });
}
