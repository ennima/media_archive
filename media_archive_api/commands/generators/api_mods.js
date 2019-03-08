schema = {
    "name":"auth.users",
    "object":"User",
    "cols":["user_uid","name","pass","email","active"],
    "functions": {
        "list":"list",
        "remove":"remove",
        "update":"update",
        "insert":"insert",
        "find":"find",
        "count":"count",
        "updatecol":"updateCol"
        }
}

schema = {
    "name":"auth.roles",
    "object":"Role",
    "cols":["role_uid", "user_uid", "role", "app_uid"],
    "functions": {
        "list":"list",
        "remove":"remove",
        "update":"update",
        "insert":"insert",
        "find":"find",
        "count":"count",
        "updatecol":"updateCol"
        }
}

schema = {
    "name":"auth.apps",
    "object":"App",
    "cols":["app_uid", "developer_uid", "name", "token", "active"],
    "functions": {
        "list":"list",
        "remove":"remove",
        "update":"update",
        "insert":"insert",
        "find":"find",
        "count":"count",
        "updatecol":"updateCol"
        }
}

schema = {
    "name":"auth.companies",
    "object":"Companie",
    "cols":["company_uid", "name", "nickname", "country", "state", "address", "lat", "lon"],
    "functions": {
        "list":"list",
        "remove":"remove",
        "update":"update",
        "insert":"insert",
        "find":"find",
        "count":"count",
        "updatecol":"updateCol"
        }
}

schema = {
    "name":"auth.hosts",
    "object":"Host",
    "cols":["host_uid","nics","name","os","ram","cpu","storage","location"],
    "functions": {
        "list":"list",
        "remove":"remove",
        "update":"update",
        "insert":"insert",
        "find":"find",
        "count":"count",
        "updatecol":"updateCol"
        }
}

schema = {
    "name":"auth.licenses",
    "object":"License",
    "cols":["lic_uid","developer_uid","app_uid","active_token","created","user_uid","host_uid"],
    "functions": {
        "list":"list",
        "remove":"remove",
        "update":"update",
        "insert":"insert",
        "find":"find",
        "count":"count",
        "updatecol":"updateCol"
        }
}

schema = {
    "name":"auth.locations",
    "object":"Location",
    "cols":["location_uid","name","company_uid","piso","area"],
    "functions": {
        "list":"list",
        "remove":"remove",
        "update":"update",
        "insert":"insert",
        "find":"find",
        "count":"count",
        "updatecol":"updateCol"
        }
}