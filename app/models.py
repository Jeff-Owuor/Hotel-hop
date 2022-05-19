
from . import db
from datetime import datetime

class Reviews(db.Model):
    
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer,primary_key = True)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    review = db.Column(db.Text())

    def save_review(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_review(self):
        db.session.delete(self)
        db.session.commit()

    # @classmethod
    # def get_reviews(cls,id):
    #     Reviews = Blogs.query.filter_by(user_id=id).all()
    #     return Blogs  
    
    def __repr__(self):
        return f'Review {self.review}'