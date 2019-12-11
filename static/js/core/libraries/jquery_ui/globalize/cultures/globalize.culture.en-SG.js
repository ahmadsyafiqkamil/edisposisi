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

Globalize.addCultureInfo( "en-SG", "default", {
	name: "en-SG",
	englishName: "English (Singapore)",
	nativeName: "English (Singapore)",
	numberFormat: {
		percent: {
			pattern: ["-n%","n%"]
		}
	},
	calendars: {
		standard: {
			days: {
				namesShort: ["S","M","T","W","T","F","S"]
			},
			patterns: {
				d: "d/M/yyyy",
				D: "dddd, d MMMM, yyyy",
				f: "dddd, d MMMM, yyyy h:mm tt",
				F: "dddd, d MMMM, yyyy h:mm:ss tt",
				M: "d MMMM"
			}
		}
	}
});

}( this ));
