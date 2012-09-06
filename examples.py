import crocodoc, time

crocodoc.api_token = ""

uuid = crocodoc.document.upload(url="http://www.irs.gov/pub/irs-pdf/fw4.pdf")
print uuid

status = crocodoc.document.status(uuid)
print status

session = crocodoc.session.create(uuid=uuid,downloadable=True)
print session

time.sleep(3)

file = open('test.pdf', 'wb')
crocodoc.download.document(file, uuid, pdf=True)
file.close()

file = open('test.png', 'wb')
crocodoc.download.thumbnail(file, uuid)
file.close()

file = open('test.txt', 'wb')
crocodoc.download.text(file, uuid)
file.close()

crocodoc.document.delete(uuid)
