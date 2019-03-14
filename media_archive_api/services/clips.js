const clips_model = require('../models/mysql/clips')
var moment = require('moment');

const date_format_store = 'YYYY-MM-DD H:mm:ss';
const date_format_display = 'DD-MM-YYYY H:mm:ss';

async function listClips(req, res){
    const clips = clips_model.list();
    clips.then(function(val){
       
        const stored_clips = Object.keys(val).map(function(key){
            
            const new_clip = {
                name: val[key].name,
                size_bytes: val[key].size_bytes,
                duration: val[key].duration,
                aspect: val[key].aspect,
                size_screen: val[key].size_screen,
                created_date: moment(val[key].created_date).format(date_format_display),
                modified_date: moment(val[key].modified_date).format(date_format_display),
                tags: val[key].tags,
                thumbnail: val[key].thumbnail,
                proxy: val[key].proxy,
                o_pxy_id: val[key].o_pxy_id,
                o_asset_type: val[key].o_asset_type,
                format_uid: val[key].format_uid,
                a_owner_uid: val[key].a_owner_uid,
                a_groups: val[key].a_groups,
                a_users: val[key].a_users,
                h_main_origin_uid: val[key].h_main_origin_uid,
                h_origins: val[key].h_origins,
                license: val[key].license,
                restored_count: val[key].restored_count
            }
            return new_clip;
        });

        
        res.json(stored_clips);
    });
}

async function addClip(req, res){
	const clip = req.body
    const new_clip ={
        name: clip.name,
        size_bytes: clip.size_bytes,
        duration: clip.duration,
        aspect: clip.aspect,
        size_screen: clip.size_screen,
        created_date: clip.created_date,
        modified_date: clip.modified_date,
        tags: clip.tags,
        thumbnail: clip.thumbnail,
        proxy: clip.proxy,
        o_pxy_id: clip.o_pxy_id,
        o_asset_type: clip.o_asset_type,
        format_uid: clip.format_uid,
        a_owner_uid: clip.a_owner_uid,
        a_groups: clip.a_groups,
        a_users: clip.a_users,
        h_main_origin_uid: clip.h_main_origin_uid,
        h_origins: clip.h_origins,
        license: clip.license,
        restored_count: clip.restored_count
    }
    clips_model.insert(new_clip)
    .then(function(val) {
        res.json(val);
    });
}

module.exports = {
    addClip,
    listClips
}