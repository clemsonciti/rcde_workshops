# Environment Variables

Variables are used to store information that can be referenced and used in scripts or commands. Bash variables are essential for automating tasks and managing system settings. These variables can hold different types of values such as strings, numbers, or lists of items.

There are two main types of variables in Bash:

- User-defined variables: These are created by the user and can hold custom values.
- Environment variables: These are predefined by the system and contain critical information about the system’s environment.

To define a variable, assign a variable to a name.

```bash
FOO="BAR"
```

Then you can access the values of the variable using a `$` followed by the variable name.

```bash
echo The value of FOO is $FOO
```

This will output:

```bash
The value of FOO is BAR
```

::::{note}
There are two ways to print the variable name and not the value. The first is to use single quotes (`'`) around the variable:

```bash
echo '$FOO'
```

The second is to escape the dollar sign with a backslash (`\`):

```bash
echo \$FOO
```
::::

## Common Environment Variables
Some common system environment variables you may encounter in Linux include:

- `$HOME`: The current user's home directory.
- `$USER`: The current user's username.
- `$PATH`: A colon-separated list of directories where executable files are located.
- `$SHELL`: The path to the user's current shell (e.g., /bin/bash).
