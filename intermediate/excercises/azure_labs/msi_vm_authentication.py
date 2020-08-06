# importing the requests library
import requests

# Step 1: Fetch an access token from a Managed Identity enabled azure resource.
# Resources with an MSI configured recieve an AAD access token by using the Azure Instance Metadata Service (IMDS)
# IMDS provides an endpoint accessible to all IaaS VMs using a non-routable well-known IP Address
# To learn more about IMDS and MSI Authentication see the following link: https://docs.microsoft.com/azure/virtual-machines/windows/instance-metadata-service
# Note that the resource here is https://vault.azure.net for public cloud and api-version is 2018-02-01
MSI_ENDPOINT = "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fvault.azure.net"
r = requests.get(MSI_ENDPOINT, headers={"Metadata": "true"})

# extracting data in json format
# This request gets an access_token from Azure AD by using the local MSI endpoint.
data = r.json()

# Step 2: Pass the access_token received from previous HTTP GET call to your key vault.
KeyVaultURL = "https://{YOUR KEY VAULT NAME}.vault.azure.net/secrets/{YOUR SECRET NAME}?api-version=2016-10-01"
kvSecret = requests.get(url=KeyVaultURL, headers={"Authorization": "Bearer " + data["access_token"]})

print(kvSecret.json()["value"])