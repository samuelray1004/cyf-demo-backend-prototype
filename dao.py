from db import db, Property

def get_all_properties():
    return [p.serialize() for p in Property.query.all()]

def create_property(street1, street2, street_number, city, state,
                    zip_code, description):
    new_property = Property(stree1=street1, street2=street2,
                            street_number=street_number, city=city, state=state,
                            zip_code=zip_code, description=description)
    db.session.add(new_property)
    db.session.commit()
    return new_property.serialize()

def get_property_by_id(property_id):
    property = Property.query.filter_by(id=property_id).first()
    if property is None:
        return None
    return property.serialize()

def update_property_by_id(property_id, body):
    property = Property.query.filter_by(id=property_id).first()
    if property is None:
        return None
    property.street1 = body.get("street1", property.street1)
    property.street2 = body.get("street2", property.street2)
    property.street_number = body.get("streetNumber", property.street_number)
    property.city = body.get("city", property.city)
    property.state = body.get("state", property.state)
    property.zip_code = body.get("zipCode", property.zip_code)
    property.description = body.get("description", property.description)
    db.session.commit()
    return property.serialize()

def delete_property_by_id(property_id):
    property = Property.query.filter_by(id=property_id).first()
    if property is None:
        return None

    db.session.delete(property)
    db.session.commit()
    return property.serialize()
