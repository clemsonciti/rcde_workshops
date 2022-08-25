
# Deploying compute nodes for a supercomputer"
teaching: 0
exercises: 0
questions:
- "How do we deploy compute nodes and relevant software programmatically?"
objectives:
- " "
keypoints:
- " "


> ## 1. Setup webhook  in CloudLab
>
> - Webhook is a mechanism to automatically push any update on your GitHub repo 
> to the corresponding CloudLab repository. 
> 
> - Login to CloudLab. 
> - Top left, under `Experiments`, select `My Profiles`. 
>
> <img src="../assets/figure/12-compute/01.png" style="height:400px">
>
> - Click on the profile created for CSC466, then select `Edit`
> 
> <img src="../assets/figure/12-compute/02.png" style="height:600px">
>
> - Click on the `Push URL` bar, then click on the blue Clipboard icon. 
> 
> <img src="../assets/figure/12-compute/03.png" style="height:600px">
>
> - Go to the corresponding GitJub repository and go to `Settings`. 
>
> <img src="../assets/figure/12-compute/04.png" style="height:600px">
>
> - Go to `Webhooks`. 
>
> <img src="../assets/figure/12-compute/05.png" style="height:600px">
>
> - Click `Add webhook`. You will need to re-enter the password for your GitHub account next. 
>
> <img src="../assets/figure/12-compute/06.png" style="height:600px">
>
> - Pass the value copied from the clipboard in CloudLab into the `Payload URL` box.
> - Click on `Add webhook`. 
>
> <img src="../assets/figure/12-compute/07.png" style="height:620px">
```


> ## 2. Create a new branch on your GitHub repo
>
> - In your GitHub repository, create a new branch called `compute`.  
>
> <img src="../assets/figure/12-compute/08.png" style="height:700px">
>
> - If you set up your webhook correctly, `compute` should show up on your 
> CloudLab profile as well
> 
> <img src="../assets/figure/12-compute/09.png" style="height:700px">
>
> - In your GitHub repository, edit the `profile.py` file with [THIS CONTENT](https://raw.githubusercontent.com/linhbngo/csc496/compute-node/profile.py). 
> - Click `Commit changes` once done to save. 
> 
> <img src="../assets/figure/12-compute/10.png" style="height:700px">
>
> - Create a new file called `install_mpi.sh` with [THIS CONTENT](https://raw.githubusercontent.com/linhbngo/csc496/compute-node/install_mpi.sh)
> - Click `Commit new file` once done to save. 
>
> <img src="../assets/figure/12-compute/11.png" style="height:700px">
>
> - Go to CloudLab, refresh the page, and confirm that the hash of your `compute` branch here 
> match with the hash on GitHub repo.  
> - `Instantiate` from the `compute` branch. 
>
> <img src="../assets/figure/12-compute/12.png" style="height:700px">
>
```

{% include links.md %}




