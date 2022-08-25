# Introduction


## 1. Fundamentals of access control

```{dropdown} The purpose and fundamentals of access control    
- `Who can do what`. 
- Ways in which users can access resources in the computer systems. 
```

```{dropdown} Information security risks (CIA)   
- Confidentiality: Keeping information secure and private
- Integrity: Protecting information from being improperly altered or modified 
by unauthorized users
- Availability: Making information available for use when needed
```

```{dropdown} Authorization versus authentication
- Both are fundamental to access control. 
- Distinct but often confused. 
- Proper authorization is dependent on authentication.
- Authentication: determining that you are exactly who you are. 
  - Something you know (password, PIN ...)
  - Something you have (smart card, key ...)
  - Something you are (biometrics ...)
- Authentication determins who you are, authorization determins what you are allowed to do
```

```{dropdown} Terminologies
Any access control models can be stated formally using the notions of `users`, `subjects`, 
`objects`, `operations`, `permissions`, `session`. 
- `Users`: People who interace with the computer systems. 
  - Multiple IDs can be matched to a single human user. 
- `Session`: An instance of a user's dialog with a system.
- `Subject`: A computer process acting on behalf of a user. 
- `Object`: Any resource accessible on a computer system, such as files, printers, 
databases, or fine-grained entities such as individual fields in database records. 
- `Operation`: An activate process invoked by a subject. 
- `Permission`: also known as `privilege`, are authorizations to perform some 
action on the system. 
```

```{dropdown} Least privilege
- Selectively assigning permission to users such that the user is given 
no more permission than is necessary to perform his or her job function. 
- Strict adherence to least privilege requires an individual to have 
different levels of permission at different times. 
  - Could lead to inconvenience
  - Requires permission to not persist beyond the needed time. 
```




## 2. A brief history of access control

```{dropdown} Mainframe era

- Notion of `subject` and `object` and access matrix

|         | General ledger | Payroll | Accounts receivabe | Accouns payable |
| ------- | -------------- | ------- | ------------------ | --------------- |
| Alice   |       R, W     |         |         R          |        R        |
| Bob     |                |   R, W  |         R          |        R        |
| Charles |       R        |         |         R          |        R        |

- RAND report for DOD in 1970 proposed a multilevel security implementation
  - confidential
  - secret
  - top-secret

- **Mathematical model for computer security** by Bell and La Padula (1976)
  - [Secure computer system: unified exposition and multics interpretation](https://apps.dtic.mil/sti/pdfs/ADA023588.pdf)
  - Security rule
    - No read up
    - No write down

- **Protection in operating systems** by Harrison, Ruzzo, and Ullman (1976)
  - [Protection in operating systems](https://dl.acm.org/doi/pdf/10.1145/360303.360333)
  - Safety is inherently undecidable in a conventional access matrix view of security

```

```{dropdown} Department of Defense standards

- 1983: [Trusted Computer System Evaluation Criteria](https://www.zedz.net/rainbow/5200.28-STD.html) (TCSEC)
  - Discretionary access control (DAC)
  - Mandatory access control (MAC)

```

```{dropdown} Clark-Wilson model

- Arguments for systems meeting the lower levels of TCSEC requirements could be 
sufficient for commercial use. 
- In reality, DAC and MAC were not sufficient for commercial purposes. 
  - Different priorities for CIA: integrity instead of confidentiality
- Clark-Wilson model:
  - well-formed transaction: users can only change data only authorized way. 
  - separation of duty: various entities responsible for confirming and auditing 
  changes ensuring consistencies. 

```

```{dropdown} Origins of RBAC
- Conceptual usage dated back to the 70s
  - Access to computer system objects is based on a user's role in an organization
  - Roles with different priviliges and responsibilites have been recognzied
  in business organizations. 
- Late 80s and early 90s
  - Roles as an abstraction for managing privileges within application and DBMS. 
  - Roles as jobs, and users can be assigned to but separated from roles. 
- NIST's study in 1992
  - showed existing products with only TCSEC-style discretionary controls 
  - proposed a generalized role-based access control model (RBAC)
- RBAC basic rules
  - Role assignment: a subject can execute transaction only if the subject
  has selected or been assigned to a role. 
  - Role authorization: a subject's active role must be authorized for the 
  subject. 
  - Transaction authorization: a subject can execute a transaction only if the 
  transaction is authorized for the subject's active role. 
```

```{dropdown} Formal description of RBAC

- The active role that the subject is currently using: $AR(s:subject)$
- Each subject may be authorized to perform one or more roles: $RA(s: subject)$
- Each role may be authorized to perform one or more transactions: $TA(r: role)$
- Transaction execution:
  - $exec(s: subject, t:tran) = {true\ iff\ s\ can\ execute\ transaction\ t}$
- Role assignment:
  - $\forall s:subject,t:tran\cdot exec(s,t)\implies AR(s) \neq \varnothing$
- Role authorization: 
  - $\forall s:subject\cdot AR(s) \subseteq RA(s)$
- Transaction authorization: 
  - $\forall s:subject,t:tran\cdot exec(s,t)\implies t \in TA(AR(s))$
- Essentially, a roleis a collection of permissions, and users receive permissions 
only through the assigned roles. 
- Controlling access via roles simplifies the management and review of access controls.
  - Roles can inherit from other roles. 
  - Clark-Wilson model is a special case of RBAC. 
- In 2004, RBAC became an international formal standard. 
```

```{dropdown} RBAC, DAC, and MAC
- DAC: A subject with certain access permission is capable of passing 
that permission to other subject. 
  - RBAC: The organization `own` all permissions. Subjects are granted 
  permission but are not allowed to pass them on. 
- MAC: controls information flow, prevent unlawful flow from high-level 
to low-level clearances. Confidentiality-focus.
  - RBAC: Integrity-focus. 
```


## 3. RBAC and the enterprise

```{dropdown} Economics of RBAC
- Improved administrative productivity in perfomming common 
authorization management function. 
  - `U`: set of individuals in a job position. 
  - `P`: set of permissions required to perform that job position. 
  - Number of associations to map individuals to permissions: $\vert{U}\cdot\vert{V}$
  - A role is a set of permissions. 
    - Set `P` can be represented by a role. 
    - Assocication of individuals to this role (the entire set): $\vert{U}+\vert{P}$
- Avoid future expenses incurred through security and privacy breaches. 

```

```{dropdown} Authorization management and resource provisioning

- ACL (Access control list) is a system-by-system fine-grained access 
control mechanism for (Linux) system administrators. 
- The scale of enterprise systems makes this task extremely overwhelming. 
- Types of resources: applications, hardware, data (fine-grained)
- Types of subjects: contractors, employees, customers, business-partners ...
- Timing: duration of contracts, ex-employees ...
- Direct mapping of permission and users (ACL) is almost impossible and not 
scalable. 
  - RBAC reduces the complexity by introducing the middle layer, role. 
  - Analogy: think about computer hardware, Assembly, high-level programming 
  languages, and programmers. 

```