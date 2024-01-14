# Cloud resume Challange Backend

<p align="center">
  <a href="">
    <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*lDi1bp7b37khnH3tPVoLuQ.png" alt="Logo" width="50%" height="50%">
  </a>

  <h3 align="center">Google Cloud Platform (GCP) Resume Challenge </h3>

  <p align="center">
    Build a serverless resume website on GCP with API backend and GitOps-based CI/CD
    <br />
    <a href="https://acloudguru.com/blog/engineering/cloudguruchallenge-your-resume-on-gcp" target="_blank"><strong>See challenge description by Mattias Andersson @CloudGuru »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alfonsmr/GCP-Cloud-Resume-Challenge-Frontend/issues">Report Bug</a>
    ·
    <a href="https://github.com/alfonsmr/GCP-Cloud-Resume-Challenge-Frontend/issues">Request Feature</a>
  </p>
</p>
**Overview**
This repository contains the backend code for the Cloud Resume Challenge. The deployment process is streamlined using the deployment.ps1 script, allowing for easy deployment of the frontend to Google Cloud Platform (GCP). This README provides guidance on using the deployment script and deploying the frontend to GCP.

## Prerequisites
Before using the deployment script, ensure you have the following prerequisites:

- [Google Cloud SDK (gcloud)](https://cloud.google.com/sdk/docs/install) installed and configured.
- GCP project created and configured.
- PowerShell environment for running the deployment script.

## Usage

**Clone Repository:**

Ensure that you have cloned the repository containing the script.

**Set Variables:**

Open and edit the variables.ps1 file to set the required deployment parameters, such as:
$servicename: The name of the Cloud Run service.
$maxinstances: The maximum number of instances to allocate for the service.
$region: The GCP region where the service will be deployed.
$project: The GCP project ID.

**Run the Script:**

Execute the deploy.ps1 script to initiate the deployment process.

**Review and Confirm:**

The script will prompt the Google Cloud SDK (gcloud) to initialize and configure your GCP project.
It will then create a vars.py file containing the specified variables for initialization.
If not already created, the script will create a Firestore database and a counter.

**Cloud Run Deployment:**

The Cloud Run service will be deployed using the specified parameters, including the source code from the current directory.
The service will be configured to allow unauthenticated access, listening on port 8080, with the maximum specified instances and CPU boost.

**Clean-up**
The provided termination script, terminate.ps1, can be executed to cleanly terminate the Cloud Run service and release associated resources.

**Notes**
Ensure that you have the Google Cloud SDK installed and configured on your local machine.
Review and customize the variables.ps1 file with your specific deployment details before running the script.
It is recommended to include error handling and additional security measures based on your specific use case and requirements.
Feel free to reach out for assistance or if you encounter any issues during the deployment process. Happy deploying!

Note: This description assumes that users have basic knowledge of Google Cloud Platform, PowerShell, and Cloud Run.
