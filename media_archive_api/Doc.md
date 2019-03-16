# API URL
## <API_URL>

The api url in development test can be like:
http://127.0.0.1:3006

# Clips

## List all clips
    
    Method: GET
    URL: <API_URL>/clips
    Data: {}

    Example: http://127.0.0.1:3006/clips/
    Response Example:
    ```json
    [
        {
            "clip_uid": 1,
            "name": "21H ROMA OSCAR-FT_DF007QCD",
            "size_bytes": 1171249408,
            "duration": "00:02:27.25",
            "aspect": "4:3",
            "size_screen": "1440x1080",
            "created_date": "25-01-2019 18:43:00",
            "modified_date": "25-01-2019 18:44:00",
            "tags": "Stratus, Milenio, Archivo",
            "thumbnail": "",
            "proxy": "",
            "o_pxy_id": "",
            "o_asset_type": "Clip",
            "format_uid": 2,
            "a_owner_uid": 1,
            "a_groups": "[\"editors\", \"viewers\", \"ingesters\", \"admins\"]",
            "a_users": "[]",
            "h_main_origin_uid": 9,
            "h_origins": "[9]",
            "license": "Milenio Lic",
            "restored_count": 0,
            "format_name": "MXF_AVCI50",
            "extension": ".mxf"
        }
    ]    
    ```

## Add new clip
    Method: POST
    URL: <API_URL>/clips
    Data: {
            "name":"Amlo Cuco",
            "size_bytes":658600,
            "duration":"00:00:00.23",
            "aspect":"16:9",
            "size_screen":"1920x1080",
            "created_date":"2019-03-13 11:10:15",
            "modified_date":"2019-03-13 22:30:03",
            "tags":"Stratus, Milenio, Chapo, Amlo",
            "thumbnail":"./clip.jpg",
            "proxy":"asdf456asda654aasdf654",
            "o_pxy_id":"4asa654asdfasd65asdasdf",
            "o_asset_type":"Clip",
            "format_uid":5,
            "a_owner_uid":5,
            "a_groups":"editors, viewers, ingesters",
            "a_users":"[5,10,3,7]",
            "h_main_origin_uid":0,
            "h_origins":"[0,1,3]",
            "license":"Milenio Lic",
            "restored_count":6
        }

    Example: http://127.0.0.1:3006/clips/
    Response Example:
    ```json
        {
            "fieldCount": 0,
            "affectedRows": 1,
            "insertId": 6,
            "serverStatus": 2,
            "warningCount": 0,
            "message": "",
            "protocol41": true,
            "changedRows": 0
        }
    ```

## Find clip
    Method: GET
    URL: <API_URL>/clips/find
    Data:{
            "name":"21H ROMA OSCAR-FT_DF007QCD",
            "mode":"strict"
         }
        name: Name of clip
        mode: mode to find the clip
              values( "strict" | "aprox" )
              strict: Find by exact name
              aprox: Find by aprox name
    Example: http://127.0.0.1:3006/clips/find
    Response Example:
    ```json
        [
            {
                "clip_uid": 1,
                "name": "21H ROMA OSCAR-FT_DF007QCD",
                "size_bytes": 1171249408,
                "duration": "00:02:27.25",
                "aspect": "4:3",
                "size_screen": "1440x1080",
                "created_date": "2019-01-26T00:43:00.000Z",
                "modified_date": "2019-01-26T00:44:00.000Z",
                "tags": "Stratus, Milenio, Archivo",
                "thumbnail": "",
                "proxy": "",
                "o_pxy_id": "",
                "o_asset_type": "Clip",
                "format_uid": 2,
                "a_owner_uid": 1,
                "a_groups": "[\"editors\", \"viewers\", \"ingesters\", \"admins\"]",
                "a_users": "[]",
                "h_main_origin_uid": 9,
                "h_origins": "[9]",
                "license": "Milenio Lic",
                "restored_count": 0,
                "format_name": "MXF_AVCI50",
                "extension": ".mxf"
            }
        ]
    ```

## Update a property of clip
    Method: PATCH
    URL: <API_URL>/clips/:clip_uid
    Data:
        {
            <key>:<value>
        }
    
    Example: http://127.0.0.1:3006/clips/1
    Sample Data: {
                    "restored_count":2
                 }

    Note: Only change one property.

    Response Example: 
    ```json
        {
            "fieldCount": 0,
            "affectedRows": 1,
            "insertId": 0,
            "serverStatus": 2,
            "warningCount": 0,
            "message": "(Rows matched: 1  Changed: 1  Warnings: 0",
            "protocol41": true,
            "changedRows": 1
        }
    ```