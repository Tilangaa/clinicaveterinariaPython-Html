from flask import Flask, render_template, request, redirect
app = Flask(__name__) #instancia o flask no app

pacientes = []

@app.route('/')
def index():
    return render_template( 'index.html', pacientes=pacientes)

@app.route('/adicionar_paciente', methods=['GET', 'POST'])
def adicionar_pacientes():
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nometutor']
        especie = request.form['especie']
        telefone = request.form['telefone']
        codigo = len(pacientes)
        pacientes.append([codigo, nome, raca, peso, nometutor, especie, telefone])
        return redirect('/')
    else:
        return render_template('adicionar_paciente.html')

@app.route('/editar_paciente/<int:codigo>', methods=['GET', 'POST'])
def editar_pacientes(codigo):
    """
    Rota para editar um contato existente.
    Se o método for POST, atualiza os detalhes do contato com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do contato para edição.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nometutor']
        especie = request.form['especie']
        telefone = request.form['telefone']
        pacientes[codigo] = [codigo, nome, telefone, peso, raca, especie, nometutor]
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        paciente = pacientes[codigo]
        return render_template('editar_paciente.html', pacientes=pacientes)  # Renderiza o formulário de edição

@app.route('/apagar_paciente/<int:codigo>')
def apagar_pacientes(codigo):
    """
    Rota para apagar um contato da lista.
    """
    del pacientes[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial


if __name__ == '__main__':
    app.run(debug=True) #executa o ap Flask