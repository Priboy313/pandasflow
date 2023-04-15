

##Упаковать сборку в архивы
####(не забудь удалить старую сборку и обновить версию, а то ошибка загрузки)
~~~
python setup.py sdist bdist_wheel
~~~


##Загрузить архивы на TestPypi
~~~
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
~~~