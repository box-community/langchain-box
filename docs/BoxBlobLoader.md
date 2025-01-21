# BoxBlobLoader


BoxBlobLoader.   
This class will help you load files from your Box instance. You must have a Box account. If you need one, you can sign up for a free developer account. You will also need a Box application created in the developer portal, where you can select your authorization type.   
**Setup**: Install ``langchain-box`` and set environment variable ``BOX_DEVELOPER_TOKEN``.   
.. code-block:: bash   
pip install -U langchain-box export BOX_DEVELOPER_TOKEN="your-api-key"   
  
This loader returns ``Blob`` objects built from files in Box. You can provide either a ``List[str]`` containing Box file IDS, a ``str`` contining a Box folder ID, a ``str`` with a query to find the right files, or a ``BoxMetadataQuery`` to find files based on its Box Metadata.   
If providing a folder ID, you can also enable recursive mode to get the full tree under that folder. If using a search query, you can use the ``BoxSearchOptions`` object to narrow the scope of your search.   
  
.. note:: A Box instance can contain Petabytes of files, and folders can contain millions of files. Be intentional when choosing what folders you choose to index. And we recommend never getting all files from folder 0 recursively. Folder ID 0 is your root folder.   
**Instantiate**:   
.. list-table:: Initialization variables :widths: 25 50 15 10 :header-rows: 1   
* - Variable - Description - Type - Default * - box_developer_token - Token to use for auth. - ``str`` - ``None`` * - box_auth - authentication object - ``langchain_box.utilities.BoxAuth`` - ``None`` * - box_file_ids - array of Box file IDs to index - ``List[str]`` - ``None`` * - box_folder_id - Box folder ID to index files from - ``str`` - ``None`` * - query - Query to search for files in Box - ``str`` - ``None`` * - recursive - Boolean to specify whether to include subfolders - ``Bool`` - ``False`` * - glob - Glob specifying which filenames to return - ``str`` - ``**/[!.]*`` * - exclude - Glob string specifying which filename patterns to exlude - ``str`` - ``None`` * - suffixes - Array of extensions to return - ``List[str]`` - ``None`` * - show_progress - Specifies whether to show a progress bar - ``Bool`` - ``False`` * - search_options - Search options to narrow the search scope in Box - ``BoxSearchOptions`` - ``None`` * - metadata_query - Box Metadata Query to find files based on their Metadata - ``BoxMetadataQuery`` - ``None`` * - images - Specify whether to return images or not - ``Bool`` - ``True`` * - docs - Specify whether to return document types of not. - ``Bool`` - ``True`` * - extra_fields - Specify Box file API fields to return as LangChain metadata. - ``List[str]`` - ``None``   
  
**Get files** — this method requires you pass the ``box_file_ids`` parameter. This is a ``List[str]`` containing the file IDs you wish to index.   
.. code-block:: python   
from langchain_box.blob_loaders import BoxBlobLoader   
box_file_ids = ["1514555423624", "1514553902288"]   
loader = BoxBlobLoader( box_file_ids=box_file_ids )   
**Get files in a folder** — this method requires you pass the ``box_folder_id`` parameter. This is a ``str`` containing the folder ID you wish to index.   
.. code-block:: python   
from langchain_box.blob_loaders import BoxBlobLoader   
box_folder_id = "260932470532"   
loader = BoxBlobLoader( box_folder_id=box_folder_id )   
**Search for files** — this method requires you pass the ``query`` parameter and optionally ``search_options``. This is a ``str`` containing the value to search for.   
.. code-block:: python   
from langchain_box.blob_loaders import BoxBlobLoader   
loader = BoxBlobLoader( query="Higgs Boson Bubble Bath" )   
**Box Metadata query** — this method requires you pass the ``BoxMetadataQuery`` object to the ``box_metadata_query`` parameter.   
.. code-block:: python   
from langchain_box.blob_loaders import BoxBlobLoader from langchain_box.utilities import BoxMetadataQuery   
query = BoxMetadataQuery( template_key="enterprise_1234.myTemplate", query="total >= :value", query_params={ "value" : 100 }, ancestor_folder_id="260932470532" )   
loader = BoxBlobLoader( box_metadata_query=query )   
**Yield Blobs**: .. code-block:: python   
for blob in loader.yield_blobs(): print(f"blob {blob}")   
.. code-block:: python   
Blob(id='1514535131595' metadata={'source': 'https://app.box.com/0/260935730128/260932470532/PO-005.txt', 'name': 'PO-005.txt', 'file_size': 211} data="b'Purchase Order Number: 005\nDate: February 13, 2024\nVendor: Quantum Quirks Co.\nAddress: 9 Wormhole Way, Singularity Station\nLine Items:\n    - Higgs Boson Bubble Bath: $30\n    - Cosmic String Yo-Yo: $15\nTotal: $45'" mimetype='text/plain' path='https://app.box.com/0/260935730128/260932470532/PO-005.txt')   
**Extra Fields** - If you want to specify additional LangChain metadata fields based on fields available in the Box File Information API, you can add them as ``extra_fields`` when instantiating the object. As an example, if you want to add the ``shared_link`` object, you would pass a ``List[str]`` object like:   
. code_block:: python   
loader = BoxBlobLoader( box_file_ids=["1234"], extra_fields=["shared_link"] )   
This will return in the metadata in the form ``"metadata" : { ..., "shared_link" : value } 

## Methods


### validate_box_loader_inputs




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _get_files_from_folder




#### Parameters
name | description | default
--- | --- | ---
self |  | 
folder_id |  | 





### yield_blobs


Yield blobs that match the requested pattern. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### count_matching_files


Count files that match the pattern without loading them. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### from_data




#### Parameters
name | description | default
--- | --- | ---
self |  | 
box_file_id |  | 




