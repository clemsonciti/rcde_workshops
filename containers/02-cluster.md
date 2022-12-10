
# Programmatic Deployment of Infrastructures
teaching: 0
exercises: 0
questions:
- ""
objectives:
- "Be able to launch OpenStack on CloudLab"
- "Understand the management of resources, including memory, CPU, storage, network, and security in the Cloud"
keypoints:
- ""


## 1. OpenStack on CloudLab    
 
- Log into [CloudLab](https://www.cloudlab.us/)
- Under **Experiments** drop down box, select **Start Experiment**.
>
<img src="../fig/05-programmatic/01.png" style="height:450px">

- Click **Change Profile**. 
>
<img src="../fig/05-programmatic/02.png" style="height:450px">
>
- Type **OpenStack** in the search box, and select the profile **OpenStack** 
as shown in the figure below. 
- Click **Select Profile** when done. 
>
<img src="../fig/05-programmatic/03.png" style="height:550px">
>
- Click **Next**. 

<img src="../fig/05-programmatic/04.png" style="height:500px">
>
- Select the options similar to the figure below. 
- If the **Parameterize** tab does not look like this, click **Previous** to 
go back one step, and then click **Next** again.
>
<img src="../fig/05-programmatic/05.png" style="height:600px">
>
- Only **Utah**, **Wisconsin**, and **Clemson** have been known to work with this 
profile. 
- I will use **Utah** for the remaining steps. 
>
<img src="../fig/05-programmatic/06.png" style="height:500px">
>
- Do not change anything on the **Schedule** step and click **Finish**. 
>
<img src="../fig/05-programmatic/07.png" style="height:500px">
>
- The startup scripts of this profile will take sometimes to run, approximately 
**thirty minutes to one hour**. 
- You will receive an email from CloudLab (to the registered) to inform you when 
the experiment is ready. 
>
<img src="../fig/05-programmatic/08.png" style="height:200px">
>
- Go to the experiment, and open the blue *Profile Instructions** box. 

<img src="../fig/05-programmatic/09.png" style="height:400px">
>
- Follow the instructions to login to OpenStack dashboard. Your passwords will be
randomly generated and unique to each experiment. 
>
<img src="../fig/05-programmatic/10.png" style="height:500px">
>
- You will see a Dashboard on a successful deployment as follows.
>
<img src="../fig/05-programmatic/11.png" style="height:600px">
>
```


## 2. Deploying compute resources from OpenStack    
 
- In the next sequence of hands-on, we will look at how OpenStack can 
support the deployment of a virtual machine inside its Nova compute 
components. 
>
```


## 3. Hands-on: Download Linux distribution
>
- We will use Alpine Linux, a light-weight distribution that was created
for containerization/cloud deployment. 
- From [Alpine Download Page](https://alpinelinux.org/downloads/), select the 
x86_64 Virtual version. 
>
<img src="../fig/05-programmatic/12.png" style="height:600px">
>
{:.slide}


## 4. Hands-on: Create cloud image
>
- Go to your CloudLab Dashboard. 
- Go to **Compute**/**Images**, then click on **Create Image**.  
>
<img src="../fig/05-programmatic/13.png" style="height:600px">
>
- Click **Browse** and find and select the downloaded ISO file from the
the previous slide. 
- Set the other parameters as shown in the figure below. 
- Click **Create Image** when done. 

<img src="../fig/05-programmatic/14.png" style="height:800px">
>
- The image will show up in the **Images** tab. 
>
<img src="../fig/05-programmatic/15.png" style="height:600px">
>
{:.slide}


## 5. Hands-on: Create volumes
>
- Go to your CloudLab Dashboard. 
- Go to **Volumes**/**Volumes**, then click on **Create Volume**.  
>
<img src="../fig/05-programmatic/16.png" style="height:600px">
>
- Set the other parameters as shown in the figure below. 
- Alpine takes up a small amount of storage, so 2GB is more than enough 
for a simple installation.
- Click **Create Volume** when done. 

<img src="../fig/05-programmatic/17.png" style="height:600px">
>
- The volume will show up in the **Volumes** tab. 
>
<img src="../fig/05-programmatic/18.png" style="height:300px">
>
{:.slide}


## 6. Hands-on: Launching a compute instance
>
- Go to your CloudLab Dashboard. 
- Go to **Compute**/**Instances** and click on **Launch Instance**.  
>
<img src="../fig/05-programmatic/19.png" style="height:300px">
>
- Set the instance name and other parameters, then click **Next**

<img src="../fig/05-programmatic/20.png" style="height:600px">
>
- Use the up arrow to select the **alpine** image as the allocated image. Click **Next**. 
>
<img src="../fig/05-programmatic/21.png" style="height:600px">
>
- Select **m1.tiny** as the compute flavor. Click **Next**. 
>
<img src="../fig/05-programmatic/22.png" style="height:600px">

- Select **flat-lan-1-net** as the connected network. Click **Launch Instance**. 
>
<img src="../fig/05-programmatic/23.png" style="height:600px">
>
- It should take a few minute for the instance to become ready. 
>
<img src="../fig/05-programmatic/24.png" style="height:300px">
>
{:.slide}


## 7. Hands-on: Volume attachment and Linux installation
>
- Go to your CloudLab Dashboard. 
- Go to **Compute**/**Instances**
- Click on the drop-down arrow under **Actions** for the alpine instance, 
then click **Attach Volume**.  
>
<img src="../fig/05-programmatic/25.png" style="height:600px">
>
- Select your `sda_****` volume ID created earlier, then click **Attach Volume**

<img src="../fig/05-programmatic/26.png" style="height:300px">
>
- Click on the drop-down arrow under **Actions** for the alpine instance. 
- Select **Console**.
>
<img src="../fig/05-programmatic/27.png" style="height:600px">
>
- Right click on **Click here to show only console** and select **Open link in new tab**.
- This helps with navigating back and forth.  
>
<img src="../fig/05-programmatic/28.png" style="height:600px">

- A new console tab appears! 
- You are now booting from the Alpine distro. 
>
<img src="../fig/05-programmatic/29.png" style="height:600px">
>
- Type **root** into the`localhost login:` prompt and hit Enter to log in. 
>
<img src="../fig/05-programmatic/30.png" style="height:400px">
>
- A quick review of Alpine installation process can be found 
on [their wiki](https://wiki.alpinelinux.org/wiki/Install_to_disk)
- Type `setup-alpine` and hit Enter to start the installation process. 
- Use the following options:
  - `Select keyboard layout`: `us`
  - `Select variant`: `us`
  - `Enter system hostname ...`: Hit Enter to accept default. 
  - `Which one do you want to initialize?`: Hit Enter to accept `eth0` as the default interface. 
  - `Ip address for eth0`: Hit Enter to accept `dhcp` as the default value. 
  - `Do you want to do any manual network configuration?`: Hit Enter to accept `n` as the default value. 
  - Enter a **complex** password for root. DO NOT MAKE AN EASY PASSWORD. If your cloud instance got 
  hacked and used for malicious purposes, you will be banned from CloudLab. Retype the password. 
  - `Which timezone are you in?`: Type `EST` and hit Enter. 
  - `HTTP/FTP proxy URL?`: Hit Enter to accept `none` as the default value. 
  - For the mirror question, type `30` (the one from princeton), then hit Enter. 
  - `Which SSH server?`: Hit Enter to accept `openssh` as the default value. 
  - `Which disk(s) would you like to use?`: Review the lines above, and select the listed disk. 
  There should be one as we already attached a volume to this instance. For me, it is `vdb`, so I 
  type in `vda` and hit Enter. 
  - `How would you like to use it?`: Type `sys` and hit Enter. 
  - `WARNING: Erase the above disk(s) and continue?`: Type `y` and hit Enter. 
>
<img src="../fig/05-programmatic/31.png" style="height:600px">
>
- Once the installation process is completed, Leave this console running and return to the Dashboard. 
- Go to **Compute**/**Instances**
- Click on the drop-down arrow under **Actions** for the alpine instance.  
- Select the `sda_****` volume ID selected earlier, then click **Detach Volume**

<img src="../fig/05-programmatic/32.png" style="height:600px">
>
- Select the `sda_****` volume ID created earlier, then click **Detach Volume**

<img src="../fig/05-programmatic/33.png" style="height:300px">
>
- Go to your CloudLab Dashboard. 
- Go to **Volumes**/**Volumes**.  
- In the **Actions** box of `sda_****`, click the drop-down arrow and select **Upload to Image**. 
>
<img src="../fig/05-programmatic/34.png" style="height:400px">

- Set **Image Name** to `alpine-disk` and **Disk Format** as `Raw`, then click 
**Upload**. 
>
<img src="../fig/05-programmatic/35.png" style="height:600px">
>
- Successful upload:
>
<img src="../fig/05-programmatic/36.png" style="height:600px">
>
{:.slide}


## 8. Challenge
- Launch another compute instance using the newly created `alpine-disk` image. 
  - Pay attention to the flavor. 
- Log into the console and confirm that you can use the root password created earlier to log in
>
> ## Expected Outcome: 
> 
> <img src="../fig/05-programmatic/37.png" style="height:600px">
>
{: .solution}
{: .challenge}


## 9. Setup Apache webserver (from the volume-based Alpine from Challenge 8)
>
- You should be inside the console after log in as root and have the root password. 
- Run the following commands to install Apache webserver
>
~~~
$ apk update
$ apk add apache2
$ rc-service apache2 start
~~~
{ :.language-bash}
>

<img src="../fig/05-programmatic/38.png" style="height:400px">
>
```


## 10. Setup public IP address
>
- To expose the webserver, we need a public IP address. 
- Go to your CloudLab Dashboard. 
- Go to **Compute**/**Instances**
- Click on the drop-down arrow under **Actions** for the alpine instance, 
then click **Associate Floating IP**. 
>
<img src="../fig/05-programmatic/39.png" style="height:600px">
>
- Click on the `+` sign to allocate IP address. 
>
<img src="../fig/05-programmatic/40.png" style="height:300px">
>
- Click on **Allocate IP**. 
>
<img src="../fig/05-programmatic/41.png" style="height:300px">
>
- Click on **Associate**.
>
<img src="../fig/05-programmatic/42.png" style="height:300px">
>
- You should see the public IP address with your instance
>
<img src="../fig/05-programmatic/43.png" style="height:300px">
>
- Try visiting this IP address now, anything?
>
```


## 12. Cloud security basic
- In the cloud, `egress` means traffic that’s leaving from inside the private network out to the 
public internet (similar to standard network definition).
- In the cloud, `ingress` refers to unsolicited traffic sent from an address in public internet to 
the private network – it is not a response to a request initiated by an inside system. In this case, 
firewalls are designed to decline this request unless there are specific policy and configuration that 
allows ingress connections.
>
<img src="../fig/05-programmatic/44.png" style="height:600px">
<img src="../fig/05-programmatic/45.png" style="height:600px">
>
```


## 11. Handle security
>
- Go to your CloudLab Dashboard. 
- Go to **Network**/**Security Group**
- Click on **Manage Rules**. 
>
<img src="../fig/05-programmatic/46.png" style="height:600px">
>
- Click `Add Rules` 
>
<img src="../fig/05-programmatic/47.png" style="height:600px">
>
- In the `Rule` drop down box, select `HTTP`, then click `Add`. 
>
<img src="../fig/05-programmatic/48.png" style="height:600px">
>
- You can see the new `Ingress` rule for HTTP.
>
<img src="../fig/05-programmatic/49.png" style="height:600px">
>
- The apache webserver is now visible
>
<img src="../fig/05-programmatic/50.png" style="height:300px">
>
```



{% include links.md %}

