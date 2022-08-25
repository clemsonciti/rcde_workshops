
# Practice Scenarios

```{dropdown} 1. Preparation

- Launch the `webserver-ldap` experiment on CloudLab. We will assume that there are three connected nodes:
  - `webserver`
  - `observer`
  - `ldap`. 

- The `webserver` should have an apache server ready (`setup_apache.sh`). 
- The `ldap` should have an ldap server ready. There should be 
one user account (student/rammy) created. 
```

```{dropdown} 2. Scenario 1: LDAP-protected web server

- Enable the `public_html` directory and create an `index.html` 
page in that directory that displays `Hello World` when access. 
- Secure this location by requiring viewer to authenticate via the 
ldap server with the `student/rammy` login/password.  

```

```{dropdown} 3. Scenario 2: Shared home directory

- Add the following users to the LDAP server
  - Make sure to change the password hash (password remains `rammy`)
  - Confirm that the users were added correctly by view the page 
  from scenario 1 using users `merino` and `dorper`. 

<script src="https://gist.github.com/linhbngo/060f8a99fbc3666b6abf8f05be54a28c.js?file=users-nfs.ldif"></script>

- Set up the NFS server on `ldap`.  
  - Create a directory called `nfs/home` and make it available 
  via NFS for both `webserver` and `observer`. 
- Setup NFS clients on `webserver` and `observer`. 
  - Create `nfs/home` and mount `/nfs/home` from `ldap` 
- Using `su` (do not use `sudo`), confirm that you can switch users, 
and that their home directories are shared across `ldap`, 
`webserver`, and `observer`.  
 
```
