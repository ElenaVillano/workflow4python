# Python and Virtual Environments

A virtual environment is a tool that isolates your Python development projects from your system installed Python and other Python environments. This gives you full control of your project and makes it easily reproducible. 

[<img src="https://www.dataquest.io/wp-content/uploads/2022/01/python-virtual-envs1-1024x576.webp" width="65"/>](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/#:~:text=NOTE%20A%20Python%20project%20folder,in%20a%20virtual%20environment%20folder.)

- Requirements for Ubuntu:

```
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

```
pyenv install -l
```

## ¿Por qué necesitamos un ambiente virtual? 

Imagine un escenario en el que está trabajando en dos proyectos Python y uno de ellos usa Pandas 1.9 y el otro usa Pandas 1.10. En tales situaciones, el ambiente virtual puede ser realmente útil para mantener las dependencias de ambos proyectos. En particular, los ambientes virtuales son soluciones simples que: 

> 1. Resuelven problemas de dependencia al permitirle usar diferentes versiones de un paquete para diferentes proyectos. Por ejemplo, podría usar el Paquete A v2.7 para el Proyecto X y el Paquete A v1.3 para el Proyecto Y. 
>  2. Permiten que cada proyecto sea independiente y reproducible capturando todas las dependencias de los paquetes en un archivo de requisitos. 
> 3. Facilitan el ordenamiento el directorio global site-packages/ al eliminar la necesidad de instalar paquetes en todo el sistema, que es posible que solo necesite para un proyecto.

## Instalar pyenv

La instalación de pyenv solo será necesario hacerlo una única vez al inicio de tu set up de bastión. 

1. Situarse sobre el directorio raíz.

```
cd 
```

2. Clonar el repo de pyenv.

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

3. Configurar el entorno de la terminal para hacer uso de pyenv. Aquí se define la variable de entorno PYENV_ROOT para que apunte a la RUTA donde Pyenv almacenará sus datos. $HOME/.pyenv es la RUTA predeterminada:

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
```

4. Agregar el ejecutable pyenv a la RUTA.

```
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
```

5. Escribir los siguientes argumentos dentro del archivo ~/.bashrc. 
*NOTA: Ejecutar `eval $(pyenv init -)` para instalar pyenv en su shell como una función de shell, habilite shims y autocompletado. Puedes ejecutar `eval "$(pyenv init --path)"` en su lugar para habilitar shims, sin integración de shell.*

```
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc 
```

6. Reinicia la terminal:
```
exec "$SHELL"
```

7. Clonar pyenv-virtualenv:

```
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```
8. Escribir inicialización de pyenv en ~/.bashrc:

```
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc 
```

9. Reiniciar de nuevo la terminal:

```
exec "$SHELL"
```

Con estos 9 pasos ya tendrás instalado pyenv. 

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
