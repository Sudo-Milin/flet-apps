from time import sleep
import flet as ft

# # Basic app structure
# def main(page: ft.Page):
#     # add/update controls on Page
#     pass

# ft.app(target=main)
# # ft.app(target=main, view=ft.WEB_BROWSER) 
# # flet.app(port=8550, target=main)

# # Flet controls
# def main(page: ft.Page):
#     t = ft.Text(value="Hello, world!", color="green")
#     page.controls.append(t)
#     page.update()

# ft.app(target=main)

# def main(page: ft.Page):
#     t = ft.Checkbox(value=True)
#     page.controls.append(t)
#     page.update()

# ft.app(target=main)

# def main(page: ft.Page):
#     t = ft.Text()
#     page.add(t)

#     for i in range(10):
#         t.value = f'Step {i}'
#         page.update()
#         time.sleep(1)
# ft.app(target=main)

def main(page: ft.Page):
# 
#     page.add(
#         ft.Row(controls=[
#         ft.Text("A"),
#         ft.Text("B"),
#         ft.Text("C")
#         ])
#     )
# 
#     page.add(
#         ft.Column(controls=[
#         ft.Text("A"),
#         ft.Text("B"),
#         ft.Text("C")
#         ])
#     )
# 
#     page.add(
#         ft.Column(controls=[
#           ft.Row(controls=[
#               ft.Text("A"),
#               ft.Text("B"),
#               ft.Text("C")
#           ]),
#           ft.Row(controls=[
#               ft.Text("A"),
#               ft.Text("B"),
#               ft.Text("C")
#           ]),
#           ft.Row(controls=[
#               ft.Text("A"),
#               ft.Text("B"),
#               ft.Text("C")
#           ]),
#           ft.Row(controls=[
#               ft.Text("A"),
#               ft.Text("B"),
#               ft.Text("C")
#           ])
#         ])
#     )
# 
#     page.add(
#     ft.Row(controls=[
#         ft.TextField(label="Your name"),
#         ft.ElevatedButton(text="Say my name!")
#     ])
#   )
    
    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i}"))
    #     if i > 4:
    #         page.controls.pop(0)    
    #     page.update()
    #     sleep(1)

    def button_clicked(b):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

ft.app(target=main)

