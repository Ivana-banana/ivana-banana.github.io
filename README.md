# ivana-banana.github.io

Сайт-визитка Ивана Пушкина: достижения, хакатоны с командой [«недовосторг»](https://nedovost.org) и отчёты по лабораторным работам.

**Сайт:** https://ivana-banana.github.io

## Локальный запуск

```bash
pip install -r requirements.txt
mkdocs serve -f source/mkdocs.yml
```

Исходники страниц — в `source/docs`, конфиг — `source/mkdocs.yml`.
При пуше в `main` GitHub Actions собирает сайт и публикует его в ветку `gh-pages`.
