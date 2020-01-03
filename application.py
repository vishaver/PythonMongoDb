from database import Database
from blogs import Blog
from menu import Menu

Database.initilize()

# post1 = Post(blog_id="1",title="My post",author="vishal",content="Hello this is vishal")
# post1.save_to_mongo()

# test = Post.from_mongo("1cb8cd70797d41298f6f7fcbb0c87c31")
# print(test)

# blog = Blog(author="vishal verma",title="Python blog4",description="Learn python zero to hero.4")
# blog.new_post()
# blog.save_to_mongo()
#
# #from_database = Blog.get_from_mongo(blog.id)
# print(blog.get_posts())

menu = Menu()
menu.run_menu()
