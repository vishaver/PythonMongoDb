from database import Database
from blogs import Blog


class Menu():
    def __init__(self):
        self.user = input("Enter author name: ")
        self.user_blog = None
        if self.user_has_account():
            print("welcome back {}".format(self.user))
        else:
            self.prompt_user_for_account()

    def user_has_account(self):
        blog = Database.find_one(collection='blogs',query={'author':self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False
    def prompt_user_for_account(self):
        title = input("Enter title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog
    def run_menu(self):
        read_or_write = input("What you want to do? R for read and W for write.")
        if read_or_write == "R":
            self.listall()
            self.viewpost()
        elif read_or_write == "W":
            self.user_blog.new_post()
        else:
            print("Thanks for visiting")

    def listall(self):
        test = Database.find(collection="blogs",query={})
        for k in test:
            print(k)

    def viewpost(self):
        blog_to_see = input("Enter the blog id which you want to see: ")
        hhoi = Blog.from_mongo(blog_to_see)
        hhoi.get_posts()







