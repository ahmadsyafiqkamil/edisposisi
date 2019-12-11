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

Globalize.addCultureInfo( "yo", "default", {
	name: "yo",
	englishName: "Yoruba",
	nativeName: "Yoruba",
	language: "yo",
	numberFormat: {
		currency: {
			pattern: ["$-n","$ n"],
			symbol: "N"
		}
	},
	calendars: {
		standard: {
			days: {
				names: ["Aiku","Aje","Isegun","Ojo'ru","Ojo'bo","Eti","Abameta"],
				namesAbbr: ["Aik","Aje","Ise","Ojo","Ojo","Eti","Aba"],
				namesShort: ["A","A","I","O","O","E","A"]
			},
			months: {
				names: ["Osu kinni","Osu keji","Osu keta","Osu kerin","Osu karun","Osu kefa","Osu keje","Osu kejo","Osu kesan","Osu kewa","Osu kokanla","Osu keresi",""],
				namesAbbr: ["kin.","kej.","ket.","ker.","kar.","kef.","kej.","kej.","kes.","kew.","kok.","ker.",""]
			},
			AM: ["Owuro","owuro","OWURO"],
			PM: ["Ale","ale","ALE"],
			eras: [{"name":"AD","start":null,"offset":0}],
			patterns: {
				d: "d/M/yyyy"
			}
		}
	}
});

}( this ));
