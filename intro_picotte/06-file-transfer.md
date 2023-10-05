# Transferring files to and from Palmetto

## CyberDuck

There are many ways to transfer files between your local computer and Palmetto. One piece of software that works for both Mac and Windows machines is called CyberDuck. You can download it [here](https://cyberduck.io/download/).

After installation, click on "Open Connection". A new window will pop out:

:::{figure} ../fig/intro_palmetto/cyberduck_1.png
Cyberduck connection settings to Palmetto
:::

Let's configure the connection:
- in the drop-down menu on top, select "SFTP" instead of the default "FTP";
- in the "Server", please specify `xfer02-ext.clemson.edu`;
- make sure that Port is set to 22;
- specify your Palmetto username and password.

Then, click on "Connect". If it complains about an "unknown fingerprint", click "Allow". Another window will pop out asking you to do two-factor verification:

:::{figure} ../fig/intro_palmetto/cyberduck_2.png
Cyberduck connection settings to Palmetto
:::

Type "1" (the number one) or the word "push" if you want to get a DUO push notification. After two-factor verification, a yet another new window will pop up, which will contain the contents of your Palmetto home directory (if this is your first time using Palmetto, it will be empty). You can go to any other folder on Palmetto by changing the path (e.g., `/scratch1/username`). You can upload files by clicking the "Upload" button, and download files by right-clicking them and selecting "Download".

## Command line (Mac and Linux users)

Another option for advanced Mac and Linux users is to use the `scp` command from the terminal. Open a new terminal, but **don't connect to Palmetto**. The `scp` command works like this:

```bash
scp <path_to_source> username@xfer02-ext.clemson.edu:<path_to_destination>
```

For example, here is the `scp` command to copy a file from the current directory on my local machine to my home directory on Palmetto (`dndawso` is my Palmetto username:

```bash
scp myfile.txt dndawso@xfer02-ext.clemson.edu:/home/dndawso/
```

... and to do the same in reverse, i.e., copy from Palmetto to my local machine:

```bash
scp dndawso@xfer02-ext.clemson.edu:/home/dndawso/myfile.txt .
```

The `.` represents the working directory on the local machine.

To copy entire folders, include the `-r` switch:

```
scp -r myfolder dndawso@xfer02-ext.clemson.edu:/home/dndawso/
```

## Globus

If you need to transfer several gigabytes of data, and you find CyberDuck too slow, you can use Globus. The interface is not as intuitive, but the file transfer speeds are much higher. [The guide to using Globus is on our website](https://www.palmetto.clemson.edu/palmetto/basic/started/#transfer-large-files-using-globus).

:::{admonition} Key Points
- Windows and Mac users can use CyberDuck for file transfer
- Mac and Linux users can use SCP for file transfer
- Large amounts of data can be transferred with Globus
:::
