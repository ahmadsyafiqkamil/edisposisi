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

Globalize.addCultureInfo( "zh-SG", "default", {
	name: "zh-SG",
	englishName: "Chinese (Simplified, Singapore)",
	nativeName: "中文(新加坡)",
	language: "zh-CHS",
	numberFormat: {
		percent: {
			pattern: ["-n%","n%"]
		}
	},
	calendars: {
		standard: {
			days: {
				names: ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"],
				namesAbbr: ["周日","周一","周二","周三","周四","周五","周六"],
				namesShort: ["日","一","二","三","四","五","六"]
			},
			months: {
				names: ["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月",""],
				namesAbbr: ["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月",""]
			},
			patterns: {
				d: "d/M/yyyy",
				D: "yyyy'年'M'月'd'日'",
				t: "tt h:mm",
				T: "tt h:mm:ss",
				f: "yyyy'年'M'月'd'日' tt h:mm",
				F: "yyyy'年'M'月'd'日' tt h:mm:ss",
				M: "M'月'd'日'",
				Y: "yyyy'年'M'月'"
			}
		}
	}
});

}( this ));
