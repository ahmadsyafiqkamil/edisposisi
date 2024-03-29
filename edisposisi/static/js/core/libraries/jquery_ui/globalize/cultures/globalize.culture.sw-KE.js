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

Globalize.addCultureInfo( "sw-KE", "default", {
	name: "sw-KE",
	englishName: "Kiswahili (Kenya)",
	nativeName: "Kiswahili (Kenya)",
	language: "sw",
	numberFormat: {
		currency: {
			symbol: "S"
		}
	},
	calendars: {
		standard: {
			days: {
				names: ["Jumapili","Jumatatu","Jumanne","Jumatano","Alhamisi","Ijumaa","Jumamosi"],
				namesAbbr: ["Jumap.","Jumat.","Juman.","Jumat.","Alh.","Iju.","Jumam."],
				namesShort: ["P","T","N","T","A","I","M"]
			},
			months: {
				names: ["Januari","Februari","Machi","Aprili","Mei","Juni","Julai","Agosti","Septemba","Oktoba","Novemba","Decemba",""],
				namesAbbr: ["Jan","Feb","Mac","Apr","Mei","Jun","Jul","Ago","Sep","Okt","Nov","Dec",""]
			}
		}
	}
});

}( this ));
