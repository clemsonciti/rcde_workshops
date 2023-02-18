# RCDE Workshops


This site is created using [jupyter-book](). A build script is set up in `build.sh`.
To create the build environment, run:

~~~
$ conda create -n jupyter-book python==3.10.0
$ source activate jupyter-book
$ conda install -c conda-forge jupyter-book
$ conda install numpy matplotlib pandas
$ pip install ghp-import
~~~

To build the workshop site and test it locally, run:

~~~
$ ./build.sh
~~~

To deploy the workshop to GitHub page, run:

~~~
$ ./build.sh pages
~~~
