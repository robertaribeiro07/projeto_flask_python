from connect import conexao
import mysql

def cadastrar(n1,n2,n3):
    mycursor,cnx=conexao()
    msg = "Cadastrado com sucesso!!!"
    sql = "INSERT INTO produtos(id_cod, nome, preco) VALUES (%s, '%s', %s) " % (n1, n2, n3)

    try:
        mycursor.execute(sql)
        cnx.commit()

    except:
        cnx.rollback()
        msg = "Preencha os dados antes de enviar!"
    cnx.close()

    return msg

def listar(n1,n2,n3):
    mycursor, cnx = conexao()
    sql = "SELECT * FROM produtos"
    mycursor.execute(sql)
    linhas = mycursor.fetchall()
    print("Número total de registros retornados: ", mycursor.rowcount)
    print("\nMostrando os produtos cadastrados")
    for linha in linhas:
        print("Id:", linha[0])
        print("Nome:", linha[1])
        print("Preço:", linha[2], "\n")
    cnx.commit()
    return linhas


def delete(id):
    mycursor, cnx = conexao()

    sql = "DELETE FROM produtos WHERE id_cod = %s"
    try:
        mycursor.execute(sql,(id,))
        cnx.commit()
        print(mycursor.rowcount, "deletado com sucesso!!!")
    except mysql.connector.Error as me:
        print(f"MySQL Error:{me}")
        cnx.rollback()
    except Exception as exp:
        print (exp)


def alterar(n1, n2, n3):
    mycursor, cnx = conexao()

    msg = "Alterado com sucesso!!!"

    sql = 'UPDATE produtos SET nome = %s, preco = %s WHERE id_cod= %s'
    values = (n2, n3, n1)
    try:
        mycursor.execute(sql, values)
        cnx.commit()
        print(mycursor.rowcount, "Alterado com sucesso!!!")

    except mysql.connector.Error as me:
        print(f"MySQL Error:{me}")
        msg = "erro"
        cnx.rollback()
    except Exception as exp:
        print(exp)

    return msg

def select(id_):
        mycursor, cnx = conexao()

        sql = "SELECT nome, preco FROM produtos WHERE id_cod = %s"
        values = (id_,)
        try:
            mycursor.execute(sql, values)
            data= mycursor.fetchone()

        except Exception as exp:
            print(exp)
        else:
            try:
                mycursor.close()
                cnx.close()
            except Exception:
                pass

            return data