xivo-ws
=========
[![Build Status](https://travis-ci.org/xivo-pbx/xivo-ws.png?branch=master)](https://travis-ci.org/xivo-pbx/xivo-ws)

xivo-ws is a python library for accessing XiVO web services.


Configuration
-------------

On your XiVO, you must create a web service user. Please refer to the [documentation](http://documentation.xivo.io/production/api_sdk/web_services.html) for more details.


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

Further documentation
---------------------


* XiVO server: http://documentation.xivo.io/production/
* Creating a web service user: http://documentation.xivo.io/production/api_sdk/web_services.html#configuration


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
