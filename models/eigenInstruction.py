import pymysql
import numpy as np
from datetime import datetime
from numpy import linalg as LA
from models.request import Request


class EigenInstruction:
    def __init__(self):
        pass

    def database_connection(self):
        """
        :return db: connection
        """
        try:
            db = pymysql.connect("localhost", "root", "vuhuynh9x", "db_app")
            return db
        except:
            print("connect database is fail!")

    def load_data(self, arr):
        """
        clear table and insert new data
        :param arr: array
        """
        db = self.database_connection()
        cursor = db.cursor()
        clear_table = 'TRUNCATE db_app.links_pages'
        cursor.execute(clear_table)
        db.commit()
        query = 'INSERT INTO db_app.links_pages(ID,User_ID,Page_Path,Referral_Path,Time)' \
                'VALUES (NULL,%s,%s,%s,%s)'
        for i in arr:
            cursor.execute(query, (i['User_ID'], i['Page_Path'], i['Referral_Path'], i['Time']))
        db.commit()

    def list_page_path(self, user_id, t1, t2):
        """
        :param user_id: user id
        :param t1: start time
               t2: end time
        :return lst: list of links in Page Path but not duplicate
        """
        db = self.database_connection()
        cursor = db.cursor()
        distinct_page_path = "SELECT DISTINCT Page_Path FROM db_app.links_pages WHERE " \
                             "User_ID = %s and Time >= %s and Time <= %s "
        cursor.execute(distinct_page_path, (user_id, t1, t2))
        page_paths = []
        try:
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                page_paths.append(row[0])
        except:
            print("Error: unable to fetch data")
        return page_paths

    def link_matrix(self, user_id, t1, t2):
        """
        :param user_id: user id
        :param t1: start time
               t2: end time
        :return A: link matrix
        """
        page_paths = self.list_page_path(user_id, t1, t2)
        cursor = self.database_connection().cursor()
        leng = len(page_paths)
        matrix = np.zeros((leng, leng))
        for i in range(0, leng):
            select_by_page_path = "SELECT Referral_Path FROM links_pages WHERE " \
                                  "User_ID = %s and Page_Path = %s and " \
                                  "Time >= %s and Time <= %s "
            cursor.execute(select_by_page_path, (user_id, page_paths[i], t1, t2))
            results = cursor.fetchall()
            for row in results:
                matrix[i, page_paths.index(row[0])] = 1 / len(results)
        self.database_connection().close()
        return matrix.T

    def compute_eigen(self, matrix):
        """
        :param: a square matrix
        :return: w: Eigenvalues
                 v: Eigenvectors
        """
        w, v = LA.eig(matrix)
        return w, v

    def get_eigen(self, request_obj: Request):
        """
        :param request_obj: object of request
        :return: w: Eigenvalues
                 v: Eigenvectors
        """
        w, v = self.compute_eigen(self.link_matrix(request_obj.user_id, request_obj.t1, request_obj.t2))
        return w, v
