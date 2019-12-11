/*
 * Copyright (c) 2019.
 * Ahmad Syafiq Kamil
 */

(function( window, undefined ) {

var Globalize;

if ( typeof require !== "undefined" &&
	typeof exports !== "undefined" &&
	typeof module !== "undefined" ) {
	// Assume CommonJS
	Globalize = require( "globalize" );
} else {
	// Global variable
	Globalize = window.Globalize;
}

Globalize.addCultureInfo( "ka-GE", "default", {
	name: "ka-GE",
	englishName: "Georgian (Georgia)",
	nativeName: "ქართული (საქართველო)",
	language: "ka",
	numberFormat: {
		",": " ",
		".": ",",
		percent: {
			",": " ",
			".": ","
		},
		currency: {
			pattern: ["-n $","n $"],
			",": " ",
			".": ",",
			symbol: "Lari"
		}
	},
	calendars: {
		standard: {
			"/": ".",
			firstDay: 1,
			days: {
				names: ["კვირა","ორშაბათი","სამშაბათი","ოთხშაბათი","ხუთშაბათი","პარასკევი","შაბათი"],
				namesAbbr: ["კვირა","ორშაბათი","სამშაბათი","ოთხშაბათი","ხუთშაბათი","პარასკევი","შაბათი"],
				namesShort: ["კ","ო","ს","ო","ხ","პ","შ"]
			},
			months: {
				names: ["იანვარი","თებერვალი","მარტი","აპრილი","მაისი","ივნისი","ივლისი","აგვისტო","სექტემბერი","ოქტომბერი","ნოემბერი","დეკემბერი",""],
				namesAbbr: ["იან","თებ","მარ","აპრ","მაის","ივნ","ივლ","აგვ","სექ","ოქტ","ნოემ","დეკ",""]
			},
			AM: null,
			PM: null,
			patterns: {
				d: "dd.MM.yyyy",
				D: "yyyy 'წლის' dd MM, dddd",
				t: "H:mm",
				T: "H:mm:ss",
				f: "yyyy 'წლის' dd MM, dddd H:mm",
				F: "yyyy 'წლის' dd MM, dddd H:mm:ss",
				M: "dd MM",
				Y: "MMMM yyyy"
			}
		}
	}
});

}( this ));
