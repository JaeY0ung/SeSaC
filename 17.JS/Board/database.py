import sqlite3

class Database():
    def __init__(self) -> None:
        self.db = sqlite3.connect('board.sqlite', check_same_thread=False)
        self.cursor = self.db.cursor()
    
    def execute(self, query, args={}):
        self.cursor.execute(query,args)

    def execute_fetch(self,query, args={}):
        self.cursor.execute(query, args)
        result = self.cursor.fetchall()
        return result
    
    def commit(self):
        self.db.commit()

if __name__ =="__main__":
    db = Database()
    
    #? 추가
    db.execute('INSERT INTO board(title, message) VALUES (?, ?)', ('title1', 'message1'))
    db.commit()

    #? 조회
    result = db.execute_fetch('SELECT * FROM board WHERE title = ?', ('title1',))
    print(result)

    #? 삭제
    db.execute('DELETE FROM board WHERE title = ?', ('title1',))
    db.commit()