from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import toga
from toga import Button, TextInput, Label, Box, App, Switch


class ToDoApp(App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

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
        if self.todo_input.value:
            item_box = Box(style=Pack(direction=ROW, padding=5))
            item_label = Label(self.todo_input.value)

            item_checkbox = Switch()

            item_checkbox.on_toggle = self.toggle_todo_item

            remove_button = Button('Remove', on_press=self.remove_todo_item)
            remove_button.style.padding_left = 10

            item_box.add(item_checkbox)
            item_box.add(item_label)
            item_box.add(remove_button)

            self.todo_list_box.add(item_box)
            self.todo_input.value = ''

    def remove_todo_item(self, widget, **kwargs):
        self.todo_list_box.remove(widget.parent)

    def toggle_todo_item(widget):
        item_label = widget.parent.children[1]
        if widget.is_on:
            item_label.style.text_decoration = 'line-through'
        else:
            item_label.style.text_decoration = 'none'


def main():
    return ToDoApp()


if __name__ == '__main__':
    app = main()
    app.main_loop()
