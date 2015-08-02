# sourceapi
API for quering Source servers, based on SourceLib

At the moment, the API is tested with Counter-Strike: Source and Global Offensive.

The API takes a json argument as follows:

    [
        [
            "z.fap.no", 27016
        ],
        [
            "z.fap.no", 27015
        ]

    ]

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
            "rules": {
                "bot_quota": "0",
                "decalfrequency": "60",
                "hlxce_plugin_version": "1.6.19",
                "hlxce_version": "",
                "hlxce_webpage": "http://www.hlxcommunity.com",
                "host_framerate": "0",
                "hpk_lite_version": "1.0.0.1",
                "metamod_version": "1.10.0V",
                "mp_autocrosshair": "1",
                "mp_autoteambalance": "1",
                "mp_buytime": "0.25",
                "mp_c4timer": "45",
                "mp_disable_respawn_times": "0",
                "mp_fadetoblack": "0",
                "mp_falldamage": "0",
                "mp_flashlight": "1",
                "mp_footsteps": "1",
                "mp_forceautoteam": "0",
                "mp_forcecamera": "0",
                "mp_forcerespawn": "1",
                "mp_fraglimit": "0",
                "mp_freezetime": "4",
                "mp_friendlyfire": "0",
                "mp_holiday_nogifts": "0",
                "mp_hostagepenalty": "5",
                "mp_limitteams": "2",
                "mp_match_end_at_timelimit": "0",
                "mp_maxrounds": "0",
                "mp_respawnwavetime": "10.0",
                "mp_roundtime": "1.75",
                "mp_scrambleteams_auto": "1",
                "mp_scrambleteams_auto_windifference": "2",
                "mp_stalemate_enable": "0",
                "mp_stalemate_meleeonly": "0",
                "mp_startmoney": "800",
                "mp_teamplay": "0",
                "mp_teams_unbalance_limit": "1",
                "mp_timelimit": "30",
                "mp_tournament": "0",
                "mp_weaponstay": "0",
                "mp_winlimit": "0",
                "nextlevel": "",
                "sb_version": "1.4.10",
                "sbchecker_version": "1.0.2",
                "sm_nextmap": "de_dust2",
                "sm_team_balance_version": "2.2.2",
                "sourcemod_version": "1.5.2",
                "sv_accelerate": "5",
                "sv_airaccelerate": "10",
                "sv_allowminmodels": "1",
                "sv_alltalk": "0",
                "sv_bounce": "0",
                "sv_cheats": "0",
                "sv_competitive_minspec": "0",
                "sv_contact": "",
                "sv_enableboost": "0",
                "sv_enablebunnyhopping": "0",
                "sv_footsteps": "1",
                "sv_friction": "4",
                "sv_gravity": "800",
                "sv_maxcmdrate": "66",
                "sv_maxrate": "30000",
                "sv_maxspeed": "320",
                "sv_maxupdaterate": "66",
                "sv_maxusrcmdprocessticks": "24",
                "sv_mincmdrate": "10",
                "sv_minrate": "15000",
                "sv_minupdaterate": "66",
                "sv_noclipaccelerate": "5",
                "sv_noclipspeed": "5",
                "sv_nostats": "0",
                "sv_password": "0",
                "sv_pausable": "0",
                "sv_rollangle": "0",
                "sv_rollspeed": "200",
                "sv_specaccelerate": "5",
                "sv_specnoclip": "1",
                "sv_specspeed": "3",
                "sv_steamgroup": "",
                "sv_stepsize": "18",
                "sv_stopspeed": "75",
                "sv_tags": "sv_pure1,zblock",
                "sv_voiceenable": "1",
                "sv_wateraccelerate": "10",
                "sv_waterfriction": "1",
                "tf_arena_use_queue": "1",
                "tv_delay": "30",
                "tv_enable": "0",
                "tv_password": "0",
                "tv_relaypassword": "0",
                "zb_status": "1",
                "zb_version": "4.72"
            },
            "secure": 1,
            "steamid": 90095528448212994,
            "version": "2230303"
        }
    }
