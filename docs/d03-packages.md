# Packages managenemt

## Pip

Package manager for Python that allows you to install additionan libraries and packages that are not part of the standar Python library. 

To see the packages that you have installed:

```
pip list
```

To install one package at a time: 

```
pip install <package>==<number-version>
```


To install the requirements for running a project: 

```
pip install -r requirements.txt
```

It is the same as list, but this one has the formart to create the requirements.txt file: 

```
pip freeze
```

To pass that to a file: 

```
pip freeze > requirements.txt
```

See the file:

```
cat requirements.txt
```


