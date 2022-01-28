### <b>fix git permission issue for ssh remote repo</b> ###

***generate the ssh key***

```
ssh-keygen -t ed25519 -C "email"
```
add the public key to github ssh key

settings -> SSH & GPG key -> add the ssh public key

![alt text](https://github.com/Smrutimayeepadhi/Learning_git/blob/master/image1.png)

add the below in **.ssh/config** file
Host github.com-<name>
	HostName github.com
	User <username>
	IdentityFile ~/.ssh/<private-keyname>

git remote add git@github.com-<name>:<username>/<reponame>.git