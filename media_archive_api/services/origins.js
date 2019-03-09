const origins_model = require('../models/mysql/origins')

async function listOrigins(){
    return origins_model.list()
}

async function addOrigin(){
    return origins_model.insert("name", "description", "ftp", "ftp_user", "ftp_pass", "ftp_host", "cif", "cif_user", "cif_pass", "cif_host", "site_uid", "capacity_bytes", "capacity_used", "capacity_free", "status")
}
module.exports = {
    listOrigins,
    addOrigin
}