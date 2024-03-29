import MySQLdb

class sql_processor:

    def __init__(self):
        self.mydb = MySQLdb.Connect(host="192.168.1.103",
                                    port=3306,
                                    user="root",
                                    passwd="",
                                    db="scrum_db")

    def process(self, request):
        cursor = self.mydb.cursor()
        command = cursor.execute(request)
        results = cursor.fetchall()
        return results

    def __del__(self):
        self.mydb.commit()
        self.mydb.close()
        print('sql destructor was run')