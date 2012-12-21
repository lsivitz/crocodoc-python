# crocodoc-python

## Introduction

crocodoc-python is a Python wrapper for the Crocodoc API.
The Crocodoc API lets you upload documents and then generate secure and customized viewing sessions for them.
Our API is based on REST principles and generally returns JSON encoded responses,
and in Python are converted to dictionaries unless otherwise noted.

## Installation

First, get the library.
Navigate into the folder you want to keep the library in.
We suggest adding the library as a submodule in your git project.

    git submodule add git@github.com:crocodoc/crocodoc-python.git

You can also get the library by cloning or downloading.

To clone:

    git clone git@github.com:crocodoc/crocodoc-python.git
    
To download:

    wget https://github.com/crocodoc/crocodoc-python/zipball/master -O crocodoc-python.zip
    unzip crocodoc-python.zip
    mv crocodoc-crocodoc-python-* crocodoc-python

Import the library:

    import crocodoc

### Dependencies

This library requires that the newest version of Python's requests module be installed.
To install or update this module:

    sudo pip install requests -U
    
## Getting Started

You can see a number of examples on how to use this library in examples.py.
These examples are interactive and you can run this file to see crocodoc-python in action.

To run these examples, open up examples.python and change this line to show your API token:

    crocodoc.api_token = 'YOUR_API_TOKEN'
    
Save the file, make sure the example-files directory is writeable, and then run examples.py:

    python examples.py
    
You should see 15 examples run with output in your terminal.
You can inspect the examples.py code to see each API call being used.

To start using crocodoc-py in your code, set your API token:

    crocodoc.api_token = 'YOUR_API_TOKEN'
    
And now you can start using the methods in crocodoc.document, crocodoc.download, and crocodoc.session.

Read on to find out more how to use crocodoc-python.
You can also find more detailed information about our API here:
https://crocodoc.com/docs/api/

## Using the Crocodoc API Library

### Errors

Errors are handled by throwing exceptions.
We throw instances of CrocodocError.

Note that any Crocodoc API call can throw an exception.
When making API calls, put them in a try/except block.
You can see examples.py to see working code for each method using try/except blocks.

### Document

These methods allow you to upload, check the status of, and delete documents.

#### Upload

https://crocodoc.com/docs/api/#doc-upload  
To upload a document, use crocodoc.document.upload().
Pass in a url (as a string) or a file resource object as keyword arguments.
This function returns a UUID of the file.

    // with a url
    uuid = crocodoc.document.upload(url=url)
    
    // with a file
    file_handle = open(file_path, 'r')
    uuid = crocodoc.document.upload(file=file_handle)
    
#### Status

https://crocodoc.com/docs/api/#doc-status  
To check the status of one or more documents, use crocodoc.document.status().
Pass in the UUID of the file or an array of UUIDS you want to check the status of.
This function returns a dictionary containing a "status" string" and a "viewable" boolean.
If you passed in an array instead of a string, this function returns an array of dictionaries containing the status for each file.

    // status contains status['status'] and status['viewable']
    status = crocodoc.document.status(uuid)
    
    // statuses contains an array of status dictionaries
    statuses = crocodoc.document.status([uuid, uuid2])
    
#### Delete

https://crocodoc.com/docs/api/#doc-delete  
To delete a document, use crocodoc.document.delete().
Pass in the UUID of the file you want to delete.
This function returns a boolean of whether the document was successfully deleted or not.

    deleted  = crocodoc.document.delete(uuid)
    
### Download

These methods allow you to download documents from Crocodoc in different ways.
You can download originals, PDFs, extracted text, and thumbnails.

#### Document

https://crocodoc.com/docs/api/#dl-doc  
To download a document, use crocodoc.download.document().
Pass in the uuid,
an optional boolean of whether or not the file should be downloaded as a PDF,
an optional boolean or whether or not the file should be annotated,
and an optional filter string.
This function returns the file contents as a string, which you probably want to save to a file.

    // with no optional arguments
    file = crocodoc.download.document(uuid)
    file_handle.write(file)
    
    // with all optional arguments
    file = crocodoc.download.document(uuid2, True, True, 'all')
    file_handle.write(file)
    
#### Thumbnail

https://crocodoc.com/docs/api/#dl-thumb  
To download a thumbnail, use crocodoc.download.thumbnail().
Pass in the uuid and optionally the width and height.
This function returns the file contents as a string, which you probably want to save to a file.

    // with no optional size arguments
    thumbnail = crocodoc.download.thumbnail(uuid)
    file_handle.write(thumbnail)
    
    // with optional size arguments (width 77, height 100)
    thumbnail = crocodoc.download.thumbnail(uuid, 77, 100)
    file_handle.write(thumbnail)

#### Text

https://crocodoc.com/docs/api/#dl-text  
To download extracted text from a document, use crocodoc.download.text().
Pass in the uuid.
This function returns the extracted text as a string.

    text = crocodoc.download.text(uuid)
    
### Session

The session method allows you to create a session for viewing documents in a secure manner.

#### Create

https://crocodoc.com/docs/api/#session-create  
To get a session key, use crocodoc.session.create().
Pass in the uuid and optionally a params dictionary.
The params dictionary can contain an "editable" boolean,
a "user" dictionary with "id" and "name" fields,
a "filter" string, a "sidebar" string,
and booleans for "admin", "downloadable", "copyprotected", and "demo".
This function returns a session key.

    // without optional params
    session_key = crocodoc.session.create(uuid)
    
    // with optional params
    user = {'id': 1, 'name': 'John Crocodoc'}
    session_key = crocodoc.session.create(uuid,
        editable=True, user=user,
        filter='all', admin=True, downloadable=True,
        copyprotected=False, demo=False, sidebar='visible'
    )
    
## Support

Please use github's issue tracker for API library support.