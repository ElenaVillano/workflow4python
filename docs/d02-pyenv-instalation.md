# [Pyenv](https://github.com/pyenv/pyenv)

Switch easily between multiple **versions of python** and virtual environments. 


## Instalation

0. Requirements for Ubuntu:

```
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

1. Be sure to be at the root of your computer: 

```
cd 
```

2. Clone the pyenv repository

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

3. Set up your shell environment for Pyenv. Define environment variable `PYENV_ROOT` to point to the path where Pyenv will store its data. `$HOME/.pyenv` is the default.

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
```

4. Add the pyenv executable to your `PATH`:

```
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
```

5. Write this additional comment on the ~/.bashrc file. 

```
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc 
```

6. Restart your sheel:
```
exec "$SHELL"
```

7. Clone pyenv-virtualenv:

```
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

8. More into your ~/.bashrc file:

```
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc 
```

9. Restart your sheel:

```
exec "$SHELL"
```

10. Check instalation: 

```
pyenv install -l
```


### Create a virtual environment with an especific Python version. 

1. Example installing python 3.8.6: 

```
pyenv install 3.8.6
```

2. Create a virtualenv with a python version.

```
pyenv virtualenv 3.8.6 <nombre_ambiente>
```

3. Verify your instalation

```
pyenv virtualenvs
```

## Activate y deactivate a pyenv automatically

Create a `.python-version` file and write the name of the virtualenv that you created. 

1. Go to the root of the project: 

```
cd <repository-name>
```

2. Edit the `.python-version` file:

```
nano .python-version
```

3. Write the name of the virtualenv:

```
<environment-name>
```

4. You'll see how whenever you get into that folder the environment is going to be activated. The recomendation is to create a virtual environment for each project that you have. Example of your virtualenvs. 


##### Extra: Activate and deactivate a pyenv in a manual way. 


```
pyenv activate <environment-name>
```


```
pyenv deactivate  <environment-name>
```
