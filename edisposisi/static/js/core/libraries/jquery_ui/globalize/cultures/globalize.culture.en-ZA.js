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

Globalize.addCultureInfo( "en-ZA", "default", {
	name: "en-ZA",
	englishName: "English (South Africa)",
	nativeName: "English (South Africa)",
	numberFormat: {
		",": " ",
		percent: {
			pattern: ["-n%","n%"],
			",": " "
		},
		currency: {
			pattern: ["$-n","$ n"],
			",": " ",
			".": ",",
			symbol: "R"
		}
	},
	calendars: {
		standard: {
			patterns: {
				d: "yyyy/MM/dd",
				D: "dd MMMM yyyy",
				t: "hh:mm tt",
				T: "hh:mm:ss tt",
				f: "dd MMMM yyyy hh:mm tt",
				F: "dd MMMM yyyy hh:mm:ss tt",
				M: "dd MMMM",
				Y: "MMMM yyyy"
			}
		}
	}
});

}( this ));
