# codeon

1)  syncdb + создание супер пользователя

2) ссылки для перехода на страницы создания/редактирования/удаления/( а также редактирования в админке) 
доступны только для залогиненого юзера.

3) использование django-command  для  получания списка групп и их студентов

manage.py datalist students   

4) все события   создания / удаления / редактирования  обьектов Студента И Группы  сохраняются в таблицу EventHistory.  Она также добавлена в djnago-admin

пример страницы залогиненого пользователя
https://www.dropbox.com/s/8hylj7h5ap6j350/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%202015-07-30%2000.43.53.png?dl=0

пример страницы не залогиненного пользователя
https://www.dropbox.com/s/x9cipqpt9v6otaf/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%202015-07-30%2000.48.13.png?dl=0

5) все события создания/удаления/редактирования  обьектов Стдента или Группы  созраняются в дополнительную сущьность EventHistory .  Ее также добавил в django-admin
