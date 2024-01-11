# GCP-Cloud-Resume-Challenge-Backend
**GCP Cloud Resume Challenge Backend**

**Overview**
The deploy.ps1 script is designed to streamline the deployment process of Cloud Run resources within your Google Cloud Platform (GCP) project. By utilizing this PowerShell script, you can easily deploy and manage your Cloud Run services on GCP.

**Usage**
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

**Notes**
Ensure that you have the Google Cloud SDK installed and configured on your local machine.
Review and customize the variables.ps1 file with your specific deployment details before running the script.
It is recommended to include error handling and additional security measures based on your specific use case and requirements.
Feel free to reach out for assistance or if you encounter any issues during the deployment process. Happy deploying!

Note: This description assumes that users have basic knowledge of Google Cloud Platform, PowerShell, and Cloud Run.
