from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

engine = create_engine("mysql+pymysql://root:12345678@localhost:3306/news") #connect
Base = declarative_base()          #declare the base

Session = sessionmaker(bind  = engine)

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key = True)
    title = Column(String(200), nullable = False)
    created_at = Column(DateTime)
    is_valid = Column(Boolean, default= True)

class OrmTest(object):

    def __init__(self):
        self.session = Session()

    def add_one(self):
        new_obj = News(
            title = 'today',
        )
        new_obj2 = News(
            title = 'yesterday'
        )
        self.session.add_all([new_obj, new_obj2])
        self.session.commit()
        return new_obj

    def get_one(self):
        '''查询一条数据query one piece of data'''
        return self.session.query(News).get(4)

    def get_more(self):
        '''查询多条数据query many pieces of data'''
        return self.session.query(News).filter_by(is_valid = True)

    def update_data(self, pk):
        '''更新单条数据update one piece of data'''
        obj = self.session.query(News).get(pk)

        if obj:
            obj.is_valid = 0
            self.session.add(obj)
            self.session.commit()
            return True
        return False

    def update_many_data(self):
        '''更新多条数据 update many pieces of data'''
        data_list = self.session.query(News).filter_by(is_valid=None)
        for item in data_list:
            item.is_valid = 1
            self.session.add(item)
        self.session.commit()

    def delete(self):
        '''删除数据delete one piece of data'''
        data = self.session.query(News).get(5)
        self.session.delete(data)
        self.session.commit()
        #删除多条数据与更新类似都用到循环，注意commit!
        #delete many pieces of data is same as the usage of update. Both of them need circle. Don't forget commit!

def main():
    obj = OrmTest()
    #rest = obj.get_one()
    #if rest:
    #  print('ID: {0} => {1}'.format(rest.id, rest.title))
    #else:
    #    print('Not exist.')
    #obj.add_one()
    #rest = obj.get_more()
    #print(rest.count())

    obj.update_many_data()

if __name__ == '__main__':
    main()
