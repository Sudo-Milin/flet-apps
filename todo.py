import flet as ft

def main(page):
    # def add_clicked(e):
    #     page.add(ft.Checkbox(label=new_task.value))
    #     new_task.value = ""
    #     new_task.focus()
    #     new_task.update()

    # new_task = ft.TextField(hint_text="Whats needs to be done?", width=600)
    # page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()
    
    def check_value(e):
        if new_task.value == "":
            button.disabled = True
        else:
            button.disabled = False
        button.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=600)
    button = ft.ElevatedButton("Add", on_click=add_clicked, 
                                                 on_hover=check_value)
    page.add(ft.Row([new_task, button]))


ft.app(target=main)