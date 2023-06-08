# Version Control Overview

Before we go over how to use any version control software, it is important to
understand the foundations of version control.

## What is Version Control?

:::{admonition} Main Idea

Version control is a **system** that **tracks changes** to files **over time**.

:::

For example, let's say you are working on `hello.c` for your class project that
is due in a few weeks. The source code for the program will change a bit each
time you work on the project.

:::{dropdown} **Version 1**: 2023/01/01 at 4:30 PM

Just starting out with a basic hello world program here.

Here's what the `hello.c` file looked like at that time:

```c
#include <stdio.h>

int main() {
   printf("Hello, World!");

   return 0;
}
```

:::

:::{dropdown} **Version 2**: 2023/01/14 at 10:15 AM

Then, you think you have learned the syntax, so you try adding your own
statement.

Here's what the `hello.c` file looked like at that time:

```c
#include <stdio.h>

int main() {
   printf("Hello, World!");
   printf("Code is cool!");

   return 0;
}
```

:::

:::{dropdown} **Version 3**: 2023/01/22 at 11:59 PM

Finally, _right before the deadline_, you read enough StackOverflow posts to get
some interactive functionality working.

Here's what the `hello.c` file looked like at that time:

```c
#include <stdio.h>

int main() {
   char* name;
   printf("Who are you? ");
   scanf("%s", &name);

   printf("Hello, %s!", name);
   printf("Code is cool!");

   return 0;
}
```

:::

A version control system would show you the history of changes to the file over
time, similar to what you saw above.

## Why should I use version control?

The definition and example above make this problem sound really simple. Many
people will try to keep track of versions themselves with special file names
like `hello.c.bak1`, `hello_BROKEN.c.old`, `hello_FINAL.c`, and so on.
Unfortunately, this solution doesn't scale well as the number of files,
collaborators, and development time grow.

As time goes on and your project gains more files, keeping track of history
manually would be tedious and error-prone. Furthermore, if you are working with
other people, you need a way to share this information.

Keep reading below to learn about the benefits of version control.

### Maintain Consistency

Version control provides a **system** for keeping track of history that is
**consistent**.

Have you ever tried to understand someone else's elaborate file naming scheme or
remember your own weeks later? Version control provides a consistent way to keep
track of history between collaborators and across projects.

### Record the Story

Version control keeps track of **why** changes were made by recording a message
with each version.

Have you ever looked back at your code weeks later and wondered why you decided
to make a certain change? By recording a message with each version, you can
review the exact steps and reasoning that resulted in the current code.

### Restore Previous Versions

Version control can help you get back to the last version of your code **that
worked**.

Have you ever tried to fix "just one more thing" before submitting a programming
assignment and broken your entire program? With version control, you can go back
to previous versions of your code to restore a working state.

### Backup Plan

Many version control systems allow you easily keep the code and history on your
local computer in sync with a server.

Have you ever had a hard disk fail in your computer? Having a backup copy of
your code elsewhere can prevent data loss.

### Collaborate Easily

Version control systems also provide a way to combine history, so that you can
work with others on your project. This allows you to work on the same files at
the same time and merge your changes together.

## What are the basic parts of a version control system?

While there are many different version control systems out there, most of them
have very similar basic parts. The components below are typically found in most
version control systems.

### Scope

Define what you want to keep track of history for. Typically a folder on your
file system.

### Objects

The individual items within the scope that you want to record history for.

### Changeset

Changesets describe which objects have changed, who changed them, and why.

### History

The history is a timeline of changesets.
