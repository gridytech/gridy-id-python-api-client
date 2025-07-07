# coding: utf-8

"""
    Gridy ID API

    Gridy ID is a Multi-Factor authentication (MFA) API service & Authenticator application for Android, IOS, Windows, MacOS, Linux & Web. 
    
    Use Gridy to replace your existing username/password authentication or Integrate Gridy ID into your adaptive authentication workflow in minutes using our API service and clients</p><p>When using the API Explorer, you will need to use the HMAC tool to generate the required headers for each request.

"""  # noqa: E501
import string
import warnings
import hmac
import hashlib

from uuid import uuid4
from datetime import datetime, timezone

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from gridyapi_client.models.api_request import ApiRequest
from gridyapi_client.models.api_response import ApiResponse

from gridyapi_client.api_client import ApiClient, RequestSerialized
from gridyapi_client.api_response import ApiResponse
from gridyapi_client.rest import RESTResponseType


class GridyIDServiceApi:

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def challenge(
        self,
        api_request: Annotated[ApiRequest, Field(description="The JSON body of the request. Contains the Gridy ID challenge request.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse:
        """Send or Cancel a Gridy ID MFA challenge request.

        :param api_request: The JSON body of the request. Contains the Gridy ID challenge request. (required)
        :type api_request: ApiRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._challenge_serialize(
            api_request=api_request,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': "ApiResponse",
            '400': "ApiResponse",
            '500': "ApiResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    def _challenge_serialize(
        self,
        api_request,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _header_params: Dict[str, Optional[str]] = {}

        _body_params: Optional[bytes] = None

        # process the body parameter
        if api_request is not None:
            _body_params = api_request

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = 'application/json; charset=utf-8'

        # set the HTTP header `Content-Type`
        if 'Content-Type' not in _header_params:
            _header_params['Content-Type'] = 'application/json; charset=utf-8'

        # set the x-gridy-apiuser header
        if 'x-gridy-apiuser' not in _header_params:
            _header_params['x-gridy-apiuser'] = self.api_client.configuration.api_user

        # set the x-gridy-cnonce header
        if 'x-gridy-cnonce' not in _header_params:
            _header_params['x-gridy-cnonce'] = str(uuid4())

        # set the x-gridy-utctime header
        if 'x-gridy-utctime' not in _header_params:
            _header_params['x-gridy-utctime'] = str(int(datetime.now(timezone.utc).timestamp()*1000))

        # set the Authorization header
        if 'Authorization' not in _header_params:
            _header_params['Authorization'] = (self.api_client.configuration
                                               .api_hmac_authorization_header
                                               .format( _header_params['x-gridy-apiuser'],
                                                str(
                                                   hmac.new(
                                                    self.api_client.configuration.api_secret.encode('UTF-8'),
                                                    self.api_client.configuration
                                                        .api_hmac_signed_headers
                                                        .format( _header_params['x-gridy-utctime'],
                                                                 _header_params['x-gridy-cnonce']
                                                                 )
                                                    .encode('UTF-8'),
                                                    hashlib.sha256
                                                ))
                                               ))

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/svc/challenge',
            header_params=_header_params,
            body=_body_params,
            _host=_host,
        )

    @validate_call
    def status(
        self,
        api_request: Annotated[ApiRequest, Field(description="The JSON body of the request. Contains the Status request.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,

        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse:
        """Check a Gridy ID MFA challenge status
        
        :param api_request: The JSON body of the request. Contains the Status request. (required)
        :type api_request: ApiRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._status_serialize(
            api_request=api_request,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiResponse",
            '204': "ApiResponse",
            '400': "ApiResponse",
            '404': "ApiResponse",
            '500': "ApiResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _status_serialize(
        self,
        api_request,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _header_params: Dict[str, Optional[str]] = {}

        _body_params: Optional[bytes] = None

        # process the body parameter
        if api_request is not None:
            _body_params = api_request

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = 'application/json; charset=utf-8'

        # set the HTTP header `Content-Type`
        if 'Content-Type' not in _header_params:
            _header_params['Content-Type'] = 'application/json; charset=utf-8'

        # set the x-gridy-apiuser header
        if 'x-gridy-apiuser' not in _header_params:
            _header_params['x-gridy-apiuser'] = self.api_client.configuration.api_user

        # set the x-gridy-cnonce header
        if 'x-gridy-cnonce' not in _header_params:
            _header_params['x-gridy-cnonce'] = str(uuid4())

        # set the x-gridy-utctime header
        if 'x-gridy-utctime' not in _header_params:
            _header_params['x-gridy-utctime'] = str( int(datetime.now(timezone.utc).timestamp()*1000))

        # set the Authorization header
        if 'Authorization' not in _header_params:
            _header_params['Authorization'] = (self.api_client.configuration
                                               .api_hmac_authorization_header
                                               .format( _header_params['x-gridy-apiuser'],
                                                str(
                                                   hmac.new(
                                                    self.api_client.configuration.api_secret.encode('UTF-8'),
                                                    self.api_client.configuration
                                                        .api_hmac_signed_headers
                                                        .format( _header_params['x-gridy-utctime'],
                                                                 _header_params['x-gridy-cnonce']
                                                                 )
                                                    .encode('UTF-8'),
                                                    hashlib.sha256
                                                ))
                                               ))

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/svc/status',
            header_params=_header_params,
            body=_body_params,
            _host=_host,
        )



    @validate_call
    def time(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse:
        """Get current UTC time

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional      
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._time_serialize(
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiResponse",
            '400': "ApiResponse",
            '500': "ApiResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    def _time_serialize(
        self,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _header_params: Dict[str, Optional[str]] =  {}

        _body_params: Optional[bytes] = None

        # process the header parameters

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = 'application/json; charset=utf-8'

        # set the HTTP header `Content-Type`
        if 'Content-Type' not in _header_params:
            _header_params['Content-Type'] = 'application/json; charset=utf-8'

        # set the x-gridy-apiuser header
        if 'x-gridy-apiuser' not in _header_params:
            _header_params['x-gridy-apiuser'] = self.api_client.configuration.api_user

        # set the x-gridy-cnonce header
        if 'x-gridy-cnonce' not in _header_params:
            _header_params['x-gridy-cnonce'] = str(uuid4())

        # set the x-gridy-utctime header
        if 'x-gridy-utctime' not in _header_params:
            _header_params['x-gridy-utctime'] = str(int(datetime.now(timezone.utc).timestamp()*1000))

        # set the Authorization header
        if 'Authorization' not in _header_params:
            _header_params['Authorization'] = (self.api_client.configuration
                                               .api_hmac_authorization_header
                                               .format(_header_params['x-gridy-apiuser'],
                                                       str(
                                                           hmac.new(
                                                               self.api_client.configuration.api_secret.encode('UTF-8'),
                                                               self.api_client.configuration
                                                               .api_hmac_signed_headers
                                                               .format(_header_params['x-gridy-utctime'],
                                                                       _header_params['x-gridy-cnonce']
                                                                       )
                                                               .encode('UTF-8'),
                                                               hashlib.sha512
                                                           ).hexdigest())
                                                       ))

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/svc/time',
            header_params=_header_params,
            body=_body_params,
            _host=_host,
        )


    @validate_call
    def verify(
        self,
        api_request: Annotated[ApiRequest, Field(description="The JSON body of the request. Contains the Gridy ID Verify request.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse:
        """Verify a Gridy ID authentication code


        :param api_request: The JSON body of the request. Contains the Gridy ID Verify request. (required)
        :type api_request: ApiRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
     
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._verify_serialize(
            api_request=api_request,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiResponse",
            '400': "ApiResponse",
            '500': "ApiResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _verify_serialize(
        self,
        api_request,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _header_params: Dict[str, Optional[str]] = {}

        _body_params: Optional[bytes] = None

        # process the body parameter
        if api_request is not None:
            _body_params = api_request

        # process the header parameters

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = 'application/json; charset=utf-8'

        # set the HTTP header `Content-Type`
        if 'Content-Type' not in _header_params:
            _header_params['Content-Type'] = 'application/json; charset=utf-8'

        # set the x-gridy-apiuser header
        if 'x-gridy-apiuser' not in _header_params:
            _header_params['x-gridy-apiuser'] = self.api_client.configuration.api_user

        # set the x-gridy-cnonce header
        if 'x-gridy-cnonce' not in _header_params:
            _header_params['x-gridy-cnonce'] = str(uuid4())

        # set the x-gridy-utctime header
        if 'x-gridy-utctime' not in _header_params:
            _header_params['x-gridy-utctime'] = str(int(datetime.now(timezone.utc).timestamp()*1000))

        # set the Authorization header
        if 'Authorization' not in _header_params:
            _header_params['Authorization'] = (self.api_client.configuration
                                               .api_hmac_authorization_header
                                               .format(_header_params['x-gridy-apiuser'],
                                                       str(
                                                           hmac.new(
                                                               self.api_client.configuration.api_secret.encode(
                                                                   'UTF-8'),
                                                               self.api_client.configuration
                                                               .api_hmac_signed_headers
                                                               .format(_header_params['x-gridy-utctime'],
                                                                       _header_params['x-gridy-cnonce']
                                                                       )
                                                               .encode('UTF-8'),
                                                               hashlib.sha256
                                                           ))
                                                       ))

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/svc/verify',
            header_params=_header_params,
            body=_body_params,
            _host=_host,
        )








    @validate_call
    def blocked(
        self,
        api_request: Annotated[ApiRequest, Field(description="The JSON body of the request. Contains the Gridy ID Blocked request.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse:
        """Check a User request against all defined IPv4 & User Blocked Rules


        :param api_request: The JSON body of the request. Contains the Gridy ID Blocked request. (required)
        :type api_request: ApiRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
     
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._blocked_serialize(
            api_request=api_request,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApiResponse",
            '400': "ApiResponse",
            '500': "ApiResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _blocked_serialize(
        self,
        api_request,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _header_params: Dict[str, Optional[str]] = {}

        _body_params: Optional[bytes] = None

        # process the body parameter
        if api_request is not None:
            _body_params = api_request

        # process the header parameters

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = 'application/json; charset=utf-8'

        # set the HTTP header `Content-Type`
        if 'Content-Type' not in _header_params:
            _header_params['Content-Type'] = 'application/json; charset=utf-8'

        # set the x-gridy-apiuser header
        if 'x-gridy-apiuser' not in _header_params:
            _header_params['x-gridy-apiuser'] = self.api_client.configuration.api_user

        # set the x-gridy-cnonce header
        if 'x-gridy-cnonce' not in _header_params:
            _header_params['x-gridy-cnonce'] = str(uuid4())

        # set the x-gridy-utctime header
        if 'x-gridy-utctime' not in _header_params:
            _header_params['x-gridy-utctime'] = str(int(datetime.now(timezone.utc).timestamp()*1000))

        # set the Authorization header
        if 'Authorization' not in _header_params:
            _header_params['Authorization'] = (self.api_client.configuration
                                               .api_hmac_authorization_header
                                               .format(_header_params['x-gridy-apiuser'],
                                                       str(
                                                           hmac.new(
                                                               self.api_client.configuration.api_secret.encode(
                                                                   'UTF-8'),
                                                               self.api_client.configuration
                                                               .api_hmac_signed_headers
                                                               .format(_header_params['x-gridy-utctime'],
                                                                       _header_params['x-gridy-cnonce']
                                                                       )
                                                               .encode('UTF-8'),
                                                               hashlib.sha256
                                                           ))
                                                       ))

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/svc/blocked',
            header_params=_header_params,
            body=_body_params,
            _host=_host,
        )
