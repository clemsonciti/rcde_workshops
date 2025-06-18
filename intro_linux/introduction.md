# What is the shell?

## Background

Usually when we interact with computers we use a **graphical user interface**
(GUI). With a GUI, we give instructions by clicking the mouse and using menus
and buttons. GUI software is easy to learn, because you can tell what actions
are available just by looking at the screen. Think of an email program: you can
write a new message, check for incoming mail, archive messages, etc. and there
are labeled buttons for all these things, so you know what choices you have.

This makes it easy to get started with a GUI, but scales poorly. Imagine you
need to send emails to 1000 students, each with the student's transcript
attached. With a GUI, this would take you hours: you'd have to click thousands
of times to create each email, attach the transcript, and send it—and you might
make a mistake!

This kind of task is where we turn to the Unix shell, which allows you to do
repetitive tasks automatically and fast. Using the shell, you could do the email
sending task above in less than a minute.

## The shell

The shell is a program where you type a "command"—a request for the computer to
do something. The shell runs the command, prints its output, and asks you for
another command. At it's core, that's it; it's pretty simple. The power of the
shell comes from the huge variety of commands available (commands can do
anything from creating an empty file to complex molecular simulations), and the
ability to connect commands together into "pipelines" that do more than the sum
of their parts.

```{note}
You might also hear the shell referred to as a *terminal* or *command-line interface*. Technically, these are three separate but related concepts, but for getting started you can think of them all as the same thing.
```

```{admonition} Why is the called a "shell"? What is Unix?
:class: note, dropdown
Great questions. The reason why the command-line interface is called a shell is lost to history. It might be because a shell is a relatively thin layer around an operating system.

[Unix](https://en.wikipedia.org/wiki/Unix) is an operating system original developed in the 1960s. The macOS and Linux operating systems of today all are derived from Unix. These systems all share a common command line interface, which is called the "Unix shell" because of its origins in the Unix operating system.

Windows is not related to Unix. It has it's own command-line interfaces (cmd.exe, Powershell), but they have their own commands that aren't compatible with Unix shell commands. This is why you had to install a Unix shell before starting the workshop if you're a Windows user.
```

The shell takes effort and time to learn. Unlike a GUI, which shows you all the
choices you have, choices on the shell are not automatically presented to you,
so you must learn the commands you need, like learning vocabulary in a new
language.

A small number of commands will take you a long way, and we'll learn those
essential few today.