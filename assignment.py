import pymysql
import numpy as np
from datetime import datetime
from numpy import linalg as LA


def database_connection():
    """
    :return db: connection
    """
    try:
        db = pymysql.connect("localhost", "root", "vuhuynh9x", "db_app")
        return db
    except:
        print("connect database is fail!")


def list_page_path(t1, t2):
    """
    :param t1: start time
           t2: end time
    :return lst: list of links in Page Path but not duplicate
    """
    db = database_connection()
    cursor = db.cursor()
    distinct_page_path = "SELECT DISTINCT Page_Path FROM db_app.links_pages WHERE Time >= %s and " \
                         "Time <= %s"
    cursor.execute(distinct_page_path, (t1, t2))
    page_paths = []
    try:
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            page_paths.append(row[0])
    except:
        print("Error: unable to fetch data")
    return page_paths


def link_matrix(t1, t2):
    """
    :param t1: start time
           t2: end time
    :return A: link matrix
    """
    page_paths = list_page_path(t1, t2)
    cursor = database_connection().cursor()
    leng = len(page_paths)
    matrix = np.zeros((leng, leng))
    for i in range(0, leng):
        select_by_page_path = "SELECT Referral_Path FROM links_pages WHERE Page_Path = %s and " \
                              "Time >= %s and Time <= %s"
        cursor.execute(select_by_page_path, (page_paths[i], t1, t2))
        results = cursor.fetchall()
        for row in results:
            matrix[i, page_paths.index(row[0])] = 1 / len(results)
    database_connection().close()
    return matrix.T


def eigenvalues_eigenvectors(matrix):
    """
    :param matrix: a square matrix
    :return: w: Eigenvalues
             v: Eigenvectors
    """
    w, v = LA.eig(matrix)
    return w, v


def display():
    """
    display Link Matrix, Eigenvalues, Eigenvectors from t1 to t2
    """
    t1, t2 = enter_input()
    w, v = eigenvalues_eigenvectors(link_matrix(t1, t2))
    print("Link Matrix from", t1, "to", t2, "is  \n", link_matrix(t1, t2))
    print("Eigenvalues is", w)
    print("Eigenvectors", v)


def enter_input():
    """
    enter input is string t1,t2 from keyboard and validate
    :return:t1,t2 is type of datetime
    """
    t1 = ''
    t2 = ''
    while True:
        try:
            t1 = input("Enter your start time t1 ")
            t1 = datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD HH:MM:SS")
            continue
        break
    while True:
        try:
            t2 = input("Enter your start time t2 ")
            t2 = datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD HH:MM:SS")
            continue
        break
    return t1, t2


def main():
    display()


if __name__ == '__main__':
    main()
