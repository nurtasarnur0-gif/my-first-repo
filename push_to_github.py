import git
import os

# ----------------------------
# Настройки
# ----------------------------

# Путь к локальному репозиторию
repo_path = r"C:\Users\Nurtas\Desktop\Новая папка (2)"  # <- твой путь

# Сообщение коммита
commit_message = "Автоматический коммит через Python"

# Имя удалённого репозитория (обычно 'origin')
remote_name = "origin"
# ----------------------------

# Проверяем, существует ли репозиторий
if not os.path.exists(repo_path):
    raise Exception(f"Репозиторий не найден по пути: {repo_path}")

repo = git.Repo(repo_path)

# Определяем текущую ветку
current_branch = repo.active_branch.name
print(f"Текущая ветка: {current_branch}")

# Добавляем все изменения
repo.git.add(A=True)

# Проверяем, есть ли изменения для коммита
if repo.is_dirty():
    # Создаём коммит
    repo.index.commit(commit_message)
    
    # Получаем список изменённых файлов
    changed_files = [item.a_path for item in repo.index.diff("HEAD~1")] + repo.untracked_files
    if changed_files:
        print("Закоммичены файлы:")
        for f in changed_files:
            print(f" - {f}")

    # Пушим на GitHub
    origin = repo.remote(name=remote_name)
    origin.push(current_branch)
    print(f"Изменения запушены на {remote_name}/{current_branch}")
else:
    print("Нет изменений для коммита.")
