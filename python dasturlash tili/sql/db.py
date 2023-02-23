import psycopg2
db_conn = psycopg2.connect(
    database="students",
    user="postgres",
    password="321",
    host="127.0.0.1",
    port ="5432"
)

cur.execute(""" 
    INSERT INTO book(nomi,muallif,narx,sahifa,nashriyot) \
        VALUES
         ('kapitan Grant bolalar','Jyul Vern',500000,688,'Asaxiy'),
         ('Atom Odatlar','Jeyms Klir',55000,350,'Kitoblar dunyosi'),
         ('Web asoslari','Samiyev Abrorbek',105000,450,'Imkon talim'),
""")
print(' Malumot qushildi')

db_conn.commit()
db_conn.close()



























# cur=db_conn.cursor()
# cur.execute("""
#             CREATE TABLE book(
#                id BIGSERIAL NOT NULL PRIMARY KEY,
#                nomi VARCHAR(100) NOT NULL,
#                muallif VARCHAR(100) NOT NULL,
#                narx FLOAT NOT NULL,
#                sahifa INT NOT NULL,
#                nashriyot VARCHAR(100) NOT NULL 
#             );
# """)
# # print('JADVAL MUVAFFAQIYATLI YARATILDI!!!')
# cur.execute("""
#         INSERT INTO bokk(nomi,muallif,narx,sahifa,nashriyot) \
#         VALUES ('Python asoslari','Alisher')

# """)
# db_conn.commit()
# db_conn.close()