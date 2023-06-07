# RCDE Workshops

This site is created using [jupyter-book](https://jupyterbook.org).

## Working Locally with Conda

A build script is set up in `build.sh`. To create the build environment, run:

```sh
$ conda create -n jupyter-book python==3.10.0
$ source activate jupyter-book
$ conda install -c conda-forge jupyter-book
$ conda install numpy matplotlib pandas
$ pip install ghp-import
```

### Building Locally

To build the workshop site and test it locally, run:

```sh
$ ./build.sh
```

### Deploying Locally

To deploy the workshop to GitHub page, run:

```sh
$ ./build.sh pages
```

## Working Locally with Docker

You can build and develop this site locally without installing any of the
Python dependencies on your machine by using the Docker interface.

### Setting up the Docker Environment

Before getting started, you will need to build the Docker image. This image
will contain all of the dependencies for the project, so you will need to
repeat this step whenever the dependencies in `requirements.txt` change.

To build the image, run:

```sh
make docker
```

### Live Development Server with Docker

The Docker setup for this project includes a live reload server that will
serve the site on localhost:8080 and automatically re-build the site whenever
you change a file.

To run the live server, run:

```sh
make docker-dev-server
```

An initial build will run before the server starts. After it is finished,
you can view the site at [localhost:8080](http://localhost:8080).

The site will re-build automatically when you change any file. The web browser
will automatically refresh the page when this occurs.

When you are done, press <kbd>Ctrl</kbd><kbd>c</kbd> to stop the server.

### Cleaning with Docker

Sometimes, it is necessary to clear the site's build cache. A script is
available to do this for you. Just run:

```sh
make docker-clean
```

### Building with Docker

To build the site, but **not start the development webserver**, you can use the
build command. Just run:

```sh
make docker-build
```

### Deploying with Docker

To deploy the site, we use the `ghp-import` package. The import process will
run in the container, then we will push from your local computer so that your
saved credentials are used (if present).

```sh
make docker-deploy
```
