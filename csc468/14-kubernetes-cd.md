
# Kubernetes Application: CI/CD pipeline - Part II"
teaching: 0
exercises: 0
questions:
- ""
objectives:
- "Being able to deploy a Jenkins server inside Kubernetes and integrate with GitHub 
  for automated building/testing."
keypoints:
- ""



> ## 1. Updated Jenkins launch
>
> - Launch an experiment from the `csc468lngo` profile using the `kubernetes-jenkins-cdci`
> branch. 
> - This branch is from [kubernetes-jenkins-cdci](https://github.com/CSC468-WCU/csc468cloud/tree/kubernetes-jenkins-cdci).
> - Once the experiment is fully deployed, **and all Startup Finished running**, 
> SSH into the head node. You don't have to do anything else. 
>   - The launching of the overlay network is now fully automated and 
>   is integrated into the `kube_manager.sh` file. 
>
```


> ## 2. Setup Jenkins
> 
> - All normal commands to launch Jenkins have been integrated into `launch_jenkins.sh`. 
>
> ~~~
> $ bash /local/repository/launch_jenkins.sh
> ~~~
> {: .language-bash}
>
> - To get the `initialAdminPassword`, you can run the following
> command directly:
>
> ~~~
> $ kubectl exec $(kubectl get pods -n jenkins | grep jenkins | awk '{print $1}') -n jenkins -- cat /var/jenkins_home/secrets/initialAdminPassword
> ~~~
> {: .language-bash}
>
> - `kubectl exec` allows users to run a bash command directly inside the specified pod.  
> - `$(kubectl get pods -n jenkins | grep jenkins | awk '{print $1}')` is a sequence of pipe commands:
>   - `$(kubectl get pods -n jenkins` get all pods
>   - `| grep jenkins ` parses the line containing the jenkins pod names
>   - `| awk '{print $1}')` gets the first column, which is the pod ID only. 
>
> - Configure Jenkins via the web interface as shown in slide 3 and 4 
> of [Kubernetes Application: CI/CD pipeline - Part I](https://www.cs.wcupa.edu/lngo/csc468/13-kubernetes-ci/index.html).
> - Add the following plugins to Jenkins:
>   - Kubernetes
>   - SSH Agent
``` 


> ## 3. Configure Jenkins 
> 
> In the subsequent slides, we are revisiting the configuration of 
> Jenkins in a more organized manner. 
> 
> - Configure SSH credentials
> - Configure one single executor to support remote SSH execution
> - Configure Kubernetes access for deploying Jenkins container-agents. 
> - Configure pod- and container-templates 
> 
```


> ## 4. Configure Jenkins: SSH credentials
> 
> - On the CloudLab head node, run `ssh-keygen` (do not enter any password when asked). 
> - Run `cat .ssh/id_rsa.pub >> .ssh/authorized_keys`
> - Run `cat ~/.ssh/id_rsa` and copy the displayed text, including the starting 
> and ending dashes without any extra spaces.  
> - On Jenkins Dashboard, go to `Manage Jenkins`/`Manage Credentials`.
>   - Click on `Jenkins` under `Stores scoped to Jenkins`, then `Global credentials (unrestricted)`.
>   - Click on `Add Credentials`. 
> - Fill in the boxes as follows:
>   - `Kind`: SSH Username with private name
>   - `Scope`: Global (Jenkins, nodes, items, all child items, etc)
>   - `ID`: cloudlab
>   - `Username`: Enter your CloudLab login username here. 
>   - `Private Key`: Check `Enter directly`, click `Add`, then paster the previously
>   copied private key to this box. 
>   - Click `OK`. 
> 
```


> ## 5. Configure Jenkins: Single executor
> 
> - On Jenkins Dashboard, go to `Manage Jenkins`/`Manage Nodes and Clouds`.
>   - Click on the gear icon for `Built-In Node` 
> - Fill in the boxes as follows:
>   - `Number of executors`: 1
>   - `Labels`: deploy
>   - `Usage`: Only build jobs with label expressions matching this node
> 
```


> ## 6. Configure Jenkins: Kubernetes
> 
> - On Jenkins Dashboard, go to `Manage Jenkins`/`Manage Nodes and Clouds`/`Configure Clouds`.
> - Select `Kubernetes` from `Add a new cloud` dropbox. 
> - Click on `Kubernetes Cloud Details`.
> - Fill in the boxes as follows:
>   - `Kubernetes Name`: kubernetes
>   - `Kubernetes URL`: Information of the `Kubernetes control plane` gotten from 
>   running `kubectl cluster-info` on the CloudLab head node.
>   - Check `Direction Connection` box.
>   - Click `Test Connection` to confirm connection. 
> 
```


> ## 7. Configure Jenkins: Pod Templates
> 
> - Continue on the `Configure Clouds` from the previous slide.
> - Click `Add Pod Template` then `Pod Template details`
> - Fill in the boxes as follows:
>   - `Name`: agent-template
>   - `Namespace`: jenkins
>   - `Usage`: Only build jobs with label expressions matching this node
>   - **Do not add container yet**
>   - Click on `Add Volume`:
>     - Select `Host Path Volume`
>     - Enter `/var/run/docker.sock` for both `Host path` and `Mount path`. 
>     - *This is to enable the building and pushing of Docker images*. 
```


> ## 8. Configure Jenkins: Container Templates
> 
> In the scope of `Pod Template`
> - Click `Add Container`
> - Fill in the boxes as follows:
>   - `Container Template Name`: golang
>   - `Docker image`: golang
> - Click `Add Container`
>   - `Container Template Name`: docker
>   - `Docker image`: docker
> - Click `Add Environment Variable` for the `docker` container template
>   - Prior to this, go to `hub.docker.com` and login to your Docker Hub account. 
>     - Go to Account Settings
>     - Go to `Security`. 
>     - Click on `New Access Token`. 
>     - Enter a short description for this token, allow `Access permission` to 
>     be `Read, Write, Delete`, and then click `Generate`. 
>     - Store this key some where safe. 
>    - First environment variable:
>      - `Key`: DOCKER_TOKEN
>      - `Value`: the access token copied from before. 
>    - Second environment variable:
>      - `Key`: DOCKER_REGISTRY
>      - `Value`: YOUR_DOCKERHUB_USERNAME/go_server
>    - Third environment variable:
>      - `Key`: DOCKER_USER
>      - `Value`: YOUR_DOCKERHUB_USERNAME
>
> - Click `Apply` and then `Save`. 
```


> ## 9. Setup the app
>
> - Create a branch called `go_app` on your `hello` repository (from the hands-on in the Jenkins' eposide).
> - The `go_app` branch should have the same contents as https://github.com/CSC468-WCU/hello/tree/go_app
> - Setup the `webhook` for the `go_app` to point to the Jenkins server in the previous slide. 
> - The composition of the files in this branch is:
>   - `main.go`: The Go file that serves as the web server (the application to be deployed).
>   - `main_test.go`: The Go file that serves as the test file (part of the CD process).
>   - `Jenkinsfile`: Setup the pipeline for Jenkins to build, test, and push and deploy (if test is passed) the 
>   Go app. 
>     - Edit the `registry` (line 4) to change to `YOUR_DOCKERHUB_USERNAME/go_server`. 
>     - Edit the `registry` (line 5) to change to `YOUR_DOCKERHUB_USERNAME`. 
>     - Edit the `registry` (line 73, 74, 75):
>       - Change my username `lngo` to your CloudLab username. 
>       - **Be careful of capitalization in your CloudLab username. It has to match exactly**.
>       - Change the IP address to the correct IP address of your head node.  
>   - `Dockerfile`: The Docker image that will package the web server. 
>   - `deployment.yml` and `service.yml`: K8 configuration files. 
>
```


> ## 10. Setup the Jenkins pipeline
>
> - Login to the Jenkins server. 
> - Select `New Item`, and create a new `Pipeline`named `go_server`.
>
> <img src="../fig/14-cdci/04.png" style="height:500px">
>
> - On `Build Triggers` tab, select `GitHub hook trigger for GITScm polling`,
> - On `Pipeline` tab, select the followings: 
>   - `Definition`: Pipeline script from SCM (*this will open new options*)
>   - `SCM`: Git
>   - `Branch Specifier`: `go_app` 
> - Click `Save`
>
> <img src="../fig/14-cdci/05.png" style="height:1000px">
>
> - Click `Build Now` to activate the first build
>
> <img src="../fig/14-cdci/06.png" style="height:600px">
>
> - Open a new browser tab and visit the IP address of `head` at port 32000 to see the running server
>
> <img src="../fig/14-cdci/07.png" style="height:400px">
>
```



> ## 11. CI/CD
>
> - Edit `main.go` in `go_app` to introduce and error.
> - Observe that the build failed, but the web server is still running. 
> - Change `main.go` and also `main_test.go` so that the build and test can pass. 
> - Observe the webserver updated after the build completes successfully. 
>
> <img src="../fig/14-cdci/08.png" style="height:1000px">
>
```




{% include links.md %}

