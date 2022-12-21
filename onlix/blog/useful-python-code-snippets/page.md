---
tags: programming, python, code, snippets
category: programming
subtitle: Some simple code snippets for copy-pasting!
---

# Useful Python Code Snippets
### Pip notice
#### Troubleshooting
If you get an ModuleNotFoundError, [open your terminal](https://www.wikihow.com/Open-Terminal-in-Windows) and type `pip` (and obviously press enter). If you get an error, please [install pip](https://pythonassets.com/posts/installing-and-using-pip-on-windows-linux-and-macos/) first. Next, try that command again. If everything works, type `pip install ` and then the module which lead to an error. You can check the code or the error traceback. For example: `pip install requests`. You can also try `pip3` if that seems to work better for you. To check what packages you have installed, type `pip freeze`. Get a warning saying you're using an old version of pip, type `pip install --upgrade pip`. Upgrading/updating is very important because in the worst case, they could even fix security vulnerabilities!

#### No package found?
Do you get the following message? 

    ERROR: Could not find a version that satisfies the requirement asd8asd (from versions: none)
    ERROR: No matching distribution found for asd8asd

This means you misspelled the library name. Go to [https://pypi.org](https://pypi.org) and search for the package you want to import!

> **Tip:** If you're using DuckDuckGo, try `!pip <package-name>`, e.g. `!pip requests`. This will automatically redirect you to the results ;)

#### Packages you need to install
Some of the following code snippets require some packages. Simply type `pip install package-name-here` in your terminal for every single one of these. An example (with output):

    pip install sklearn

    Collecting sklearn
    ...
    Downloading scikit_learn-1.1....whl (30.4 MB)
        ━━━━━━━━━━━━━━━━━━━━━━ 30.4/30.4 MB 14.0 MB/s eta 0:00:00
    ...
        ━━━━━━━━━━━━━━━━━━━━━━ 307.0/307.0 kB 34.4 MB/s eta 0:00:00
    ...
    Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn, sklearn
    Running setup.py install for sklearn ... done
    Successfully installed ...

The dots (`...`) are by me to shorten the example.

If you want to install more than one package at once, separate them using a space. For example:

    pip install pandas sklearn requests

Which will install all of them. Then

If you are unsure wether you've already downloaded a package or not, don't worry - `pip` will simply skip the installation or update the package. So just install all of the packages to be sure!

***

## File objects
### String to BytesIO/pseudo file [(Virtual File Processing)](https://stackoverflow.com/questions/18550127/how-to-do-virtual-file-processing)

Have you ever wondered how you can create a download button on your Flask website without having to actually save anything on your hard drive? This can be really useful for output files, logs or similar.

It's actually pretty simple!

    import io 
    io.BytesIO('Hello World!'.encode('utf-8')

The code snippet above isn't that useful without any context, but can help you to understand how you can
convert strings to io.BytesIO objects.

Here's an example of how you can implement this functionality for your Flask server:
    
    ...

    @app.route('/example.log')
    def log_download():
        text = 'Hello, world!'

        return flask.send_file(io.BytesIO(text.encode('utf-8')), mimetype='text/html', attachment_filename='example.log' ,as_attachment=True)

    ...

This will create a website route (`/example.log`) with a file download. You can change the variable `text` to represent any string you want to. How about the current time?

## Get Date & Time (`datetime`)
The following code will return the current time and date nicely formatted.
You might also want to check out the [Python strftime cheatsheet](https://strftime.org/).

### Code
    from datetime import datetime

    # TIP · Don't use "time" as a variable name
    # because it could lead to conflicts with the "time" library!
    
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(current_time)
    
### Example Output
    25/09/2022 10:12:51

## Unix Timestamp `int` to `datetime`
The following code won't format the code - for that, see the section above.

    import datetime
    
    unix_time = 1664094041
    date_time = datetime.datetime.fromtimestamp(unix_time) # a datetime object

It's as simple as that!

## Get Linux Distribution Name & Info
This only works on Linux systems! Python will grab the content of `/etc/os-release` and return a dictionary we can work with:

### Code
    import platform

    distro = platform.freedesktop_os_release()
    
    print(distro.get('NAME')) # Distro Name
    print(distro.get('ID_LIKE') or 'Linux Kernel') # Distro is based on...
    print(distro.get('BUILD_ID') or distro.get('VERSION_ID') # Distro Version

### Example output
    EndeavourOS
    arch
    2022.04.08

or:

    Debian GNU/Linux
    Linux Kernel
    10

### Troubleshooting
    Traceback (most recent call last):
    File "[...]", line 3, in <module>
        distro = platform.freedesktop_os_release()
    AttributeError: 'module' object has no attribute 'freedesktop_os_release'

This could mean you're using an older version of Python (3.10+ is supported!). But don't worry! There are also [backports](https://pypi.org/project/freedesktop_os_release/) available.

## Networking
### Get the device's IP Address, location, ISP info, domain & more 
According to [the API's website](https://ipinfo.io/missingauth), up to 50K requests/month are allowed.
That should be more than enough. It can take a few seconds to get the IP info, though.

### Dependencies
Before we can run the code, we might also need to quickly install the needed packages.
Don't know how to use pip or think you don't have it installed? Getting an error?
See [the top of this page](#pip-notice)!

- `requests`

### Code
    import requests
    import webbrowser

    response = requests.get('https://ipinfo.io/json').json() # send website request
    print(response['ip'])
    print(f'{response["city"]} in {response["region"]}, {response["country"]}')
    print(response.get('org') or 'No organization.')

    if response.get('hostname'): # website detected on server
        if input(f'Website detected: {response.get("hostname")}. Type y and press enter to open.') == 'y':
            webbrowser.open('hostname')

### Example output
My server:

    173.212.213.133
    Oberdorla in Thuringia, DE
    AS51167 Contabo GmbH
    Website detected: vmd80690.contaboserver.net. Type y and press enter to open.

or: (I changed it up a bit)

    74.145.169.142
    Berlin in Berlin, DE
    AS5555 Vodafone Deutschland GmbH
