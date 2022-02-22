def process_geocoder_data(g):
    try:
        address = g.json["raw"]["address"]
        latitude = g.json["raw"]["lat"]
        longitude = g.json["raw"]["lon"]
    except TypeError:
        return False

    try:
        street = address["street"]
    except KeyError:
        try:
            street = address["road"]
        except KeyError:
            street = ""
    else:
        try:
            street += f" {address['house_number']}"
        except KeyError:
            pass

    try:
        city = address["city"]
    except KeyError:
        try:
            city = address["county"]
        except KeyError:
            city = ""

    try:
        zip_code = address["postcode"]
    except KeyError:
        zip_code = ""

    try:
        country = address["country"]
    except KeyError:
        country = ""

    return {
        "latitude": latitude,
        "longitude": longitude,
        "street": street,
        "city": city,
        "zip_code": zip_code,
        "country": country,
    }
