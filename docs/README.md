# Python Documentation

## Classes

**[BoxBlobLoader](BoxBlobLoader.md)**: BoxBlobLoader.   
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

**[BoxLoader](BoxLoader.md)**: BoxLoader.   
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

**[BoxRetriever](BoxRetriever.md)**: Box retriever.   
`BoxRetriever` provides the ability to retrieve content from your Box instance in a couple of ways.   
1. You can use the Box full-text search to retrieve the complete document(s) that match your search query, as `List[Document]` 2. You can use the Box AI Platform API to retrieve the results from a Box AI prompt. This can be a `Document` containing the result of the prompt, or you can retrieve the citations used to generate the prompt to include in your vectorstore.   
Setup: Install ``langchain-box``:   
.. code-block:: bash   
pip install -U langchain-box   
Instantiate:   
To use search:   
.. code-block:: python   
from langchain_box.retrievers import BoxRetriever   
retriever = BoxRetriever()   
To use Box AI:   
.. code-block:: python   
from langchain_box.retrievers import BoxRetriever   
file_ids=["12345","67890"]   
retriever = BoxRetriever(file_ids)   
  
Usage: .. code-block:: python   
retriever = BoxRetriever() retriever.invoke("victor") print(docs[0].page_content[:100])   
.. code-block:: none   
[ Document( metadata={ 'source': 'url', 'title': 'FIVE_FEET_AND_RISING_by_Peter_Sollett_pdf' }, page_content='\n3/20/23, 5:31 PM F...' ) ]   
Use within a chain: .. code-block:: python   
from langchain_core.output_parsers import StrOutputParser from langchain_core.prompts import ChatPromptTemplate from langchain_core.runnables import RunnablePassthrough from langchain_openai import ChatOpenAI   
retriever = BoxRetriever(box_developer_token=box_developer_token, character_limit=10000)   
context="You are an actor reading scripts to learn about your role in an upcoming movie." question="describe the character Victor"   
prompt = ChatPromptTemplate.from_template( """Answer the question based only on the context provided.   
Context: {context}   
Question: {question}""" )   
def format_docs(docs): return "\n\n".join(doc.page_content for doc in docs)   
chain = ( {"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser() )   
chain.invoke("Victor")  # search query to find files in Box )   
.. code-block:: none   
'Victor is a skinny 12-year-old with sloppy hair who is seen sleeping on his fire escape in the sun. He is hesitant to go to the pool with his friend Carlos because he is afraid of getting in trouble for not letting his mother cut his hair. Ultimately, he decides to go to the pool with Carlos.'   
**Extra Fields** - If you want to specify additional LangChain metadata fields based on fields available in the Box File Information API, you can add them as ``extra_fields`` when instantiating the object. As an example, if you want to add the ``shared_link`` object, you would pass a ``List[str]`` object like:   
. code_block:: python   
loader = BoxBlobLoader( box_file_ids=["1234"], extra_fields=["shared_link"] )   
This will return in the metadata in the form ``"metadata" : { ..., "shared_link" : value } 

**[DocumentFiles](DocumentFiles.md)**: DocumentFiles(Enum).   
An enum containing all of the supported extensions for files Box considers Documents. These files should have text representations. 

**[ImageFiles](ImageFiles.md)**: ImageFiles(Enum).   
An enum containing all of the supported extensions for files Box considers images. 

**[BoxAuthType](BoxAuthType.md)**: BoxAuthType(Enum).   
An enum to tell BoxLoader how you wish to autheticate your Box connection.   
Options are:   
TOKEN - Use a developer token generated from the Box Deevloper Token. Only recommended for development. Provide ``box_developer_token``.   
CCG - Client Credentials Grant. provide ``box_client_id`, ``box_client_secret`, and ``box_enterprise_id`` or optionally `box_user_id`.   
JWT - Use JWT for authentication. Config should be stored on the file system accessible to your app. provide ``box_jwt_path``. Optionally, provide ``box_user_id`` to act as a specific user 

**[BoxAuth](BoxAuth.md)**: **BoxAuth**   
The `box-langchain` package offers some flexibility to authentication. The most basic authentication method is by using a developer token. This can be found in the [Box developer console](https://account.box.com/developers/console) on the configuration screen. This token is purposely short-lived (1 hour) and is intended for development. With this token, you can add it to your environment as `BOX_DEVELOPER_TOKEN`, you can pass it directly to the loader, or you can use the `BoxAuth` authentication helper class.   
  
`BoxAuth` supports the following authentication methods:   
  
* **Token** — either a developer token or any token generated through the Box SDK * **JWT** with a service account * **JWT** with a specified user * **CCG** with a service account * **CCG** with a specified user   
  
> **NOTE**: >    If using JWT authentication, you will need to download the configuration from >    the Box developer console after generating your public/private key pair. Place >    this file in your application directory structure somewhere. You will use the >    path to this file when using the `BoxAuth` helper class. If you wish to use >    OAuth2 with the authorization_code flow, please use `BoxAuthType.TOKEN` with >    the token you have acquired.   
  
For more information, learn about how to set up a [Box application](https://developer.box.com/guides/getting-started/first-application/), and check out the [Box authentication guide](https://developer.box.com/guides/authentication/select/) for more about our different authentication options.   
  
**Simple implementation**:   
  
To instantiate, you must provide a `langchain_box.utilities.BoxAuthType`.   
  
BoxAuthType is an enum to tell BoxLoader how you wish to autheticate your Box connection.   
  
Options are:   
  
TOKEN - Use a developer token generated from the Box Deevloper Token. Only recommended for development. Provide ``box_developer_token``.   
CCG - Client Credentials Grant. provide `box_client_id`, `box_client_secret`, and `box_enterprise_id` or optionally `box_user_id`.   
JWT - Use JWT for authentication. Config should be stored on the file system accessible to your app. Provide `box_jwt_path`. Optionally, provide `box_user_id` to act as a specific user.   
  
**Examples**:   
  
**Token**   
  
```python   
from langchain_box.document_loaders import BoxLoader from langchain_box.utilities import BoxAuth, BoxAuthType   
auth = BoxAuth( auth_type=BoxAuthType.TOKEN, box_developer_token=box_developer_token )   
loader = BoxLoader( box_auth=auth, ... ) ```   
  
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

**[SearchTypeFilter](SearchTypeFilter.md)**: SearchTypeFilter.   
Enum to limit the what we search. 

**[BoxSearchOptions](BoxSearchOptions.md)**: 

**[BoxMetadataQuery](BoxMetadataQuery.md)**: 

**[_BoxAPIWrapper](_BoxAPIWrapper.md)**: Wrapper for Box API. 


## Functions

### get_min_version



#### Parameters
name | description | default
--- | --- | ---
version |  | 





### get_min_version_from_toml



#### Parameters
name | description | default
--- | --- | ---
toml_path |  | 





### test_placeholder


Used for compiling integration tests without running any real tests. 




### auth







### env_vars







### test_one_file



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_multiple_files



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_folder



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_folder_recursive



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_search



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_metadata_query



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_extra_fields



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### auth







### env_vars







### test_one_file



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_multiple_files



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_folder



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_folder_recursive



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_extra_fields



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### auth







### env_vars







### test_search



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_box_ai



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_box_ai_multiple



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_box_ai_citations



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_box_ai_citations_only



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_extra_fields



#### Parameters
name | description | default
--- | --- | ---
auth |  | 
env_vars |  | 





### test_all_imports







### test_direct_token_initialization







### test_failed_direct_token_initialization







### test_auth_initialization







### test_failed_file_initialization







### test_folder_initialization







### test_file_load



#### Parameters
name | description | default
--- | --- | ---
mocker |  | 





### test_direct_token_initialization







### test_failed_direct_token_initialization







### test_auth_initialization







### test_failed_file_initialization







### test_folder_initialization







### test_failed_initialization_files_and_folders







### test_file_load



#### Parameters
name | description | default
--- | --- | ---
mocker |  | 





### test_direct_token_initialization







### test_failed_direct_token_initialization







### test_auth_initialization







### test_search



#### Parameters
name | description | default
--- | --- | ---
mocker |  | 





### test_search_options



#### Parameters
name | description | default
--- | --- | ---
mocker |  | 





### test_ai



#### Parameters
name | description | default
--- | --- | ---
mocker |  | 





### test_ai_answer_citations



#### Parameters
name | description | default
--- | --- | ---
mocker |  | 





### test_ai_citations_only



#### Parameters
name | description | default
--- | --- | ---
mocker |  | 





### mock_worker



#### Parameters
name | description | default
--- | --- | ---
mocker |  | 





### test_token_initialization







### test_failed_token_initialization







### test_jwt_eid_initialization







### test_jwt_user_initialization







### test_failed_jwt_initialization







### test_ccg_eid_initialization







### test_ccg_user_initialization







### test_failed_ccg_initialization







### test_direct_token_initialization







### test_auth_initialization







### test_failed_initialization_no_auth







### test_get_documents_by_file_ids



#### Parameters
name | description | default
--- | --- | ---
mock_worker |  | 
mocker |  | 





### test_get_documents_by_folder_id



#### Parameters
name | description | default
--- | --- | ---
mock_worker |  | 
mocker |  | 





### test_box_search



#### Parameters
name | description | default
--- | --- | ---
mock_worker |  | 
mocker |  | 





### test_ask_box_ai_single_file



#### Parameters
name | description | default
--- | --- | ---
mock_worker |  | 
mocker |  | 





### test_ask_box_ai_multiple_files



#### Parameters
name | description | default
--- | --- | ---
mock_worker |  | 
mocker |  | 





### _make_iterator


Create a function that optionally wraps an iterable in tqdm. 
#### Parameters
name | description | default
--- | --- | ---
length_func |  | 
show_progress |  | False




