import streamlit as st

from helpers import files

todos = files.get_todos()


def add_todo():
    todo: str = st.session_state['new_todo'] + '\n'
    todos.append(todo.capitalize())
    files.write_todos(todos_arg=todos)


def main():
    st.title('To-do app')
    st.subheader('Todo list:')

    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            files.write_todos(todos_arg=todos)
            del st.session_state[todo]
            st.experimental_rerun()

    st.text_input(label='Enter a todo: ', placeholder='Add new todo...',
                  on_change=add_todo, key='new_todo')

    st.session_state


if __name__ == '__main__':
    main()
