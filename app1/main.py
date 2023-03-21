user_prompt: str = 'Enter a todo: '
todos_count_prompt: str = 'Enter count of todos you want: '

todos_count: int = int(input(todos_count_prompt))
todos: list = [input(user_prompt) for _ in range(todos_count)]
todos_length = len(todos)

print(*[f"Todo: '{todo}'" for todo in todos], sep='\n')
print(f"Todos length: {todos_length}")
