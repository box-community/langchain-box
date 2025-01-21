# BoxLoader


BoxLoader.   
This class will help you load files from your Box instance. You must have a Box account. If you need one, you can sign up for a free developer account. You will also need a Box application created in the developer portal, where you can select your authorization type.   
If you wish to use either of the Box AI options, you must be on an Enterprise Plus plan or above. The free developer account does not have access to Box AI.   
In addition, using the Box AI API requires a few prerequisite steps:   
* Your administrator must enable the Box AI API * You must enable the ``Manage AI`` scope in your app in the developer console. * Your administrator must install and enable your application.   
**Setup**: Install ``langchain-box`` and set environment variable ``BOX_DEVELOPER_TOKEN``.   
.. code-block:: bash   
pip install -U langchain-box export BOX_DEVELOPER_TOKEN="your-api-key"   
  
This loader returns ``Document`` objects built from text representations of files in Box. It will skip any document without a text representation available. You can provide either a ``List[str]`` containing Box file IDS, or you can provide a ``str`` contining a Box folder ID. If providing a folder ID, you can also enable recursive mode to get the full tree under that folder.   
.. note:: A Box instance can contain Petabytes of files, and folders can contain millions of files. Be intentional when choosing what folders you choose to index. And we recommend never getting all files from folder 0 recursively. Folder ID 0 is your root folder.   
**Instantiate**:   
.. list-table:: Initialization variables :widths: 25 50 15 10 :header-rows: 1   
* - Variable - Description - Type - Default * - box_developer_token - Token to use for auth. - ``str`` - ``None`` * - box_auth - client id for you app. Used for CCG - ``langchain_box.utilities.BoxAuth`` - ``None`` * - box_file_ids - client id for you app. Used for CCG - ``List[str]`` - ``None`` * - box_folder_id - client id for you app. Used for CCG - ``str`` - ``None`` * - recursive - client id for you app. Used for CCG - ``Bool`` - ``False`` * - character_limit - client id for you app. Used for CCG - ``int`` - ``-1`` * - extra_fields - Specify Box file API fields to return as LangChain metadata. - ``List[str]`` - ``None``   
  
**Get files** — this method requires you pass the ``box_file_ids`` parameter. This is a ``List[str]`` containing the file IDs you wish to index.   
.. code-block:: python   
from langchain_box.document_loaders import BoxLoader   
box_file_ids = ["1514555423624", "1514553902288"]   
loader = BoxLoader( box_file_ids=box_file_ids, character_limit=10000  # Optional. Defaults to no limit )   
**Get files in a folder** — this method requires you pass the ``box_folder_id`` parameter. This is a ``str`` containing the folder ID you wish to index.   
.. code-block:: python   
from langchain_box.document_loaders import BoxLoader   
box_folder_id = "260932470532"   
loader = BoxLoader( box_folder_id=box_folder_id, recursive=False  # Optional. return entire tree, defaults to False )   
**Load**: .. code-block:: python   
docs = loader.load() docs[0]   
.. code-block:: python   
Document(metadata={'source': 'https://dl.boxcloud.com/api/2.0/ internal_files/1514555423624/versions/1663171610024/representations /extracted_text/content/', 'title': 'Invoice-A5555_txt'}, page_content='Vendor: AstroTech Solutions\nInvoice Number: A5555\n\nLine Items:\n    - Gravitational Wave Detector Kit: $800\n    - Exoplanet Terrarium: $120\nTotal: $920')   
**Lazy load**: .. code-block:: python   
docs = [] docs_lazy = loader.lazy_load()   
for doc in docs_lazy: docs.append(doc) print(docs[0].page_content[:100]) print(docs[0].metadata)   
.. code-block:: python   
Document(metadata={'source': 'https://dl.boxcloud.com/api/2.0/ internal_files/1514555423624/versions/1663171610024/representations /extracted_text/content/', 'title': 'Invoice-A5555_txt'}, page_content='Vendor: AstroTech Solutions\nInvoice Number: A5555\n\nLine Items:\n    - Gravitational Wave Detector Kit: $800\n    - Exoplanet Terrarium: $120\nTotal: $920')   
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





### lazy_load


Load documents. Accepts no arguments. Returns `Iterator[Document]` 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




