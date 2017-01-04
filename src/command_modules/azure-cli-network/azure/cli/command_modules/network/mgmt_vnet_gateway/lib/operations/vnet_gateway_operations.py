# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
#pylint: skip-file

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_operation import AzureOperationPoller
import uuid

from .. import models


class VnetGatewayOperations(object):
    """VnetGatewayOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create_or_update(
            self, resource_group_name, deployment_name, public_ip_address, virtual_network, virtual_network_gateway_name, enable_bgp=False, content_version=None, asn=None, bgp_peering_address=None, gateway_type="Vpn", location=None, peer_weight=None, public_ip_address_type="existingId", sku="Basic", tags=None, virtual_network_type="existingId", vpn_type="RouteBased", custom_headers=None, raw=False, **operation_config):
        """Create a new VnetGateway.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param enable_bgp: Flag to enable BGP settings.
        :type enable_bgp: bool
        :param public_ip_address: Name or ID of public IP address to use.
        :type public_ip_address: str
        :param virtual_network: Name or ID of a virtual network that contains
         a subnet named 'GatewaySubnet'.
        :type virtual_network: str
        :param virtual_network_gateway_name: Gateway name.
        :type virtual_network_gateway_name: str
        :param content_version: If included it must match the ContentVersion
         in the template.
        :type content_version: str
        :param asn: Autonomous System Number to use for the BGP settings.
        :type asn: str
        :param bgp_peering_address: IP address to use for BGP peering.
        :type bgp_peering_address: str
        :param gateway_type: Gateway type. Possible values include: 'Vpn',
         'ExpressRoute'
        :type gateway_type: str or :class:`gatewayType
         <Default.models.gatewayType>`
        :param location: Location for resources.
        :type location: str
        :param peer_weight: Weight added to routes learned through BGP
         peering.
        :type peer_weight: str
        :param public_ip_address_type: Type of Public IP Address to associate
         with the VPN gateway. Possible values include: 'existingName',
         'existingId'
        :type public_ip_address_type: str or :class:`publicIpAddressType
         <Default.models.publicIpAddressType>`
        :param sku: VPN Gateway SKU. Possible values include: 'Basic',
         'Standard', 'HighPerformance', 'UltraPerformance'
        :type sku: str or :class:`sku <Default.models.sku>`
        :param tags: Tags object.
        :type tags: object
        :param virtual_network_type: Type of virtual network to supply to the
         VPN gateway. Possible values include: 'existingId', 'existingName'
        :type virtual_network_type: str or :class:`virtualNetworkType
         <Default.models.virtualNetworkType>`
        :param vpn_type: VPN routing type. Possible values include:
         'RouteBased', 'PolicyBased', 'Dedicated'
        :type vpn_type: str or :class:`vpnType <Default.models.vpnType>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`DeploymentExtended
         <Default.models.DeploymentExtended>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        parameters = models.DeploymentVnetGateway(content_version=content_version, asn=asn, bgp_peering_address=bgp_peering_address, enable_bgp=enable_bgp, gateway_type=gateway_type, location=location, peer_weight=peer_weight, public_ip_address=public_ip_address, public_ip_address_type=public_ip_address_type, sku=sku, tags=tags, virtual_network=virtual_network, virtual_network_gateway_name=virtual_network_gateway_name, virtual_network_type=virtual_network_type, vpn_type=vpn_type)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=64, min_length=1, pattern='^[-\w\._]+$'),
            'deploymentName': self._serialize.url("deployment_name", deployment_name, 'str', max_length=64, min_length=1, pattern='^[-\w\._]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'DeploymentVnetGateway')

        # Construct and send request
        def long_running_send():

            request = self._client.put(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 201]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            deserialized = None

            if response.status_code == 200:
                deserialized = self._deserialize('DeploymentExtended', response)
            if response.status_code == 201:
                deserialized = self._deserialize('DeploymentExtended', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)
