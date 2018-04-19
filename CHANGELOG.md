# Changelog

This file is a manually maintained list of changes for each release.

## v0.3.1 (2018-04-19)

- Cache mechanism to store already translated menus in order to save the API calls to GCP
- Minor bugfixes

## v0.3.0 (2018-04-18)

- Official Google Translate API calls using GCP
- Minor bugfixes

## v0.2.4 (2018-02-20)

- Fully Russian language support thanks to [Ali Kasimov](mailto:akasimov@cisco.com)
- More restaurant exceptions
- Minor bugfixes

## v0.2.3 (2018-02-12)

- Parsing restaurant website exceptions

## v0.2.2 (2018-02-12)

- Sending errors directly to admin room
- Bugfix with translation of exceptions
- Bugfix with webhook handling

## v0.2.1 (2018-02-09)

- Worker thread signal handling
- Minor bugfixes with time handling and unicode encoding
- Database connection health checking

## v0.2.0 (2018-02-08)

- Voting support for people who often goes alone for a lunch
- Creating a new thread which periodically checks the time

## v0.1.7 (2018-02-05)

- Added support to parse menus from restaurant websites
- Minor bugfixes with Czech language abbreviation and empty parameters

## v0.1.6 (2018-02-01)

- Fully Croatian language support

## v0.1.5 (2018-02-01)

- Fully Slovak language support

## v0.1.4 (2018-01-31)

- Minor bugfix with sending message to itself
- Fully Turkish language support thanks to [Ozge Kurtaslan](mailto:okurtasl@cisco.com)
- Fully Polish language support thanks to [Dominik Stefaniak](mailto:dostefan@cisco.com)

## v0.1.3 (2018-01-31)

- Minor bugfix with setting different language and encoding
- Fully Czech language support
- Preparation for other languages

## v0.1.2 (2018-01-30)

- Fully feature lunch menu bot to give you the daily menu
- Storing user preferred restaurants in the MySQL database
- Leveraging Zomato API to get the daily menu
- Translating into desired language

## v0.1.1 (2018-01-29)

- Simple response tu the user showing bot capabilities
- Creating structured project rather than simple script

## v0.1.0 (2018-01-23)

- First stable release handling webhooks from Spark cloud
- Environment setup including Docker and Python interpreter
- Accessing and modifying database for new users and rooms
