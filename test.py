from __future__ import absolute_import
from __future__ import print_function
import malleable
from malleable.utility import MalleableError

try:
    p = malleable.Profile()
    p.ingest("./amazon.profile")
    if p.validate():
        request = p.get.construct_client("mydomain.sample", "mydatata")
        print(request.url, request.headers, request.body)
except MalleableError as e:
    print(str(e))
