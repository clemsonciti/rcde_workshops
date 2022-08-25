
# Kubernetes Application: CI/CD pipeline - Part I"
teaching: 0
exercises: 0
questions:
- ""
objectives:
- "Being able to deploy a Jenkins server inside Kubernetes and integrate with GitHub 
  for automated building/testing."
keypoints:
- ""



> ## 1. Preparation: individual!
>
> - Each student should launch an experiment of their own. 
> - Visit [Dr. Ngo's Kubernetes-Jenkins branch](https://github.com/CSC468-WCU/csc468cloud/tree/kubernetes-jenkins) and create a copy of this branch in your GitHub CloudLab profile repository. 
> - You can overwrite the existing main branch, or, even better, create a new branch. 
> - Once the experiment is fully deployed, **and all Startup Finished running**:
> - SSH into the head node and run the followings
>
> ~~~
> $ cd
> $ bash /local/repository/launch_network.sh
> $ kubectl get nodes
> ~~~
> {: .language-bash}
>
```


> ## 2. Introduction to Jenkins
> 
> - [Jenkins](https://www.jenkins.io/)
> - Open-source automation server that allows continuous integration:
>   - Recognized whenever source code is changed and/or updated. 
>   - Automatic building and testing of updated codes.  
``` 


> ## 3. Deploy Jenkins on Kubernetes
>
> - SSH to the headnode of your Kubernetes cluster. 
>
> ~~~
> $ kubectl create namespace jenkins
> $ kubectl create -f /local/repository/jenkins.yaml --namespace jenkins
> $ kubectl get pods -n jenkins
> ~~~
> {: .language-bash}
>
> - Repeat the `kubectl get pods -n` command a few time until you see that the 
> `jenkins` pod is up and running. 
>
> <img src="../fig/13-jenkins/01.png" style="height:500px">
>
> - What did we just deploy: [jenkins.yaml](https://github.com/CSC468-WCU/csc468cloud/blob/kubernetes-jenkins/jenkins.yaml).
>   - [Kubernetes' deployment template](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).
>   - `spec.replicas`: 1
>   - `spec.containers`: `linhbngo/jenkins-gcc:latest`
>   - `spec.containers.ports`: `http-port`:8000 and `jnlp-port`:50000
>   - ...
>
> - Next, run the commands to create Service.
>   - A `Service` is an abstraction that defines a logical set of Pods and a 
>   policy by which to **access** them. 
>   - The set of pods targeted by a service is determined by a `selector`. 
>   - It allows the decoupling of the microservices provided by the pods and 
>   the actual pods themselves (which could be created and destroyed as needed).
> - [The service file for the Jenkins' pod.](https://github.com/CSC468-WCU/csc468cloud/blob/kubernetes-jenkins/jenkins-service.yaml)
>
> ~~~
> $ kubectl create -f /local/repository/jenkins-service.yaml --namespace jenkins
> $ kubectl get services --namespace jenkins
> ~~~
> {: .language-bash}
>
> <img src="../fig/13-jenkins/02.png" style="height:250px">
>
> ~~~
> $ kubectl get nodes -o wide
> ~~~
> {: .language-bash}
>
> - Grab one of the values of `INTERNAL-IP`, open a browser 
> and go to `INTERNAL-IP:30000`
>
> <img src="../fig/13-jenkins/03.png" style="height:500px">
>
> - To find the default password:
>   - Write down the `NAME` value from the first command and
>   use that for the second command. 
>
> ~~~
> $ kubectl get pods -n jenkins
> $ kubectl logs jenkins-794699f9bc-45tkq -n jenkins
> ~~~
> {: .language-bash}
>
> <img src="../fig/13-jenkins/04.png" style="height:700px">
>
> - Copy and paste the initial admin password to the Jenkins' page and hit 
> `Continue`. 
>
```


> ## 4. Configure Jenkins
>
> - Click on `Install selected plugins`
>
> <img src="../fig/13-jenkins/05.png" style="height:700px">
>
> - You can either try to create the first admin user or Skip and continue
> as admin. 
>
> <img src="../fig/13-jenkins/06.png" style="height:700px">
>
> - Click `Save and Finish`, then `Start using Jenkins`
>
> <img src="../fig/13-jenkins/07.png" style="height:700px">
> <img src="../fig/13-jenkins/08.png" style="height:700px">
> <img src="../fig/13-jenkins/09.png" style="height:700px">
>
```


> ## 5. Integrate Git and Jenkins
>
> - Create a new public GitHub repository named `hello` with the contents
> similar to [this repository](https://github.com/CSC468-WCU/hello)
> - In your `hello` repo, go to `Settings/Webhooks` and add a 
> new webhook with the settings similar to the screenshot. 
>   - **NOTE**: The Payload URL should be **YOUR** jenkin server URL. 
>   - Click `Add webhook` when done. 
>
> <img src="../fig/13-jenkins/10.png" style="height:700px">
>
> - On your Jenkins dashboard, select `New Item`, then setup the new project
> with the settings similar to the screenshot below. Clicl `OK` when done. 
> 
>
> <img src="../fig/13-jenkins/11.png" style="height:700px">
>
> - Click `Source Code Management`:
>
> <img src="../fig/13-jenkins/12.png" style="height:700px">
>
> - Click `Build Triggers` and select `GitHub hook trigger for GITScm polling`. 
> - Click `Build`/`Add build step` and select `Execute shell`. 
>
> <img src="../fig/13-jenkins/13.png" style="height:700px">
>
> - Enter `make` in the Command box, then click `Save`. 
>
> <img src="../fig/13-jenkins/14.png" style="height:700px">
>
> - Make an edit to your C file in the hello repo and observe how the jenkins 
> server launches a build. 
>
> <img src="../fig/13-jenkins/15.png" style="height:700px">
>
> - Explore the interface to learn more about the details of the build. 
> - Try to push an incorrect edit to the C file and see how the Jenkins server
> update the build. 
>
```


> ## 6. Setup Jenkins agents to run on the Kubernetes cluster
>
> - **Reminder**: If you are launching a new experiment
> 
> ~~~
> $ bash /local/repository/launch_network.sh
> ~~~
> {: .language-bash}
>
> - Expand NodePort range by editing `/etc/kubernetes/manifests/kube-apiserver.yaml` and add the following line:
>   - `service-node-port-range=30000-50000`
>
> <img src="../fig/13-jenkins/22.png" style="height:800px">
>
> - `sa` stands for `service account`. 
> 
> ~~~
> $ kubectl create namespace jenkins
> $ kubectl create clusterrolebinding permissive-binding --clusterrole=cluster-admin --user=admin --user=kubelet --group=system:serviceaccounts
> $ kubectl -n kube-system create sa jenkins
> $ kubectl create clusterrolebinding jenkins --clusterrole cluster-admin --serviceaccount=jenkins:jenkins
> $ kubectl create -f /local/repository/jenkins.yaml --namespace jenkins
> $ kubectl create -f /local/repository/jenkins-service.yaml --namespace jenkins
> ~~~
> {: .language-bash}
>
> After setup Jenkins (see slides 4), let's add Kubernetes support
>
> - Go to **Manage Jenkins**, then **Manage Nodes and Clouds**, go to the setting of the built-in node
> and set the number of executors to 0.  
>
> <img src="../fig/13-jenkins/16.png" style="height:200px">
>
> - Go to **Manage Jenkins**, then **Manage Plugins**
>   - Type `Kubernetes` into the search box and select the Kubernetes plugin. 
>   - Click `Install without Restart`. 
>   - Scroll to the bottom of the following page and check the `Restart Jenkins after installing` box. 
>   - Wait until Jenkins restart and log back in. 
> 
> <img src="../fig/13-jenkins/17.png" style="height:600px">
>
> - **Manage Jenkins**, then **Manage Nodes and Clouds**, then **Configure Cloud**.
> - Select `Kubernetes` from `Add a new cloud` dropbox. 
> 
> <img src="../fig/13-jenkins/18.png" style="height:300px">
>
```


> ## 7. Setup Jenkins/Kubernetes: configure Kubernetes Cloud details
>
> - Run `kubectl cluster-info` to get the information about the `Kubernetes control plane`. 
> 
> ~~~
> $ kubectl cluster-info
> ~~~ 
> {: .language-bash}
>
> <img src="../fig/13-jenkins/19.png" style="height:200px">
>
> - Enter the information as shown in the figure below:
>   - `Kubernetes URL`: use the information from `Kubernetes control plane`. 
>   - Check `Direct Connection` box. 
>   - Click `Test Connection` to confirm successful connection. 
> 
> <img src="../fig/13-jenkins/20.png" style="height:800px">
>
```


> ## 8. Setup Jenkins/Kubernetes: configure Pod Templates
>
> - Click `Pod Templates`.
>   - Click `Add Pod Template`.  
>   - Click `Add Container`. 
> - Fill in information about the template for Pod/Container as shown below
> 
> <img src="../fig/13-jenkins/21.png" style="height:800px">
>
> - Click `Save`. 
>
```


> ## 9. Launch a new pipeline
>
> - Create a branch from your `hello` repository and named it `hello_kube`.
> Make sure that this `hello_kube` branch is copied from [the instructor's hello repo's hello_kube branch](https://github.com/CSC468-WCU/hello/tree/hello_kube)
> 
> - In `Jenkins`, create a `New Item` of type `Pipeline` and name it `hello_kube`.
> - Under `Build Triggers` and check `GitHub hook trigger for GITScm polling`. 
> - Under `Pipeline` select `Pipeline script from SCM`. 
> - Once `SCM` appears, select `Git` and provide the `Repository URL` for **your** hello repo. 
> - Under `Branch to build`, change `*/master` to `*/hello_kube`.
> - Make sure that `Script Path`, enter `Jenkinsfile`. 
>   - This is the `Jenkinsfile` in the `hello_kube` branch. 
>   - Click `Apply`. 
> 
> <img src="../fig/13-jenkins/23.png" style="height:600px">
>
> - Click `Save`. 
>
```


> ## 10. Where the wild things are
>
> <iframe frameborder="0" style="width:100%;height:643px;" src="https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1#G13PZw5Fv7WSumADF2GOBy2Yw_WHlTx-h9"></iframe>
>
{:.slide}

{% include links.md %}

