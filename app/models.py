from app import db
import sqlalchemy.orm as so
import sqlalchemy as sa
from datetime import datetime, timezone

class Event(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, nullable = False)
    location: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)
    event_date: so.Mapped[datetime] = so.mapped_column(sa.DATE, nullable=False, default=lambda: datetime.now(timezone.utc))
    ticket_price: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)
    capacity: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    catering_ind: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)
    catering: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=True)  #Comma-separated choices, e.g: "sot_drinks,meals"
    attachment_filename: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=True)

    __table_args__ = (db.UniqueConstraint("title", "location", "event_date"),)

"""
flask shell
from app import db       - First time only
[db.drop_all()]          - To clear database
db.create_all()          - Every time you update models.py
exit()
"""


