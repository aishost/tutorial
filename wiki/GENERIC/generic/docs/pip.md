practice_django

pip install django
# https://django-crispy-forms.readthedocs.io/en/latest/install.html
pip install django-crispy-forms==1.1.13

#https://github.com/un1t/django-cleanup
pip install django-cleanup==5.2.0

pip install pillow

https://pypi.org/project/django-ckeditor/
pip install django-ckeditor

#https://channels.readthedocs.io/en/stable/installation.html
python -m pip install -U channels

#https://django-allauth.readthedocs.io/en/latest/installation.html
pip install django-allauth

## Настройка dotenv

[dotenv](https://pypi.org/project/python-dotenv/)

`pip install python-dotenv`

```python


from pathlib import Path
import os
from dotenv import load_dotenv
from django.contrib.messages import constants as messages

# Loading ENV
env_path = Path('.') / '.env'

#env_path = '.test.env'
load_dotenv(dotenv_path=env_path)
```





#https://django-braces.readthedocs.io/en/latest/
pip install django-braces

pip install mkdocs
https://www.mkdocs.org/

pip install mkdocs-awesome-pages-plugin

https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin


pip install mkdocs-material
https://squidfunk.github.io/mkdocs-material/getting-started/