#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для извлечения контента из HTML файлов Google Sites
и создания markdown файлов для Hugo
"""

import os
from pathlib import Path
from bs4 import BeautifulSoup

# Маппинг файлов HTML -> Markdown
FILE_MAPPING = {
    "главная-страница.html": ("content/_index.md", "Главная страница"),
    "главная-страница/что-такое-компульсивная-игромания.html": ("content/what-is-gambling.md", "Что такое компульсивная игромания?"),
    "главная-страница/3.html": ("content/how-ianon-helps/_index.md", "И-Анон может помочь"),
    "главная-страница/3/подходит-ли-мне-и-анон.html": ("content/how-ianon-helps/is-it-for-me.md", "Подходит ли мне И-Анон?"),
    "главная-страница/3/может-ли-ваш-ребенок-быть-компульсивным-игроком.html": ("content/how-ianon-helps/can-your-child.md", "Может ли ваш ребенок быть компульсивным игроком?"),
    "главная-страница/3/как-на-нас-влияет-компульсивная-игровая-зависимость-близких.html": ("content/how-ianon-helps/how-it-affects-us.md", "Как на нас влияет компульсивная игровая зависимость близких"),
    "главная-страница/3/вы-росли-рядом-с-компульсивным-игроком.html": ("content/how-ianon-helps/grew-up-near.md", "Вы росли рядом с компульсивным игроком"),
    "главная-страница/3/часто-задаваемые-вопросы.html": ("content/how-ianon-helps/faq.md", "Часто задаваемые вопросы"),
    "главная-страница/3/десять-хороших-слов-о-сообществе-и-анон.html": ("content/how-ianon-helps/ten-good-words.md", "Десять хороших слов о сообществе И-Анон"),
    "главная-страница/3/предложения-и-анон.html": ("content/how-ianon-helps/ianon-suggestions.md", "Предложения И-Анон"),
    "главная-страница/3/краткий-обзор-инструментов-и-анон.html": ("content/how-ianon-helps/brief-overview.md", "Краткий обзор инструментов И-Анон"),
    "главная-страница/двенадцать-шагов-и-анон.html": ("content/twelve-steps.md", "Двенадцать Шагов И-Анон"),
    "главная-страница/двенадцать-шагов-к-единству-и-анон.html": ("content/twelve-traditions.md", "Двенадцать Шагов к Единству И-Анон"),
    "главная-страница/литература-и-анон.html": ("content/literature.md", "Литература И-Анон"),
    "главная-страница/контакты-и-анон-в-казахстане.html": ("content/contacts.md", "Контакты И-Анон в Казахстане"),
}

def extract_text_from_html(html_content):
    """Извлекает текстовый контент из HTML используя BeautifulSoup"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Ищем все параграфы с классом zfr3Q (основной класс для контента в Google Sites)
    paragraphs = soup.find_all('p', class_='zfr3Q')
    
    # Также ищем заголовки h1-h6 с классом zfr3Q
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'], class_='zfr3Q')
    
    content_lines = []
    
    # Добавляем заголовки
    for h in headings:
        text = h.get_text(strip=True)
        if text and text not in ['ЧТО ТАКОЕ КОМПУЛЬСИВНАЯ ИГРОМАНИЯ?']:  # Пропускаем дубликаты заголовков
            content_lines.append(f"## {text}")
            content_lines.append("")
    
    # Добавляем параграфы
    for p in paragraphs:
        text = p.get_text(strip=True)
        if text:
            content_lines.append(text)
            content_lines.append("")  # Пустая строка между параграфами
    
    return "\n".join(content_lines)

def create_markdown_file(md_path, title, content):
    """Создает markdown файл с frontmatter"""
    # Создать директории если нужно
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    
    # Формат markdown с frontmatter
    markdown_content = f"""---
title: "{title}"
date: 2025-12-27
draft: false
---

{content}
"""
    
    # Записать файл
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✓ Создан: {md_path}")

def main():
    base_path = Path("temp_old_site/sites.google.com/view/i-anon-kz")
    
    print("Начинаем извлечение контента...\n")
    
    for html_file, (md_file, title) in FILE_MAPPING.items():
        html_path = base_path / html_file
        
        if not html_path.exists():
            print(f"✗ Не найден: {html_path}")
            continue
        
        # Читаем HTML
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Извлекаем контент
        content = extract_text_from_html(html_content)
        
        if not content:
            print(f"⚠ Контент не найден в: {html_file}")
            content = "(Контент будет добавлен позже)"
        
        # Создаем markdown
        create_markdown_file(md_file, title, content)
    
    print("\n✅ Готово!")

if __name__ == "__main__":
    main()
