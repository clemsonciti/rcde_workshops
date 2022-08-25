# Setup

- This semester, we will utilize the department server, `molly`, for all our in-class hands-on, 
assignments, and lab activities. To connect to `molly`, we will use a mechanism called `Secure Shell`,
or `SSH`. 

- `SSH` is a cryptographic network protocol for secure communication over an unsecured network. `SSH`
allows us to open a command-line terminal to login to `molly`. 

## Access to molly server

- Student accounts for `molly` are created on the first day of class. 
  - The professor will hand out login name/password. 
  - The password is not the same as your WCUPA password. 
- Students added later to the class should contact the professor to request access to `molly`. 
{:.callout}


## Command line terminal software on Windows

- Download and install [Windows Terminal from the Microsoft Store](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab).
>


## Command line terminal software on Mac
>
- Use the Search box (magnifying glass on top-right of your Mac Desktop) and type in the word `Terminal`. 
- Launch the resulting Terminal app. 
>


## Connect to molly via SSH
>
- Launch the Terminal application (windows or Mac). 
- Type the following and press `Enter`. 
  - `USERID` is **your** WCUPA email login without the `@wcupa.edu` part. 
- If/when asked `Are you sure you want to continue connecting (/yes/no/[fingerprint])?`, 
type `yes` and press Enter. 
- It is normal if you type in your password when asked and nothing shows up. It is a security
feature, so that other cannot look at your screen and count the number of letters in your 
password. 
>
~~~
ssh USERID@molly.cs.wcupa.edu
~~~

>
- The figures below demonstrate SSH to `molly` with the professor's login ID. 

<img src="fig/setup/01.png" alt="SSH to molly from a Windows Terminal" style="height:600px">
>
<img src="fig/setup/02.png" alt="SSH to molly from a Mac Terminal" style="height:600px">
>


## Change your password
>
- After login to `molly` for the first time, type `passwd` and press Enter to change 
the default password. 
- You will be asked to provide your original password, and retype a new password two 
times. 
>
~~~
passwd
~~~

>
- The figures below demonstrate SSH to `molly` with the professor's login ID. 

<img src="fig/setup/03.png" alt="Changing password" style="height:150px">
>


{% include links.md %}
