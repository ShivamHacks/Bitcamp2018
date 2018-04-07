var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://mainuser:onlinedbk123@ds237379.mlab.com:37379/maindb";

/*
Creds:
- MainUser
- dbklab
*/

var jsonfile = require('jsonfile');

MongoClient.connect(url, function(err, db) {

	if (err) throw err;
	var dbo = db.db("maindb");

	/* Create collection */
	dbo.createCollection("course_grades", function(err, res) {
		if (err) throw err;
		console.log("Collection created!");

		/* Clear collection */
		dbo.collection("course_grades").remove({}, function(err, res) {
			if (err) throw err;
			console.log("Collection cleared!");

			/* Fill collection */
			courses = [];
			data = jsonfile.readFileSync('table.json');
			for (var course in data) {
				data[course]['_id'] = course;
				courses.push(data[course]);
			}

			dbo.collection("course_grades").insertMany(courses, function(err, res) {
				if (err) throw err;
				console.log("inserted all courses!");
				db.close();
			});


		});
	});

});

/*
MongoClient.connect(url, function(err, db) {

	if (err) throw err;
	var dbo = db.db("maindb");

	/* Clear collection
	dbo.collection("course_grades").remove({}, function(err, res) {
		if (err) throw err;
		console.log("Collection cleared!");
		db.close();
	});

});

MongoClient.connect(url, function(err, db) {

	if (err) throw err;
	var dbo = db.db("maindb");

	/* Fill collection
	courses = [];
	data = jsonfile.readFileSync('table.json');
	for (var course in data) {
		data[course]['_id'] = course;
		courses.push(data[course]);
	}

	dbo.collection("course_grades").insertMany(courses, function(err, res) {
		if (err) throw err;
		console.log("inserted all courses!");
		db.close();
	});

});

MongoClient.connect(url, function(err, db) {

	if (err) throw err;
	var dbo = db.db("maindb");

	/* Print collection
	dbo.collection("course_grades").find({}).toArray(function(err, result) {
		if (err) throw err;
		console.log('found a bunch of courses!');
		db.close();
	});

});

MongoClient.connect(url, function(err, db) {

	if (err) throw err;
	var dbo = db.db("maindb");

	/* Print collection
	dbo.collection("course_grades").find({ _id: 'AASP100' }).toArray(function(err, result) {
		if (err) throw err;
		console.log(result);
		db.close();
	});

});
*/