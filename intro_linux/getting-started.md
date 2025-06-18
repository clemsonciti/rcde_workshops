# Getting started

## The prompt

When you first open the shell, you'll see the *prompt*, indicating that the
shell is waiting for input.

The prompt usually has some information about the system (e.g. your username, or
the name of your computer), followed by a `$`. In the examples for this
workshop, we’ll show the prompt as `$`:

```
$
```

If your prompt looks different (it might not have a `$`), don't worry. The Prompt
is customizable and appears differently on different systems.

```{warning}
When following the examples, *do not type the prompt* when typing commands. Only type the command that follows the prompt.
```

To execute a command, type it into the prompt and press `Enter`. When the
command completes you be returned to the prompt.

## Our first command

Let's try typing our first command. Type `whoami` at the prompt, and press enter:

```
$ whoami
```

The `whoami` command output your username. The shell will print your username,
then return you to the prompt, where you can type another command:

```
$ whoami
jjp366
$
```

```{warning}
The shell is case-sensitive and typo-sensitive; commands need to be entered
exactly as shown. It's important to use the right case (upper or lower), to use
spaces when needed, and not to use spaces when not needed. For example, if you
type `whoam` instead of `whoami`, you will get an error:

~~~
$ whoam
bash: whoam: command not found
~~~
```

Don't stress out about these sorts of errors. Nothing will break as a result of
them, and it's normal to get lots of errors like this when learning the shell
for the first time.