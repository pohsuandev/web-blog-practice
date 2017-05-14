import uuid
from src.common.database import Database
import datetime

class Post(object):

    def __init__(self, blog_id, content, author, created_date=datetime.datetime.utcnow(), _id=None):#如果沒有給值，就會是default，並且有預設值的參數要放在沒有預設值的後面
        self.blog_id = blog_id # 辨識blog是誰的
        self.title = _id
        self.content = content
        self.author = author
        self.created_date = created_date
        # self.id = id #辨識post
        self._id = uuid.uuid4().hex if _id is None else _id
        #4產生random id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self): #回傳建立blog的資訊，為了存入資料庫
        return{
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }
    @classmethod
    def from_mongo(cls, id):
        #找blog中的其中一篇post
        #post.from_mongo('123')
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
        #讓回傳結果是list
        #找blog中的所有post

