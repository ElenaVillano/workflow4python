# Python Workflow

## Virtual Environments

A virtual environment is a tool that isolates your Python development projects from your system installed Python and other Python environments. This gives you full control of your project and makes it easily reproducible. Any changes on dependencies installed in a virtual environment won't affect the dependencies of other virtual environments or system-wide libraries.

[<img src="https://www.dataquest.io/wp-content/uploads/2022/01/python-virtual-envs1-1024x576.webp" width="800"/>](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/#:~:text=NOTE%20A%20Python%20project%20folder,in%20a%20virtual%20environment%20folder.)

### Why do we need Virtual Environments?

1. They solve dependency problems allowing to use different versions of a package. For example, using the package A v2.7 for project X and the package A v1.3 for the project Y. 
2. They allow each project to be independent and reproducible capturing all the dependencies of the packages in one requirement files. 
3. They facilitate the order of the site-package global directory, because they eliminate the necessity of installing packages in the main system, when you might just require it for one project. The other use case that magnifies the importance of using Python virtual environments is when you’re working on managed servers or production environments where you can’t modify the system-wide packages because of specific requirements.
4. This would lead to compatibility issues because Python cannot simultaneously use multiple versions of the same package.


Python virtual environments create isolated contexts to keep dependencies required by different projects separate so they don't interfere with other projects or system-wide packages. Setting up virtual environments is the best way to isolate different Python projects, especially if these projects have different and conflicting dependencies. As a piece of advice for new Python programmers, always set up a separate virtual environment for each Python project, and install all the required dependencies inside it — never install packages globally.

### Virtualenv vs pyenv, which one to use?

Virtualenv: Creates different virtual environments in the Python version of your system and has a very simple installation.
Pyenv: Switch easily between multiple **versions of Python** and virtual environments.


## SUGESTED repository structure:

- config/local: where you place the credentials *
- docs: documents
- imgs: images
- infraestructure: bash files
- notebooks: .ipynb files
- sql: sql scripts to build the databases 
- src/
    - utils: general functions that are used around 
    - pipeline: tasks to run the complete process 
    - experiments: code drafts 
- tmp: things you won't upload to the repository *
- .gitignore: * this file is very important
- README.md: Instructions to use your repository
- requirements.txt
- .gitkeep: just to keep the structure of the folders without any file


