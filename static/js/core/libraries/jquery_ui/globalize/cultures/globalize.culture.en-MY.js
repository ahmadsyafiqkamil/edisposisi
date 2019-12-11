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

Globalize.addCultureInfo( "en-MY", "default", {
	name: "en-MY",
	englishName: "English (Malaysia)",
	nativeName: "English (Malaysia)",
	numberFormat: {
		percent: {
			pattern: ["-n%","n%"]
		},
		currency: {
			symbol: "RM"
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
