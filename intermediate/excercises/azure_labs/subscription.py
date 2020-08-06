def get_policy_definitions_list_by_management_group(self, managementGroupId):
    """
    Get the policy definitions from a management group
    :param managementGroupId:
    """
    api_endpoint = self.config['AZURESDK']['policy_definitions_list_by_management_group']
    api_endpoint = api_endpoint.format(managementGroupId=managementGroupId)

    with request_authenticated_azure_session() as req:
        policy_definitions_response = req.get(api_endpoint)

    return policy_definitions_response