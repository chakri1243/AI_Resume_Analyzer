from database import db


class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(300),
        nullable=False
    )


class ResumeReport(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer
    )

    filename = db.Column(
        db.String(300)
    )

    filepath = db.Column(
        db.String(500)
    )
    ats_score = db.Column(
        db.Integer
    )

    match_score = db.Column(
        db.Integer
    )

    date = db.Column(
        db.String(100)
    )
class WebsiteVisit(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    ip_address = db.Column(
        db.String(100)
    )

    user_agent = db.Column(
        db.String(500)
    )

    date = db.Column(
        db.String(100)
    )