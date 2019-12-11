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

Globalize.addCultureInfo( "lo-LA", "default", {
	name: "lo-LA",
	englishName: "Lao (Lao P.D.R.)",
	nativeName: "ລາວ (ສ.ປ.ປ. ລາວ)",
	language: "lo",
	numberFormat: {
		pattern: ["(n)"],
		groupSizes: [3,0],
		percent: {
			groupSizes: [3,0]
		},
		currency: {
			pattern: ["(n$)","n$"],
			groupSizes: [3,0],
			symbol: "₭"
		}
	},
	calendars: {
		standard: {
			days: {
				names: ["ວັນອາທິດ","ວັນຈັນ","ວັນອັງຄານ","ວັນພຸດ","ວັນພະຫັດ","ວັນສຸກ","ວັນເສົາ"],
				namesAbbr: ["ອາທິດ","ຈັນ","ອັງຄານ","ພຸດ","ພະຫັດ","ສຸກ","ເສົາ"],
				namesShort: ["ອ","ຈ","ອ","ພ","ພ","ສ","ເ"]
			},
			months: {
				names: ["ມັງກອນ","ກຸມພາ","ມີນາ","ເມສາ","ພຶດສະພາ","ມິຖຸນາ","ກໍລະກົດ","ສິງຫາ","ກັນຍາ","ຕຸລາ","ພະຈິກ","ທັນວາ",""],
				namesAbbr: ["ມັງກອນ","ກຸມພາ","ມີນາ","ເມສາ","ພຶດສະພາ","ມິຖຸນາ","ກໍລະກົດ","ສິງຫາ","ກັນຍາ","ຕຸລາ","ພະຈິກ","ທັນວາ",""]
			},
			AM: ["ເຊົ້າ","ເຊົ້າ","ເຊົ້າ"],
			PM: ["ແລງ","ແລງ","ແລງ"],
			patterns: {
				d: "dd/MM/yyyy",
				D: "dd MMMM yyyy",
				t: "H:mm tt",
				T: "HH:mm:ss",
				f: "dd MMMM yyyy H:mm tt",
				F: "dd MMMM yyyy HH:mm:ss",
				M: "dd MMMM",
				Y: "MMMM yyyy"
			}
		}
	}
});

}( this ));
