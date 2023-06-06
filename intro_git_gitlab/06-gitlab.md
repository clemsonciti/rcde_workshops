# GitLab

GitLab is a web interface for a server that provides Git repository services.
The Research Computing and Data team has an instance available at
[git.rcd.clemson.edu](https://git.rcd.clemson.edu) for **research** and
**educational** use by Clemson users.

```{figure} ../fig/intro_git_gitlab/gitlab_repo.png
---
width: 80%
---
Screenshot of a GitLab repository page.
```

## Getting Started
All users with an account on Palmetto can login to [Gitlab](https://git.rcd.clemson.edu). To create a new git repository, click the "New Project" button.
On the New Project page, you can choose to create a blank project, create one from a template, or import a project from an existing source (GitLab/GitHub/BitBucket).

When creating a blank project, you will need to choose a name and pick a group or namespace. You can create projects under your username namespace and any groups you have permission to.
You can also change the visibility of the project (Private is the default setting) and whether you want to initialize the repository with a README file.

:::{admonition} Project Limitations

Each individual project is limited to 10GB in size. Users are limited in the number of personal projects they can create.

:::

## Features

### [Web IDE](https://docs.gitlab.com/ee/user/project/web_ide/)
Edit files in your browser and commit without having to clone repository.

```{figure} ../fig/intro_git_gitlab/gitlab_web_ide.png
---
width: 80%
---
Screenshot of the GitLab Web IDE
```

### [Issues](https://docs.gitlab.com/ee/user/project/issues/)
Collaborate on problems, track upcoming features, and ask questions.

### [Wiki](https://docs.gitlab.com/ee/user/project/wiki/)
Create a wiki for your project or group. GitLab manages the history of the wiki in git for version history.
Use the wiki to document:
- Onboarding procedure for new lab members
- How to benchmark your jobs on Palmetto
- Style guidelines for papers and posters

### [Git-LFS](https://git-lfs.com)
Git Large File Storage is fully supported by GitLab to track updates for large files that don't normally work well with git.
Track changes to:
- Images
- Videos
- 3D models (SolidWorks, AutoCAD, etc.)
- AI/ML models

### Container Registry and CI/CD
GitLab has it's own container registry hosted at https://registry.rcd.clemson.edu. The RCD team provides runners to run CI/CD pipelines
for compiling projects and building container images. More information can be found in the [CI/CD Pipelines with GitLab workshop](https://docs.rcd.clemson.edu/training/workshop_catalog/sdlc/gitlab_ci_cd) (Coming Fall 2023)
