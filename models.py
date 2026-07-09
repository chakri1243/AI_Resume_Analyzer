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

    ats_score = db.Column(
        db.Integer
    )

    match_score = db.Column(
        db.Integer
    )

    date = db.Column(
        db.String(100)
    )