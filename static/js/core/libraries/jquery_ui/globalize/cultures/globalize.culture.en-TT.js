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

Globalize.addCultureInfo( "en-TT", "default", {
	name: "en-TT",
	englishName: "English (Trinidad and Tobago)",
	nativeName: "English (Trinidad y Tobago)",
	numberFormat: {
		currency: {
			groupSizes: [3,0],
			symbol: "TT$"
		}
	},
	calendars: {
		standard: {
			patterns: {
				d: "dd/MM/yyyy",
				D: "dddd, dd MMMM yyyy",
				t: "hh:mm tt",
				T: "hh:mm:ss tt",
				f: "dddd, dd MMMM yyyy hh:mm tt",
				F: "dddd, dd MMMM yyyy hh:mm:ss tt",
				M: "dd MMMM",
				Y: "MMMM yyyy"
			}
		}
	}
});

}( this ));
