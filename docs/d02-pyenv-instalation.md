# Python and Virtual Environments

A virtual environment is a tool that isolates your Python development projects from your system installed Python and other Python environments. This gives you full control of your project and makes it easily reproducible. Any changes on dependencies installed in a virtual environment won't affect the dependencies of other virtual environments or system-wide libraries.

[<img src="https://www.dataquest.io/wp-content/uploads/2022/01/python-virtual-envs1-1024x576.webp" width="800"/>](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/#:~:text=NOTE%20A%20Python%20project%20folder,in%20a%20virtual%20environment%20folder.)

## Why do we need Virtual Environments?

1. They solve dependency problems allowing to use different versions of a package. For example, using the package A v2.7 for project X and the package A v1.3 for the project Y. 
2. They allow that each project is independent and reproducible capturing all the dependencies of the packages in one requirement files. 
3. The facilitate the order of the site-package global directory, because they eliminate the necesity of installing packages in the main system, when you might just require it for one project. The other use case that magnifies the importance of using Python virtual environments is when you’re working on managed servers or production environments where you can’t modify the system-wide packages because of specific requirements.
4. This would lead to compatibility issues because Python cannot simultaneously use multiple versions of the same package.


Python virtual environments create isolated contexts to keep dependencies required by different projects separate so they don't interfere with other projects or system-wide packages. Basically, setting up virtual environments is the best way to isolate different Python projects, especially if these projects have different and conflicting dependencies. As a piece of advice for new Python programmers, always set up a separate virtual environment for each Python project, and install all the required dependencies inside it — never install packages globally.

## Virtualenv vs pyenv, which one to use?

### [Virtualenv](https://pypi.org/project/virtualenv/)

Creates different virtual environments in the Python version of your system and has a very simple instalation.

#### Instalation

```
pip install virtualenv
```

Create a virtual environment

```
virtualenv <my_env_name>
```

Activate virtualenv

```
source <my_env_name>/bin/activate
```

Deactivate

```
deactivate
```


### [Pyenv](https://github.com/pyenv/pyenv)

Switch easily between multiple **versions of python** and virtual environments. 


#### Instalation

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



## Instalar un ambiente virtual con una versión de Python específica. 

1. Primero instalamos el Python con el que trabajaremos, en este caso estamos utilizando la versión 3.8.6, pero ésta puede cambiar dependiendo de las necesidades del proyecto. 

```
pyenv install 3.8.6
```

2. Crear un ambiente virtual. Por cada proyecto en el cuál se esté involucrado, es recomendable crear un ambiente virtual.

```
pyenv virtualenv 3.8.6 <nombre_ambiente>
```

3. Verifica que instalaste bien tu pyenv con la siguiente línea que enlista todos los ambientes que tienes:

```
pyenv virtualenvs
```

## Activar y desactivar un pyenv de manera automática

Dentro del archivo `.python-version` solo colocas el nombre del ambiente virtual que quieres que se active por default en el directorio correspondiente al proyecto. Para hacer este archivo:  

1. Situarse en el directorio raíz del proyecto:

```
cd <nombre_repositorio>
```

2. Editar el archivo `.python-version`:

```
nano .python-version
```

3. Dentro del archivo solo escribes:

```
<nombre_ambiente>
```

Se guardan modificaciones con ^X y cierras el archivo.




##### Extra: Activar y desactivar un pyenv de manera manual

Para activar un ambiente virtual tienes que situarte en el proyecto de interés y activar ambiente virtual.

```
pyenv activate <nombre_ambiente>
```

y para desactivarlo es con: 

```
pyenv deactivate <nombre_ambiente>
```
