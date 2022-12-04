# datadumper

A file dumping application written in Django.

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

2. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

3. Install local postgres:

    ```
    $ docker run --name datadumper-postgres -p 5432:5432 \
    -e POSTGRES_USER=datadumper -e POSTGRES_PASSWORD=complexpassword123 \
    -e POSTGRES_DB=datadumper -d postgres
    ```
    To check if docker container is running:

    ```
    $ docker ps -f name=datadumper-postgres
    ```

4. Apply migrations:

    ```
    (venv)$ python manage.py makemigrations
    (venv)$ python manage.py migrate
    ```

5. Run the server:

    ```sh
    (venv)$ python manage.py runserver
    ```
    
6. Navigate to [http://localhost:8000/](http://localhost:8000/) in your favorite web browser.

## Notes

```
If you get a DisallowedHost error, add localhost and 127.0.0.1 to ALLOWED_HOSTS inside core/settings.py.
```

```
An alternative to creating a createsu command is to SSH into one of the EC2 instances and run Django's default createsuperuser command.
```