# Docker Containers


```{dropdown} 0. Setup

- Go to your GitHub project repository (on the first day), create a new branch called `docker` from the `main branch`, 
and modify to add the following components from [this link](https://github.com/CSC468-WCU/csc468cloud/tree/docker):
  - The `docker_config` directory and its content (`daemon.json`).
  - The `install_docker.sh` file.
  - The `profile.py` file. 
- **Check and make sure all the contents are correctly copied!**
- Go to CloudLab, open your profile, switch to `Edit` mode and click `Update`. The new `docker` branch should show up.  
- Instantiate an experiment from this branch. 
- **Only login after the Startup column becomes Finished** and type the following command: `sudo docker info | grep "Docker Root Dir"`
- Confirm that you have something similar to the screenshot below

:::{image} ../fig/csc586//13-docker/00.png
:class: bg-primary mb-1
:height: 100px
:align: center
:::

```
 



```{dropdown} 1. Why do we want container?

:::{image} ../fig/csc586//13-docker/01.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```



```{dropdown} 2. The issue: who does what?

:::{image} ../fig/csc586//13-docker/02.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```



```{dropdown} 3. Inspiration for Docker

:::{image} ../fig/csc586//13-docker/03.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```


```{dropdown} 4. Inspiration for Docker: intermodal shipping containers

:::{image} ../fig/csc586//13-docker/04.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```


```{dropdown} 5. Modern shipping ecosystem

:::{image} ../fig/csc586//13-docker/05.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```


```{dropdown} 6. A shipping container system for applications

:::{image} ../fig/csc586//13-docker/02.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```


```{dropdown} 7. Who does what? We don't care ...

:::{image} ../fig/csc586//13-docker/07.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```


```{dropdown} 8. Cloud-native applications on container

:::{image} ../fig/csc586//13-docker/08.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```


```{dropdown} 9. Hands-on: Getting started

- SSH into your CloudLab experiment.   
- Check version of Docker: 


~~~
$ docker version
~~~

:::{image} ../fig/csc586//13-docker/09.png
:class: bg-primary mb-1
:height: 600px
:align: center
:::


- Docker is client-server application.
  - Docker daemon (Engine): receives and processes incoming Docker API request 
  and requires root privilege.
  - Docker Hub registry: collection of public images (https://hub.docker.com/).
  - Docker client : Talks to the Docker daemon via the docker API and the registry API.

```


```{dropdown} 10. Hands-on: Hello world

- Docker `containers` are instantiated from Docker `images`. 
- You can check availability of local `images` and `containers`. 

~~~
$ docker image ls
$ docker container ls
~~~

:::{image} ../fig/csc586//13-docker/10.png
:class: bg-primary mb-1
:height: 100px
:align: center
:::

- We can issue the following to start a service that will echo `hello world` to the screen. 
- This requires a Linux container to run the `echo` command. 

~~~
$ docker run alpine echo hello world
~~~


- `docker`: invoke the container engine. 
- `run`: subcommand to run a container. 
- `alpine`: name of the image based on which a container will be launched. 
- `echo hello world`: the command to be executed in the container environment. 

~~~
$ docker image ls
$ docker container ls
$ docker container ls --all
$ docker run alpine echo hello world
$ docker container ls --all
~~~

:::{image} ../fig/csc586//13-docker/11.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```


```{dropdown} 11. Hands-on: Interactive container

- We can launch a container and get into the shell of the container. 


~~~
$ docker run -it ubuntu bash
~~~

:::{image} ../fig/csc586//13-docker/12.png
:class: bg-primary mb-1
:height: 150px
:align: center
:::

- You are now in a new prompt: a shell inside the container
- `-it`: combination of `-i` and `-t`. 
  - `-i` tells Docker to connect to the container’s stdin for interactive mode
  - `-t` tells Docker that we want a pseudo-terminal

```


```{dropdown} 12. Hands-on: run something interactively

- The following commands are done inside the container. 
- Let's attempt to run `figlet`

~~~
# figlet hello
~~~


- There will be an error. 
- The current container does not have the `figlet` program yet. 

```


```{dropdown} 13. Hands-on: installing and then running

- The following commands are done inside the container. 

~~~
# apt-get update
# apt-get install -y figlet
# figlet hello
~~~

:::{image} ../fig/csc586//13-docker/13.png
:class: bg-primary mb-1
:height: 600px
:align: center
:::

```


```{dropdown} 14. Exercise

- Type `exit` to shutdown the container and back to your normal terminal. 
- Repeat the process of launching an interactive container from start and try 
running `figlet` again. 
- Is the program still there?

```



```{dropdown} 15. Hands-on: Background container

- You should have already exited out of the container shell and back to the CloudLab environment. 
- Run the following command
- Press `Ctrl-C` to stop after a few time stamps. 

~~~
$ docker run jpetazzo/clock
~~~

```



```{dropdown} 16. Hands-on: Background container

- Run the following command 

~~~
$ docker run -d jpetazzo/clock
$ docker ps
~~~

```



```{dropdown} 17. Hands-on: View log of your background container

- Use the first four characters of your container ID to view the log of the running Docker container
- Use `--tail N` to only look at the tail of the log. 

~~~
$ docker container ls
$ docker logs --tail 5 YOUR_CONTAINER_ID
 ~~~

```


```{dropdown} 18. Exercise

- Find out how to kill a running container by using `docker kill`. 
{: .challenge}

```


```{dropdown} 19. Docker images

- Image = files + metadata
- The files form the root filesystem of the container
- The metadata describes things such as:
  - The author of the image
  - The command to execute in container when starting it
  - Environment variables to be set
  - ...
- Images are made of layers, conceptually stacked on top of each other.
- Each layer can add, change, and remove files and/or metadata.
- Images can share layers to optimize disk usage, transfer times, and memory use.

```


```{dropdown} 20. Example of a Java webapp

- CentOS base layer
- Packages and configuration files added by our local IT
- JRE
- Tomcat
- Our application’s dependencies
- Our application code and assets
- Our application configuration

```


```{dropdown} 21. The read-write layer

:::{image} ../fig/csc586//13-docker/25.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

```


```{dropdown} 22. Containers versus images

- An image is a read-only filesystem.
- A container is an encapsulated set of processes running in a 
read-write copy of that filesystem.
- To optimize container boot time, copy-on-write is used instead of regular copy.
- `docker run` starts a container from a given image. 

:::{image} ../fig/csc586//13-docker/26.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

- Object-oriented analogy
  - Images are conceptually similar to classes
  - Layers are conceptually similar to inheritance
  - Containers are conceptually similar to instances

```


```{dropdown} 23. How do we change an image?

- It is read-only, we don’t.
- We create a new container from the image
- We make changes to the container. 
- When we are satisfied with the changes, we transform them into a new layer.
- A new image is created by stacking the new layer on top of the old image.

```


```{dropdown} 24. Image namespaces

- Official images (ubuntu, busybox, …)
  - Root namespace. 
  - Small, distro images to be used as bases for the building process.
  - Ready-to-use components and services (redis, postgresl …)
- User (and organizations) images: `<registry_name>/<image_name>:[version]`
  - jpetazzo/clock:latest
  - linhbngo/csc331:latest
- Self-hosted images
  - Images hosted by third party registry
  - `URL/<image_name>`

```


```{dropdown} 25. Hands-on: show current images

- If this is a new experiment, go ahead and run the following commands to get 
some images loaded. 

~~~
$ docker run hello-world
$ docker run alpine echo This is alpine
$ docker run ubuntu echo This is ubuntu
$ docker image ls
~~~

:::{image} ../fig/csc586//13-docker/27.png
:class: bg-primary mb-1
:height: 200px
:align: center
:::

```



```{dropdown} 26. Hands-on: search images

- We can search for available images in the public Docker Hub 

~~~
$ docker search mysql
~~~

:::{image} ../fig/csc586//13-docker/28.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

```



```{dropdown} 27. General steps to create an image

- Create a container using an appropriate base distro
- Inside the container, install and setup the necessary software
- Review the changes in the container
- Turn the container into a new image
- Tag the image

:::{image} ../fig/csc586//13-docker/31.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

```


```{dropdown} 28. Hands-on: create a container with a base distro

- Remember to note your container ID. 

~~~
$ docker run -it ubuntu
~~~

```



```{dropdown} 29. Hands-on: install software inside the container

~~~
# apt-get update
# apt-get install -y figlet
# exit
~~~

:::{image} ../fig/csc586//13-docker/32.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

```


```{dropdown} 30. Hands-on: check for differences

- Remember to note your container ID. 

~~~
$ docker diff 16b0
~~~

:::{image} ../fig/csc586//13-docker/33.png
:class: bg-primary mb-1
:height: 500px
:align: center
:::

- A: A file or directory was added
- D: A file or directory was deleted
- C: A file or directory was changed

```


```{dropdown} 31. Hands-on: commit changes into a new image

- Remember to note your container ID. 

~~~
$ docker commit 16b0 ubuntu_figlet_$USER
$ docker image ls
$ docker history fe101
~~~

:::{image} ../fig/csc586//13-docker/34.png
:class: bg-primary mb-1
:height: 500px
:align: center
::: 

- From the screenshot:
  - The `docker commit ...` command created a new image named `ubuntu_figlet_lngo` that 
  has the following unique id: `fe101865e2ed`. 
  - The `docker image ls` command shows this image.
  - The `docker history fe101` shows the layers making up this image, which include 
  the layer that is the base ubuntu image `54c9d`. 

```


```{dropdown} 32. Exercise

- Test run the new `ubuntu_figlet` image by launching an interactive container
using this image, then immediately run `figlet hello world`. 

```


```{dropdown} 33. Automatic image construction: Dockerfile

- A build recipe for a container image.
- Contains a series of instructions telling Docker/Podman how an image is to be constructed.
- The `docker build` command builds an image from a Dockerfile.

```


```{dropdown} 34. Hands on: writing the first Dockerfile

- The following commands are done in the terminal (Ubuntu WSL on Windows/Mac Terminal). 

~~~
$ cd
$ mkdir myimage
$ cd myimage
$ nano Dockerfile
~~~


- Type the following contents into the nano editor

<script src="https://gist.github.com/linhbngo/b9f794bed306562f2eb85da310ae7b5e.js?file=Dockerfile.1"></script>

- `FROM`: the base image for the build
- `RUN`: represents one layer of execution. 
- `RUN` commands must be non-interactive.
- Save and quit after you are done. 

- To build the image

```


```{dropdown} 35. Hands on: build the image

- The following commands are done in the terminal (Ubuntu WSL on Windows/Mac Terminal). 
- Check that you are still inside `myimage`

~~~
$ pwd
$ docker build -t figlet_$USER .
~~~


- `-t` indicates a tag named `figlet` will be applied to the image. 
- `.` indicates that the `Dockerfile` file is in the current directory. 

:::{image} ../fig/csc586//13-docker/35.png
:class: bg-primary mb-1
:height: 1000px
:align: center
:::

- The build context is the `Dockerfile` file in the current directory (`.`)
and is sent to the container engine. This context allows constructions of images 
with additional resources from local files inside the build context.
- The base image is `Ubuntu`.
- For each `RUN` statement, a container is created from the base image for the execution of the 
- commands. Afterward, the resulting container is committed into an image that becomes the 
base for the next `RUN`. 

```


```{dropdown} 36. Exercise

- Use `docker image ls` and `docker history ...` to check which layer is reused for
this image. 
- Test run the new `ubuntu_figlet` image by launching an interactive container
using this image, then immediately run `figlet hello world`. 

```


```{dropdown} 37. Hands on: CMD

- Edit your Dockerfile so that it has the following content

<script src="https://gist.github.com/linhbngo/b9f794bed306562f2eb85da310ae7b5e.js?file=Dockerfile.2"></script>

- `CMD`: The command to be run if the container is invoked without
any command. 
- Rebuild the image with the tag `figlet_cmd_$USER`. 
- Run the following command

~~~
$ docker run figlet_cmd_$USER
~~~

:::{image} ../fig/csc586//13-docker/36.png
:class: bg-primary mb-1
:height: 600px
:align: center
:::

- Question: Did we use any additional storage for this new image?

```


```{dropdown} 38. Hands on: Overriding CMD

- With CMD, the `-it` flag does not behave as expected 
without a parameter. 
- To override CMD, we can provide a command

~~~
$ docker run -it figlet_cmd_$USER
$ docker run -it figlet_cmd_$USER bash
~~~

:::{image} ../fig/csc586//13-docker/37.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

```


```{dropdown} 39. Hands on: ENTRYPOINT

-`ENTRYPOINT` defines a base command (and its parameters) 
for the container. 
- The command line arguments are appended to those parameters. 
- Edit `Dockerfile` as follows:

<script src="https://gist.github.com/linhbngo/b9f794bed306562f2eb85da310ae7b5e.js?file=Dockerfile.3"></script>

- Rebuild the image with the tag `figlet_entry_$USER`. 
- Run the followings:

~~~
$ docker run figlet_entry_$USER golden rams
~~~

:::{image} ../fig/csc586//13-docker/38.png
:class: bg-primary mb-1
:height: 600px
:align: center
:::

```


```{dropdown} 40. Hands on: Why not both

- `ENTRYPOINT` and `CMD` can be used together. 
- The command line arguments are appended to those parameters. 
- Edit `Dockerfile` as follows:

<script src="https://gist.github.com/linhbngo/b9f794bed306562f2eb85da310ae7b5e.js?file=Dockerfile.4"></script>

- Rebuild the image with the tag `figlet_both_$USER`. 
- Run the followings:

~~~
$ docker run figlet_both_$USER golden rams
$ docker run figlet_both_$USER
~~~

:::{image} ../fig/csc586//13-docker/39.png
:class: bg-primary mb-1
:height: 700px
:align: center
:::

```


```{dropdown} 41. Hands on: Caveat

- `/bin/bash` does not work as expected.  

~~~
$ docker run -it figlet_both_$USER bash
$ docker run -it --entrypoint bash figlet_both_$USER
# exit
~~~

:::{image} ../fig/csc586//13-docker/40.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

```


```{dropdown} 42. Hands on: Importing and building external code

- Create the following file called `hello.c`:

<script src="https://gist.github.com/linhbngo/b9f794bed306562f2eb85da310ae7b5e.js?file=hello.c"></script>

- Create the following Dockerfile called `Dockerfile.hello`:

<script src="https://gist.github.com/linhbngo/b9f794bed306562f2eb85da310ae7b5e.js?file=Dockerfile.5"></script>

- You can build an image with a specific Dockerfile

~~~
$ docker build -t hello_$USER -f Dockerfile.hello .
$ docker run hello_$USER
~~~

```



```{dropdown} 43. Challenge

- Create an account on [Docker Hub](https://hub.docker.com). 
- Find out how to login from the command line and push the recently created `hello` image 
to your Docker Hub account. 

```


```{dropdown} 44. Networking for container

- How can services provided by a container become available to the world? 

:::{image} ../fig/csc586//13-docker/43.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

```




```{dropdown} 45. Hands on: a simple web server

~~~
$ docker run -d -P nginx
$ docker ps
~~~


- `-P`: make this service reachable from other computers (`--publish-all`)
- `-d` : run in background
- Where is the port?

:::{image} ../fig/csc586//13-docker/44.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

:::{image} ../fig/csc586//13-docker/45.png
:class: bg-primary mb-1
:height: 300px
:align: center
:::

```



```{dropdown} 47. Hands on: How does the container engine know which port to map?

- This is described in the `Dockerfile` and can be inspected. 
- The keyword for this action is `EXPOSE`. 

:::{image} ../fig/csc586//13-docker/46.png
:class: bg-primary mb-1
:height: 100px
:align: center
:::

- Why do we have to map ports?
  - Containers cannot have public IPv4 addresses.
  - We are running low on IPv4 addresses anyway. 
  - Internally to host, containers have their own private addresses
    - Services have to be exposed port by port.
    - These have to be mapped to avoid conflicts.

```


```{dropdown} 48. Hands on: manual allocation of port numbers

~~~
$ docker run -d -p 8000:80 nginx
$ docker run -d -p 8080:80 -p 8888:80 nginx
~~~


- Convention: `port-on-host:port-on-container`
- Check out the web servers at all of these ports 

```


```{dropdown} 49. Integrating containers into your infrastructure

- Manually add the containers to the infrastructure via container-generated public port. 
- Predetermine a port on the infrastructure, then set the corresponding port mapping 
when run the containers.
- Use a network plugin to connect the containers with network tunnels/VLANS …
- Deploy containers across a physical cluster using Kubernetes.  

```


```{dropdown} 50. Container network model

- Provide the notion of a `network` to connect containers
- Provide top level command to manipulate and observe these networks: 
  - `docker network`

~~~
$ docker network
$ docker network ls
~~~

:::{image} ../fig/csc586//13-docker/47.png
:class: bg-primary mb-1
:height: 400px
:align: center
:::

- What's in a container network?
  - Conceptually, it is a virtual switch
  - It can be local to a single Engine (on a single host) or global 
  (spanning multiple hosts).
  - It has an associated IP subnet.
  - The container engine will allocate IP addresses to the containers connected to a network.
  - Containers can be connected to multiple networks.
  - Containers can be given per-network names and aliases.
  - The name and aliases can be resolved via an embedded DNS server. 

```


```{dropdown} 51. Hands on: create a network

~~~
$ docker network create ramnet
$ docker network ls
~~~

:::{image} ../fig/csc586//13-docker/48.png
:class: bg-primary mb-1
:height: 200px
:align: center
:::

```



```{dropdown} 52. Hands on: placing containers on a network

~~~
$ docker run -d --name es --net ramnet elasticsearch:2
$ docker run -it --net ramnet alpine sh
# ping es
# exit
~~~

:::{image} ../fig/csc586//13-docker/49.png
:class: bg-primary mb-1
:height: 600px
:align: center
:::

```
