# HackTheRoofCICDDemo

## Fork this repository
1. Navigate to https://github.com/dslovin/HackTheRoofCICDDemo
2. Click the "Fork" button on the top right
![Fork Logo](https://help.github.com/assets/images/help/repository/fork_button.jpg)
3. Confirm you now have a repository in the format of `https://github.com/[YOUR GITHUB USERNAME]/HackTheRoofCICDDemo`

## Login to GCP
1. Login to http://console.google.com
2. Switch to correct project

## Setup Build Triggers
1. Navigate to `Cloud Build` in the GCP Console
2. Within `Cloud Build`, navigate to `Triggers`
3. Click on `Connect Repository`
4. `Show More Options` and ensure `GitHub (mirrored)` is selected and click `Continue`
5. Authorize `Cloud Build` to access projects in your account 
6. Select your `HackTheRoofCICDDemo` repository and click `Connect repository`
7. Select `Done`
8. Click on `+ Create Trigger` on the top of the page
9. Use the following values:

| Variable | Value | 
| --- | --- |
| Repository | `**[YOUR GITHUB USERNAME]**/HackTheRoofCICDDemo` |
| Name | `HTR Trigger` |
| Description | _input any description_ |
| Trigger type | Branch |
| Branch (regex) | .* |
| Included files filter (glob) | _leave empty_ |
| Ignored files filter (glob) | _leave empty_ |
| Build Configuration | Dockerfile |
| Dockerfile directory | / |
| Dockerfile name | Dockerfile |
| Image name | gcr.io/**[project name]**/github.com/**[YOUR GITHUB USERNAME]**/hacktheroofcicddemo:$SHORT_SHA (this should be default) |
10. Click `Create trigger`
11. Click `Run trigger` and ensure that Cloud Build is building the container without errors 

At this point, Google Cloud Build should be building the container and storing it in [Google Container Registry](https://cloud.google.com/container-registry/)

## Edit Container to Confirm

## Setup Repository
Use [this repository] for the lab by entering this command into Cloud Shell
```bash 
mkdir htr
cd htr
git clone https://github.com/dslovin/HackTheRoofCICDDemo
```

## Create Github Repository
We will create a project called "htr_lab" under your account. Use your web browser
1. Navigate to [GitHub's new project page](https://github.com/new)
2. For repository name, use "htr_lab"
3. Choose between Public and Private project (both work for this lab)
4. Click "Create Repository"
5. Push our code to the newly created 
```bash


```

## TODO
Create 4 Projects
Cloud Build API
