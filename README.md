# Городской кочевник — интерактивный дашборд

Готовый дашборд находится в `index.html`. Он использует Vue 3 и D3.js v7 через CDN, а данные и изображения загружаются из соседних файлов `data.json` и `images.json`.

## Структура данных

`data.json` — массив строк заказа:

```json
{
  "order": "210902-646-9623",
  "date": "2021-09-02",
  "status": "доставлен",
  "created": "0.6159",
  "delivered": "0.6416",
  "address": "...",
  "name": "Название позиции",
  "category": "Категория",
  "price": 99,
  "discountPrice": 79,
  "discount": 20,
  "quantity": 1,
  "total": 79
}
```

`images.json` — объект соответствия числового префикса файла изображения его локальному пути. В интерфейсе изображения назначаются товарным карточкам детерминированно, чтобы все позиции получили визуальный маркер.

## Что реализовано

- KPI: уникальные заказы, сумма трат и средняя скидка.
- Динамика по месяцам за последние 24 месяца с выбором метрики.
- Наведение на точку/месяц на графике динамики показывает вертикальный маркер, месяц и точное значение.
- Топ позиций по количеству или сумме.
- Множественная интерактивная фильтрация по категориям с пересчётом всех показателей.
- Таблица категорий с тратами, заказами, средней позицией и долей.
- Локальные изображения товаров из `items`.
- Tooltip товара с мини-графиком изменения цены.
- Адаптивный премиальный тёмный интерфейс.

## Обновление данных из Excel

При изменении `df.xlsx` запустите из папки проекта:

```bash
python build_data.py
```

Скрипт преобразует лист Excel в `data.json` и заново создаёт `images.json`.

## Проверка локально

```bash
python -m http.server 8765
```

Откройте `http://localhost:8765/`. Запуск через HTTP-сервер нужен, потому что браузер блокирует `fetch()` локальных JSON-файлов при открытии HTML двойным щелчком.

## Публикация на GitHub Pages

### Вариант A — через GitHub Desktop

1. Войдите в GitHub и нажмите **New repository**.
2. Назовите репозиторий, например `city-nomad-dashboard`, выберите **Public**. Не добавляйте README автоматически, если он уже есть в этой папке.
3. Установите GitHub Desktop и выберите **File → Add local repository**.
4. Укажите папку проекта `Visualizations`. Если GitHub Desktop предложит создать репозиторий, подтвердите.
5. В поле summary введите `Create analytics dashboard` и нажмите **Commit to main**.
6. Нажмите **Publish repository**, выберите созданный репозиторий и оставьте его публичным.
7. На GitHub откройте **Settings → Pages**.
8. В **Build and deployment** выберите **Deploy from a branch**, ветку `main`, папку `/ (root)` и нажмите **Save**.
9. Через 1–3 минуты откройте адрес `https://ВАШ_ЛОГИН.github.io/city-nomad-dashboard/`.

### Вариант B — через командную строку Git

Откройте PowerShell в папке проекта и выполните команды. Замените URL на адрес своего репозитория:

```powershell
cd "C:\Users\ASUS Tuf F15\Documents\Visualizations"
git init
git branch -M main
git add index.html data.json images.json README.md items build_data.py
git commit -m "Create interactive order dashboard"
git remote add origin https://github.com/ВАШ_ЛОГИН/city-nomad-dashboard.git
git push -u origin main
```

Если Git запросит авторизацию, войдите через браузер GitHub или используйте GitHub CLI:

```powershell
gh auth login
gh repo create city-nomad-dashboard --public --source=. --remote=origin --push
```

После `push` включите **Settings → Pages → Deploy from a branch → main → /(root)**. В репозитории должна лежать именно такая структура:

```text
index.html
data.json
images.json
items/
```

Не переименовывайте папку `items`: пути к изображениям в `images.json` относительные. Проверяйте готовую ссылку в режиме «Инкогнито»; если страница пустая, откройте DevTools → Console и проверьте, что `data.json` и `images.json` не возвращают ошибку 404.

Для сдачи скриншот назовите в формате: **«Неделя 4. Имя и Фамилия»**.
