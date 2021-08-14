from models import User, Post, db
from app import app

db.drop_all()
db.create_all()

# u1 = User(first_name="John", last_name="River")
# u2 = User(first_name="Bob", last_name="Jones")
# p1 = Post(title="Hey y'all", content="Down by the bay...", user_id="1")
# p2 = Post(title="Get ready", content="Run everyone", user_id="2")

# db.session.add(u1)
# db.session.add(u2)

# db.session.commit()

# db.session.add(p1)
# db.session.add(p2)

# db.session.commit()
