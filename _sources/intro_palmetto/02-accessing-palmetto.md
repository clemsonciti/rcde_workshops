# Accessing the Palmetto Cluster

Palmetto is accessed using the SSH (["Secure shell"](https://en.wikipedia.org/wiki/Ssh_(Secure_Shell))) protocol. Palmetto runs the *SSH server*; on your local machine, you will need to run *SSH client* which connects to a server using a command-line *terminal*. The commands that are entered on the terminal are processed by the server on Palmetto.

## Mac

To start the SSH client on a Mac, you can open the Terminal Application (which is usually located in `Applications` &rarr; `Utilities`) and run the following:

```bash
ssh <your clemson username>@login.palmetto.clemson.edu
```

## Windows

For Windows, first you need to download and install
[MobaXterm Home Edition](https://mobaxterm.mobatek.net/download.html).

:::{important}
It is important that you unzip the downloaded installer prior to installation.
The zipped installer file contains an additional data file besides the installer
executable. This data file is not accessible if the installer executable is
called from inside the zipped file (something Windows allows you to do).
:::

After MobaXterm starts, click the `Session` button.

:::{figure} ../fig/intro_palmetto/mobaxterm_0.png
Main MobaXterm Windows
:::


Select SSH session and use the following parameters (whichever required), then click `OK`:

* Remote host: `login.palmetto.clemson.edu`
* SSH-browser type: Enhanced SCP
* Port: 22

:::{figure} ../fig/intro_palmetto/mobaxterm_1.png
MobaXterm SSH Session Settings
:::

## Entering Username and Password

At this stage, for both Mac and Windows, you will be asked to enter your username
and password, then DUO option. Use your usual Clemson username (without @clemson.edu part) and Clemson
password.

:::{note}
As you type your password, nothing will appear (not even asterisks). This can be confusing, but it
is the expected behaviour. The SSH server is still receiving your password.
:::

:::{figure} ../fig/intro_palmetto/mobaxterm_2.png
Logging into palmetto
:::

::::{admonition} Windows Users
With MobaXterm, you may be asked to save your password.  For now, press No.

:::{figure} ../fig/intro_palmetto/mobaxterm_3.png
MobaXterm asking to save password
:::
::::

When logged in,
you are presented with a welcome message
and the following "prompt":

~~~bash
[username@login001 ~]$
~~~

The prompt in a bash shell usually
contains a (`$`) sign,
and shows that the shell is waiting for input.
The prompt may also contain other information:
this prompt tells you `your username` and which node
you are connected to -
`login001` is the "login" node.
It also tells you your current directory,
i.e., `~`, which, as you will learn shortly,
is short for your *home* directory.

In the figure below, MobaXterm also gives you a GUI browser of your home
directory on Palmetto. For Mac OS and Linux terminal, you will only have the
command line interface to the right.


:::{figure} ../fig/intro_palmetto/mobaxterm_4.png
Logged into Palmetto on MobaXterm
:::

:::{admonition} Key Points
- Palmetto can be accessed by an SSH (secure shell) client
- Windows user can use `MobaXterm` application
- Mac users can use the `Terminal` application
:::

