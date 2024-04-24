import flet
import requests
from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    TextField,
    UserControl,
    colors,
    icons,
)


class Task(UserControl):
    def __init__(self, task_name: object, task_status_change: object, task_delete: object) -> object:
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        self.display_task = Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        for i in requests.get('http://127.0.0.1:8000/').json():
            if i['title'] == self.display_task.label:
                url = f"http://127.0.0.1:8000/update/{i['id']}"
                date = {
                    'title': self.edit_name.value,
                    'content': 'please work'
                }
                requests.put(url, date)
                break
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
        self.page.clean()
        main(self.page)

    def status_changed(self, e):
        self.completed = self.display_task.value
        if self.display_task.value:
            print('True')
            print(self.title)
        else:
            print("False")
        self.task_status_change(self)

    def delete_clicked(self, e):
        for i in requests.get('http://127.0.0.1:8000/').json():
            if i['title'] == self.task_name:
                url = f"http://127.0.0.1:8000/delete/{i['id']}"
                requests.delete(url)
                break
        self.update()
        self.page.clean()
        main(self.page)


class TodoApp(UserControl):
    def build(self):
        self.new_task = TextField(hint_text="Whats needs to be done?", expand=True)
        self.tasks = Column()

        for i in requests.get('http://127.0.0.1:8000/').json():
            task = Task(i['title'], self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)

        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="all"), Tab(text="active"), Tab(text="completed")],
        )

        self.items_left = Text("0 items left")

        return Column(
            width=600,
            controls=[
                Row([Text(value="Todos", style="headlineMedium")], alignment="center"),
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.items_left,
                            ],
                        ),
                    ],
                ),
            ],
        )

    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        date = {
            'title': task.task_name,
            'content': 'bla bla bla'
        }
        requests.post('http://127.0.0.1:8000/create/', date)
        self.new_task.value = ""
        self.update()
        self.clean()
        main(self.page)

    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def tabs_changed(self, e):
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                    status == "all"
                    or (status == "active" and task.completed == False)
                    or (status == "completed" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"
        super().update()


def main(page: Page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()

    app = TodoApp()

    page.add(app)


flet.app(target=main)
