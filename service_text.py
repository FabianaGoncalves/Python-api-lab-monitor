import time
import requests
import os
import platform


def command(a):
    b = os.system("%s" % a)
    return b


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
                return resposta
        else:
            print("")


# criação do cliente

while True:

    url = "http://172.16.200.136:3030"

    patrimonio = platform.node()
    login = os.getlogin()

    acesso = requests.get("http://172.16.200.136:3030/check/%s" % patrimonio)
    acesso_js = acesso.json()

    if acesso_js["Status"] == "False":

        print("---------Salas Cadastradas----------\n"
              "1 - Laboratório de Informática 01\n"
              "2 - Laboratório de Informática 02\n"
              "3 - Laboratório de Redes\n"
              "4 - Laboratório de EAD\n"
              "5 - Laboratório de CAD\n"
              "6 - Laboratório de Simulações\n"
              "0 - Teste\n")

        op = int(input("Informe o valor numérico correspondente a sala: "))

        sala = ""

        if op == 1:
            sala = "Laboratório de Informática 01"
        elif op == 2:
            sala = "Laboratório de Informática 02"
        elif op == 3:
            sala = "Laboratório de Redes"
        elif op == 4:
            sala = "Laboratório de EAD"
        elif op == 5:
            sala = "Laboratório de CAD"
        elif op == 6:
            sala = "Laboratório de Simulações"
        elif op == 0:
            sala = "Teste"
        else:
            print("Escolha um valor váido!")

        dados = net_data()
        dados_rede = dados.split("|")
        ip = dados_rede[0].strip("'")
        mac = dados_rede[1]
        gateway = dados_rede[2]

        url += ("/pc/%s/%s/%s/%s/%s/%s" % (str(patrimonio), str(login), str(ip), str(mac), str(gateway), str(sala)))

        acesso = requests.get(url)

    else:
        acesso_usr = requests.get("http://172.16.200.136:3030/att/usr/%s/%s" % (patrimonio, login))
        acesso_js_usr = acesso_usr.json()

        url += ("/status/%s" % patrimonio)
        acesso = requests.get(url)
        acesso_js = acesso.json()

        if acesso_js["Status"] == "OFF":
            command('route delete 0.0.0.0')
            time.sleep(10)

        elif acesso_js["Status"] == "ON":

            acesse_gateway = requests.get("http://172.16.200.136:3030/gateway/%s" % patrimonio)
            gateway_js = acesse_gateway.json()

            if acesso_js:
                gateway_valor = gateway_js["gateway"]
                command('route add 0.0.0.0 mask 0.0.0.0 %s' % gateway_valor)
                time.sleep(10)

            # capture (sniffing)

            else:
                print("")

        else:
            print("")
