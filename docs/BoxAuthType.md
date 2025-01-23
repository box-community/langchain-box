# BoxAuthType


BoxAuthType(Enum).   
An enum to tell BoxLoader how you wish to autheticate your Box connection.   
Options are:   
TOKEN - Use a developer token generated from the Box Deevloper Token. Only recommended for development. Provide ``box_developer_token``.   
CCG - Client Credentials Grant. provide ``box_client_id`, ``box_client_secret`, and ``box_enterprise_id`` or optionally `box_user_id`.   
JWT - Use JWT for authentication. Config should be stored on the file system accessible to your app. provide ``box_jwt_path``. Optionally, provide ``box_user_id`` to act as a specific user 

## Methods

