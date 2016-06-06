# Group Application

## Applications Collection [/api/app{?id,name}]

### List all Applications [GET]

+ Request (application/json)

    + Headers

            Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==

+ Response 200 (application/json)
    + Body

            [
                {
                    "id": "{8A76FC95-0086-4BCE-9517-DC09DDB5652F}",
                    "name": "Chromium"
                },
                {
                    "id": "{430FD4D0-B729-4F61-AA34-91526481799D}",
                    "name": "Potato"
                }
            ]

### Create an Application [POST]

+ Parameters
    * id (required, string, `{8A76FC95-0086-4BCE-9517-DC09DDB5652F}`)
    * name (required, string, `Chromium`)

+ Request (application/json)

    + Headers

            Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==

    + Body

            {
                "id": "{8A76FC95-0086-4BCE-9517-DC09DDB5652F}",
                "name": "Chromium",
            }

+ Response 201

        {
            "id": "{8A76FC95-0086-4BCE-9517-DC09DDB5652F}",
            "name": "Chromium",
        }

## Application [/api/app/{id}]

### Retrieve an Application [GET]

+ Request (application/json)

    + Headers

            Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==

+ Response 200 (application/json)

        {
            "id": "{8A76FC95-0086-4BCE-9517-DC09DDB5652F}",
            "name": "Chromium",
            "data_set": [
                {
                    "id": 5,
                    "app": "{8A76FC95-0086-4BCE-9517-DC09DDB5652F}",
                    "index": "Test",
                    "name": 0,
                    "value": "",
                }
            ]
        }

### Remove an Application [DELETE]

+ Request

    + Headers

            Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==

+ Response 204