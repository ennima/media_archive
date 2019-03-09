const clips_model = require('../models/mysql/clips')

async function listClips(){
    return clips_model.list()
}

async function addClip(){
	return clips_model.insert("name", "size_bytes", "duration", "aspect", "size_screen", "created_date", "modified_date", "tags", "thumbnail", "proxy", "o_pxy_id", "o_asset_type", "format_uid", "a_owner_uid", "a_groups", "a_users", "h_main_origin_uid", "h_origins", "license", "restored_count")
}

module.exports = {
    addClip,
    listClips
}