#Terminate service and free up resource
# reading variables
. .\variables.ps1
#Cleanup service
gcloud run services delete $servicename --region=$region --project=$project
#Clean up images
gcloud config set artifacts/repository cloud-run-source-deploy
gcloud artifacts packages delete $servicename --location=$region