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

Globalize.addCultureInfo( "ms-MY", "default", {
	name: "ms-MY",
	englishName: "Malay (Malaysia)",
	nativeName: "Bahasa Melayu (Malaysia)",
	language: "ms",
	numberFormat: {
		currency: {
			decimals: 0,
			symbol: "RM"
		}
	},
	calendars: {
		standard: {
			firstDay: 1,
			days: {
				names: ["Ahad","Isnin","Selasa","Rabu","Khamis","Jumaat","Sabtu"],
				namesAbbr: ["Ahad","Isnin","Sel","Rabu","Khamis","Jumaat","Sabtu"],
				namesShort: ["A","I","S","R","K","J","S"]
			},
			months: {
				names: ["Januari","Februari","Mac","April","Mei","Jun","Julai","Ogos","September","Oktober","November","Disember",""],
				namesAbbr: ["Jan","Feb","Mac","Apr","Mei","Jun","Jul","Ogos","Sept","Okt","Nov","Dis",""]
			},
			AM: null,
			PM: null,
			patterns: {
				d: "dd/MM/yyyy",
				D: "dd MMMM yyyy",
				t: "H:mm",
				T: "H:mm:ss",
				f: "dd MMMM yyyy H:mm",
				F: "dd MMMM yyyy H:mm:ss",
				M: "dd MMMM",
				Y: "MMMM yyyy"
			}
		}
	}
});

}( this ));
