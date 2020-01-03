from database import Database
import uuid
import datetime

class Post():
    def __init__(self,blog_id,title,content,author,date=datetime.datetime.today(),id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_data = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        print("post function callting save to db function")
        Database.insert(collection="posts",data=self.json())

    def json(self):
        print("json function called")
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title':self.title,
            'author':self.author,
            'created_data':self.created_data,
            'content':self.content
        }

    @staticmethod
    def from_mongo(id):
        print("from_mongo function called.Finding one entry in posts collection ")
        return Database.find_one(collection='posts',query={'id':id})

    @staticmethod
    def from_blog(id):
        print("Finding blog entry in posts collections")
        test = Database.find(collection="posts",query={'blog_id':id})
        for j in test:
            print(j)