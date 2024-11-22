import requests, flet as ft

def verify_api_online(size=12):
       
    try:
        #site da minha api 
        site = requests.get('https://toolbox-rosy-psi.vercel.app')

        print(site)

        #retorna um valor de acordo com o resultado requisitado (200 on) (502 off)
        if site.status_code == 200:
            size = size

            #bola verde para estatus online
            return ft.Container(
            width=size,                 #largura
            height=size,                #altura
            bgcolor=ft.colors.GREEN,    # Cor verde para online
            border_radius=size / 2,     # Deixar o Container redondo (divide por 2 para sempre igualar ao tamanho do cirvulo caso aumente)
        )

        elif site.status_code == 502:
            size = size

            #bola cinza para estatus offline
            return ft.Container(
            width=size,                     #largura
            height=size,                    #altura
            bgcolor=ft.colors.GREY_700,     # Cor cinza para online
            border_radius=size / 2,         # Deixar o Container redondo (divide por 2 para sempre igualar ao tamanho do cirvulo caso aumente)
        )
    
    except requests.ConnectionError as error:
        return ft.Container(
            width=size,                     #largura
            height=size,                    #altura
            bgcolor=ft.colors.GREY_700,     # Cor cinza para online
            border_radius=size / 2,        # Deixar o Container redondo (divide por 2 para sempre igualar ao tamanho do cirvulo caso aumente)
            data=print('Sem conexão com a internet')
        )   
    
        

if __name__ == '__main__':
    verify_api_online()