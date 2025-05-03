# 1. Git getting started
- [1. Git getting started](#1-git-getting-started)
  - [1.1. ssh in Git for windows](#11-ssh-in-git-for-windows)
  - [1.2. some ssh client config first](#12-some-ssh-client-config-first)
  - [1.3. clone repo](#13-clone-repo)
  - [1.4. select working branch](#14-select-working-branch)
  - [1.5. Getting started with git](#15-getting-started-with-git)
  - [1.6. git best practice](#16-git-best-practice)

for windows users use [Git for Windows](https://git-scm.com/download/win)
for windows users, git for windows provide a mimimum set of features such as bash execution and ability to use ssh, you can still use your favorite ssh client as long as it provides agent features. if not or unsure please follow these steps :

## 1.1. ssh in Git for windows

Execute git bash and get the 2 hands on the keyboard, are you really claiming you're driving hard with a hand on the gear stick ?-) do not worry we'll get rid of this bad habit slowly

execute command (/!\ warning figures will probably not match this example in your case ;-) :

    ssh-agent
    SSH_AGENT_PID=1339; export SSH_AGENT_PID;
    echo Agent pid 1339;
    Agent pid 1339

POUR EVITER L ERREUR
```
jemesmain@echinix:~$ ssh-add /home/jemesmain/.ssh/jemesmain
Could not open a connection to your authentication agent.
jemesmain@echinix:~$ ssh-add ~/.ssh/jemesmain
Could not open a connection to your authentication agent.
```

Preferer l'instruction
```
jemesmain@echinix:~$ eval $(ssh-agent)
Agent pid 2160375
jemesmain@echinix:~$ echo $SSH_AUTH_SOCK 
/tmp/ssh-XXXXXXbyZVSz/agent.2160374
```


Time to switch gear, select the command output text and copy it to the buffer, paste it in the shell, and 2 hands back on the wheel, type enter to exec to set the env variables.

run command (/!\ warning path need to be adjusted unless you are having a .ssh dir your home dir), this might ask you for the key passphrase, if you're driving one hand while doing this you're driving dangerously !!! (says the sec guy)

    ssh-add ~/.ssh/<some_private_key>
    Enter passphrase for /c/Users/<you>/.ssh/<some_private_key>:
    Identity added: /c/Users/<you>/.ssh/<some_private_key> (some_user)

the agent will provide the authentication for ssh, it's used to connect to echinix and to authenticate on the git server.

pour WINDOWS

To install:

PowerShellGet\Install-Module posh-sshell -Scope CurrentUser
PowerShellGet\Install-Module posh-git -Scope CurrentUser
In your ps1 file:

Import-Module posh-git
Import-Module posh-sshell
Start-SshAgent

ssh-agent

 on verifie avec Get-Service ssh-agent pour savoir si le service est démarré.
 ssh-add private key



## 1.2. some ssh client config first

add following forwarding to your ssh client :
```
-L33022:192.168.0.21:22
```

or with a .ssh/config file, you're a pilot if this is done with 2 hands on the wheel uh the keyboard only !-), please make sure the User match yours on echinix.

```
Host echinix
  HostName echinix.energyleaks.org
  # ProxyCommand ssh security1 exec nc %h %p
  Port 38022
  User <some_user>
  ServerAliveCountMax 5
  Compression yes
  #RDP
  LocalForward 33389 127.0.0.1:3389
  #git
  LocalForward 33022 192.168.0.21:22
  ```
for safety reason and because we'll get to VPN configure soon enough the git is reachable through a ssh port forwarding

With ~/.ssh/config set, run the command

    ssh echinix

if the connection succeeds, this should open the port 33022 on your localhost, it'll be the entry point to communicate to the git server.

the connection to echinix must be kept alive, if not port forwarding does not work and you won't be able to communicate with the git server. leave the windows minimised and open a second git bash to continue the procedure

## 1.3. clone repo

clone repo with
depuis un pc en connection ssh
```
git clone ssh://git@localhost:33022/Users/git/echinix/echinix.git
git clone ssh://bicyclo@1localhost:33022/Users/bicyclo/bicyclo/bicyclo.git
```
depuis echinix
```
jemesmain@echinix:~$ git clone ssh://git@192.168.0.21:22/Users/git/echinix/echinix.git
Cloning into 'echinix'...
git clone ssh://bicyclo@192.168.0.21:/Users/bicyclo/bicyclo/bicyclo.git

```

cela crée un répertoire echinix sur le pc local qui est associé au serveur echinix local que l'on atteint en tant que localhost via le ssh configuré plus haut

make sure you are running an ssh agent with your priv key.

## 1.4. select working branch

check available branch on remote
```
 git branch -r
  origin/master
  origin/xtrmus-steelthread
```

let's checkout our main branch code, there's the remote origin/\<branch\> and the local branch named with the same label

```
 git checkout -b xtrmus-steelthread
Switched to a new branch 'xtrmus-steelthread'
```
cela permet de creer une nouvelle branche au projet /jemesmain/promptopia
using this naming can be a bit confusing, let's try to clarify that.
Si vous ne vous etes pas déplacé dans le répertoire echinix vous obtenez
```
jemesmain@groland:~$ git checkout -b jemesmain/test
fatal : ni ceci ni aucun de ses répertoires parents n'est un dépôt git : .git
jemesmain@groland:~$ cd echinix/
jemesmain@groland:~/echinix$ git checkout -b jemesmain/test
Basculement sur la nouvelle branche 'jemesmain/test'

```
pour voir les références

```
git show-ref
b88e7bdae34f1bee753f40f28c5af583e682c371 refs/heads/master
bf0d1b0a5d048132f2d6f2c5557aa7af47cf3dc8 refs/heads/xtrmus-steelthread
b88e7bdae34f1bee753f40f28c5af583e682c371 refs/remotes/origin/master
07303b75e6261756cb98bed376cdf682e47b1340 refs/remotes/origin/xtrmus-steelthread     # <- this is the ref to the remote branch
```
let's enable changed tracking between the remote and local branch
```
git branch --set-upstream-to=origin/xtrmus-steelthread xtrmus-steelthread
```
j'avais oublié de faire un set-upstream avant de faire
```
git add .
jemesmain@groland:~/echinix$ git commit
[jemesmain/test 0cb834a] initial test
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.txt
jemesmain@groland:~/echinix$ git push
fatal : La branche courante jemesmain/test n'a pas de branche amont.
Pour pousser la branche courante et définir la distante comme amont, utilisez

    git push --set-upstream origin jemesmain/test

Pour que cela soit fait automatiquement pour les branches sans
suivi distant, voir "push.autoSetupRemote' dans 'git help config'.

```

et donc j'ai fais un set-upstream après ;-)

```
jemesmain@groland:~/echinix$ git push --set-upstream origin jemesmain/test
Énumération des objets: 3, fait.
Décompte des objets: 100% (3/3), fait.
Compression par delta en utilisant jusqu'à 4 fils d'exécution
Compression des objets: 100% (2/2), fait.
Écriture des objets: 100% (2/2), 247 octets | 247.00 Kio/s, fait.
Total 2 (delta 0), réutilisés 0 (delta 0), réutilisés du pack 0
To ssh://localhost:33022/Users/git/echinix/echinix.git
 * [new branch]      jemesmain/test -> jemesmain/test
la branche 'jemesmain/test' est paramétrée pour suivre 'origin/jemesmain/test'.
```


let's have a check at a glance
```
 git branch -vv
  master                    b88e7bd [origin/master] first commit
* xtrmus-steelthread 07303b7 [origin/xtrmus-steelthread] add git details
```
the * shows the current working branch. git tracks changes from the remote branch you can use git pull to get most recent changes from remote

## 1.5. Getting started with git
review local status of files as stored in file system
```
 git status
On branch origin/xtrmus-steelthread
Your branch is up to date with 'remotes/origin/xtrmus-steelthread'.

nothing to commit, working tree clean
```
let change a file, edit README.md for instance and save the file, now git says
```
git status
On branch origin/xtrmus-steelthread
Your branch is up to date with 'remotes/origin/xtrmus-steelthread'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
review changes in the README.md file
```
git diff README.md
```

happy with the changes, still willing to commit them
```
git commit -m 'improving git getting started section' README.md
[origin/xtrmus-steelthread a474fc3] improving git getting started section
 1 file changed, 14 insertions(+), 3 deletions(-)
 ```

 git status now says
 ```
 git status
On branch origin/xtrmus-steelthread
Your branch is ahead of 'remotes/origin/xtrmus-steelthread' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

let's share this change with all user by pushing it to the remote branch
```
git push origin HEAD:xtrmus-steelthread
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 976 bytes | 976.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
To ssh://localhost:33022/Users/git/echinix/echinix.git
   a474fc3..bdb85f5  HEAD -> xtrmus-steelthread
```

and make sure we are getting the last changes from them
```
git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 326 bytes | 163.00 KiB/s, done.
From ssh://localhost:33022/Users/git/echinix/echinix
   99af46e..74a6988  xtrmus-steelthread -> origin/xtrmus-steelthread
Updating 99af46e..74a6988
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

et voilà ! need a short recap ?
```
             ┌─────────────┐                                     
             │git clone ...│                                     
             └──────┬──────┘                                     
             ┌──────▽──────┐                                     
             │git branch -r│                                     
             └──────┬──────┘                                     
            ┌───────▽───────┐                                     
            │git checkout -b│                                     
            │<some_branch>  │                                     
            └───────┬───────┘                                     
┌───────────────────▽──────────────────┐                         
│git branch                            │                         
│--set-upstream-to=origin/<some_branch>│                         
│<some_branch>                         │                         
└───────────────────┬──────────────────┘                         
            ┌───────▽──────┐                                     
            │git branch -vv│                                     
            └───────┬──────┘                                     
              ______▽_________                                   
             ╱                ╲                                   
        ____╱ work in progres  ╲_________________________________
       │ no ╲                  ╱                                 │
       │     ╲________________╱                                  │
       │             │yes                                        │
       │      _______▽_______     ┌────────────────────────────┐ │
       │     ╱               ╲    │git commit -m '<some details│ │
       │    ╱ git status show ╲___│on the change>' ... '       │ │
       │    ╲ modifications   ╱yes└──────────────┬─────────────┘ │
       │     ╲_______________╱                   │               │
       │             │no                         │               │
       │             └───────┬───────────────────┘               │
       │                ┌────▽───┐                               │
       │                │git pull│                               │
       │                └────┬───┘                               │
       │                     └───────────────────────────────────┘
    ┌──▽─┐                                                       
    |done│                                                       
    └────┘                                                       

```
getting started with git in [git.yaml](docs/diagon/git.yaml)


f(x) = 1 + x / (1 + x)

## 1.6. git best practice
Group your changes with a personnal local branch, for the sake of the explain, let's create a working branch from xtrmus-steelthread

    |                                                                                                 ┌─────────────┐                                     
    |                                                                                                 │git clone ...│                                     
    |                                                                                                 └──────┬──────┘                                     
    |                                                                                                 ┌──────▽──────┐                                     
    |                                                                                                 │git branch -r│                                     
    |                                                                                                 └──────┬──────┘                                     
    |                                                                                                ┌───────▽───────┐                                     
    |                                                                                                │git checkout -b│                                     
    |                                                                                                │<some_branch>  │                                     
    |                                                                                                └───────┬───────┘                                     
    |                                                                                    ┌───────────────────▽──────────────────┐                         
    |                                                                                    │git branch                            │                         
    |                                                                                    │--set-upstream-to=origin/<some_branch>│                         
    |                                                                                    │<some_branch>                         │                         
    |                                                                                    └───────────────────┬──────────────────┘                         
    |                                                                                                ┌───────▽──────┐                                     
    |                                                                                                │git branch -vv│                                     
    |                                                                                                └───────┬──────┘                                     
    |                                                                                                 ┌──────▽──────┐                                     
    |                                                                                                 │git branch -b│                                     
    |                                                                                                 │<myownbranch>│                                     
    |                                                                                                 └──────┬──────┘                                     
    |                                                                                                  ______▽_________                                   
    |                                                                                                 ╱                ╲                                   
    |                                                                                            ____╱ work in progres  ╲_________________________________
    |                                                                                           │ no ╲                  ╱                                 │
    |                                                                                           │     ╲________________╱                                  │
    |                                                                                           │             │yes                                        │
    |                                                                                           │      _______▽_______     ┌────────────────────────────┐ │
    |                                                                                           │     ╱               ╲    │git commit -m '<some details│ │
    |                                                                                           │    ╱ git status show ╲___│on the change>' ... '       │ │
    |                                                                                           │    ╲ modifications   ╱yes└──────────────┬─────────────┘ │
    |                                                                                           │     ╲_______________╱                   │               │
    |                                                                                           │             │no                         │               │
    |                                                                                           │             └───────┬───────────────────┘               │
    |                                                                                           │                     └───────────────────────────────────┘
    |                                                   _________________                       │                                                         
    |                                                  ╱                 ╲                                                                                 
    |            _____________________________________╱ merge in progress ╲________________                                                               
    |           │                                  no ╲                   ╱                │                                                               
    |           │                                      ╲_________________╱                 │                                                               
    |           │                                               │yes                       │                                                               
    |           │                                        ┌──────▽──────┐                   │                                                               
    |           │                                        │git checkout │                   │                                                               
    |           │                                        │<some_branch>│                   │                                                               
    |           │                                        └──────┬──────┘                   │                                                               
    |           │                                          ┌────▽───┐                      │                                                               
    |           │                                          │git pull│                      │                                                               
    |           │                                          └────┬───┘                      │                                                               
    |           │                                        ┌──────▽──────┐                   │                                                               
    |           │                                        │git checkout │                   │                                                               
    |           │                                        │<myownbranch>│                   │                                                               
    |           │                                        └──────┬──────┘                   │                                                               
    |           │                                         ┌─────▽────┐                     │                                                               
    |           │                                         │git merge │                     │                                                               
    |           │                                         └─────┬────┘                     │                                                               
    |           │                       ___________________     │                          │                                                               
    |           │                      ╱                   ╲                               │                                                               
    |           │ ____________________╱ tests or merge fail ╲____________________________  │                                                               
    |           ││                 no ╲                     ╱                            │ │                                                               
    |           ││                     ╲___________________╱                             │ │                                                               
    |           ││                               │yes                                    │ │                                                               
    |           ││                       ________▽__________                             │ │                                                               
    |           ││                      ╱                   ╲                            │ │                                                               
    |           ││                 ____╱ git merge           ╲_________________________  │ │                                                               
    |           ││                │ no ╲ <some_branch> fails ╱                         │ │ │                                                               
    |           ││                │     ╲___________________╱                          │ │ │                                                               
    |           ││                │               │yes                                 │ │ │                                                               
    |           ││                │     ┌─────────▽─────────┐                          │ │ │                                                               
    |           ││                │     │fix issues reported│                          │ │ │                                                               
    |           ││                │     │by git status      │                          │ │ │                                                               
    |           ││                │     └─────────┬─────────┘                          │ │ │                                                               
    |           ││                │         ______▽_______                             │ │ │                                                               
    |           ││                │        ╱              ╲    ┌─────────────────────┐ │ │ │                                                               
    |           ││                │       ╱ some conflicts ╲___│git add <fixed_files>│ │ │ │                                                               
    |           ││                │       ╲ is resolved    ╱yes└──────────┬──────────┘ │ │ │                                                               
    |           ││                │        ╲______________╱               │            │ │ │                                                               
    |           ││                │               │no                     │            │ │ │                                                               
    |           ││                │               └─────┬─────────────────┘            │ │ │                                                               
    |           ││                │                     └──────────────────────────────┘ │ │                                                               
    |           ││       _________▽___________                                           │ │                                                               
    |           ││      ╱                     ╲                                          │ │                                                               
    |           ││ ____╱ functionnal test fail ╲_______________________________          │ │                                                               
    |           │││ no ╲                       ╱                               │         │ │                                                               
    |           │││     ╲_____________________╱                                │         │ │                                                               
    |           │││                │yes                                        │         │ │                                                               
    |           │││         _______▽_______     ┌────────────────────────────┐ │         │ │                                                               
    |           │││        ╱               ╲    │git commit -m '<some details│ │         │ │                                                               
    |           │││       ╱ git status show ╲___│on the change>' ... '       │ │         │ │                                                               
    |           │││       ╲ modification    ╱yes└──────────────┬─────────────┘ │         │ │                                                               
    |           │││        ╲_______________╱                   │               │         │ │                                                               
    |           │││                │no                         │               │         │ │                                                               
    |           │││                └───────┬───────────────────┘               │         │ │                                                               
    |           │││                        └───────────────────────────────────┘         │ │                                                               
    |           ││└──────────────────────────────────────────────────────────────────────┘ │                                                               
    |           │└─────────────────────────────────────────────────────────────────────────┘                                                               
    |    ┌──────▽──────┐                                                                                                                                   
    |    │git checkout │                                                                                                                                   
    |    │<some_branch>│                                                                                                                                   
    |    └──────┬──────┘                                                                                                                                   
    |    ┌──────▽──────┐                                                                                                                                   
    |    │git merge    │                                                                                                                                   
    |    │<myownbranch>│                                                                                                                                   
    |    └──────┬──────┘                                                                                                                                   
    | ┌─────────▽────────┐                                                                                                                                 
    | │git push origin   │                                                                                                                                 
    | │HEAD:<some_branch>│                                                                                                                                 
    | └─────────┬────────┘                                                                                                                                 
    |        ┌──▽──┐                                                                                                                                       
    |        │done!│                                                                                                                                       
    |        └─────┘                                                                                                                                       
    |
to change please edit 'working in your own branch' in [git.yaml](docs/diagon/git.yaml)
file:///private/var/mobile/Containers/Shared/AppGroup/5437794A-EA0E-4045-8225-40CE0F8DEC4D/File%20Provider%20Storage/Repositories/echinix/Git.README.*md*