# Work Project Log — Day 1 (2025-08-28)

## Що зроблено
- Створено репозиторій Git (`.gitignore` налаштовано, середовище `.venv` виключено з трекінгу).
- Ініціалізовано Django-проєкт `core` та додаток `tracker`.
- Налаштовано `settings.py`: підключено `rest_framework`, `corsheaders`, `djoser`, `tracker`; додано конфігурацію для JWT та CORS.
- Виконано базові міграції, створено суперкористувача, налаштовано адмінку.
- Додано моделі:
  - `Category` (user, name, color, created_at)
  - `TimeEntry` (user, category, started_at, ended_at, note, created_at)
- Зроблено міграції для моделей.
- Додано `serializers.py` для `Category` і `TimeEntry`.
- Додано `views.py` з `CategoryViewSet` та `TimeEntryViewSet` (фільтрація по користувачу).
- Додано `tracker/urls.py` з DRF `DefaultRouter` для маршрутів `/api/categories/` та `/api/entries/`.
- Підключено Djoser для auth та JWT: `/auth/users/`, `/auth/jwt/create`.
- Перевірено роботу API:
  - Реєстрація/логін користувачів через JWT.
  - Створення категорій і записів часу (прив’язка до користувача).
  - Отримання списків категорій та записів.
- Протестовано через PowerShell (`Invoke-RestMethod`) і Django Admin.

## Проблеми та рішення
- **Git зациклював .venv** → виправлено `.gitignore` та перезаписано в ASCII.
- **Windows PowerShell і кирилиця в JSON** → текст відображається «кракозябрами». Вирішується через VS Code REST Client/Postman. В адмінці дані зберігаються коректно.
- **Помилка `tracker.urls`** → створено файл `tracker/urls.py` з роутером.

## Definition of Done (День 1)
- ✅ Репозиторій з README та .gitignore.
- ✅ Django-проєкт + app `tracker`.
- ✅ Auth через Djoser + JWT.
- ✅ Моделі Category і TimeEntry + міграції.
- ✅ Адмінка працює, суперкористувач створений.
- ✅ API для створення/отримання даних (прив’язка до користувача).

---

## Наступні кроки (День 2 план)
- Тестування CRUD через REST Client/Postman (з кирилицею).
- Мінімальний фронтенд (React/Next.js): логін + перегляд категорій і записів.
- Почати планувати Summary (AI-аналітику часу).

