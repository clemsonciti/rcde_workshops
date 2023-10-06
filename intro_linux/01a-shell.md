# Shell Specifics

## Prompt

The prompt provides information to the user and means the shell is waiting for a command. On Palmetto, your prompt might look like this:

```
[username@picotte001 ~]$
```

The prompt in a bash shell usually consists of a dollar (`$`) sign and may also contain other information:
this prompt tells you `your username` and which node
you are connected to -
`picotte001` is the "login" node.
It also tells you your current directory,
i.e., `~`, which, as you will learn shortly,
is short for your *home* directory.
We will mostly refer to the prompt as just `$`, i.e.,

~~~
$
~~~

To execute a command, type it into the prompt and press `Enter`. When the command completes you be returned to the prompt.

![Command Syntax](../fig/shell_command_syntax.svg)