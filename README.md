# gridy-id-python-api-client

Gridy ID is a Multi-Factor authentication (MFA) API service & Authenticator application for Android, IOS, Windows, MacOS, Linux & Web .

Use Gridy to replace your existing username/password authentication or Integrate Gridy ID into your adaptive authentication workflow in minutes using our API service and clients



## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/gridytech/gridy-id-python-api-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/gridytech/gridy-id-python-api-client.git`)

Then import the package:
```python
import gridyapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gridyapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import gridyapi_client
from gridyapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gridy.io
# See configuration.py for a list of all supported configuration parameters.
configuration = gridyapi_client.Configuration(
    host="https://api.gridy.io/prod"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API User Id
configuration.api_user = os.environ["GRIDY_API_USER"]

# Configure API User Secret
configuration.api_secret = os.environ["GRIDY_API_SECRET"]

# Enter a context with an instance of the API client
with gridyapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridyapi_client.GridyIDServiceApi(api_client)
    api_request = {
                      "id": < Your ownreference >,
                      "utctime": < UTC Timestamp >,
                      "apiUser": < Your Api User ID >,
                      "type": 150,
                      "body": {
                            "gridyUser": Base64Encoded( < User Email Address >),
                            "challengeType": < "UserKeyAndPattern" | "UserKeyPatternAndPin" | "UserKeyAndUserPin" | "UserKeyAndUserFace" | "UserKeyAndUserVoice" >,
                            "challengeExpiry": < "ThreeMins" | "FiveMins" | "TenMins" | "FifteenMins" | "ThirtyMins" | "SixtyMins" >,
                            "enableQRCode": < true | false >,
                            "enableAutoVerify": < true | false >,
                            "profile": "<Your Assigned User Profile Reference>",
                            "status": "NEW"
                        }
                  }  # ApiRequest | The JSON body of the request. Contains the Gridy ID challenge request.

    try:
        # Send or Cancel a Gridy ID MFA challenge request.
        api_response = api_instance.challenge(api_request)
        print("The response of GridyIDServiceApi->challenge:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GridyIDServiceApi->challenge: %s\n" % e)

```


## Documentation for API Endpoints

All URIs are relative to *https://api.gridy.io/prod*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
[*GridyIDServiceApi*] | [**challenge**](https://support.gridy.io/docs/api/challenge.html) | **POST** /v1/svc/challenge | Send or Cancel a Gridy ID MFA challenge request.
[*GridyIDServiceApi*] | [**status**](https://support.gridy.io/docs/api/status.html) | **POST** /v1/svc/status | Check a Gridy ID MFA challenge status
[*GridyIDServiceApi*] | [**time**](https://support.gridy.io/docs/api/time.html) | **GET** /v1/svc/time | Get current UTC time
[*GridyIDServiceApi*] | [**verify**](https://support.gridy.io/docs/api/verify.html) | **POST** /v1/svc/verify | Verify a Gridy ID authentication code
[*GridyIDServiceApi*] | [**blocked**](https://support.gridy.io/docs/api/blocked.html) | **POST** /v1/svc/blocked | Check IPv4 & User Blocked Rules.


## Documentation For Models

 - [ApiRequest](doc/ApiRequest.md)
 - [ApiResponse](doc/ApiResponse.md)


## Documentation For Authorization


[Authentication](https://support.gridy.io/docs/api/security.html) schemes defined for the API:


<a id="x-gridy-apiuser"></a>
### x-gridy-apiuser
- **Type**: GRIDY-HMAC
- **Parameter name**: x-gridy-apiuser
- **Location**: HTTP header

<a id="x-gridy-cnonce"></a>
### x-gridy-cnonce

- **Type**: GRIDY-HMAC
- **Parameter name**: x-gridy-cnonce
- **Location**: HTTP header

<a id="x-gridy-utctime"></a>
### x-gridy-utctime

- **Type**: GRIDY-HMAC
- **Parameter name**: x-gridy-utctime
- **Location**: HTTP header

<a id="Authorization"></a>
### Authorization

- **Type**: GRIDY-HMAC
- **Parameter name**: Authorization
- **Location**: HTTP header


## Author gridy.io




