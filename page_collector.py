import pandas as pd
import cfscrape
from bs4 import BeautifulSoup
import re
import time

total_n_page = {"mg+belo-horizonte":2000,"ro+porto-velho":99,"am+manaus":480,"ac+rio-branco":2,"ms+campo-grande":314,"ap+macapa":1,"df+brasilia":1290,"rr+boa-vista":4,"mt+cuiaba":1190,"to+palmas":48,"sp+sao-paulo":2000,"pi+teresina":525,"rj+rio-de-janeiro":2000,"pa+belem":580,"go+goiania":2000,"ba+salvador":2000,"sc+florianopolis":2000,"ma+sao-luis":380,"al+maceio":280,"rs+porto-alegre":2000,"pr+curitiba":2000,"ce+fortaleza":2000,"pe+recife":2000,"pb+joao-pessoa":770,"se+aracaju":297,"rn+natal":990,"es+vitoria":380}

lista_local = ["mg+belo-horizonte","ro+porto-velho","am+manaus","ac+rio-branco","ms+campo-grande","ap+macapa","df+brasilia","rr+boa-vista","mt+cuiaba","to+palmas","sp+sao-paulo","pi+teresina","rj+rio-de-janeiro","pa+belem","go+goiania","ba+salvador","sc+florianopolis","ma+sao-luis","al+maceio","rs+porto-alegre","pr+curitiba","ce+fortaleza","pe+recife","pb+joao-pessoa","se+aracaju","rn+natal","es+vitoria"]           

pagina = "https://www.zapimoveis.com.br/aluguel/apartamentos/{local}/?pagina={page}"

list_strings = []
list_estado = []

def page_items_collector():
                        
    scraper = cfscrape.create_scraper()

    for endereco in lista_local:

        total_de_paginas = int(total_n_page[endereco] / 24)

        for n_page in range(1,total_de_paginas+1):
            
            time.sleep(2)

            url = pagina.format(local=endereco, page=n_page)

            result = scraper.get(url)
            soup = BeautifulSoup(result.content, 'html.parser')
            string = str(soup.select('script', type='text/javascript')[5])

            print("---------------------------------")
            print("Buscando por:",endereco,", pagina" , n_page)
            print("---------------------------------")

            for i in range(1,49):

                pattern = re.search("-apartamento-", str(string))

                if pattern:
                    string_resultado = string[pattern.regs[0][0]:(pattern.regs[0][1]+120)]
                    string = string.replace(string[pattern.regs[0][0]:(pattern.regs[0][1]+120)], "")
                    list_strings.append(string_resultado)
                    string_resultado = ""
                    list_estado.append(endereco)
                else:
                    break                        


    df_output = pd.DataFrame(columns=["Link","Região"])
    df_output["Link"] = list_strings
    df_output["Região"] = list_estado
    df_output.to_excel('page_items_output_2.xlsx')


if __name__ == "__main__":
    page_items_collector()

