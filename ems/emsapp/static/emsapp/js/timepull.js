	function optionLoop(start, end, id, this_day) {
		var i, opt;
		opt = null;
		for (i = start; i <= end ; i++) {
			if (i === this_day) {
				opt += "<option value='" + i + "' selected>" + i + "</option>";
			} else {
				opt += "<option value='" + i + "'>" + i + "</option>";
			}
		}
		return document.getElementById(id).innerHTML = opt;
	};

	var optionLoop, this_day, this_month, this_year, today;
    today = new Date();
    this_year = today.getFullYear();
    this_month = today.getMonth() + 1;
    this_day = today.getDate();


	optionLoop(1950, this_year, 'id_year', this_year);
  	optionLoop(1, 12, 'id_month', this_month);
	optionLoop(1, 12, 'id_day', this_day);
 	optionLoop(1950, this_year, 'id2_year', this_year);
	optionLoop(1, 12, 'id2_month', this_month);
