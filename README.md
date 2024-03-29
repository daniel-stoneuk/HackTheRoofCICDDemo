# HackTheRoofCICDDemo

![CI/CD Image](https://cloud.google.com/solutions/continuous-integration/images/hero-banner.png)

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
| Build Configuration | Cloud Build configuration file (yaml or json) |
| Cloud Build configuration file location  | / cloudbuild.yaml |
| Dockerfile name | Dockerfile |
10. Click `Create trigger`
11. Click `Run trigger` and ensure that Cloud Build is building the container without errors 
12. Navigate to `History` to check the build history for this to ensure no errors

At this point, Google Cloud Build should be building the container and storing it in [Google Container Registry](https://cloud.google.com/container-registry/) and deploying to cloud run!

## Edit Container to Confirm
Now edit the container, follow the history and see if it works! Try putting an error in the Dockerfile and see what happens.



## TODO
- [ ] Create 4 Projects
- [ ] Cloud Build API
- [ ] Cloud Build Service Account to Service Account User
- [ ] Cloud Build Service Account to Cloud Run Admin
- [ ] GKE API
- [ ] Cloud Build Service Account to Kubernetes Engine Developer
- [ ] Cloud Vision API

## GKE Continuous Delivery (WIP - but works)
```bash
gcloud container clusters create htr-gke --zone us-east1-b --machine-type "n1-standard-1" --image-type "COS" --num-nodes "3"
```
Switch Build Trigger to cloudbuild_gke.yaml


## GCE Continous Delivery (broken)
```bash
gcloud compute instances create-with-container htr-site --container-image gcr.io/$PROJECT_ID/hacktheroofcicddemo
```

## Add ACLs to Cloud Storage
gsutil acl ch -u derek@dslovin.com:R gs://chalupa-images/1.jpg (for 1)
gsutil acl ch -u 990943260827-compute@developer.gserviceaccount.com:R gs://chalupa-images/1.jpg
