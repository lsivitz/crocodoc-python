import os
import sys
import time

import crocodoc
from crocodoc import CrocodocError

crocodoc.api_token = 'YOUR_API_TOKEN'

"""
Example #1

Upload a file to Crocodoc. We're uploading Form W4 from the IRS by URL.
"""
print 'Example #1 - Upload Form W4 from the IRS by URL.'
form_w4_url = 'http://www.irs.gov/pub/irs-pdf/fw4.pdf'
sys.stdout.write('  Uploading... ')
uuid = None

try:
    uuid = crocodoc.document.upload(url=form_w4_url)
    print 'success :)'
    print '  UUID is ' + uuid
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message

"""
Example #2

Check the status of the file from Example #1.
"""
print ''
print 'Example #2 - Check the status of the file we just uploaded.'
sys.stdout.write('  Checking status... ')

try:
    status = crocodoc.document.status(uuid)

    if status.get('error') == None:
        print 'success :)'
        print '  File status is ' + status['status'] + '.'
        print '  File ' + ('is' if status['viewable'] else 'is not') + ' viewable.'
    else:
        print 'failed :('
        print '  Error Message: ' + status['error']
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message
    
"""
Example #3

Upload another file to Crocodoc. We're uploading Form W4 from the IRS as a PDF.
"""
print ''
print 'Example #3 - Upload a sample .pdf as a file.'
uuid2 = None
file_path = './example-files/form-w4.pdf'

if (os.path.isfile(file_path)):
    file_handle = open(file_path, 'r')
    sys.stdout.write('  Uploading... ')
    uuid2 = None
    
    try:
        uuid2 = crocodoc.document.upload(file=file_handle)
        print 'success :)'
        print '  UUID is ' + uuid2
    except CrocodocError as e:
        print 'failed :('
        print '  Error Code: ' + str(e.status_code)
        print '  Error Message: ' + e.error_message
else:
    print '  Skipping because the sample pdf can\'t be found.'
    
"""
Example #4

Check the status of both files we uploaded in Examples #1 and #3.
"""
print ''
print 'Example #4 - Check the status of both files at the same time.'
sys.stdout.write('  Checking statuses... ')

try:
    statuses = crocodoc.document.status([uuid, uuid2])

    if (len(statuses) != 0):
        print 'success :)'
        
        if (statuses[0].get('error') == None):
            print '  File #1 status is ' + statuses[0]['status'] + '.'
            print '  File #1 ' + ('is' if statuses[0]['viewable'] else 'is not') + ' viewable.'
        else:
            print '  File #1 failed :('
            print '  Error Message: ' + statuses[0]['error']
        
        if (statuses[1].get('error') == None):
            print '  File #2 status is ' + statuses[1]['status'] + '.'
            print '  File #2 ' + ('is' if statuses[1]['viewable'] else 'is not') + ' viewable.'
        else:
            print '  File #2 failed :('
            print '  Error Message: ' . statuses[1]['error']
    else:
        print 'failed :('
        print '  Statuses were not returned.'
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message
    
"""
Example #5

Wait ten seconds and check the status of both files again.
"""
print ''
print 'Example #5 - Wait ten seconds and check the statuses again.'
sys.stdout.write('  Waiting... ')
time.sleep(10)
print 'done.'
sys.stdout.write('  Checking statuses... ')

try:
    statuses = crocodoc.document.status([uuid, uuid2])

    if (len(statuses) != 0):
        print 'success :)'
        
        if (statuses[0].get('error') == None):
            print '  File #1 status is ' + statuses[0]['status'] + '.'
            print '  File #1 ' + ('is' if statuses[0]['viewable'] else 'is not') + ' viewable.'
        else:
            print '  File #1 failed :('
            print '  Error Message: ' + statuses[0]['error']
        
        if (statuses[1].get('error') == None):
            print '  File #2 status is ' + statuses[1]['status'] + '.'
            print '  File #2 ' + ('is' if statuses[1]['viewable'] else 'is not') + ' viewable.'
        else:
            print '  File #2 failed :('
            print '  Error Message: ' . statuses[1]['error']
    else:
        print 'failed :('
        print '  Statuses were not returned.'
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message
    
"""
Example #6

Delete the file we uploaded from Example #1.
"""
print ''
print 'Example #6 - Delete the first file we uploaded.'
sys.stdout.write('  Deleting... ')

try:
    deleted = crocodoc.document.delete(uuid)
    
    if deleted:
        print 'success :)'
        print '  File was deleted.'
    else:
        print 'failed :('
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message

"""
Example #7

Download the file we uploaded from Example #3 as an original
"""
print ''
print 'Example #7 - Download a file as an original.'
sys.stdout.write('  Downloading... ')

try:
    file = crocodoc.download.document(uuid2)
    filename = os.path.dirname(os.path.abspath(__file__)) + '/example-files/test-original.pdf'
    file_handle = open(filename, 'w')
    file_handle.write(file)
    print 'success :)'
    print '  File was downloaded to ' + filename + '.'
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message
    
"""
Example #8

Download the file we uploaded from Example #3 as a PDF
"""
print ''
print 'Example #8 - Download a file as a PDF.'
sys.stdout.write('  Downloading...')

try:
    file = crocodoc.download.document(uuid2, True)
    filename = os.path.dirname(os.path.abspath(__file__)) + '/example-files/test.pdf'
    file_handle = open(filename, 'w')
    file_handle.write(file)
    print 'success :)'
    print '  File was downloaded to ' + filename + '.'
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message

"""
Example #9

Download the file we uploaded from Example #3 with all options
"""
print ''
print 'Example #9 - Download a file with all options.'
sys.stdout.write('  Downloading...')

try:
    file = crocodoc.download.document(uuid2, True, True, 'all')
    filename = os.path.dirname(os.path.abspath(__file__)) + '/example-files/test-with-options.pdf'
    file_handle = open(filename, 'w')
    file_handle.write(file)
    print 'success :)'
    print '  File was downloaded to ' + filename + '.'
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message

"""
Example #10

Download the file we uploaded from Example #3 as a default thumbnail
"""
print ''
print 'Example #10 - Download a default thumbnail from a file.'
sys.stdout.write('  Downloading...')

try:
    file = crocodoc.download.thumbnail(uuid2)
    filename = os.path.dirname(os.path.abspath(__file__)) + '/example-files/thumbnail.png'
    file_handle = open(filename, 'w')
    file_handle.write(file)
    print 'success :)'
    print '  File was downloaded to ' + filename + '.'
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message

"""
Example #11

Download the file we uploaded from Example #3 as a large thumbnail
"""
print ''
print 'Example #11 - Download a large thumbnail from a file.'
sys.stdout.write('  Downloading...')

try:
    file = crocodoc.download.thumbnail(uuid2, 250, 250)
    filename = os.path.dirname(os.path.abspath(__file__)) + '/example-files/thumbnail-large.png'
    file_handle = open(filename, 'w')
    file_handle.write(file)
    print 'success :)'
    print '  File was downloaded to ' + filename + '.'
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message

"""
Example #12

Create a session key for the file we uploaded from Example #3 with default
options.
"""
print ''
print 'Example #12 - Create a session key for a file with default options.'
sys.stdout.write('  Creating... ')
session_key = None

try:
    session_key = crocodoc.session.create(uuid2)
    print 'success :)'
    print '  The session key is ' + session_key + '.'
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message
    
"""
Example #13

Create a session key for the file we uploaded from Example #3 all of the
options.
"""
print ''
print 'Example #13 - Create a session key for a file with all of the options.'
sys.stdout.write('  Creating... ')
session_key = None

try:
    user = {'id': 1, 'name': 'John Crocodoc'}
    session_key = crocodoc.session.create(uuid2,
        editable=True, user=user,
        filter='all', admin=True, downloadable=True,
        copyprotected=False, demo=False, sidebar='visible'
    )
    print 'success :)'
    print '  The session key is ' + session_key + '.'
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message
    
"""
Example #14

Delete the second file we uploaded.
"""
print ''
print 'Example #14 - Delete the first file we uploaded.'
sys.stdout.write('  Deleting... ')

try:
    deleted = crocodoc.document.delete(uuid2)
    
    if deleted:
        print 'success :)'
        print '  File was deleted.'
    else:
        print 'failed :('
except CrocodocError as e:
    print 'failed :('
    print '  Error Code: ' + str(e.status_code)
    print '  Error Message: ' + e.error_message
