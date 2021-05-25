# Комп'ютерний практикум №3

Виконав: Мироненко Роман, КМ-82
    
____
 
 Інструкція з запуску: 
   1) Завантажити даний репозиторій та у папці з ним ініціалізувати git-репозиторій - `git init`
   2) Увійти в акаунт Heroku - `heroku login`
   3) Додати аддон "Heroku Postgres"
   4) Додати зміни - `git add .`
   5) Закомітити - `git commit -am "make it better"`
   6) Задеплоїти - `git push heroku master`

----

Додаток розгорнуто на хмарному хостингу Heroku, його можна відкрити за посиланням: https://db-kp3.herokuapp.com/

---- 

Також, додаток можна запустити на локальному сервері, для цього у файлі *app.py* строчку `app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("postgres", "postgresql")` замінити наступним:`app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:port/bdname'`

