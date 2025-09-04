# 📝 Шаблон коміт-повідомлень (Conventional Commits)

```
<тип>: <короткий опис змін>

[Детальний опис (опціонально)]
```

---

## 🔹 Типи змін (з прикладами під Django)

| Тип        | Коли використовувати                                    | Приклад                                      |
|------------|----------------------------------------------------------|----------------------------------------------|
| **feat:**  | нова фіча, функціонал                                   | `feat: add tracker serializers and views`    |
| **fix:**   | виправлення багу                                        | `fix: correct url path for login view`       |
| **chore:** | рутинні зміни, конфіги, скрипти, .gitignore             | `chore: update .gitignore for venv`          |
| **docs:**  | документація, README, коментарі                         | `docs: add API usage examples to README`     |
| **style:** | форматування, пробіли, лапки, PEP8                      | `style: reformat views.py with black`        |
| **refactor:** | переписування коду без зміни логіки                   | `refactor: extract common logic to base view`|
| **test:**  | тести, фікстури                                         | `test: add unit tests for Category model`    |
| **build:** | залежності, requirements.txt                            | `build: upgrade Django to 5.0.1`             |
| **perf:**  | оптимізації швидкодії                                   | `perf: optimize query in TimeEntry view`     |

---

## 🔹 Приклади правильних комітів
- `feat: add JWT authentication endpoints`  
- `fix: resolve migration conflict for Customer model`  
- `chore: configure pre-commit hooks for black`  
- `docs: add installation steps to project_master_plan_full.md`  
- `refactor: simplify serializer logic`  
- `test: add API tests for TimeEntry CRUD`  

---

## 🔹 Формат для довгого коміту
```
feat: add dashboard templates

- created base_app.html
- added dashboard.html with sidebar
- connected template inheritance
```
