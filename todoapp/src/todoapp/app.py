import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga import Button, TextInput, Label, Box, App, Switch
import json
import os


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

        self.load_todo_items()

    def add_todo_item(self, widget):
        if self.todo_input.value:
            self.create_todo_item(self.todo_input.value, False)
            self.todo_input.value = ''
            self.save_todo_items()

    def create_todo_item(self, text, completed):
        item_box = Box(style=Pack(direction=ROW, padding=5))
        item_label = Label(text)

        item_checkbox = Switch(text='')
        item_checkbox.is_on = completed
        item_checkbox.on_toggle = self.toggle_todo_item

        remove_button = Button('Remove', on_press=self.remove_todo_item)
        remove_button.style.padding_left = 10

        item_box.add(item_checkbox)
        item_box.add(item_label)
        item_box.add(remove_button)

        self.todo_list_box.add(item_box)

        if completed:
            item_label.style.text_decoration = 'line-through'

    def remove_todo_item(self, widget, **kwargs):
        self.todo_list_box.remove(widget.parent)
        self.save_todo_items()

    def toggle_todo_item(self, widget):
        item_label = widget.parent.children[1]
        if widget.is_on:
            item_label.style.text_decoration = 'line-through'
        else:
            item_label.style.text_decoration = 'none'
        self.save_todo_items()

    def save_todo_items(self):
        todo_items = []
        for item_box in self.todo_list_box.children:
            item_checkbox = item_box.children[0]
            item_label = item_box.children[1]
            todo_items.append({'text': item_label.text, 'completed': item_checkbox.is_on})

        with open('todo_items.json', 'w') as f:
            json.dump(todo_items, f)

    def load_todo_items(self):
        if os.path.exists('todo_items.json'):
            with open('todo_items.json', 'r') as f:
                todo_items = json.load(f)
                for item in todo_items:
                    self.create_todo_item(item['text'], item['completed'])


def main():
    return ToDoApp()


if __name__ == '__main__':
    app = main()
    app.main_loop()
