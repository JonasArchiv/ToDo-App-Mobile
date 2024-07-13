from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga import Button, TextInput, Label, Box, App


class ToDoApp(App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        self.todo_list_box = Box(style=Pack(direction=COLUMN, padding=5))

        self.todo_input = TextInput(placeholder="Add a ToDo item")
        self.add_button = Button('Add', on_press=self.add_todo_item)
        self.input_box = Box(style=Pack(direction=ROW, padding=5))
        self.input_box.add(self.todo_input)
        self.input_box.add(self.add_button)

        self.main_box = Box(style=Pack(direction=COLUMN, padding=10))
        self.main_box.add(self.input_box)
        self.main_box.add(self.todo_list_box)

        self.main_window.content = self.main_box
        self.main_window.show()

    def add_todo_item(self, widget):
        # Add the ToDo item to the list
        if self.todo_input.value:
            self.todo_list_box.add(Label(self.todo_input.value))
            self.todo_input.value = ''  # Clear input box


def main():
    return ToDoApp()


if __name__ == '__main__':
    app = main()
    app.main_loop()