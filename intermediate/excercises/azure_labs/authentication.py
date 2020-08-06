import logging
from getpass import getpass

import requests
from contextlib import contextmanager
import adal
import inspect

def authenticate(tenant_id, client, secret):
    resource_uri = "https://management.azure.com/"
    authority_url = "https://login.microsoftonline.com/" + tenant_id
    context = adal.AuthenticationContext(authority_url)
    token = context.acquire_token_with_client_credentials(resource_uri, client, secret)

    return token

@contextmanager
def request_authenticated_azure_session(accessToken):
    """
    Context manager for Azure API calls
    :return: requests.session
    """
    session = None
    try:
        session = requests.session()
        session.headers.update(
                {"Authorization": "Bearer " + accessToken})
        yield session

    except Exception as excp:

        print(excp)
        func = inspect.currentframe().f_back.f_code
        logging.critical(
            "Error creating authenticated session in {} contained in {}".format(func.co_name, func.co_filename,))

    finally:
        if session:
            session.close()

def main():
    # this is training code.  We don't want to read credentials here
    tenant_id = input("Enter the tenant id: ")
    client_id = input("Please enter the client id for the service principal: ")
    client_key = input('Enter service principal key: ')

    # Let's authenticate
    token_response = authenticate(tenant_id, client_id, client_key)
    print("Response: ", token_response)
    print("Access token: ", token_response['accessToken'])

    #Pass the authentication token to a request session

    session = request_authenticated_azure_session(token_response['accessToken'])
    print(session)

    api_endpoint = "https://management.azure.com/providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policyDefinitions?api-version=2019-09-01"
    # The tenant id is the root management group
    api_endpoint = api_endpoint.format(managementGroupId=tenant_id)

    with session as req:
        response = req.get(api_endpoint)
        if response.status_code in range(200, 299):
            print(response.json())
        else:
            print("Oops!")

if __name__ == "__main__":
    main()
