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

Globalize.addCultureInfo( "mt-MT", "default", {
	name: "mt-MT",
	englishName: "Maltese (Malta)",
	nativeName: "Malti (Malta)",
	language: "mt",
	numberFormat: {
		percent: {
			pattern: ["-%n","%n"]
		},
		currency: {
			pattern: ["-$n","$n"],
			symbol: "€"
		}
	},
	calendars: {
		standard: {
			firstDay: 1,
			days: {
				names: ["Il-Ħadd","It-Tnejn","It-Tlieta","L-Erbgħa","Il-Ħamis","Il-Ġimgħa","Is-Sibt"],
				namesAbbr: ["Ħad","Tne","Tli","Erb","Ħam","Ġim","Sib"],
				namesShort: ["I","I","I","L","I","I","I"]
			},
			months: {
				names: ["Jannar","Frar","Marzu","April","Mejju","Ġunju","Lulju","Awissu","Settembru","Ottubru","Novembru","Diċembru",""],
				namesAbbr: ["Jan","Fra","Mar","Apr","Mej","Ġun","Lul","Awi","Set","Ott","Nov","Diċ",""]
			},
			patterns: {
				d: "dd/MM/yyyy",
				D: "dddd, d' ta\\' 'MMMM yyyy",
				t: "HH:mm",
				T: "HH:mm:ss",
				f: "dddd, d' ta\\' 'MMMM yyyy HH:mm",
				F: "dddd, d' ta\\' 'MMMM yyyy HH:mm:ss",
				M: "d' ta\\' 'MMMM",
				Y: "MMMM yyyy"
			}
		}
	}
});

}( this ));
