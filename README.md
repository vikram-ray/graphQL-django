### project for graphQL query

1. clone this repo
2. OPTIONAL: create a virtual env - `python -m venv .venv` and `source .venv.bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate` - to create a Tables in DB
5. create a superuser - `python manage.py createsuperuser`
6. `python manage.py runserver` - start the server
7. Populate data in Movie, Director, Actor from admin - `http://127.0.0.1:8000/admin/`
8. Visit `http://localhost:8000/graphql` to view UI of GrqphiQl
9. Run query `{ movie { name } }` and you should see the result.

OR

10. Visit `http://localhost:8000/graphql#query=%7B%0A%20%20movie%20%7B%0A%20%20%20name%0A%20%20%7D%0A%7D` to see the movie list.

## Notes

1. Added CircleCI - read the config.yaml file
