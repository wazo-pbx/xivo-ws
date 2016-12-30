xivo-ws
=========
[![Build Status](https://travis-ci.org/wazo-pbx/xivo-ws.png?branch=master)](https://travis-ci.org/wazo-pbx/xivo-ws)

xivo-ws is a python library for accessing the "old" Wazo web services.

These web services are provided by the web-interface. They are **obsolete** and
will be removed soon. You should not use them in new developments, and if you
were already using them, you should migrate to the [Wazo REST
APIs](http://documentation.wazo.community/en/stable/api_sdk/rest_api/rest_api.html).


Configuration
-------------

On your Wazo, you must create a web service user.


Example
-------

~~~
from xivo_ws import XivoServer, User, UserLine

xivo_server = XivoServer('skaro', 'my_username', 'my_password')

user = User()
user.firstname = 'Jack'
user.lastname = 'Johnson'
user.line = UserLine(context='default', number=1001)

xivo_server.users.add(user)
~~~

More examples are available in the ```examples``` directory.


xivo-ws-debug
-------------

   > users add

will pop your editor, in which you should write a Python dictionary to be sent
to the WS

   > users delete 32

will delete user whose id is 32.

```-v``` option allows you to see what is sent and received to/from the WS.


Releasing a new version
-----------------------

    git commit

Read version number in xivo_ws/version.py.

    git tag <version>

    make upload

    git push --tags

Edit the version file and increase version number.

    git commit
