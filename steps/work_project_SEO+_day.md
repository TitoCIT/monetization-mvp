# Work Project Log — Day 3 (2025-08-30)

## Орієнтир
День 3 присвячено **публічному сайту (лендинг + базові сторінки)** на Django Templates + Tailwind і **вбудуванню SEO-основи** з першого дня, без переробок згодом. Кабінет організації поки path-based (`/app/<org>/…`) з `noindex`.

---

## План на день
1) **UI каркас (public site)**
   - Створити `base.html` (Tailwind), компоненти: header (лого, меню), footer, контейнер, кнопки, таблиці.
   - Сторінки: **Home (Landing)**, **Features**, **Pricing**, **FAQ**, **About**, **Contacts**, **Login**, **Register**.
   - Навігація/меню: верхнє, активний стан, адаптивність.
   - Порожні сторінки «Blog list / Blog post» (каркас під майбутній контент).

2) **Auth сторінки (стилізація)**
   - Шаблони логіну/реєстрації/відновлення паролю (використати стандартні Django views, оформити під загальний стиль).
   - Redirection після логіну в `/app/<active_org>/dashboard/` (тимчасово — `/app/default/dashboard/`).

3) **SEO-основа (технічне)**
   - Чисті URL: name-based routes, слуги для блогу (резерв).
   - **`<title>` + `meta description`** як блоки у `base.html` + контекст-процесор для `canonical_url`.
   - **Open Graph/Twitter** мета у `base.html`.
   - **Sitemap/robots**: `django.contrib.sitemaps`, `sitemap.xml`, `robots.txt`.
   - **Breadcrumbs** (хлібні крихти) у layout.
   - **JSON-LD**: `Organization`, `BreadcrumbList` (через шаблонний контекст).
   - **noindex** для `/app/...`, `/admin/`, `/auth/...`.

4) **Кабінет (мінімум UI)**
   - `templates/app/base_app.html` (header з перемикачем організації — поки заглушка).
   - Сторінки: **Dashboard (порожній стан)**, **Customers list**, **Products list** (по 1 шаблону-таблиці).
   - Лейаут/меню для `/app/<org>/…` (окремо від публічного).

5) **Тест швидкодії та доступності**
   - Перевірити lazy-load зображень, alt-тексти, контрастність, фокус-стани.
   - Перевірити рендер без JS (SSR), час першого контенту.

6) **Документація**
   - Описати у README: маршрути публічного сайту, структуру шаблонів, SEO-практики, де лежать sitemap/robots/schema.

---

## Точні кроки (команди/заготовки)
- Tailwind: підключити через CDN на старті (перехід на build пізніше).
- `templates/public/base.html`, `templates/public/partials/{header,footer}.html`.
- `templates/public/{home.html,features.html,pricing.html,faq.html,about.html,contacts.html,login.html,register.html}`.
- `templates/app/{base_app.html,dashboard.html,customers_list.html,products_list.html}`.
- Контекст-процесор `seo_context` → `canonical_url`, `schema_json`.
- `sitemaps.py` (StaticViewSitemap, BlogSitemap-заготовка), `urls.py` → `sitemap.xml`.
- `robots.txt` у static.
- Додати meta-блоки у base.html: title, meta_description, og:*, twitter:*.
- В `views.py` для кожної публічної сторінки передавати `schema_json` (Organization/BreadcrumbList).

---

## Definition of Done (День 3)
- Публічні сторінки **Home/Features/Pricing/FAQ/About/Contacts/Login/Register** відмальовуються з єдиним лейаутом.
- У кожної сторінки є унікальні `<title>` та `meta description` (через блоки/контекст).
- `sitemap.xml` і `robots.txt` доступні; `/app/` розмічено `noindex`.
- JSON-LD `Organization` + `BreadcrumbList` на публічних сторінках.
- Кабінет `/app/<org>/dashboard/` рендериться (порожній стан) з меню.
- README оновлено розділом «Публічний сайт та SEO-основа».

---

## Проблеми/ризики (позначити під час робіт)
- Tailwind через CDN: може бути ліміт кастомізації → за необхідності перейти на build-конфіг у Спринті 2.
- Дубль-контент (якщо додамо варіанти URL): одразу слідкувати за canonical.
- Валідація Schema.org (JSON-LD): перевірити валідатором; якщо будуть попередження — виправити в беклозі.

---

## Беклог / Примітки на наступні дні
- Перехід на subdomains для організацій (`<org>.domain.com`) + канонікали.
- Блог (CRUD з адмінки), OG-ізображення генератор.
- `FAQPage` (JSON-LD) і сторінка політики конфіденційності/умов.
- Локалізація та `hreflang` (EN/PL).
- Build Tailwind (purge, minify), критичні CSS у head.
- Компоненти для форм/валідацій (уніфіковані шаблони).
- Accessibility-аудит (повний) і перевірка Core Web Vitals на проді.
