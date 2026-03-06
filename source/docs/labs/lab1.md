# Лабораторная работа №1  
## Тема: Создание сайта для лабораторных работ

---

## Цель работы

- Освоить процесс создания статического сайта с использованием генератора документации MkDocs.


- Научиться организовывать структуру документации проекта (портфолио лабораторных работ).


- Изучить базовые принципы работы с системой контроля версий Git и платформой GitHub.


- Развернуть статический сайт с использованием механизма GitHub Pages на домене вида username.github.io.


- Освоить базовую настройку темы оформления и конфигурационного файла mkdocs.yml.

---

## Задание

- Создать публичный репозиторий на GitHub для размещения сайта-портфолио.

- Настроить GitHub Pages так, чтобы публикация осуществлялась из каталога /docs ветки main.


---

## Исходный код

```
# === Основная информация ===
site_name: Лабораторные работы — Иван Пушкин
site_description: Портфолио лабораторных работ по курсу программирования
site_author: Иван Пушкин

# === Тема Material ===
theme:
  name: material
  language: ru
  palette:
    scheme: slate
    primary: indigo
    accent: amber
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - content.code.copy
    - toc.follow

# === Навигация ===
nav:
  - Главная: index.md
  - Об авторе: about.md
  - Лабораторные работы:
      - Лабораторная работа №1: labs/lab1.md
      - Лабораторная работа №2: labs/lab2.md
      - Лабораторная работа №3: labs/lab3.md
      - Лабораторная работа №4: labs/lab4.md
      - Лабораторная работа №5: labs/lab5.md

# === Расширения Markdown ===
markdown_extensions:
  - codehilite:
      guess_lang: false
      linenums: false
  - tables
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg

# === Отключение поиска ===
plugins:
  - search:
      enabled: false

extra:
  copyright: ""
  generator: false 
```


---

## Выводы

- Для реализации сайта выбрана тема "Materials" как максимально нейтральная

- Статический сайт с использованием GitHub Pages развёрнут

- Освоена базовая настройка темы оформления и конфигурационного файла mkdocs.yml