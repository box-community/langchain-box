# BoxAuth


**BoxAuth**   
The `box-langchain` package offers some flexibility to authentication. The most basic authentication method is by using a developer token. This can be found in the [Box developer console](https://account.box.com/developers/console) on the configuration screen. This token is purposely short-lived (1 hour) and is intended for development. With this token, you can add it to your environment as `BOX_DEVELOPER_TOKEN`, you can pass it directly to the loader, or you can use the `BoxAuth` authentication helper class.   
  
`BoxAuth` supports the following authentication methods:   
  
* **Token** — either a developer token or any token generated through the Box SDK   
* **JWT** with a service account   
* **JWT** with a specified user   
* **CCG** with a service account   
* **CCG** with a specified user   
  
> **NOTE**: If using JWT authentication, you will need to download the configuration from the Box developer console after generating your public/private key pair. Place this file in your application directory structure somewhere. You will use the path to this file when using the `BoxAuth` helper class. If you wish to use OAuth2 with the authorization_code flow, please use `BoxAuthType.TOKEN` with the token you have acquired.   
  
For more information, learn about how to set up a [Box application](https://developer.box.com/guides/getting-started/first-application/), and check out the [Box authentication guide](https://developer.box.com/guides/authentication/select/) for more about our different authentication options.   
  
**Simple implementation**:   
  
To instantiate, you must provide a `langchain_box.utilities.BoxAuthType`.   
  
BoxAuthType is an enum to tell BoxLoader how you wish to autheticate your Box connection.   
  
Options are:   
  
TOKEN - Use a developer token generated from the Box Developer Token. Only recommended for development. Provide `box_developer_token`.   
  
CCG - Client Credentials Grant. provide `box_client_id`, `box_client_secret`, and `box_enterprise_id` or optionally `box_user_id`.   
  
JWT - Use JWT for authentication. Config should be stored on the file system accessible to your app. Provide `box_jwt_path`. Optionally, provide `box_user_id` to act as a specific user.   
  
**Examples**:   
  
**Token**   
  
```python   
from langchain_box.document_loaders import BoxLoader   
from langchain_box.utilities import BoxAuth, BoxAuthType   
auth = BoxAuth(   
auth_type=BoxAuthType.TOKEN,   
box_developer_token=box_developer_token   
)   
loader = BoxLoader(   
box_auth=auth,   
...   
)  ```   
  
  
**JWT with a service account**   
  
```python   
from langchain_box.document_loaders import BoxLoader from langchain_box.utilities import BoxAuth, BoxAuthType   
auth = BoxAuth( auth_type=BoxAuthType.JWT, box_jwt_path=box_jwt_path )   
loader = BoxLoader( box_auth=auth, ... ) ```   
  
  
**JWT with a specified user**   
  
```python   
from langchain_box.document_loaders import BoxLoader from langchain_box.utilities import BoxAuth, BoxAuthType   
auth = BoxAuth( auth_type=BoxAuthType.JWT, box_jwt_path=box_jwt_path, box_user_id=box_user_id )   
loader = BoxLoader( box_auth=auth, ... ) ```   
  
  
**CCG with a service account**   
  
```python   
from langchain_box.document_loaders import BoxLoader from langchain_box.utilities import BoxAuth, BoxAuthType   
auth = BoxAuth( auth_type=BoxAuthType.CCG, box_client_id=box_client_id, box_client_secret=box_client_secret, box_enterprise_id=box_enterprise_id )   
loader = BoxLoader( box_auth=auth, ... ) ```   
  
  
**CCG with a specified user**   
  
```python   
from langchain_box.document_loaders import BoxLoader from langchain_box.utilities import BoxAuth, BoxAuthType   
auth = BoxAuth( auth_type=BoxAuthType.CCG, box_client_id=box_client_id, box_client_secret=box_client_secret, box_user_id=box_user_id )   
loader = BoxLoader( box_auth=auth, ... ) ``` 

## Methods


### validate_box_auth_inputs


Validate auth_type is set 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _authorize




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### get_client


Instantiate the Box SDK. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




