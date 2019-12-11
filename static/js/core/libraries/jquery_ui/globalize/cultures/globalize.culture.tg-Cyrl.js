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

Globalize.addCultureInfo( "tg-Cyrl", "default", {
	name: "tg-Cyrl",
	englishName: "Tajik (Cyrillic)",
	nativeName: "Тоҷикӣ",
	language: "tg-Cyrl",
	numberFormat: {
		",": " ",
		".": ",",
		groupSizes: [3,0],
		negativeInfinity: "-бесконечность",
		positiveInfinity: "бесконечность",
		percent: {
			pattern: ["-n%","n%"],
			groupSizes: [3,0],
			",": " ",
			".": ","
		},
		currency: {
			pattern: ["-n $","n $"],
			groupSizes: [3,0],
			",": " ",
			".": ";",
			symbol: "т.р."
		}
	},
	calendars: {
		standard: {
			"/": ".",
			days: {
				names: ["Яш","Душанбе","Сешанбе","Чоршанбе","Панҷшанбе","Ҷумъа","Шанбе"],
				namesAbbr: ["Яш","Дш","Сш","Чш","Пш","Ҷм","Шн"],
				namesShort: ["Яш","Дш","Сш","Чш","Пш","Ҷм","Шн"]
			},
			months: {
				names: ["Январ","Феврал","Март","Апрел","Май","Июн","Июл","Август","Сентябр","Октябр","Ноябр","Декабр",""],
				namesAbbr: ["Янв","Фев","Мар","Апр","Май","Июн","Июл","Авг","Сен","Окт","Ноя","Дек",""]
			},
			monthsGenitive: {
				names: ["январи","феврали","марти","апрели","маи","июни","июли","августи","сентябри","октябри","ноябри","декабри",""],
				namesAbbr: ["Янв","Фев","Мар","Апр","Май","Июн","Июл","Авг","Сен","Окт","Ноя","Дек",""]
			},
			AM: null,
			PM: null,
			patterns: {
				d: "dd.MM.yy",
				D: "d MMMM yyyy",
				t: "H:mm",
				T: "H:mm:ss",
				f: "d MMMM yyyy H:mm",
				F: "d MMMM yyyy H:mm:ss",
				Y: "MMMM yyyy"
			}
		}
	}
});

}( this ));
