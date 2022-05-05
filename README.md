# minicraig
an extremely minimalistic "anyonymous discussion board" CRUD app showcasing Django class-based views and server-side template rendering

# local run instructions:
======
- this was developed using python 3.10 on macosx 
- db is expected to be called 'assessment4'
- gonna want you a `postgresql` server running
- `createdb assessment4`
- create a venv `python -m venv ~/path_to_wherever_you_want`
- activate that venv `source ~/wherever_you_put_the_last_thing/bin/activate`
- install all dependencies with `pip install -r requirements.txt`
- project is called minicraig, which contains only a single app called minicraig_site
- inside minicraig site, there is some starter data under fixtures which is named seed.json
- `cd assessment4` if you haven't already
- `python manage.py migrate` to get that db in shape
- `python manage.py loaddata seed`
- new terminal tab and `psql assessment4` to verify that stuff is in there with `\d`
- `python manage.py runserver` and then open localhost:8000 in a new window in (so you can see the page titles i came up with) your browser of choice, mine is Brave
- start clicking and typing away
