from database import Database
from posts import Post
import uuid
import datetime

class Blog():
    def __init__(self,author,title,description,id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        print("Creating a new post")
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter date in format DDMMYYY :")
        print("Calling Post class with collected inputs.")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.strptime(date,"%d%m%Y"))
        post.save_to_mongo()

    def get_posts(self):
        print("Get posts from post collections with blogid")
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        print("Save blogs data blogs collection")
        Database.insert(collection="blogs",data=self.json())

    def json(self):
        print("Calling json function for blog data.")
        return {'author':self.author,
                'title':self.title,
                'description':self.description,
                'id':self.id}

    @staticmethod
    def from_mongo(id):
        blog_data = Database.find_one(collection='blogs',query={'id':id})
        print("blogdata ==>",blog_data)
        return Blog(author=blog_data["author"],title=blog_data["title"],description=blog_data["description"],id=blog_data["id"])