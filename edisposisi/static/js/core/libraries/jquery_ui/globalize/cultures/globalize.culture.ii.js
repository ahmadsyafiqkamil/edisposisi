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

Globalize.addCultureInfo( "ii", "default", {
	name: "ii",
	englishName: "Yi",
	nativeName: "ꆈꌠꁱꂷ",
	language: "ii",
	numberFormat: {
		groupSizes: [3,0],
		"NaN": "ꌗꂷꀋꉬ",
		negativeInfinity: "ꀄꊭꌐꀋꉆ",
		positiveInfinity: "ꈤꇁꑖꀋꉬ",
		percent: {
			pattern: ["-n%","n%"],
			groupSizes: [3,0]
		},
		currency: {
			pattern: ["$-n","$n"],
			symbol: "¥"
		}
	},
	calendars: {
		standard: {
			firstDay: 1,
			days: {
				names: ["ꑭꆏꑍ","ꆏꊂ꒔","ꆏꊂꑍ","ꆏꊂꌕ","ꆏꊂꇖ","ꆏꊂꉬ","ꆏꊂꃘ"],
				namesAbbr: ["ꑭꆏ","ꆏ꒔","ꆏꑍ","ꆏꌕ","ꆏꇖ","ꆏꉬ","ꆏꃘ"],
				namesShort: ["ꆏ","꒔","ꑍ","ꌕ","ꇖ","ꉬ","ꃘ"]
			},
			months: {
				names: ["ꋍꆪ","ꑍꆪ","ꌕꆪ","ꇖꆪ","ꉬꆪ","ꃘꆪ","ꏃꆪ","ꉆꆪ","ꈬꆪ","ꊰꆪ","ꊯꊪꆪ","ꊰꑋꆪ",""],
				namesAbbr: ["ꋍꆪ","ꑍꆪ","ꌕꆪ","ꇖꆪ","ꉬꆪ","ꃘꆪ","ꏃꆪ","ꉆꆪ","ꈬꆪ","ꊰꆪ","ꊯꊪꆪ","ꊰꑋꆪ",""]
			},
			AM: ["ꂵꆪꈌꈐ","ꂵꆪꈌꈐ","ꂵꆪꈌꈐ"],
			PM: ["ꂵꆪꈌꉈ","ꂵꆪꈌꉈ","ꂵꆪꈌꉈ"],
			eras: [{"name":"ꇬꑼ","start":null,"offset":0}],
			patterns: {
				d: "yyyy/M/d",
				D: "yyyy'ꈎ' M'ꆪ' d'ꑍ'",
				t: "tt h:mm",
				T: "H:mm:ss",
				f: "yyyy'ꈎ' M'ꆪ' d'ꑍ' tt h:mm",
				F: "yyyy'ꈎ' M'ꆪ' d'ꑍ' H:mm:ss",
				M: "M'ꆪ' d'ꑍ'",
				Y: "yyyy'ꈎ' M'ꆪ'"
			}
		}
	}
});

}( this ));
