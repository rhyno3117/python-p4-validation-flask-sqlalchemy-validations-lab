#!/usr/bin/env python3

from app import app
from models import db, Author, Post



if __name__ == '__main__':
    
    with app.app_context():
        # a1 = Author(name="Baran", phone_number = "00000")
        # db.session.add(a1)
        # db.session.commit()
        # a1 = Author(name="Tri", phone_number = "3032234567")
        # db.session.add(a2)
        # db.session.commit()
         
        import ipdb; ipdb.set_trace()
