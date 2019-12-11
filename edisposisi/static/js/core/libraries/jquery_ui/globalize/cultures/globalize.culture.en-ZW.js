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

Globalize.addCultureInfo( "en-ZW", "default", {
	name: "en-ZW",
	englishName: "English (Zimbabwe)",
	nativeName: "English (Zimbabwe)",
	numberFormat: {
		currency: {
			symbol: "Z$"
		}
	}
});

}( this ));
