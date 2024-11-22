import flet as ft
from utils.api import verify_api_online


def main(page: ft.Page):
    #tamanho da tela (altura e largura)
    width = page.window_width
    height = page.window_height

    #primeira coluna
    primary_column = ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        
                        #texto dos status
                        ft.Text(
                            value='Status: '
                        ),

                        #função que desenha a bola de acordo com o status on/off
                        verify_api_online()
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
        ],
        width=width
    )


    page.add(
        primary_column
    )

ft.app(main)
