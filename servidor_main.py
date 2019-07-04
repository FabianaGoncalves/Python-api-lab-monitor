import flask
from Servico import fuctions as f

app = flask.Flask("Imperium")
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def pag_inicial():
    resposta = {
        "Ansewer": "Pagina em branco",
        "Autenticar_usuário": "/autenticar/usuario/senha",
        "Adicionar computador": "/pc/patrimonio/usuario/ip/mac/gateway/sala",
        "Checar status do PC": "/status/patrimonio",
        "Atualizar Status": "/att_status/patrimonio/status",
        "Checar Cliente": "/check/patrimonio",
        "Checar dados": "/get/patriomonio",
        "Atualizar Usuário": "/att/usr/patrimonio/usuario",
        "Desligar sala": "/sala/off/nome_da_sala",
        "Ligar sala": "/sala/on/nome_da_sala",
        "Dados do usuário por sala": "/sala/pc/nome_da_sala",
        "coletar gateway": "/gate/patrimônio"
    }
    return flask.jsonify(resposta)


# autenticar o usuário
@app.route("/autenticar/<string:usuario>/<string:senha>")
def autenticar_usuario(usuario, senha):
    existe = f.listar_v("count(id)", "usuario where nome = '%s'" % usuario)[0][0]
    resposta = {"Status": ""}

    if existe == 1:
        value = f.validar_usr(usuario, senha)
        if value == 1:
            resposta["Status"] = "válido"
            return flask.jsonify(resposta)
        else:
            resposta["Status"] = "inválido"
            return flask.jsonify(resposta)
    else:
        resposta["Status"] = "usuário não cadastrado"
        return flask.jsonify(resposta)

# checar status de rede do computador
@app.route("/status/<string:patrimonio>")
def checar_status(patrimonio):
    existe = f.listar_v("count(patrimonio)", "pc where patrimonio = '%s'" % patrimonio)[0][0]
    resposta = {"Status": ""}

    if existe == 1:
        status = f.status(patrimonio)

        if status[0][0] == "True":
            resposta["Status"] = "ON"
            return flask.jsonify(resposta)
        elif status[0][0] == "False":
            resposta["Status"] = "OFF"
            return flask.jsonify(resposta)
        else:
            resposta["Status"] = "Deu Ruim!"
            return flask.jsonify(resposta)
    else:
        resposta["Status"] = "Patrimônio não encontrado"
        return flask.jsonify(resposta)


@app.route("/check/<string:patrimonio>")
def checar(patrimonio):  # OK
    existe = f.listar_v("count(patrimonio)", "pc where patrimonio = '%s'" % patrimonio)[0][0]
    resposta = {"Status": ""}

    if existe == 0:
        resposta["Status"] = "False"
        return flask.jsonify(resposta)
    else:
        resposta["Status"] = "True"
        return flask.jsonify(resposta)

# cadastrar pc no banco de dados
@app.route("/pc/<string:patrimonio>/<string:usuario>/<string:ip>/<string:mac>/<string:gateway>/<string:sala>")
def adicionar_computador(patrimonio, usuario, ip, mac, gateway, sala):
    resposta = {"Status": ""}
    status = "True"
    f.adicionar_PC(patrimonio, usuario, ip, mac, gateway, sala, status)
    resposta["Status"] = "Computador adicionado!"
    flask.jsonify(resposta)

# atualizar usuário
@app.route("/att/usr/<string:patrimonio>/<string:usuario>")
def atualizar_usuario(patrimonio, usuario):
    existe = f.listar_v("count(usuario)", "pc where patrimonio = '%s'" % patrimonio)[0][0]
    resposta = {"Status": ""}

    if existe == 1:
        f.atualizar_usuario(patrimonio, usuario)
        resposta["Status"] = "OK"
        return flask.jsonify(resposta)
    else:
        resposta["Status"] = "NONE"
        return flask.jsonify(resposta)


# Tentando adaptar para o JS manipular


# atualizar o status de rede
@app.route("/att_status/<string:patrimonio>/<string:status>", methods=['GET'])
def atualizar_status(patrimonio, status):
    existe = f.listar_v("count(patrimonio)", "pc where patrimonio = '%s'" % patrimonio)[0][0]
    resposta = {"Status": ""}

    if existe == 1:
        resposta["Status"] = "Status atualizado"
        f.atualizar_status(patrimonio, status)
        response = flask.jsonify(resposta)
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    else:
        resposta["Status"] = "Patrimônio não encontrado"
        response = flask.jsonify(resposta)
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response


@app.route("/sala/off/<string:sala>", methods=['GET'])
def desligar_sala(sala):
    patrimonios = f.buscar_sala(sala)
    for i in patrimonios:
        f.atualizar_status(i[0], "False")
    resposta = {"Status_Sala": "OFF"}
    response = flask.jsonify(resposta)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route("/sala/on/<string:sala>", methods=['GET'])
def ligar_sala(sala):
    patrimonios = f.buscar_sala(sala)
    for i in patrimonios:
        f.atualizar_status(i[0], "True")
    resposta = {"Status_Sala": "ON"}
    response = flask.jsonify(resposta)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route("/sala/pc/<string:sala>", methods=['GET'])
def buscar_pc_sala(sala):
    dados = f.buscar_pc_sala(sala)
    patrimonios = []
    usuarios = []

    for i in dados:
        patrimonios.append(i[0])
        usuarios.append(i[1])

    resposta = {
        "patrimonios": patrimonios,
        "usuarios": usuarios
    }
    response = flask.jsonify(resposta)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route("/gateway/<string:patrimonio>")
def gateway(patrimonio):
    existe = f.listar_v("count(patrimonio)", "pc where patrimonio = '%s'" % patrimonio)[0][0]
    resposta = {"gateway": ""}

    if existe == 1:
        gate = f.gateway(patrimonio)
        gate1 = gate[0][0]
        resposta["gateway"] = gate1
        response = flask.jsonify(resposta)


        return response
    else:
        pass


"""
@app.route("/sala/pc/<string:sala>",methods=['GET'])
def buscar_pc_sala(sala):
    dados = f.buscar_pc_sala(sala)
    resposta = {"Patrimonio": "",
                "Usuario":""}
    for i in dados:
        resposta["Patrimonio"] += ("%s|" % i[0])
        resposta["Usuário"] += ("%s|" % i[1])
        response = flask.jsonify(resposta)
        response.headers.add('Access-Control-Allow-Origin', '*')
    return response
"""


app.run("0.0.0.0", 3030)
