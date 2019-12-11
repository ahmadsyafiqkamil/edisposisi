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

Globalize.addCultureInfo( "fil", "default", {
	name: "fil",
	englishName: "Filipino",
	nativeName: "Filipino",
	language: "fil",
	numberFormat: {
		currency: {
			symbol: "PhP"
		}
	},
	calendars: {
		standard: {
			days: {
				names: ["Linggo","Lunes","Martes","Mierkoles","Huebes","Biernes","Sabado"],
				namesAbbr: ["Lin","Lun","Mar","Mier","Hueb","Bier","Saba"],
				namesShort: ["L","L","M","M","H","B","S"]
			},
			months: {
				names: ["Enero","Pebrero","Marso","Abril","Mayo","Hunyo","Hulyo","Agosto","Septyembre","Oktubre","Nobyembre","Disyembre",""],
				namesAbbr: ["En","Peb","Mar","Abr","Mayo","Hun","Hul","Agos","Sept","Okt","Nob","Dis",""]
			},
			eras: [{"name":"Anno Domini","start":null,"offset":0}]
		}
	}
});

}( this ));
