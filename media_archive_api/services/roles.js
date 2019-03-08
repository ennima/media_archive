const roles_ctrl = require('../models/mysql/roles')

/**
 * Get a list of all roles
 * @returns {Promise} Promise with data or error
 */
async function getAllRoles(){
	const prom = roles_ctrl.list()
	const prom2 = roles_ctrl.listUsersByRole("developer")
	const prom3 = roles_ctrl.getUserRoles("113")
	var roles = await Promise.all([prom,prom2,prom3])
	console.log(typeof(roles))
	
	console.log("------------asdfasdf")

	return {roles:roles[0], developers:roles[1].length, user_113:roles[2].length}
}


module.exports = {
	getAllRoles
}