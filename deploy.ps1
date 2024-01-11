#This script was created to deploy Cloud Run resources in your GCP project
# reading variables
. .\variables.ps1

#initialization
#gcloud init
gcloud config set project $project

#init variables.py

$sn="servicename='"+$servicename+"'"
$mi="maxinstances="+$maxinstances
$r="region='"+$region+"'"
$p="project='"+$project+"'"
Set-Content -Path .\vars.py -Value $sn
Add-Content -Path .\vars.py -Value $mi
Add-Content -Path .\vars.py -Value $r
Add-Content -Path .\vars.py -Value $p

#create firestore db and counter if not created
#gcloud firestore databases create --location=''$region''


gcloud run deploy $servicename --source . --allow-unauthenticated --port=8080 --max-instances=$maxinstances --cpu-boost --region=$region --project=$project