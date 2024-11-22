import flet as ft

def main(page: ft.Page):
    # Criar uma bolinha verde (online)
    online_status = ft.Container(
        width=12,
        height=12,
        bgcolor="green",  # Cor verde para online
        border_radius=6,  # Deixar o Container redondo
    )

    # Criar uma bolinha cinza (offline)
    offline_status = ft.Container(
        width=12,
        height=12,
        bgcolor="black",  # Cor cinza para offline
        border_radius=6,  # Deixar o Container redondo
    )

    page.add(
        ft.Row(
            [
                ft.Text("Online:"),
                online_status,
                ft.Text("Offline:"),
                offline_status,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
