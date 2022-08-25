
# Kubernetes"
teaching: 0
exercises: 0
questions:
- "How does Kubernetes work with Docker?"
objectives:
- "Knowing how to deploy services using Kubernetes"
keypoints:
- ""



> ## 1. Preparation: 
>
> - This episode will provide the main framework to link the services of your project together. 
> - For this episode, each team only need to modify their project repository.
>   - Create a new branch called **kubernetes** from your Docker branch.  
> - Visit [Dr. Ngo's Kubernetes branch](https://github.com/CSC468-WCU/csc468cloud/tree/kubernetes) and 
> and make sure that **all files** in your **kubernetes** branch match up with the files from `csc468cloud`'s 
> **kubernetes** branch. 
>   - Having team members double/triple check!
> - Each member then should instantiate from their team's CloudLab project profile. 
> - Once the experiment is fully deployed, **and all Startup Finished running**:
>   - SSH into the head node and run the followings
>
> ~~~
> $ cd
> $ bash /local/repository/launch_network.sh
> $ kubectl get nodes
> ~~~
> {: .language-bash}
>
> <img src="../fig/11-kubernetes/01.png" style="height:300px">
>
```


> ## 2. Automated Kubernetes Deployment 
> 
> - This is done via Kubernetes Objects, described through YAML files. 
> - **Kubernetes objects** are persistent entities in the Kubernetes system, which represent the state of your cluster. 
>   - What containerized applications are running (and on which nodes)
>   - The resources available to those applications
>   - The policies around how those applications behave, such as restart policies, upgrades, and fault-tolerance
> - *A Kubernetes object is a "record of intent"--once you create the object, the Kubernetes system will 
> constantly work to ensure that object exists. By creating an object, you're effectively telling the 
> Kubernetes system what you want your cluster's workload to look like; this is your cluster's desired state.*
> - [Documentation](https://kubernetes.io/docs/reference/kubernetes-api/)
>
```


> ## 3. Sequence of commands to launch ram_coin on Kubernetes
>
> - First, we deploy a registry service. This is equivalent to a local 
> version of Docker Hub.  
> 
> ~~~
> $ cd
> $ kubectl create deployment registry --image=registry
> $ kubectl expose deploy/registry --port=5000 --type=NodePort
> $ kubectl get svc
> ~~~
> {: .language-bash}
>
> <img src="../fig/11-kubernetes/02.png" style="height:300px">
>
> - We can patch configurations of deployed services
> 
> ~~~
> $ kubectl patch service registry --type='json' --patch='[{"op": "replace", "path": "/spec/ports/0/nodePort", "value":30000}]'
> $ kubectl get svc
> ~~~
> {: .language-bash}
>
> - You can see the external port has now been changed (patched)
> 
> <img src="../fig/11-kubernetes/03.png" style="height:300px">
>
>
{:.slide}


> ## 4. Building and pushing images for ramcoin
>
> - We test our local registry by pulling `busybox` from Docker Hub and then 
> tag/push it to our local registry. 
> 
> ~~~
> $ docker pull busybox
> $ docker tag busybox 127.0.0.1:30000/busybox
> $ docker push 127.0.0.1:30000/busybox
> $ curl 127.0.0.1:30000/v2/_catalog
> ~~~
> {: .language-bash}
>
> <img src="../fig/11-kubernetes/04.png" style="height:400px">
>
> - Next, we clone ramcoin repository
>
> ~~~
> $ git clone https://github.com/CSC468-WCU/ram_coin.git
> $ cd ~/ram_coin
> $ docker-compose -f docker-compose.images.yml build
> $ docker-compose -f docker-compose.images.yml push
> $ curl 127.0.0.1:30000/v2/_catalog
> $ kubectl create deployment redis --image=redis
> $ for SERVICE in hasher rng webui worker; do kubectl create deployment $SERVICE --image=127.0.0.1:30000/$SERVICE:v0.1; done
> $ kubectl expose deployment redis --port 6379
> $ kubectl expose deployment rng --port 80
> $ kubectl expose deployment hasher --port 80
> $ kubectl expose deploy/webui --type=NodePort --port=80
> $ kubectl get svc
> ~~~
> {: .language-bash}
> 
> <img src="../fig/11-kubernetes/05.png" style="height:400px">
>
> - Identify the port mapped to port 80/TCP for webui service. You can 
> use this port and the hostname of the `head` node from CloudLab to access 
> the now operational ram coin service. 
>
> <img src="../fig/11-kubernetes/06.png" style="height:500px">
>
> - `svc` is abbreviation for `services`. 
> - You can see the difference between `services` and `pods`
> 
> ~~~
> $ kubectl get services
> $ kubectl get pods
> ~~~
> {: .language-bash}
>
> <img src="../fig/11-kubernetes/09.png" style="height:500px">
>
{:.slide}


> ## 5. Exercise
>
> - Patch the webui service so that it uses port 30080 as the external port
>
> <img src="../fig/11-kubernetes/07.png" style="height:900px">
>
```



> ## 6. Setup a Kubernetes Dashboard
>
> - Run the following commands from inside the `ram_coin` directory
>
> ~~~
> $ kubectl apply -f dashboard-insecure.yaml
> $ kubectl apply -f socat.yaml
> $ kubectl get namespace
> $ kubectl get svc --namespace=kubernetes-dashboard
> $ kubectl patch service kubernetes-dashboard -n kubernetes-dashboard --type='json' --patch='[{"op": "replace", "path": "/spec/ports/0/nodePort", "value":30082}]'
> ~~~
> {: .language-bash}
>
>
> - Go to the `head` node URL at port `30082` for `kubernetes-dashboard`
> - Hit `skip` to omit security (**don't do that at your job!**).
>
> <img src="../fig/11-kubernetes/08.png" style="height:1200px">
>
```


> ## 7. Kubernetes namespace
>
> - Provides a mechanism for isolating groups of resources within a single cluster. 
> - Uniqueness is enforced only  within a single namespace for namespaced objects 
>   (`Deployment` and `Services`)
> - Uniquess of other cluster-wide objects (`StorageClass`, `Nodes`, `PersistentVolumes`, etc) is 
>   enforced across namespaces. 
> - Run the following commands from inside the `ram_coin` directory
> - `namespaces`, `namespace` or `ns`
> ~~~
> $ kubectl get namespaces
> $ kubectl get ns
> $ kubectl get namespace
> ~~~
> {: .language-bash}
>
> <img src="../fig/11-kubernetes/10.png" style="height:400px">
>
> - Using `--namespace` or `-n` let you specify a namespace and look at objects within 
> that namespace. 
> - Without any specification, it is the default namespace (`default`)
>
> ~~~
> $ kubectl get ns
> $ kubectl get pods -n kubernetes-dashboard
> $ kubectl get pods
> $ kubectl get services --namespace kubernetes-dashboard
> $ kubectl get services
> ~~~
> {: .language-bash}
>
> <img src="../fig/11-kubernetes/11.png" style="height:450px">
>
```


> ## 8. Remove pods and services
>
> - Removing pods is equivalent to removing deployment 
> - Removing pods and services separately
>
> ~~~
> $ kubectl get pods
> $ kubectl get deploy
> $ kubectl delete deploy redis
> $ kubectl get services
> $ kubectl delete services redis
> $ kubectl get services
> $ kubectl get deploy
> ~~~
> {: .language-bash}
>
> <img src="../fig/11-kubernetes/12.png" style="height:400px">
>
```


> ## 9. Exercise
>
> - Delete the rest of the ramcoin deployments and services in the default namespace
> - Confirm via command line API and dashboard that everything stops running. 
>
```


> ## 10. Automated Kubernetes Deployment 
> 
> ~~~
> $ kubectl create namespace ramcoin
> $ kubectl create -f ramcoin.yaml --namespace ramcoin
> $ kubectl get pods -n ramcoin
> $ kubectl create -f ramcoin-service.yaml --namespace ramcoin
> $ kubectl get services --namespace ramcoin
> ~~~
> {: .language-bash}
>
```


> ## 11. Automated recovery 
> 
> - Check status and deployment locations of all pods on the `head` node
>
> ~~~
> $ kubectl get pods -n ramcoin -o wide
> ~~~
> {: .language-bash}
>
> - SSH into `worker-1` and reset the Kubelet. Enter `y` when asked. 
>
> ~~~
> $ sudo kubeadm reset
> ~~~
> {: .language-bash}
>
>
> - Run the following commands on `head` to observe the events 
>   - After a few minutes, `worker-1` becomes `NotReady` via `kubectl get nodes`
>   - After five minutes, `kubectl get pods -n ramcoin -o wide` will show that 
>   pods on `worker-1` being terminated and replications are launched on `worker-2` 
>   to recover the **desired state** of ramcoins. 
>   - The five-minute duration can be set by the `--pod-eviction-timeout` parameter. 
> 
> ~~~
> $ kubectl get nodes
> $ kubectl get pods -n ramcoin -o wide
> ~~~
> {: .language-bash}
>
> <img src="../fig/11-kubernetes/13.png" style="height:400px">
>
```




{% include links.md %}

