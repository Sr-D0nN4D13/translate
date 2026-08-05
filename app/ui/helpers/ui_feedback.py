import asyncio
import flet as ft


class UIFeedback:

    @staticmethod
    async def animate_copy(button: ft.IconButton):

        original = button.icon

        button.icon = ft.Icons.CHECK

        button.update()

        await asyncio.sleep(0.30)

        button.icon = original

        button.update()