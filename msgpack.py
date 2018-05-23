import umsgpack
print(umsgpack.packb({u"compact": True, u"schema": 0}))

print(umsgpack.unpackb(b'\x82\xa7compact\xc3\xa6schema\x00'))