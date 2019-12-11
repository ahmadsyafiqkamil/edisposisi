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

Globalize.addCultureInfo( "uz-Latn", "default", {
	name: "uz-Latn",
	englishName: "Uzbek (Latin)",
	nativeName: "U'zbek",
	language: "uz-Latn",
	numberFormat: {
		",": " ",
		".": ",",
		percent: {
			pattern: ["-n%","n%"],
			",": " ",
			".": ","
		},
		currency: {
			pattern: ["-n $","n $"],
			decimals: 0,
			",": " ",
			".": ",",
			symbol: "so'm"
		}
	},
	calendars: {
		standard: {
			firstDay: 1,
			days: {
				names: ["yakshanba","dushanba","seshanba","chorshanba","payshanba","juma","shanba"],
				namesAbbr: ["yak.","dsh.","sesh.","chr.","psh.","jm.","sh."],
				namesShort: ["ya","d","s","ch","p","j","sh"]
			},
			months: {
				names: ["yanvar","fevral","mart","aprel","may","iyun","iyul","avgust","sentyabr","oktyabr","noyabr","dekabr",""],
				namesAbbr: ["yanvar","fevral","mart","aprel","may","iyun","iyul","avgust","sentyabr","oktyabr","noyabr","dekabr",""]
			},
			AM: null,
			PM: null,
			patterns: {
				d: "dd/MM yyyy",
				D: "yyyy 'yil' d-MMMM",
				t: "HH:mm",
				T: "HH:mm:ss",
				f: "yyyy 'yil' d-MMMM HH:mm",
				F: "yyyy 'yil' d-MMMM HH:mm:ss",
				M: "d-MMMM",
				Y: "MMMM yyyy"
			}
		}
	}
});

}( this ));
