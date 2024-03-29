---
title: Quik
---

You can trade on russian exchanges via Evraon. Quik terminal is used to connect to brokers.
So all data will be transferred from your phone via Quik to exchanges and back to your phone.
Unfortunately, Quik can not be avoided. For this to work you need:

- to have a running and logged in instance of Quik
- to follow instructions for Lua scripts from [EvraonQ](https://github.com/avently/EvraonQ)
- to download Evraon server, which should be run on a computer and be connected to Quik.
  On [this page](https://github.com/avently/Evraon/releases) download `evraon.jar`. Create a directory,
  for example, with a name like Evraon, save the file inside it. Then follow an instruction
  [for installing and running](/en/docs/installation/) of your own server
- when you'll be able to connect from the mobile app to your server, create a new profile from
  the settings page of the app, select Quik from a dropdown list, name the profile and save.

A main setup is done, and you should be able to see Quik's tickers inside the app.

For a trading we need to see anonymous trades. You want to enable tickers you'll be trading on only.
To do this press on `System` -> `Data request` -> `Request data for anonymous trades...` ->
choose instruments class you interested in -> `Instruments filter` -> choose needed instruments ->
`Ok` -> `Ok`. Cool, we are done here.

Ensure that you see anonymous trades within Evraon on a trading page. If don't see any
instruments classes just contact your broker and ask it to enable the trades for your account.
Most of the people don't need them so that's why some brokers have the trades disabled for users.
