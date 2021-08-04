from flask import render_template, request
import fucns



def rotas(app):
    @app.route('/')
    def principal():
        return (render_template('principal.html'))

    @app.route('/cad', methods=['GET', 'POST'])
    def index():
        ms = ""
        if request.method == 'POST':
            n1 = (request.form['id'])
            n2 = request.form['nome']
            n3 = (request.form['valor'])
            ms =fucns.cadastrar(n1, n2, n3)

        return (render_template('index.html', msg = ms))

    @app.route('/sobre')
    def sobre():
        return (render_template('sobre.html'))


    @app.route('/listar')
    def listar():
        n1,n2,n3= 0, " ", 0

        linhas = fucns.listar(n1, n2,n3)
        return (render_template('listar.html', linhas=linhas))

    @app.route('/deletar', methods=['GET', 'POST'])
    def delete():
        if request.method == 'GET':
            id = int(request.args.get('id'))
            print(id)
            fucns.delete(id)

            return (render_template('listar.html'))

    @app.route('/altera/<id_>', methods=['GET', 'POST'])
    def alterar(id_):
        ms=""
        data = fucns.select(id_)
        if request.method == 'POST':
            n1 = int(request.form['id'])
            n2 = request.form['nome']
            n3 = int(request.form['valor'])

            ms = fucns.alterar(n1, n2, n3)
            data = fucns.select(id_)


        return render_template('alterar.html',data=data, id_=id_, msg = ms)
