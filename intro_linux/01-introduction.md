# Introducing the Shell

The Palmetto cluster is running the Linux operating system (more specifically, [CentOS 8](https://www.centos.org/)). An *operating system* is a special software that coordinates the computer's hardware and other software. Other popular operating systems are Windows and Mac OS. 

This workshop will teach you how to use the Linux command line interface. For this purpose, we will use the *terminal* software, such as MobaXTerm or Putty (on Windows machines) or Terminal (on Mac and Linux machines). We will use the terminal sowtare to enter the Linux commands which will be immediately executed by Palmetto. The terminal does not use graphical features (like windows or buttons) and the use of the mouse is very limited. This is the most direct way to interact with Palmetto; there is an option of graphical user interface (whih we will not cover in today's workshop), but this way is indirect because the graphical interaction needs to be translated into Linux commands by the operating system. Another advantage of using the Linux commands is *scripting*, where we can order the oprerating system to perform some ations repeatedly instead of clicking the mouse each time we need to perform the action.    

Most Linux computers, including Palmetto, run a separate program called **command shell**.
What the user types goes into the shell,
which then figures out what commands to run and orders the computer to execute them. Note, the shell is called *the shell* because it encloses the operating system in order to hide some of its complexity and make it simpler to interact with.

A shell is a program like any other.
What's special about it is that its job is to run other programs
rather than to do calculations itself.
Palmetto runs the shell that's called **Bash**, which is the most popular Linux shell.


The command line interface works as follows. You enter the command, press "Enter", and the operating system executes the command. When it's done, you are prompted to enter the next command. It is possible to stop the execution by typing Ctrl+C.

A word of warning: Linux is case-sensitive and typo-sensitive. Commands need to be entered directly as shown; it is important to use the right case (upper or lower), to use spaces when they are needed, and not to use spaces when they are not needed.

Now, let's log into Palmetto.


