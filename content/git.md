# Working with git

## Version control

Git is a method for what software developers call version control, allowing you to efficiently store and share versions of your code (or whatever you're working on) and to collaborate on projects, with an easy way of integrating changes. Rather than making new copies of a document every time you add changes (a very common practice among scientists writing papers, alas), the git software keeps track only of the changes in your document, allowing you to step back however far you wish, and comparing versions - both with changes you made, and with changes made by collaborators. The 'undo' option in many other software packages does the same thing. Very likely you've unwittingly already worked with versions of git, for example when writing in Overleaf.

## GitLab

TU Delft hosts a local server with GitLab software, which is an implementation of git with a lot of useful extensions. Anyone with a TU Delft netid can get a GitLab account, simply by logging in on <https://gitlab.tudelft.nl>. You can then be added to projects or start your own.

The easiest way to work on a project on GitLab with version control is to use an integrated environment in a writing package, such as VSCode. The website of VSCode contains detailed instructions. I find it easiest to start an empty project on GitLab, then link it (with the provided key) in VSCode; you can then simply add files to the project folder, which VSCode will sync for you with your GitLab repository. If you have never used git, there are a few setup steps; plenty of online tutorials will guide you through them.

## Upload a project from a local file system to GitLab

Source: [Stackoverflow: How to upload project from local file system to GitLab](https://stackoverflow.com/questions/70038069/how-to-upload-project-from-local-file-system-to-gitlab)

NB: This is a hands-on instruction for use on a terminal. There's no need to do any of this if you integrate with a development environment.

1. You have to create a new repository. Use the following command to create a Git repository. It can be used to convert an existing, unversioned project to a Git repository or initialize a new, empty repository. A .git folder is created in your directory. This folder contains Git records and configuration files. You should not edit these files directly.

```{code}
git init
```

2. If you want to add the files to track with git then you need to use the `git add` command. If you want to add new or modified or deleted files in the current directory, then add . to select all the files.

```{code}
git add .
```

3. `git commit` creates a snapshot of the changes made to a Git repository, which can then be pushed to the main repository. The -m option of the commit command lets you write the commit message.

```{code}
git commit -m "first commit"
```

4. You add a “remote” to tell Git which remote repository in GitLab is tied to the specific local folder on your computer. The remote tells Git where to push or pull from. You have to create a project to hold your files. **You should create a project in gitlab. The path of that project should be given in the following command.**

```{code}
git remote add origin git@gitlab.com:username/projectpath.git
```

5. Get the changes from the remote with `git pull`

```{code}
git pull origin master
```

6. Push the commits to the GitLab project with `git push`

```{code}
git push origin master
```

7. If any problems occur in pushing, use the following command for force push

```{code}
git push --force origin master
```