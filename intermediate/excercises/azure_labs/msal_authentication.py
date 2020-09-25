import requests
from msal import ConfidentialClientApplication
from intermediate.excercises.azure_labs.adal_authentication import request_authenticated_azure_session

def main(tenant_id, client_id, client_secret):
    authority = "https://login.microsoftonline.com/{tenant_id}".format(tenant_id=tenant_id)
    app = ConfidentialClientApplication(client_id=client_id, authority=authority,
                                        client_credential=client_secret)

    token_response = app.acquire_token_for_client(["https://graph.microsoft.com/.default"])
    print("Response: ", token_response)
    print("Access token: ", token_response['access_token'])

    api_endpoint = "https://management.azure.com/providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policyDefinitions?api-version=2019-09-01"
    # The tenant id is the root management group
    api_endpoint = api_endpoint.format(managementGroupId=tenant_id)

    session = request_authenticated_azure_session(token_response['access_token'])
    with session as req:
        response = req.get(api_endpoint)
        if response.status_code in range(200, 299):
            print(response.json())
        else:
            print("Oops!")

if __name__ == "__main__":
    # this is training code.  We don't want to read credentials here
    tenant_id = input("Enter the tenant id: ")
    client_id = input("Please enter the client id for the service principal: ")
    client_key = input('Enter service principal key: ')

    main(tenant_id, client_id, client_key)