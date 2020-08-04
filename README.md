# sourceapi

[![Build Status](https://drone.fap.no/api/badges/kradalby/sourceapi/status.svg)](https://drone.fap.no/kradalby/sourceapi)

API for quering Source servers, based on SourceLib

At the moment, the API is tested with Counter-Strike: Source and Global Offensive.

The API takes a json argument as follows:

    {
        'data': 'ip:port'
    }

Below the route table, a sample response from the "all" route.

## Routes

There is a hosted version of this API at source.fap.no.

| Route                           | HTTP method | Description            |
| ------------------------------- | ----------- | ---------------------- |
| source.fap.no/api/v1/all        | POST        | Get all information    |
| source.fap.no/api/v1/serverinfo | POST        | Get server information |
| source.fap.no/api/v1/playerinfo | POST        | Get player information |
| source.fap.no/api/v1/ping       | POST        | Get ping information   |
| source.fap.no/api/v1/rules      | POST        | Get rules information  |

## Example response

Note that the ping is based on the time from the given API instance.

    {
        "status": "success",
        "data": [
            "z.fap.no:27015": {
                "appid": 240,
                "dedicated": "d",
                "edf": 145,
                "gamedesc": "Counter-Strike: Source",
                "gamedir": "cstrike",
                "hostname": "dfekt.no | Dust2 Only",
                "map": "de_dust2",
                "maxplayers": 28,
                "network_version": 17,
                "numbots": 0,
                "numplayers": 1,
                "os": "l",
                "passworded": 0,
                "ping": 0.016348838806152344,
                "players": [
                    {
                    "index": 0,
                    "kills": 0,
                    "name": "rasmusharlevchristiansen",
                    "time": 166.60467529296875
                    }
                ],
                "port": 27015,
                "secure": 1,
                "steamid": 90095528448212994,
                "version": "2230303"
            }
        ]
    }
