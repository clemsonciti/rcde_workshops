
# Docker Swarm"
teaching: 0
exercises: 0
questions:
- "How can we deploy containers across nodes?"
objectives:
- ""
keypoints:
- ""



> ## 1. Overview: teamwork!
>
> - Deploy your Docker profile (from episode 9) on CloudLab prior to class
> - This is a team deployment, only one team member needs to deploy the experiment. 
>
```


> ## 2. Overview of services to be deployed
>
> - We will clone the practice service into head and perform a normal docker compose to 
> observe this service. 
>
> ~~~
> $ cd
> $ git clone https://github.com/jpetazzo/container.training
> $ cd ~/container.training/dockercoins
> $ docker-compose up
> ~~~
> {: .language-bash}
> 
```


> ## 3. What is this application?
>
> - It is a DockerCoin miner! 
> - How DockerCoins works:
>   - generate a few random bytes
>   - hash these bytes
>   - increment a counter (to keep track of speed)
>   - repeat forever!
> - **It is not a cryptocurrency!**
> 
```


> ## 4. Micro-services of DockerCoin
>
> - `rng` = web service generating random bytes
> - `hasher` = web service computing hash of POSTed data
> - `worker` = background process calling `rng` and `hasher`
> - `webui` = web interface to watch progress
> - `redis` = data store (holds a counter updated by worker)
> - https://github.com/jpetazzo/container.training/blob/master/dockercoins/docker-compose.yml
> 
```


> ## 5. How DockerCoin works?
>
> - `worker` invokes web service `rng` to generate random bytes
> - `worker` invokes web service `hasher` to hash these bytes
> - `worker` does this in an infinite loop
> - Every second, `worker` updates `redis` to indicate how many loops were done
> - `webui` queries `redis`, and computes and exposes "hashing speed" in our browser
>
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
> <img src="../fig/09-swarm/01.png" style="height:500px">
>
```


> ## 7. How services find one another in container mode?
>
> - We do not hard-code IP addresses in the code
> - We do not hard-code FQDN in the code, either
> - We just connect to a service name, and container-magic does the rest
> - (And by container-magic, we mean "a crafty, dynamic, embedded DNS server")
> - Example: https://github.com/jpetazzo/container.training/blob/master/dockercoins/worker/worker.py
> 
```


> ## 8. Hands-on: check the web services
>
> - Navigate to a browser and use the IP address of your head node
> and the port 8000 to view the performance of DockerCoin
>
> <img src="../fig/09-swarm/02.png" style="height:500px">
>
> - On your terminal, use `Ctrl-C` to stop the application. 
> - Restart the application, this time using `-d` to run the service
> in background mode. 
> 
```


> ## 9. Hands-on: Scaling up the application
>
> - Do we have enough resources to scale up?
>
> ~~~
> $ top
> ~~~
> {: .language-bash}
>
> - Type `q` to quit `top`. 
> - We observed idle CPU cycles and little to non I/O activities
>
```


> ## 10. Hands-on: scaling with Docker compose
>
> ~~~
> $ docker-compose up -d --scale worker=2
> $ docker-compose ps
> ~~~
> {: .language-bash}
>
> - What is the change in the graph?
> - What is the change in the CPU usage (using `top`)?
>
> <img src="../fig/09-swarm/03.png" style="height:500px">
>
> - Try scaling up to 10 workers (`--scale worker=10`)
> - What happens to the performance graph? Do we have a 10x scale?
> - What happens to our CPU?
> - What happens to our I/O
>
> <img src="../fig/09-swarm/04.png" style="height:500px">
>
> - Check latency of `rng`
> - Check latency of `hasher`
>
> ~~~
> $ httping -c 3 localhost:8001
> $ httping -c 3 localhost:8002
> ~~~
> {: .language-bash}
>
> - Which port shows slower ping? Which service is it?
> - Docker-compose let us scale on a local physical host. 
>
> ~~~
> $ docker-compose down
> ~~~
> {: .language-bash}
>
```


> ## 11. SwarmKit
>
> - Open source tool kit to build multi-node systems
> - Reusable library. 
> - Plumbing part of the Docker ecosystem. 
> - Adopted into Docker as Docker Swarm 
> 
```


> ## 12. Features
>
> - Highly-available, distributed store based on Raft consensus algorithm. 
> - Raft was developed by Ongaro, Diego, and John Ousterhout at Stanford. 
> - *In search of an understandable consensus algorithm.* In 2014 USENIX Annual 
> Technical Conference, pp. 305-319. 2014.
> - Dynamic reconfiguration of Raft without interrupting cluster operations
> - Services managed with declarative API
> - Integration with overlay networks and load balancing
> - Strong emphasis on security 
> 
```


> ## 13. SwarmKit concepts
>
> - A cluster will be at least one node.
> - A node can be a manager and a worker. 
> - A manager actively takes part in the Raft consensus and keeps the Raft log.
> - You can talk to a manager using the SwarmKit API.
> - One manager is elected as the leader; other manager merely forward requests to it. 
> - The workers get their instructions from the managers.
> - Both workers and managers can run containers. 
> 
```


> ## 14. SwarmKit concepts
>
> - The managers expose the SwarmKit API.
> - Using the API, you can indicate that you want to run a service.
> - A service is specified by its desired state: which image, how many instances…
> - The leader uses different subsystems to break down services into tasks: 
> orchestrator, scheduler, allocator, dispatcher.
> - A task corresponds to a specific container, assigned to a specific node. 
> - Nodes know which tasks should be running, and will start or stop containers accordingly. 
> 
```


> ## 15. Declarative versus imperative
>
> - Declarative programming is a programming paradigm that expresses the logic 
> of a computation without describing its control flow.
> - Imperative programming is a programming paradigm that uses statements that 
> change a program’s state. 
> 
> <script src="https://gist.github.com/linhbngo/b9f794bed306562f2eb85da310ae7b5e.js?file=example.py"></script>
>
> - Imperative systems:
>   - Simpler
>   - If a task is interrupted, we have to restart from scratch
> - Declarative systems:
>   - If a task is interrupted, we can figure out what’s missing and do 
>   only what’s necessary.
>   - We need to be able to observe the system to find out the difference 
>   between what we have and what we want. 
>
```


> ## 16. Hands-on: swarm mode
>
> - By default, SwarmKit features are asleep until you active Swarm mode
> - Swarm Mode commands:
>   - `docker swarm`: enable Swarm mode, join Swarm, adjust Swarm’s parameters
>   - `docker node`: view nodes, promote/demote managers, manage nodes
>   - `docker service`: create and manage services. 
> - Run the following on head node:
>
> ~~~
> $ cd
> $ docker swarm init --advertise-addr eth1:7777 --listen-addr eth1:7777
> ~~~
> {: .language-bash}
>
> - In this profile, CloudLab nodes have two IP addresses:
>   - Public IP address: `eth0`
>   - Private IP address: `eth1`
>
> <img src="../fig/09-swarm/05.png" style="height:200px">
> 
> - Read the output and use the provided commands on the worker nodes to 
> have these nodes joining the swarm. 
>
> <img src="../fig/09-swarm/06.png" style="height:50px">
> <img src="../fig/09-swarm/07.png" style="height:50px">
>
> - To view the swarm nodes
>
> ~~~
> $ docker node ls
> ~~~
> {: .language-bash}
>
> <img src="../fig/09-swarm/08.png" style="height:100px">
>
> ~~~
> $ docker-compose down
> ~~~
> {: .language-bash}
>
```


> ## 17. Application on Swarm
>
> - **Build** images for application,
> - **Ship** these images with a registry, 
> - **Run** services using these images. 
> - Why?
>   - For `docker-compose` up, images are built locally for services.
>   - For a Swarm, images need to be distributed.
>   - The easiest way is to use a Docker registry.
>
```



> ## 18. Hands-on: launching a registry inside the Swarm
>
> - On head node:
>
> ~~~
> $ docker service create --name registry --publish 5000:5000 registry
> $ docker service ps registry
> $ curl 127.0.0.1:5000/v2/_catalog
> ~~~
> {: .language-bash}
>
> - Test the registry:
>
> ~~~
> $ docker pull busybox
> $ docker tag busybox 127.0.0.1:5000/busybox
> $ docker push 127.0.0.1:5000/busybox
> $ curl 127.0.0.1:5000/v2/_catalog
> ~~~
> {: .language-bash}
>
> - This is a demo registry with no security (without TLS)!
>
> ~~~
> $ /bin/bash
> $ cd
> $ cd container.training/dockercoins/
> $ export REGISTRY=127.0.0.1:5000
> $ export TAG=v0.1
> $ for SERVICE in hasher rng webui worker; do docker build -t $REGISTRY/$SERVICE:$TAG ./$SERVICE; docker push $REGISTRY/$SERVICE:$TAG; done
> $ curl 127.0.0.1:5000/v2/_catalog
> ~~~
> {: .language-bash}
>
> - Launching the overlay network and other services
> 
> ~~~
> $ docker network create --driver overlay dockercoins
> $ docker service create --network dockercoins --name redis redis
> $ export REGISTRY=127.0.0.1:5000
> $ export TAG=v0.1
> $ for SERVICE in hasher rng webui worker; do docker service create --network dockercoins --detach=true --name $SERVICE $REGISTRY/$SERVICE:$TAG; done
> $ docker service ls
> $ docker service update webui --publish-add 8000:80
> $ docker service ls
> ~~~
> {: .language-bash}
>
> - Rescale your workers and observe whether there are increases in mining performance. 
>
```


{% include links.md %}

