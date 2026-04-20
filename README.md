# openai
Built with ❤️ using OpenAI, Streamlit, Docker and Google Cloud Run.


## local development
 create a virtual environment
```
$ python3 -m venv venv
```

activate virual environment
```
$ source venv/bin/activate
```
 install dependencies
 ```
 $ pip install -r requirements.txt
 ```
 
change python interpretor to python virtual environment
```
	•	Cmd + Shift + P (macOS)
```

## setting up CI/CD with gitaction
set below secrets in github
```
GCP_PROJECT_ID=gcp-project-id
GCP_REGION=europe-west3
SERVICE_ACCOUNT_EMAIL=<NAME>@<PROJECT_ID>.iam.gserviceaccount.com
SERVICE_NAME=chatbot-service
WORKLOAD_IDENTITY_PROVIDER=projects/<PROJECT_NUMBER>/locations/global/workloadIdentityPools/<POOL_NAME>/providers/<PROVIDER_NAME>
```

## update OIDC

```
$ gcloud iam workload-identity-pools providers update-oidc github-provider \
--location="global" \
--workload-identity-pool="github-pool" \
--attribute-condition="assertion.repository_owner=='Ranjit-Banglore'"
```

