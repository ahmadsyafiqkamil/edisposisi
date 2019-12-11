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

Globalize.addCultureInfo( "es-US", "default", {
	name: "es-US",
	englishName: "Spanish (United States)",
	nativeName: "Español (Estados Unidos)",
	language: "es",
	numberFormat: {
		groupSizes: [3,0],
		"NaN": "NeuN",
		negativeInfinity: "-Infinito",
		positiveInfinity: "Infinito",
		percent: {
			groupSizes: [3,0]
		}
	},
	calendars: {
		standard: {
			days: {
				names: ["domingo","lunes","martes","miércoles","jueves","viernes","sábado"],
				namesAbbr: ["dom","lun","mar","mié","jue","vie","sáb"],
				namesShort: ["do","lu","ma","mi","ju","vi","sa"]
			},
			months: {
				names: ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre",""],
				namesAbbr: ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic",""]
			},
			eras: [{"name":"d.C.","start":null,"offset":0}],
			patterns: {
				M: "dd' de 'MMMM",
				Y: "MMMM' de 'yyyy"
			}
		}
	}
});

}( this ));
