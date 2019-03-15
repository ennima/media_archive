const origins_model = require('../models/mysql/origins')

async function listOrigins(req, res){
    origins_model.list()
    .then(function(val) {
        res.json(val);
    });
}

async function addOrigin(req, res){
    const origin = req.body;
    const new_origin = {
        'name':origin.name,
        'description':origin.description,
        'ftp':origin.ftp,
        'ftp_user':origin.ftp_user,
        'ftp_pass':origin.ftp_pass,
        'ftp_host':origin.ftp_host,
        'cif':origin.cif,
        'cif_user':origin.cif_user,
        'cif_pass':origin.cif_pass,
        'cif_host':origin.cif_host,
        'site_uid':origin.site_uid,
        'capacity_bytes':origin.capacity_bytes,
        'capacity_used':origin.capacity_used,
        'capacity_free':origin.capacity_free,
        'status':origin.status
    }
    origins_model.insert(new_origin)
    .then(function(val) {
        res.json(val);
    });
}
module.exports = {
    listOrigins,
    addOrigin
}