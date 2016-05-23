=====
Merge
=====

Merge is a Django app to perform document template/data merge

Quick start
-----------

1. Add "merge" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'merge',
    ]

2. Include the merge URLconf in your project urls.py like this::

    url(r'^merge/', include('merge.urls')),

3. Run `python manage.py migrate` to create the merge models.

