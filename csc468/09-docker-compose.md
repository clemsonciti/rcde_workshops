
# Docker Compose"
teaching: 0
exercises: 0
questions:
- "How can we design the blueprint for a complex infrastructure?"
objectives:
- ""
keypoints:
- ""



> ## 1. Preparation: individual!
>
> - For this episode, deploy one CloudLab experiment per student. 
> - You can instantiate from your team's Docker profile, but still, 
> **one experiment per student**.  
> - Once the experiment is fully deployed, each student should confirm that they can run 
> the following command:
>
> ~~~
> $ docker info
> $ docker run hello-world
> ~~~
> {: .language-bash}
>
```


> ## 2. Docker compose: why?
>
> - Dockerfiles are great for building container images.
> - Dockerfiles are not quite satisfactory if you have to link multiple containers 
> into a complex infrastructure.
> - We want the ability to write custom scripts (program everything!) to automatically build, 
> run, and connect containers together. 
> - This is possible via Docker Compose.
> - For Podman, it is called Buildah. 
> 
```


> ## 3. In a nutshell
>
> - External, Python-based tool. 
> - Open source.
> - Simple deployment workflow
>   - Checkout code
>   - Run `docker-compose up`
>   - Everything is up and running!
> 
```


> ## 4. Overview of compose
>
> - Design of a container stack is described in a YAML file called `docker-compose.yml`.
> - Run `docker-compose up`.
> - Compose automatically pulls images, builds containers, and starts them. 
> - Compose can
>   - Set up links, volumes, and other Docker options for the container stack. 
>   - Run containers in the background or in the foreground.
> 
```


> ## 5. Docker compose demonstration
>
> - Run the following commands:
>
> ~~~
> $ cd
> $ git clone https://github.com/CSC468-WCU/ram_coin.git
> $ cd ram_coin
> $ docker-compose up
> ~~~
> {: .language-bash}
> 
> - Visit YOUR_CLOUDLAB_HEADNODE:8000 to see the deployed webserver. 
> - Does it work?
> - Open another terminal, connect to your CloudLab headnode and run `docker ps` to see 
> how many containers were deployed by the docker-compose. 
> - Press `Ctrl-C` to stop the containers. 
```


> ## 6. Sections of a compose file
>
> - Use `cat` or `nano` to view `docker-compose.yaml` file. 
> - `version` is mandatory (“2” or later).
> - `services` is mandatory. A service is one or more replicas of the same 
> image running as containers.
> - `networks` is optional and indicates to which networks containers should be connected. 
> By default, containers will be connected on a private, per-compose-file network.
> - `volumes` is optional and can define volumes to be used and/or shared by the containers. 
> 
```


> ## 7. Compose file versions
>
> - Version 1 is legacy.
> - Version 2 has support for networks and volumes.
> - Version 3 has support for deployment options.
> 
```


> ## 8. Containers in docker-compose.yaml
>
> - Each service in the YAML file must container either `build` or `image`.
> - `build` indicates a path containing a Dockerfile.
> - `image` indicates an image name (local or on registry).
> - If both are specified, an image will be built from the build directory and named `image`
> - Other parameters are optional and typically what you would add to docker run
>   - command = CMD
>   - ports = -p
>   - volumes = -v
> 
```


> ## 9. Hands-on: Rerun ram_coin in background
>
> ~~~
> $ docker-compose -d up
> $ docker-compose ps
> ~~~
> {: .language-bash}
>
```


> ## 10. Hands-on: cleanup
>
> ~~~
> $ docker-compose kill
> $ docker-compose rm
> ~~~
> {: .language-bash}
>
```


{% include links.md %}

