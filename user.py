from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

user_roles = db.Table(
    'user_roles',
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key = True),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
    
)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column (db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column (db.String(255), nullable=False)
    is_active_flag = db.Column (db.Boolean, default=True, nullable=False)
    created_at = db.Column (db.DateTime, default=datetime.utcnow, nullable = False)
    
    roles = db.relationship("Role", secondary=user_roles, back_populates="users")
    
    def set_password (self, raw):
        self.password_hash = generate_password_hash(raw)
    
    def check_password(self, raw):
        return check_password_hash(self.password_hash, raw)
    
    def has_permission(self, code):
        __tablename__ = "roles"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), unique=True, nullable=False)
        users = db.relationship ("User", secondary=user_roles, back_populates="roles")
        
        permissions = db.relationship("Permission", secondary="role_permissions", back_populates="roles")
        
    class Permission(db.Model):
        __tablename__ = "permissions"
        id = db.Column (db.Integer, primary_key=True)
        code = db.Column (db.String(80), unique=True, nullable=False)
        description = db.Column (db.String(255), nullable=True)
        roles = db.relationship ("Role", secondary="role_permissions", back_populates="permissions")
        
    role_permissions = db.Table(
        "role_permissions",
        db.Column("role_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
        db.Column("permission_id", db.Integer, db.ForeignKey("permissions.id"), primary_key=True),
        
    )