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

Globalize.addCultureInfo( "en-029", "default", {
	name: "en-029",
	englishName: "English (Caribbean)",
	nativeName: "English (Caribbean)",
	numberFormat: {
		currency: {
			pattern: ["-$n","$n"]
		}
	},
	calendars: {
		standard: {
			firstDay: 1,
			patterns: {
				d: "MM/dd/yyyy"
			}
		}
	}
});

}( this ));
