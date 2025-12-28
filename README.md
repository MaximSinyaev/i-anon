# И-Анон Казахстан

Официальный сайт объединения И-Анон в Казахстане - программа восстановления для родственников и друзей людей с компульсивной игроманией.

## О проекте

Этот сайт построен с использованием [Hugo](https://gohugo.io/) - быстрого генератора статических сайтов и публикуется через GitHub Pages.

## Локальная разработка

### Предварительные требования

- Hugo версии 0.153.3 или выше (с extended версией)
- Git

### Запуск локально

1. Клонируйте репозиторий:
```bash
git clone --recurse-submodules <URL-вашего-репозитория>
cd ianon
```

2. Запустите локальный сервер:
```bash
hugo server -D
```

3. Откройте браузер по адресу: http://localhost:1313

### Редактирование контента

Все страницы находятся в директории `content/`:

- `content/_index.md` - главная страница
- `content/what-is-gambling.md` - Что такое компульсивная игромания?
- `content/how-ianon-helps/` - раздел "И-анон может помочь" со всеми подстраницами
  - `is-it-for-me.md` - Подходит ли мне И-анон?
  - `can-your-child.md` - Может ли ваш ребенок быть компульсивным игроком?
  - `how-it-affects-us.md` - Как на нас влияет компульсивная игровая зависимость близких
  - `grew-up-near.md` - Вы росли рядом с компульсивным игроком
  - `faq.md` - Часто задаваемые вопросы
  - `ten-good-words.md` - Десять хороших слов о сообществе И-Анон
  - `ianon-suggestions.md` - Предложения И-анон
  - `brief-overview.md` - Краткий обзор инструментов И-анон
- `content/twelve-steps.md` - Двенадцать Шагов И-анон
- `content/twelve-traditions.md` - Двенадцать Шагов к Единству И-анон
- `content/literature.md` - Литература И-анон
- `content/contacts.md` - Контакты И-анон в Казахстане

Для редактирования откройте нужный `.md` файл и измените содержимое между `---` разделителями.

### Добавление логотипа

Поместите ваш логотип в `static/images/logo.png`

## Публикация

Сайт автоматически публикуется на GitHub Pages при каждом push в ветку `main`.

### Первоначальная настройка GitHub Pages

1. Создайте репозиторий на GitHub (например, `ianon-kz/ianon-kz.github.io`)

2. Добавьте remote и сделайте первый push:
```bash
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/ianon-kz/ianon-kz.github.io.git
git branch -M main
git push -u origin main
```

3. В настройках репозитория на GitHub:
   - Перейдите в **Settings** → **Pages**
   - В разделе **Source** выберите **GitHub Actions**

4. Подождите несколько минут - сайт появится по адресу: `https://ianon-kz.github.io/`

### Настройка собственного домена

1. В настройках репозитория: **Settings** → **Pages** → **Custom domain**

2. Введите ваш домен (например, `ianon.kz`)

3. У вашего регистратора домена добавьте DNS записи:
   
   **Для домена без www (ianon.kz):**
   ```
   Тип: A
   Имя: @
   Значение: 185.199.108.153
   Значение: 185.199.109.153
   Значение: 185.199.110.153
   Значение: 185.199.111.153
   ```

   **Для www поддомена (www.ianon.kz):**
   ```
   Тип: CNAME
   Имя: www
   Значение: ianon-kz.github.io
   ```

4. Обновите `baseURL` в `hugo.toml` на ваш домен:
   ```toml
   baseURL = 'https://ianon.kz/'
   ```

5. Создайте файл `static/CNAME` с вашим доменом:
   ```
   ianon.kz
   ```

6. Commit и push изменений

7. В настройках GitHub Pages отметьте "Enforce HTTPS" (может потребоваться подождать до 24 часов)

## Структура проекта

```
ianon/
├── .github/
│   └── workflows/
│       └── hugo.yml          # GitHub Actions для деплоя
├── content/                   # Контент сайта в Markdown
│   ├── _index.md             # Главная страница
│   ├── how-ianon-helps/      # Раздел с подстраницами
│   └── ...                   # Другие страницы
├── static/                    # Статические файлы (изображения, favicon)
├── themes/                    # Темы Hugo
│   └── ananke/               # Используемая тема
├── hugo.toml                 # Конфигурация сайта
└── README.md                 # Этот файл
```

## Поддержка

При возникновении вопросов обращайтесь к [документации Hugo](https://gohugo.io/documentation/) или [GitHub Pages](https://docs.github.com/pages).
