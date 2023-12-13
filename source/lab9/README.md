Лабораторна робота № 9. Створення та рефакторінг програмно-інформаційного продукту засобами Python

Мета: розробка програмно-інформаційного продукту засобами Python 
План роботи
Завдання 1. Створити скрипт запуску лабораторних робіт 1-8 (Runner) з єдиним меню для управління додатками використовуючи патерн FACADE https://refactoring.guru/uk/design-patterns/facade

Завдання 2. Зробити рефакторінг додатків, які були зроблені в лб 1-8, для підтримки можливості запуску через Runner

Завдання 3. Зробити рефакторинг додатків, які були зроблені в лб 1-8, використовуючи багаторівневу архітектуру додатків (див. приклад нижче) та принципи об’єктно-орієнтованого підходу

Завдання 4. Створити бібліотеку класів, які повторно використовуються у всіх лабораторних роботах та зробити рефакторінг додатків для підтримки цієї бібліотеки. Таких класів в бібліотеці має буде як найменш 5

Завдання 5. Додати логування функцій в класи бібліотеки програмного продукту використовуючи https://docs.python.org/uk/3/howto/logging.html

Завдання 6. Додати коментарі до програмного коду та сформувати документацію програмного продукту засобами pydoc. Документація має бути представлена у вигляді сторінок тексту на консолі, подана у веб-браузері та збережена у файлах HTML

Завдання 7. Документація та код програмного продукту має бути розміщено в GIT repo

Завдання 8. Проведіть статичний аналіз коду продукту засобами PYLINT https://pylint.readthedocs.io/en/stable/ та виправте помилки, які були ідентифіковані. Первинний репорт з помилками додайте до звіту лабораторної роботи

Завдання 9. Підготуйте звіт до лабораторной роботи

Приклад організаціі Layered Architecture (LA) of Applications
 Базові рівні додатка:
•  UI
•  BLL 
•  DAL
•  Sources (DB, Files,…) 

Деталі можна прочитати за посиланням https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch01.html
You can use the following approach to create a directory structure for projects:
Project
  Data  // You can save your text files here
    Lab1
    Lab2
    …
Init or Config //- Use JSON to create config file for your App
Shared > // All of classes, that can be used in other lab works 
   >Classes
UI 
>Menu
>MenuBuilder
  Classes  // Special classes for your lab work
Runner > Simple class to run your app (lab work)
*This directory structure can be changed depending on your needs

Налаштування логеру та базові налаштування програмного продукту мають бути в окремому файлі налаштування вашого продукту - config/init/..