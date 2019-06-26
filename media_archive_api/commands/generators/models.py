import os, collections
import io
from datetime import datetime

def arayToListString( array, chr=None , key_val=False ):
	list_string = ""
	count = 0
	last_item_index = len( array)
	end_line = ""
	for i in array:
		count += 1
		if ( count == last_item_index ):
			end_line = ""
		else:
			end_line = ", "
		
		if(chr == None):
			list_string +=  i + end_line
		else:
			if(key_val == False):
				list_string +=  chr + end_line
			else:
				list_string += i + " = " + chr + end_line
	return list_string

def object_plural(schema):
	return schema["object"]+"s"


def insert_jsdoc(schema):
	jsDoc_params = "/**\n" + " * Insert " + schema["object"] + "\n"
	jsDoc_params += " * @param {Object} "+schema["object"]+" Clip object whit data.\n"
	# for item in schema["cols"]:
	# 	if(item.upper() == schema["object"].upper()):
	# 		jsDoc_params += " * @param {String} "+item+" {0} \n".format(item.capitalize()+" name")	
	# 	else:
	# 		jsDoc_params += " * @param {String} "+item+" {0} \n".format(item.replace("_"," ").capitalize())
	jsDoc_params += " * @returns {Promise} Promise with data or error\n"
	jsDoc_params += " */"
	return jsDoc_params

def insert_function(schema):
	schema_object = schema["object"].lower()
	
	cols_str = arayToListString(schema["cols"])
	cols_str_chr = arayToListString(schema["cols"],"?")
	values = arayToListString([schema_object+"."+item+"\n" for item in schema["cols"]])
	# print(values)

	insert_template = "function insert({0}) ".format(schema_object)+"{\n" + "  return db.runQuery(`INSERT INTO {0}".format(schema["name"])
	insert_template += "\n        ({0})".format(cols_str) + "\n"
	insert_template += "        VALUES({0});`, [".format(cols_str_chr) + "\n        " +values +"]);" + "\n}"
	return insert_template



def update_jsdoc(schema):
	jsDoc_params = "/**\n" + " * Update " + schema["object"] + "\n"
	for item in schema["cols"]:
		if(item.upper() == schema["object"].upper()):
			jsDoc_params += " * @param {String} "+item+" {0} \n".format(item.capitalize()+" name")	
		else:
			jsDoc_params += " * @param {String} "+item+" {0} \n".format(item.replace("_"," ").capitalize())
	jsDoc_params += " * @returns {Promise} Promise with data or error\n"
	jsDoc_params += " */"
	return jsDoc_params

def update_function(schema):
	cols_str = arayToListString(schema["cols"])
	cols_str_chr = arayToListString(schema["cols"],"?")
	template = "function update({0}) ".format(cols_str)+"{\n" + "  return db.runQuery(`UPDATE {0}".format(schema["name"])
	template += "\n    SET " + arayToListString(schema["cols"],"?",True) +"\n"
	template += "    WHERE {0}.{1} = ?;`, [".format(schema["name"],schema["cols"][0]) +"\n"
	template += "    "+cols_str +","+schema["cols"][0] + " ]);\n}"
	
	return template


def update_val_jsdoc(schema):
	jsDoc_params = "/**\n" + " * Update {0} only one column value".format(schema["object"])+"\n"
	jsDoc_params += " * @param {String}"+" {0} {1} ID".format(schema["cols"][0],schema["object"])+"\n"
	jsDoc_params += " * @param {String} col_name Name of property\n"
	jsDoc_params += " * @param {String} val New value for property\n"
	jsDoc_params += " * @returns {Promise} Promise with data or error\n"
	jsDoc_params += " */"

	return jsDoc_params

def update_val_function(schema):
	template = "function updateCol("+schema["cols"][0]+", col_name, val) {\n"
	template += "  return db.runQuery(`UPDATE "+schema["name"]+"\n"
	template += "    SET ${col_name} = ?\n"
	template += "    WHERE {0}.{1} = ?;`, [".format(schema["name"],schema["cols"][0])+"\n"
	template += "    val,{0}]);".format(schema["cols"][0])+"\n}"
	
	return template



def remove_jsdoc(schema):
	jsDoc_params = "/**\n" + " * Delete {0} by {0} ID".format(schema["object"])+"\n"
	jsDoc_params += " * @param {String}"+" {0} {1} ID".format(schema["cols"][0],schema["object"])+"\n"
	jsDoc_params += " * @returns {Promise} Promise with data or error\n"
	jsDoc_params += " */"

	return jsDoc_params

def remove_function(schema):
	template = "function remove("+schema["cols"][0]+") {\n"
	template += "  return db.runQuery(`DELETE FROM "+schema["name"]+"\n"
	template += "  WHERE {0}.{1} = ?;`, [{1}]);".format(schema["name"], schema["cols"][0])+"\n}"

	return template

def list_jsdoc(schema):
	jsDoc_params = "/**\n" + " * Get a list of {0}".format(schema["object"].lower()+"s")+"\n"
	jsDoc_params += " * @returns {Promise} Promise with data or error\n"
	jsDoc_params += " */"
	return jsDoc_params

def list_function(schema):
	template = "function list() {\n"
	template += "  return db.runQuery(`SELECT * FROM {0};`, []);".format(schema["name"]) +"\n"
	template +="}"

	return template

def find_jsdoc(schema):
	jsDoc_params = "/**\n" + " * Find a {0} by ID".format(schema["object"].capitalize())+"\n"
	jsDoc_params += " * @param {String}"+" {0} {1}\n".format(schema["cols"][0], schema["cols"][0].replace("_"," ").capitalize())
	jsDoc_params += " * @returns {Promise} Promise with data or error\n"
	jsDoc_params += " */"
	return jsDoc_params

def find_function(schema):
	template = "function find( "+schema["cols"][0]+" ) {\n"
	template += "  return db.runQuery(`SELECT * FROM {0}\n      WHERE {0}.{1} = ?;`, [{1}]);".format(schema["name"],schema["cols"][0]) +"\n"
	template +="}"

	return template

def count_jsdoc(schema):
	jsDoc_params = "/**\n" + " * Get a number of total {0}".format(schema["object"].lower()+"s")+"\n"
	jsDoc_params += " * @returns {Promise} Promise with data or error\n"
	jsDoc_params += " */"
	return jsDoc_params

def module_jsdoc(author, title, blank_lines):
	blank_line = " * \n"
	title = " * {0} \n".format(title)
	jsDoc_params = "/**\n"+ title + blank_line*blank_lines +" * Developed by {0}".format(author)+"\n"
	jsDoc_params += " * {0}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	jsDoc_params += " */\n\n"
	return jsDoc_params

def count_function(schema):
	template = "function count() {\n"
	template += "  return db.runQuery('SELECT COUNT(*) as total_{1} FROM {0};', []);".format(schema["name"],schema["object"].lower()+"s") +"\n"
	template +="}"

	return template

def module_exports(schema):
	list_string = "module.exports = {\n"
	count = 0
	
	end_line = ""
	ordered_functions = collections.OrderedDict(sorted(schema["functions"].items()))
	last_item_index = len(ordered_functions)

	for key, val in ordered_functions.items():

		count += 1
		if ( count == last_item_index ):
			end_line = ""
		else:
			end_line = ", "
		list_string += "    "+val + end_line +"\n"
	list_string += "};"

	return list_string

def print_functions(schema):
	ordered_functions = collections.OrderedDict(sorted(schema["functions"].items()))
	code_string = ""
	function_interlineado = "\n \n \n"
	for key, val in ordered_functions.items():
		if(key.lower() == "list"):
			code_string += list_jsdoc(schema) + "\n" 
			code_string += list_function(schema)
			code_string += function_interlineado
		if(key.lower() == "update"):
			code_string += update_jsdoc(schema) + "\n" 
			code_string += update_function(schema)
			code_string += function_interlineado
		if(key.lower() == "updatecol"):
			code_string += update_val_jsdoc(schema) + "\n" 
			code_string += update_val_function(schema)
			code_string += function_interlineado
		if(key.lower() == "remove"):
			code_string += remove_jsdoc(schema) + "\n" 
			code_string += remove_function(schema)
			code_string += function_interlineado
		if(key.lower() == "insert"):
			code_string += insert_jsdoc(schema) + "\n" 
			code_string += insert_function(schema)
			code_string += function_interlineado
		if(key.lower() == "find"):
			code_string += find_jsdoc(schema) + "\n" 
			code_string += find_function(schema)
			code_string += function_interlineado
		if(key.lower() == "count"):
			code_string += count_jsdoc(schema) + "\n" 
			code_string += count_function(schema)
			code_string += function_interlineado

	return code_string

if __name__ == '__main__':
	
	

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

	print(insert_jsdoc(schema))
	print(insert_function(schema))

	# module_name = object_plural(schema).lower() + ".js"
	# doc_title = "Model for {0} schema".format(object_plural(schema))
	# doc_string = module_jsdoc("Enrique Nieto Martínez",doc_title,1)
	# header = "const db = require('./db');" + "\n\n"

	# module_code = doc_string + header + print_functions(schema) + module_exports(schema)
	# # print(module_code)

	# # path_save = "..\\..\\models\\"
	# path_save = ".\\build\\"

	# # MAC OS
	# # path_save = "..//..//models//"
	# # path_save = ".//build//"

	# dirname = os.path.dirname(__file__)
	# filename = os.path.join(dirname, path_save + module_name)
	# if os.path.exists(path_save):
	# 	print("existe Path")
	# 	print("saving: ",module_name)
	# 	with io.open(filename,'w',encoding='utf8') as f:
	# 		f.write(module_code)

