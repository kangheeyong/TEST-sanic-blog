from myblog.database import db_session, init_db, drop_db
from myblog.models import Post, User


drop_db()
init_db()
user = User(username='user', email='user@blog.com', password='password')
db_session.add(user)
db_session.commit()
post1 = Post(title='첫 번째 게시물', content='첫 번째 게시물 내용', author=user)
post2 = Post(title='두 번째 게시물', content='두 번째 게시물 내용', author=user)
db_session.add(post1)
db_session.add(post2)
db_session.commit()

