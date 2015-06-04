# poster
A simple tool for publish blog

###Install from source code

>1. git clone https://github.com/aducode/poster.git
2. cd poster
3. python setup.py install

###Quick Usage

>Usage:
>        poster action title [date]
>
>action list:
>
>        init: init github pages
>        clear: clear generated files
>        create name [date]: create new blog
>        remove name [date]: remove exist blog
>        list [name] [date]: list blog
>        build: markdown to html

###Directory structure

>* **.id** index of the markdown files
* **.layout**  layout files path
* **.posts/date/markdown.md**  markdown files
* **posts/date/html.html**  html files, when excute poster build, the html files translated fom markdown files
* **index.html**
