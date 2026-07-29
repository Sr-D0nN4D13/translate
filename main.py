import flet as ft

from app.app import TranslateApp


def main(page: ft.Page):

    TranslateApp(page)


if __name__ == "__main__":

    ft.run(main)