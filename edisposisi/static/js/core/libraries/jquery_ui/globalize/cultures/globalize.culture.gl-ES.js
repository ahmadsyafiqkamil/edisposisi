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

Globalize.addCultureInfo( "gl-ES", "default", {
	name: "gl-ES",
	englishName: "Galician (Galician)",
	nativeName: "galego (galego)",
	language: "gl",
	numberFormat: {
		",": ".",
		".": ",",
		"NaN": "NeuN",
		negativeInfinity: "-Infinito",
		positiveInfinity: "Infinito",
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
				names: ["domingo","luns","martes","mércores","xoves","venres","sábado"],
				namesAbbr: ["dom","luns","mar","mér","xov","ven","sáb"],
				namesShort: ["do","lu","ma","mé","xo","ve","sá"]
			},
			months: {
				names: ["xaneiro","febreiro","marzo","abril","maio","xuño","xullo","agosto","setembro","outubro","novembro","decembro",""],
				namesAbbr: ["xan","feb","mar","abr","maio","xuñ","xull","ago","set","out","nov","dec",""]
			},
			AM: ["a.m.","a.m.","A.M."],
			PM: ["p.m.","p.m.","P.M."],
			eras: [{"name":"d.C.","start":null,"offset":0}],
			patterns: {
				d: "dd/MM/yyyy",
				D: "dddd, dd' de 'MMMM' de 'yyyy",
				t: "H:mm",
				T: "H:mm:ss",
				f: "dddd, dd' de 'MMMM' de 'yyyy H:mm",
				F: "dddd, dd' de 'MMMM' de 'yyyy H:mm:ss",
				M: "dd MMMM",
				Y: "MMMM' de 'yyyy"
			}
		}
	}
});

}( this ));
