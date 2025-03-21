# .bashrc and Environment Customization

The `.bashrc` file is a script that is executed every time a new Bash shell session is started for an interactive user. This file contains various settings and customizations that affect the behavior of the shell. It’s typically located in the home directory (`~/.bashrc`), and you can edit it to set environment variables, define custom functions, or tweak other shell settings.

The `.bashrc` file is loaded automatically when you start a terminal. After making changes, you can reload it by running:

```bash
source ~/.bashrc
```

## Customizing .bashrc

Custom variables can be set in `~/.bashrc` that will be available in all scripts and shell sessions.

```bash
export MY_VAR="some value"
export SCRATCH="/scratch/$USER"
```

:::{note}
In `~/.bashrc`, you must `export` the variable to make it available in scripts and child processes.
:::

## Making changes to $PATH

`$PATH` defines the directories that the shell searches when you run a command. These directories are a colon separated string that is searched from left to right. View your current `$PATH`  with:

```bash
echo $PATH
```

If you want to add a directory to your `$PATH`, update the variable in your `~/.bashrc`.

```bash
export PATH=$PATH:~/bin
export PATH=$PATH:~/.local/bin
```

:::{warning}
Be careful changing the value of $PATH. Always make sure to include the current value in your new value, or else you might lose access to builtin commands.
:::

If not making changes to `$PATH`, you will need to provide a full path to the executable you wish to run. Without the full path, the shell will search the `$PATH` and return "Command Not Found". For example, if you're trying to run the bash script `run.sh` that is located at `/home/$USER/scripts/run.sh`, you can do so in the following ways:

If your current working directory is `/home/$USER/scripts`:

```bash
./run.sh
```

Otherwise:

```bash
/home/$USER/scripts/run.sh
```

As you can see, adding `~/scripts` to your `$PATH` can eliminate the need to enter the full path to the script and allow you to run the script from any directory. You can add additional scripts to that folder and run them without making other changes.
