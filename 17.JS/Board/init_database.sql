-- 파일을 바로 적용하기: sqlite3 board.sqlite < init_database.sql
DROP TABLE IF EXISTS board;

CREATE TABLE board (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50) NOT NULL,
    message VARCHAR(200)
)