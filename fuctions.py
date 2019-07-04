import sqlite3

conexao_bd = None  # variavel global de conexão


def iniciar():  # iniciar a conexão com o banco
    global conexao_bd
    conexao_bd = sqlite3.connect("banco.db")
    # print("Conexão iniciada")


def validar_usr(x, y):  # Validar o usuário pelo banco
    iniciar()
    conect_c = conexao_bd.cursor()
    conect_select = conect_c.execute("select nome,senha from usuario where nome='%s'" % x)
    conexao_bd.commit()
    result = conect_select.fetchall()
    conect_c.close()
    if result[0][0] == x and result[0][1] == y:
        return 1
    else:
        return 0


def listar_v(x, y):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("SELECT %s FROM %s" % (x, y))
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp


def adicionar_PC(patrimonio, usuario, ip, mac, gateway, sala, status):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("insert into pc values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (patrimonio,
                                                                                                      usuario, ip, mac,
                                                                                                      gateway, sala,
                                                                                                      status))
    conexao_bd.commit()
    conex_sel.fetchall()
    conex_c.close()


def status(patrimonio):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("SELECT status FROM pc where patrimonio = '%s'" % patrimonio)
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp


def atualizar_status(patrimonio, status):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_c.execute("update pc set status = '%s' where patrimonio = '%s'" % (status, patrimonio))
    conexao_bd.commit()
    conex_c.close()


def buscar_usuario(patrimonio):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("SELECT usuario FROM pc where patrimonio = '%s'" % patrimonio)
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp


def atualizar_usuario(patrimonio, usuario):
    usr = buscar_usuario(patrimonio)

    if usr[0][0] != usuario:
        iniciar()
        conex_c = conexao_bd.cursor()
        conex_c.execute("update pc set usuario = '%s' where patrimonio = '%s'" % (usuario, patrimonio))
        conexao_bd.commit()
        conex_c.close()
        return 1
    else:
        return 0


def gateway(patrimonio):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("SELECT gateway FROM pc where patrimonio = '%s'" % patrimonio)
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp


def buscar_sala(sala):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("SELECT patrimonio FROM pc where sala like '%s'" % sala)
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp


def buscar_pc_sala(sala):
    iniciar()
    conex_c = conexao_bd.cursor()
    conex_sel = conex_c.execute("SELECT patrimonio,usuario FROM pc where sala like '%s'" % sala)
    conexao_bd.commit()
    resp = conex_sel.fetchall()
    conex_c.close()
    return resp


def net_data():  # função para coletar os dados de rede

    import netifaces

    interface_name = netifaces.interfaces()  # captura o nome das interfaces
    for i in interface_name:  # percorrendo a lista de interfaces e realizando o teste em cada uma
        data = netifaces.ifaddresses(i)  # captura os dados ip,mac,broadcast das interfaces

        if len(data) == 3:  # interfaces ativas do sistema tem um tamanho de dados de resposta na lista == 3
            filtro_mac_0 = data[-1000]  # o campo -1000 corresponde ao valor do MAC
            filtro_mac_1 = filtro_mac_0[0]  # manipulação de lista
            mac = filtro_mac_1["addr"]
            filtro_ip_0 = data[2]  # os dados de IPV4 estão no indice 2
            filtro_ip_1 = filtro_ip_0[0]
            # como a resposta do netifaces é uma lista com dicionários
            # dentro é nescessário extrair o dicionário que queremos da lista
            ip = filtro_ip_1["addr"]
            # o campo do dicionário que corresponde ao ip é addr nesse comando ele é filtrado

            if ip != '127.0.0.1':  # retirando o ip de loopback sobra somente a rede cabeada.
                # print(i)
                gws = netifaces.gateways()  # captura o gateway
                filtro_gw_0 = gws['default']  # para o gateway default
                filtro_gw_1 = filtro_gw_0[2]  # manipulação de dados
                gateway = filtro_gw_1[0]

                rip = ip
                rmac = mac
                rgateway = gateway

                resposta = ("%a|%s|%s" % (rip, rmac, rgateway))  # valor para a resposta
        else:
            print("")
    return resposta


def command(a):
    import os
    b = os.system("%s" % a)
    return b


def net_name():  # função para coletar o nome da interface

    import netifaces

    interface_name = netifaces.interfaces()  # captura o nome das interfaces
    for i in interface_name:  # percorrendo a lista de interfaces e realizando o teste em cada uma
        data = netifaces.ifaddresses(i)  # captura os dados ip,mac,broadcast das interfaces

        if len(data) == 3:  # interfaces ativas do sistema tem um tamanho de dados de resposta na lista == 3
            filtro_ip_0 = data[2]  # os dados de IPV4 estão no indice 2
            filtro_ip_1 = filtro_ip_0[0]
            ip = filtro_ip_1["addr"]

            if ip != '127.0.0.1':  # retirando o ip de loopback sobra somente a rede cabeada.
                resposta = i
        else:
            print("")
    return resposta


#print(net_name())
