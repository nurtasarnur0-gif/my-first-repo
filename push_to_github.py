import git
import os

# ----------------------------
# Настройки
# ----------------------------

repo_path = r"C:\Users\Nurtas\Desktop\Новая папка (2)"  # Путь к репозиторию
commit_message = "Автоматический коммит через Python"
remote_name = "origin"
# ----------------------------

# Проверяем, существует ли репозиторий
if not os.path.exists(repo_path):
    raise Exception(f"Репозиторий не найден по пути: {repo_path}")

repo = git.Repo(repo_path)

# Определяем текущую ветку
current_branch = repo.active_branch.name
print(f"Текущая ветка: {current_branch}")

# Проверяем, есть ли изменения ДО add
if not repo.is_dirty(untracked_files=True):
    print("Нет изменений для коммита.")
    exit()

# Получаем изменённые файлы до коммита
changed_files = repo.git.status("--porcelain").splitlines()
changed_files = [line[3:] for line in changed_files]  # формат: " M file.txt"

# Добавляем всё
repo.git.add(A=True)

# Коммит
repo.index.commit(commit_message)

# Печать изменённых файлов
print("Закоммичены файлы:")
for f in changed_files:
    print(f" - {f}")

# Пушим
origin = repo.remote(name=remote_name)
push_result = origin.push(current_branch)

print(f"Изменения запушены на {remote_name}/{current_branch}")

