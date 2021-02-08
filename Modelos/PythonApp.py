import PySimpleGUI as sg
import pandas as pd
import pickle

# Criando janelas e estilos(layouts)--------------------------------------------------------------------------------------------------------
def janela_inicial():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Olá!')],
        [sg.Text('Descubra o valor de aluguel do seu imóvel')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('ImóvelApp', layout = layout, finalize = True)

def janela_apresentacao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Digite seu nome e cidade:')],
        [sg.Text('Nome: '), sg.Input(size=(28,0), key='nome')],
        [sg.Text('Cidade:'), sg.Combo(["belo horizonte","porto-velho","manaus","rio-branco","campo-grande","macapa","brasilia","boa-vista","cuiaba","palmas","sao-paulo","teresina","rio-de-janeiro","belem","goiania","salvador","florianopolis","sao-luis","maceio","porto-alegre","curitiba","fortaleza","recife","joao-pessoa","aracaju","natal","vitoria"], key='capital')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('ImóvelApp', layout = layout, finalize = True)

def janela_imovel1():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Insira os valores do imóvel:')],
        [sg.Text('Valor do condomínio:', size=(18,0)), sg.Spin([i for i in range(0,500)], initial_value=0, size=(10,0), key='Valor_condomínio')],
        [sg.Text('Valor do IPTU:', size=(18,0)), sg.Spin([i for i in range(0,500)], initial_value=0, size=(10,0), key='Valor_iptu')],
        [sg.Text('Tamanho do imóvel(m²):', size=(18,0)), sg.Spin([i for i in range(0,500)], initial_value=0, size=(10,0), key='Área_total')],
        [sg.Text('Quantidade de quartos:', size=(18,0)), sg.Spin([i for i in range(0,500)], initial_value=0, size=(10,0), key='Qt_quartos')],
        [sg.Text('Quantidade de vagas:', size=(18,0)), sg.Spin([i for i in range(0,500)], initial_value=0, size=(10,0), key='Qt_vagas')],
        [sg.Text('Quantidade de banheiros:', size=(18,0)), sg.Spin([i for i in range(0,500)], initial_value=0, size=(10,0), key='Qt_banheiros')],
        [sg.Button('Continuar'), sg.Button('Voltar')]
    ]
    return sg.Window('ImóvelApp', layout = layout, finalize = True)

def janela_imovel2():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Marque as características presentes no imóvel:')],
        [sg.Checkbox('Academia', key = 'Academia'), sg.Checkbox('Acesso para deficientes', key = 'Acesso_para_deficientes')],
        [sg.Checkbox('Ar condicionado', key = 'Ar_condicionado'), sg.Checkbox('Área de serviço', key = 'Área_de_serviço')],
        [sg.Checkbox('Armário embutido', key = 'Armário_embutido'), sg.Checkbox('Armário na cozinha', key = 'Armário_na_cozinha')],
        [sg.Checkbox('Bicicletário', key = 'Bicicletário'), sg.Checkbox('Churrasqueira', key = 'Churrasqueira')],
        [sg.Checkbox('Circuito de segurança', key = 'Circuito_de_segurança'), sg.Checkbox('Conexão à internet', key = 'Conexão_à_internet')],
        [sg.Checkbox('Elevador', key = 'Elevador'), sg.Checkbox('Espaço gourmet', key = 'Espaço_gourmet')],
        [sg.Checkbox('Garagem', key = 'Garagem'), sg.Checkbox('Interfone', key = 'Interfone')],
        [sg.Checkbox('Lavanderia', key = 'Lavanderia'), sg.Checkbox('Mobiliado', key = 'Mobiliado')],
        [sg.Checkbox('Piscina', key = 'Piscina'), sg.Checkbox('Playground', key = 'Playground')],
        [sg.Checkbox('Quadra de tênis', key = 'Quadra_de_tênis'), sg.Checkbox('Quadra poliesportiva', key = 'Quadra_poliesportiva')],
        [sg.Checkbox('Salão de festas', key = 'Salão_de_festas'), sg.Checkbox('Sauna', key = 'Sauna')],
        [sg.Checkbox('Segurança 24h', key = 'Segurança_24h'), sg.Checkbox('Sistema de alarme', key = 'Sistema_de_alarme')],
        [sg.Checkbox('Spa', key = 'Spa'), sg.Checkbox('Varanda', key = 'Varanda')],
        [sg.Button('Calcular'), sg.Button('Voltar')]
    ]
    return sg.Window('ImóvelApp', layout = layout, finalize = True)

def janela_resultado():
    sg.theme('Reddit')
    layout = [
        [sg.Text(nome)],
        [sg.Text('O valor do aluguel é de aproximadamente:')],
        [sg.Text(valor)],
        [sg.Button('Sair'), sg.Button('Nova Consulta')]
    ]
    return sg.Window('ImóvelApp', layout = layout, finalize = True)

# Criar a janela inicial--------------------------------------------------------------------------------------------------------------------
janela1, janela2, janela3, janela4, janela5 = janela_inicial(), None, None, None, None

# Criar o loop de leitura de eventos--------------------------------------------------------------------------------------------------------
while True:
    
    window, event, values = sg.read_all_windows()
    
    # Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == sg.WIN_CLOSED:
        break
        
    # Quando queremos ir para próxima janela
    if window == janela1 and event == 'Continuar':
        janela1.hide()
        janela2 = janela_apresentacao()
               
    # Quando queremos ir para próxima janela2
    if window == janela2 and event == 'Continuar':
        nome = values['nome']
        cidade = values['capital']
        janela3 = janela_imovel1()
        janela2.hide()
        
    # Quando queremos ir para próxima janela3
    if window == janela3 and event == 'Continuar':
        Valor_condomínio = values['Valor_condomínio']
        Valor_iptu = values['Valor_iptu']
        Área_total = values['Área_total']
        Qt_quartos = values['Qt_quartos']
        Qt_vagas = values['Qt_vagas']
        Qt_banheiros = values['Qt_banheiros']       
        
        janela3.hide()
        janela4 = janela_imovel2()
        
    if window == janela5 and event == 'Nova Consulta':
        df = pd.DataFrame()
        janela5.hide()
        janela4.hide()
        janela2 = janela_apresentacao()        

    # Quando queremos voltar na janela
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela2 = janela_apresentacao()

    if window == janela4 and event == 'Voltar':
        janela3 = janela_imovel1()
        janela4.hide()
        
    if window == janela5 and event == 'Sair':
        break
  
    # Apresentando resultados
    if window == janela4 and event == 'Calcular':
        
        #-------------------------------------------- Pegando as variáveis númericas
        df = pd.DataFrame()
        df['Valor_condomínio'] = [Valor_condomínio]
        df['Valor_iptu'] = [Valor_iptu]
        df['Área_total'] = [Área_total]
        df['Qt_quartos'] = [Qt_quartos]
        df['Qt_vagas'] = [Qt_vagas]
        df['Qt_banheiros'] = [Qt_banheiros]
        
        #------------------------------------ Pegando as variáveis de características
        for k,v in values.items():
            df[k] = [1 if values[k] == True else 0]
        
        #------------------------------------ Pegando as variáveis de localidade
        cols = ["belo horizonte","porto-velho","manaus","rio-branco","campo-grande","macapa","brasilia","boa-vista","cuiaba",\
                "palmas","sao-paulo","teresina","rio-de-janeiro","belem","goiania","salvador","florianopolis","sao-luis","maceio",\
                "porto-alegre","curitiba","fortaleza","recife","joao-pessoa","aracaju","natal","vitoria"]
        
        for i in cols:
            df[i] = [0]
            
        for i in cols:
            df[i] = 1 if cidade == i else 0
        
        #------------------------------------ Fazendo as previsões        
        model = pickle.load(open('model.sav', 'rb'))
        
        y_pred = model.predict(df)
        
        valor = "R$" + str(int(y_pred[0]))
        
        janela5 = janela_resultado()
        
        #sg.popup(valor)
        