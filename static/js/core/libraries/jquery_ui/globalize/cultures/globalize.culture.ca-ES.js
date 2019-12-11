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

Globalize.addCultureInfo( "ca-ES", "default", {
	name: "ca-ES",
	englishName: "Catalan (Catalan)",
	nativeName: "català (català)",
	language: "ca",
	numberFormat: {
		",": ".",
		".": ",",
		"NaN": "NeuN",
		negativeInfinity: "-Infinit",
		positiveInfinity: "Infinit",
		percent: {
			",": ".",
			".": ","
		},
		currency: {
			pattern: ["-n $","n $"],
			",": ".",
			".": ",",
			symbol: "€"
		}
	},
	calendars: {
		standard: {
			firstDay: 1,
			days: {
				names: ["diumenge","dilluns","dimarts","dimecres","dijous","divendres","dissabte"],
				namesAbbr: ["dg.","dl.","dt.","dc.","dj.","dv.","ds."],
				namesShort: ["dg","dl","dt","dc","dj","dv","ds"]
			},
			months: {
				names: ["gener","febrer","març","abril","maig","juny","juliol","agost","setembre","octubre","novembre","desembre",""],
				namesAbbr: ["gen","feb","març","abr","maig","juny","jul","ag","set","oct","nov","des",""]
			},
			AM: null,
			PM: null,
			eras: [{"name":"d.C.","start":null,"offset":0}],
			patterns: {
				d: "dd/MM/yyyy",
				D: "dddd, d' / 'MMMM' / 'yyyy",
				t: "HH:mm",
				T: "HH:mm:ss",
				f: "dddd, d' / 'MMMM' / 'yyyy HH:mm",
				F: "dddd, d' / 'MMMM' / 'yyyy HH:mm:ss",
				M: "dd MMMM",
				Y: "MMMM' / 'yyyy"
			}
		}
	}
});

}( this ));
