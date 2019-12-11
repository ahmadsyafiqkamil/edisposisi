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

Globalize.addCultureInfo( "sr-Cyrl-BA", "default", {
	name: "sr-Cyrl-BA",
	englishName: "Serbian (Cyrillic, Bosnia and Herzegovina)",
	nativeName: "српски (Босна и Херцеговина)",
	language: "sr-Cyrl",
	numberFormat: {
		",": ".",
		".": ",",
		negativeInfinity: "-бесконачност",
		positiveInfinity: "+бесконачност",
		percent: {
			",": ".",
			".": ","
		},
		currency: {
			pattern: ["-n $","n $"],
			",": ".",
			".": ",",
			symbol: "КМ"
		}
	},
	calendars: {
		standard: {
			"/": ".",
			firstDay: 1,
			days: {
				names: ["недеља","понедељак","уторак","среда","четвртак","петак","субота"],
				namesAbbr: ["нед","пон","уто","сре","чет","пет","суб"],
				namesShort: ["н","п","у","с","ч","п","с"]
			},
			months: {
				names: ["јануар","фебруар","март","април","мај","јун","јул","август","септембар","октобар","новембар","децембар",""],
				namesAbbr: ["јан","феб","мар","апр","мај","јун","јул","авг","сеп","окт","нов","дец",""]
			},
			AM: null,
			PM: null,
			eras: [{"name":"н.е.","start":null,"offset":0}],
			patterns: {
				d: "d.M.yyyy",
				D: "d. MMMM yyyy",
				t: "H:mm",
				T: "H:mm:ss",
				f: "d. MMMM yyyy H:mm",
				F: "d. MMMM yyyy H:mm:ss",
				M: "d. MMMM"
			}
		}
	}
});

}( this ));
