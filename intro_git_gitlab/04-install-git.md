# Installing Git

Before you can run any `git` commands, you must have a copy of Git installed on
your computer.

## Windows

For Windows systems, download and run the installer from
[git-scm.com](https://git-scm.com/download).

After you finish the installation, find and open **Git Bash** from the Start
menu. The `git` command is only available through this special terminal window
by default.

## macOS

On macOS, Git is available as part of Apple's command line developer tools. To
access these tools, open **Terminal** from the **Utilities** section of your
Applications folder.

Run the following command to install the command line developer tools.

```sh
sudo xcode-select --install
```

Before you can use the command line developer tools, you must accept the terms
of the license agreement.

```sh
sudo xcodebuild -license
```

Now, you should be able to use the `git` command in your Terminal.

## Linux

On Linux, you will need to install Git through your package manager.

The following command will work on Ubuntu and other Debian-based operating
systems. If you are using a different distribution, you will need to do some
research to locate the correct command and package names.

```sh
sudo apt-get install git
```

Now, you should be able to use the `git` command in your Terminal.
