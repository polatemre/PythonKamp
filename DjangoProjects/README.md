# Django projesi olusturma
```properties
foo@bar:~$ django-admin startproject bookstore
```
# Çalıştırma (proje içinde)
```properties
foo@bar:~$ python manage.py runserver
```
# Uygulama oluşturma
```properties
foo@bar:~$ python manage.py startapp <uygulama_adi>
foo@bar:~$ python manage.py startapp books
```
# Veritabanı oluşturma (ilk defa oluşturacaksak veya yaptığımız değişikliklerin veritabanına yansıması için kullanılır)
```properties
foo@bar:~$ python manage.py migrate
```
# Eklediğimiz uygulama entitylerinin migrationlarını oluşturur
```properties
foo@bar:~$ python manage.py makemigrations <uygulama_adi>
foo@bar:~$ python manage.py makemigrations books
```
# Oluşturduğumuz migrationları veritabanına gönderir
```properties
foo@bar:~$ python manage.py sqlmigrate <uygulama_adi> <migration_ismi>
foo@bar:~$ python manage.py sqlmigrate books 0001
```
# ORM kullanmak için
```properties
foo@bar:~$ python manage.py shell
foo@bar:~$ from books.models import Author, Book
foo@bar:~$ from django.utils import timezone
foo@bar:~$ author = Author(name="Victor Hugo",created=timezone.now())
foo@bar:~$ author.save()
foo@bar:~$ author.name="Yaşar Kemal"
foo@bar:~$ author.save()
foo@bar:~$ Author.objects.all()
```
## ORM Filter kullanımı
```properties
foo@bar:~$ Author.objects.filter(id=1)
foo@bar:~$ Author.objects.filter(pk=3)
foo@bar:~$ Author.objects.filter(name__startswith="Yaşar")
foo@bar:~$ Author.objects.filter(created__year=2021)
foo@bar:~$ Author.objects.filter(created__year=timezone.now().year, name__endswith="Kemal")
```
## ORM ile ilişkisel sorgulama yapma
```properties
foo@bar:~$ author = Author.objects.get(id=1)
foo@bar:~$ author.book_set.create(name="Sefiller",created=timezone.now(),price=20) 
```
# Admin paneli şifresi oluşturma
```properties
foo@bar:~$ python manage.py createsuperuser
```