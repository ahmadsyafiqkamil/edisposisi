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

Globalize.addCultureInfo( "si", "default", {
	name: "si",
	englishName: "Sinhala",
	nativeName: "සිංහල",
	language: "si",
	numberFormat: {
		groupSizes: [3,2],
		negativeInfinity: "-අනන්තය",
		positiveInfinity: "අනන්තය",
		percent: {
			groupSizes: [3,2]
		},
		currency: {
			pattern: ["($ n)","$ n"],
			symbol: "රු."
		}
	},
	calendars: {
		standard: {
			"/": "-",
			firstDay: 1,
			days: {
				names: ["ඉරිදා","සඳුදා","අඟහරුවාදා","බදාදා","බ්\u200dරහස්පතින්දා","සිකුරාදා","සෙනසුරාදා"],
				namesAbbr: ["ඉරිදා","සඳුදා","කුජදා","බුදදා","ගුරුදා","කිවිදා","ශනිදා"],
				namesShort: ["ඉ","ස","අ","බ","බ්\u200dර","සි","සෙ"]
			},
			months: {
				names: ["ජනවාරි","පෙබරවාරි","මාර්තු","අ\u200cප්\u200dරේල්","මැයි","ජූනි","ජූලි","අ\u200cගෝස්තු","සැප්තැම්බර්","ඔක්තෝබර්","නොවැම්බර්","දෙසැම්බර්",""],
				namesAbbr: ["ජන.","පෙබ.","මාර්තු.","අප්\u200dරේල්.","මැයි.","ජූනි.","ජූලි.","අගෝ.","සැප්.","ඔක්.","නොවැ.","දෙසැ.",""]
			},
			AM: ["පෙ.ව.","පෙ.ව.","පෙ.ව."],
			PM: ["ප.ව.","ප.ව.","ප.ව."],
			eras: [{"name":"ක්\u200dරි.ව.","start":null,"offset":0}],
			patterns: {
				d: "yyyy-MM-dd",
				D: "yyyy MMMM' මස 'dd' වැනිදා 'dddd",
				f: "yyyy MMMM' මස 'dd' වැනිදා 'dddd h:mm tt",
				F: "yyyy MMMM' මස 'dd' වැනිදා 'dddd h:mm:ss tt",
				Y: "yyyy MMMM"
			}
		}
	}
});

}( this ));
