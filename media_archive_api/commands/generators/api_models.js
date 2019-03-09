schema = {
		"name":"media_archive.clips",
		"object":"Clip",
		"cols":["clips_uid","name","size_bytes","duration","aspect","size_screen","created_date","modified_date","tags","thumbnail","proxy","o_pxy_id","o_asset_type","format_uid","a_owner_uid","a_groups","a_users","h_main_origin_uid","h_origins","license","restored_count"],
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
		"name":"media_archive.origins",
		"object":"Origin",
		"cols":["origin_uid","name","description","ftp","ftp_user","ftp_pass","ftp_host","cif","cif_user","cif_pass","cif_host","site_uid","capacity_bytes","capacity_used","capacity_free","status"],
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
		"name":"media_archive.transactions",
		"object":"Transaction",
		"cols":["transaction_uid","clip_uid","action","date","user_uid","host_uid","app_uid","description"],
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
