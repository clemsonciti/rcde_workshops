# Transferring files to and from Picotte

## CyberDuck

There are many ways to transfer files between your local computer and Picotte. One piece of 
software that works for both Mac and Windows machines is called CyberDuck. You can download 
it [here](https://cyberduck.io/download/).

After installation, click on "Open Connection". A new window will pop out:

:::{figure} ../fig/intro_picotte/cyberduck_1.png
Cyberduck connection settings to Picotte
:::

Let's configure the connection:
- in the drop-down menu on top, select "SFTP" instead of the default "FTP";
- in the "Server", please specify `picottelogin.urcf.drexel.edu`;
- make sure that Port is set to 22;
- specify your Picotte username and password.

Then, click on "Connect". If it complains about an "unknown fingerprint", click "Allow". Another window will pop out asking you to do two-factor verification:

:::{figure} ../fig/intro_Picotte/cyberduck_2.png
Cyberduck connection settings to Picotte
:::

At this point, another new window will pop up, which will contain the contents of your Picotte home directory 
(if this is your first time using Picotte, it will be empty). You can go to any other folder on Picotte by changing the 
path (e.g., `/beegfs/scratch/username`). You can upload files by clicking the "Upload" button, and download files by 
right-clicking them and selecting "Download".

:::{figure} ../fig/intro_Picotte/cyberduck_2fa.png
Home directory contents
:::



## Command line (Mac and Linux users)

Another option for advanced Mac and Linux users is to use the `scp` command from the terminal. Open a 
new terminal, but **don't connect to Picotte**. The `scp` command works like this:

~~~bash
scp <path_to_source> username@picottelogin.urcf.drexel.edu:<path_to_destination>
~~~

For example, here is the `scp` command to copy a file from the current directory on my local machine 
to my home directory on Picotte (`lbn28` is my Picotte username):

~~~bash
scp myfile.txt username@picottelogin.urcf.drexel.edu::/home/lbn28/
~~~

... and to do the same in reverse, i.e., copy from Picotte to my local machine:

~~~bash
scp lbn28@picottelogin.urcf.drexel.edu:/home/lbn28/myfile.txt .
~~~

The `.` represents the working directory on the local machine.

To copy entire folders, include the `-r` switch:

~~~bash
scp -r myfolder lbn28@picottelogin.urcf.drexel.edu:/home/lbn28/
~~~