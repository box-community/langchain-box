# _BoxAPIWrapper


Wrapper for Box API. 

## Methods


### validate_box_api_inputs




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### get_box_client




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _do_request




#### Parameters
name | description | default
--- | --- | ---
self |  | 
url |  | 





### _get_text_representation




#### Parameters
name | description | default
--- | --- | ---
self |  | 
file_id |  | ""





### _is_returnable




#### Parameters
name | description | default
--- | --- | ---
self |  | 
file_info |  | 
path |  | 





### _generate_path




#### Parameters
name | description | default
--- | --- | ---
self |  | 
file_info |  | 





### _get_extra_fields




#### Parameters
name | description | default
--- | --- | ---
self |  | 
file |  | 
metadata |  | 
extra_fields |  | 





### get_document_by_file_id


Load a file from a Box id. Accepts file_id as str. Returns `Document` 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
file_id |  | 





### get_folder_items


Get all the items in a folder. Accepts folder_id as str. returns box_sdk_gen.Items 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
folder_id |  | 





### search_box




#### Parameters
name | description | default
--- | --- | ---
self |  | 
query |  | 
return_ids |  | False





### ask_box_ai




#### Parameters
name | description | default
--- | --- | ---
self |  | 
query |  | 
box_file_ids |  | 
answer |  | True
citations |  | False





### metadata_query




#### Parameters
name | description | default
--- | --- | ---
self |  | 
query |  | 





### get_blob_from_file_id




#### Parameters
name | description | default
--- | --- | ---
self |  | 
file_id |  | 




