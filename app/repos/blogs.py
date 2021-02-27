#!/usr/bin/python
# -*- coding: utf-8 -*-
import app.helpers.dbclient as db
import json

class Blogs:

    """blogs repository"""

    def __init__(self):
        super().__init__()
        self.db = db.Dbclient()
        print(self.db)

    def __str__(self):
        return super().__str__('blogs_class')

    def get_all_blogs(self):
        qry = """
            SELECT * FROM blogs
                """
        res = self.db.fetch(qry)
        return res.to_json(orient='records', indent=4)

    def get_one_blog(self, data):
        qry = \
            """
        SELECT * FROM blogs where id = %s
        """ \
            % data['id']
        res = self.db.fetch(qry)
        return res.to_json(orient='records', indent=4)

    def get_one_blog(self, data):
        qry = \
            """
        SELECT * FROM blogs where id = %s
        """ \
            % data['id']
        res = self.db.fetch(qry)
        return res.to_json(orient='records', indent=4)

    def add_blog(self, data):
        _res = {}
        user_id = data['userId']
        title = data['title']
        subtitle = data['subtitle']
        body = data['body']
        img = data['img']
        published = data['published']
        createdAt = data['createdAt']

        updatedAt = data['updatedAt']

        qry = \
            """
        INSERT INTO blogs(user_id, title, subtitle, body, img, published, createdAt, updatedAt)\
        values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s") 
        """ \
            % (user_id, title, subtitle, body, img, published, createdAt, updatedAt)
        res = self.db.execute(qry)

        if res == True:

            _res['status'] = 'Success'
        else:
            _res['status'] = 'Failed'
            raise EOFError('record not added')
        return json.dumps(_res)
