import mysql.connector


def conexao():
    cnx = mysql.connector.connect(user="root", password="klavkalax07@", host="127.0.0.1", database='bdprodutos')
    mycursor = cnx.cursor()
    return (mycursor, cnx)
