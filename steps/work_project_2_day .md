# Work Project Log — Day 2
Дата: 2025-08-29 10:36

## Що зроблено (підсумок Дня 2)
- **Архітектура multi-company**: додані моделі `Organization`, `Membership`, `Customer`, `Product`, `Order`, `OrderItem` (ізоляція по `organization`).
- **API (DRF)**: підключені `CustomerViewSet` і `ProductViewSet` через базовий `OrgScopedModelViewSet`.
- **Маршрути**: у `tracker/urls.py` зареєстровано `categories`, `entries`, `customers`, `products`.
- **Міграції**: виконано `makemigrations` → `migrate` (створені індекси та унікальні обмеження по `organization`).
- **Дані**: створено `Organization: Default Org`, `Membership: (admin → Default Org, Owner)`.
- **JWT**: отримання токена і доступ до захищених ендпоінтів.
- **Кирилиця/UTF-8**: 
  - виявлено проблему із PowerShell (кракозябри/`????`);
  - підтверджено, що **бекенд/БД ОК** (створення записів через Django shell і адмінку показує нормальну кирилицю);
  - налаштовано стабільну відправку даних як **UTF-8 bytes** з `Content-Type: application/json; charset=utf-8`;
  - додано рекомендації для VS Code (files.encoding=utf8, terminal UTF-8).
- **Перевірки**:
  - `GET /api/customers/` та `GET /api/products/` = 200 OK (спочатку порожньо);
  - `POST /api/customers/` (ТОВ Ромашка, ТОВ Лаванда) — створюються з коректною кирилицею;
  - `POST /api/products/` (Товар 100 та ін.) — створюються з коректною кирилицею.
- **Замовлення**: через /admin створено `Order` із `OrderItem` (Product: «Товар 100», Qty: 2, Price: 199.99).

## Деталі/Команди (корисно для повторення)
```powershell
# JWT
$body = @{ username="admin"; password="***" } | ConvertTo-Json
$resp = Invoke-RestMethod -Uri "http://127.0.0.1:8000/auth/jwt/create" -Method Post -ContentType "application/json" -Body $body
$token = $resp.access
$headers = @{ Authorization = "Bearer $token" }

# Перевірка API
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/customers/" -Headers $headers
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/products/" -Headers $headers

# Відправка UTF-8 байтами (приклад створення продукту)
$json  = @{ sku="SKU-100"; name="Товар 100"; price="199.99"; category="Основні" } | ConvertTo-Json -Depth 5 -Compress
$bytes = [System.Text.Encoding]::UTF8.GetBytes($json)
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/products/" -Method Post -Headers $headers -ContentType "application/json; charset=utf-8" -Body $bytes
```

## Технічні нотатки/ризики, виявлені на Д2
- **Кодування в PowerShell**: без явного UTF-8 були «кракозябри». Вирішено через:
  - `chcp 65001`, встановлення Input/OutputEncoding в UTF-8 і відправку **байтів** UTF-8;
  - альтернатива — Postman або VS Code REST Client (UTF-8 by default).
- **Root API `/api/`**: іноді показував не всі лінки — напряму перевіряємо `.../customers/`, `.../products/`.
- **Токен**: у нових терміналах змінна `$headers` відсутня → перевидавати токен.

---

## План на День 3 (фокус: UI кабінету + SEO-основа публічного сайту)
### 1) Кабінет `/app/<org>/...` (мінімальний скелет)
- `templates/app/base_app.html` + базова навігація (Dashboard, Customers, Products, Orders).
- `templates/app/{dashboard.html, customers_list.html, products_list.html}` — порожні таблиці з даними через DRF (read-only).
- Route-стаб: `path("app/<str:org>/dashboard/", TemplateView(...))`.

### 2) Публічний сайт (SEO базис)
- `templates/public/base.html` з блоками: `<title>`, `meta description`, OpenGraph/Twitter, `canonical`.
- `sitemap.xml` (`django.contrib.sitemaps`) і статичний `robots.txt`.
- Сторінки: Home, Features, Pricing, FAQ, About, Contacts (з унікальними title/description).

### 3) Полірування бекенду
- Автообчислення `Order.total_amount` (signal або override `save()`).
- Виправлення назв у адмінці: `verbose_name_plural = "Categories" / "Time entries"`.

### Definition of Done (Д3)
- Рендериться `/app/<org>/dashboard/` (порожній стан) + посилання на списки Customers/Products.
- Усі публічні сторінки мають унікальні `<title>`/`meta description`, доступний `sitemap.xml`, `robots.txt`.
- Створено 1–2 записи через UI (read-only списки), бекенд незмінно працює з UTF-8.
- Коміт із позначкою: `Day 3: app skeleton + SEO base`.

## Що надати в новому чаті (щоб швидко втягнутись)
- Цей файл **work_project_2_day.md**.
- Поточні `tracker/urls.py`, `views.py`, `models.py`, `serializers.py` (якщо були зміни).
- `settings.py` (блоки `INSTALLED_APPS`, `REST_FRAMEWORK`, `TEMPLATES`).

