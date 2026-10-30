from datetime import datetime
from .extensions import db

class category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    products =db.relationship("Product", back_populates="category")
    
    def __repr__(self):
        return f"<Category {self.name}>"
    
class Supplier (db.Model):
    __tablename__ = 'suppliers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    contact_info = db.Column(db.String(255), nullable=True)
    
    products = db.relationship("Product", back_populates="supplier")
    
    def __repr__(self):
        return f"<Supplier {self.name}>"

class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(80), unique=True, nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    expiration_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)