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

Globalize.addCultureInfo( "en-PH", "default", {
	name: "en-PH",
	englishName: "English (Republic of the Philippines)",
	nativeName: "English (Philippines)",
	numberFormat: {
		currency: {
			symbol: "Php"
		}
	}
});

}( this ));
