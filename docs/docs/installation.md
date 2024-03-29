---
title: Installation
---

=== "Android"

    Open in [Google Play](https://play.google.com/store/apps/details?id=com.evraon.trading)

    After installation you will be able to setup the server and app without problems and with instructions.

=== "Linux/Windows/Mac"

    Download from [Github](https://github.com/avently/Evraon/releases)

    Ensure you have installed Java: [can be downloaded here](https://www.java.com/en/download/manual.jsp).

    Create a new directory, e.g, on a desktop. Then type in a terminal:
    ```bash
    java -jar
    ```
    there is a space after -jar. Move evraon.jar file inside the terminal window and press enter.

    You'll get something like this (Linux):
    ```bash
    java -jar /home/user/Desktop/evraon/evraon.jar
    ```

    Server will be started. Since then you'll be able to connect to it via mobile app.

#### How to connect to the server with the mobile app:

- add new server
- enter IP address of the computer you use (where the server have been working). Usually it looks like 192.168.1.x. Enter a port 5515. To find a correct IP address you need:

    - in Linux: type in terminal `ifconfig`, you'll see `inet` word followed by the IP address. Just find a corrent network interface of you Wifi from all list of networks
    - in Windows: press two buttons `Win + X`, then select command prompt, type `ipconfig` and enter. You'll see the IP address after `IPv4`.

- Provide username and password. You can find them after first start inside server.json. They are randomly generated for every installation.

That's it, you can connect now to the server.
