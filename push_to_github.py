import git
import os

# ----------------------------
# Настройки
# ----------------------------

# Путь к локальному репозиторию
repo_path = r"C:\Users\Nurtas\Desktop\Новая папка (2)"
# <- замени на путь к твоему репо

# Сообщение коммита
commit_message = "Автоматический коммит через Python"

# Имя удалённого репозитория (обычно 'origin')
remote_name = "origin"

# Ветка (обычно 'main' или 'master')
branch_name = "main"
# ----------------------------

# Проверяем, существует ли репозиторий
if not os.path.exists(repo_path):
    raise Exception(f"Репозиторий не найден по пути: {repo_path}")

repo = git.Repo(repo_path)

# Добавляем все изменения
repo.git.add(A=True)

# Проверяем, есть ли изменения для коммита
if repo.is_dirty():
    # Создаём коммит
    repo.index.commit(commit_message)
    print(f"Коммит создан: {commit_message}")

    # Пушим на GitHub
    origin = repo.remote(name=remote_name)
    origin.push(branch_name)
    print(f"Изменения запушены на {remote_name}/{branch_name}")
else:
    print("Нет изменений для коммита.")
