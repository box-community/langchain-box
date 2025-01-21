# BoxRetriever


Box retriever.   
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

## Methods


### validate_box_loader_inputs




#### Parameters
name | description | default
--- | --- | ---
self |  | 





### _get_relevant_documents




#### Parameters
name | description | default
--- | --- | ---
self |  | 
query |  | 




