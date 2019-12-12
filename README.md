# controlq API

## Python Version Management

First of all, you may need to install [pyenv](https://github.com/pyenv/pyenv) in order to manage multiple version of python.
It is not necessary.
pyenv can be installed via brew 
```bash
$ brew install pyenv
```
Windows
```CMD
$ pip install pyenv-win
```
Pipenv installation
```bash
$ pip install pipenv
```
pipenv installation(if you need)
`pip install pipenv`

### Install the Python version with pyenv(it is not necessary as long as you use python 3.6.9).
step 1
`pyenv install 3.6.9`
step 2
`pyenv local 3.6.9`

#### Python Package Management.
This project uses pipenv for managing our packages and creating virtual environment to isolate our dependencies. If you have installed pipenv it should be as simple as:

install the dependencies.
`pipenv install -d`

In case you you are not sure which version of pyenv you are running this command can help you to sort it out. -rm will remove the virtual environment and start it again.

```bash
$ pyenv install 3.6.9
$ pyenv local 3.6.9
$ pipenv --rm
$ pipenv --python 3.6.9
$ pipenv install -d
```

##### API documentation.
There is swagger and redocs as options.

http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/

###### Run Migrations and start Django.
 Once your dependencies are sorted run the command
 ```bash
 $ pipenv shell
 $ python manager.py migrate
 $ python manager.py runserver
```

You should get this confirmation.

```bash
$ System check identified no issues (0 silenced).
$ December 12, 2019 - 09:41:34
$ Django version 3.0, using settings 'control_q.settings'
$ Starting development server at http://127.0.0.1:8000/
$ Quit the server with CONTROL-C.
```

###### Comments
contact: gilsondia@gmail.com
phone: 0415 691 863


