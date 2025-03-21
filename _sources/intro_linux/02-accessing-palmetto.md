# Accessing the Palmetto Cluster

## Remote login (SSH)

To be able to run commands on Palmetto from your own machine, you will first need to log in. We will login via **SSH** which will provide us a shell on one of Palmetto's login nodes.

For Mac OS X, you can open the Terminal Application (which is usually in Applications &rarr; Utilities folder) and run the following:

~~~
ssh <your Clemson username>@slogin.palmetto.clemson.edu
~~~

After logging in and completing Duo 2FA you are presented with a welcome message and the following "prompt":

~~~
[username@vm-slurm-p-login01 ~]$
~~~

More information about accesing Palmetto via SSH can be found on the [RCD Documentation Site](https://docs.rcd.clemson.edu/palmetto/connect/ssh/)

Let's enter our first command!
Type the command `whoami`, then press the Enter key (sometimes marked Return) to send the command to the shell.
The command's output is the ID of the current user.

~~~
$ whoami
~~~
